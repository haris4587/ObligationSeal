"""Read-only verification of public finalized Studionet evidence. Never signs/sends."""
import base64
import hashlib
import json
from pathlib import Path
import requests
from genlayer_py.abi import calldata
ROOT=Path(__file__).resolve().parents[1]
def canonical(x):return json.dumps(x,sort_keys=True,separators=(',',':'),ensure_ascii=True,allow_nan=False)
def digest(x):return hashlib.sha256(canonical(x).encode()).hexdigest()
def rpc(method,params):
    r=requests.post('https://studio.genlayer.com/api',json={'jsonrpc':'2.0','id':1,'method':method,'params':params},timeout=45)
    r.raise_for_status(); data=r.json()
    assert 'error' not in data,data
    return data['result']
def save(name,data):
    (ROOT/'evidence'/name).write_text(json.dumps(data,indent=2)+'\n')
def read(s,method,args):
    result=rpc('gen_call',[{'from':s['sender'],'to':s['address'],'type':'read','status':'finalized','data':'0x'+calldata.encode({'method':method,'args':args}).hex()}])
    if isinstance(result,dict):
        assert result['status']['code']==0,result
        result=result['data']
    return json.loads(calldata.decode(bytes.fromhex(result.removeprefix('0x'))))
def verify():
    s=json.loads((ROOT/'evidence/live-summary.json').read_text())
    source=base64.b64decode(rpc('gen_getContractCode',[s['address']]))
    assert source==(ROOT/'contracts/obligation_seal.py').read_bytes()
    assert hashlib.sha256(source).hexdigest()==s['source_sha256']
    (ROOT/'evidence/deployed-source.py').write_bytes(source)
    # Compare exact source against committed public GitHub bytes too.
    ref=s.get('final_commit',s['implementation_commit'])
    url=f'https://raw.githubusercontent.com/haris4587/ObligationSeal/{ref}/contracts/obligation_seal.py'
    github=requests.get(url,timeout=45); github.raise_for_status()
    assert github.content==source,'GitHub/deployment source mismatch'
    txs={}
    for name,h in s['transactions'].items():
        tx=rpc('eth_getTransactionByHash',[h]); save(name+'-transaction.json',tx)
        assert tx['status']=='FINALIZED', (name,tx['status'])
        assert tx['leader_only'] is False and tx['result_name']=='MAJORITY_AGREE',(name,tx['result_name'])
        assert tx['to_address']==s['address']
        txs[name]={'hash':h,'status':tx['status'],'result_name':tx['result_name'],'leader_only':tx['leader_only']}
        if name=='evaluate':
            receipts=tx['consensus_data']['leader_receipt']
            if isinstance(receipts,dict): receipts=[receipts]
            assert receipts and all(x['execution_result']=='SUCCESS' for x in receipts),receipts
            validators=tx['consensus_data'].get('validators',[])
            assert validators, 'Missing validator receipts'
            votes=tx['consensus_data']['votes']
            assert sum(v=='agree' for v in votes.values()) > len(votes)//2, votes
            for x in validators:
                if x.get('vote')=='agree':
                    assert x.get('execution_result')=='SUCCESS',x
                else:
                    assert x.get('vote')=='idle' and x['genvm_result']['error_code']=='CONSENSUS_VALIDATOR_QUORUM_REACHED',x
            txs[name]['votes']=votes
    a=read(s,'get_agreement',[s['agreement_id']]); save('finalized-agreement.json',a)
    assert digest(a)==s['agreement_id']
    assert a['agreement']==json.loads((ROOT/'examples/agreement.json').read_text())
    r=read(s,'get_request',[s['request_id']]);save('finalized-request.json',r)
    assert digest({'domain':'ObligationSeal/1/delivery','agreement_id':s['agreement_id'],'package':r['package']})==s['request_id']
    assert r['package_hash']==digest(r['package'])
    assert r['package']==json.loads((ROOT/'examples/breached.json').read_text())
    previous=''
    for attempt in range(1,r['attempts']+1):
        receipt=read(s,'get_decision',[s['request_id'],attempt]);save(f'decision-{attempt}.json',receipt)
        d=receipt['decision'];h=receipt['decision_hash']
        assert digest(d)==h and d['previous']==previous
        assert d['request_id']==s['request_id'] and d['agreement_id']==s['agreement_id'] and d['package_hash']==r['package_hash'] and d['attempt']==attempt
        previous=h
    assert r['head']==previous
    assert r['status']==d['result']['outcome']=='BREACHED'
    evidence=[]; documents=[]
    for e in r['package']['evidence']:
        response=requests.get(e['url'],timeout=45);response.raise_for_status(); b=response.content
        assert len(b)==e['bytes'] and hashlib.sha256(b).hexdigest()==e['sha256']
        documents.append(json.loads(b))
        evidence.append({'url':e['url'],'sha256':e['sha256'],'bytes':len(b),'verified':True})
    for row in d['result']['requirements']:
        for cite in row['citations']:assert cite['quote'] in documents[cite['source']]['content']
    assert [row['state'] for row in d['result']['requirements']]==['SATISFIED','VIOLATED']
    assert d['result']['obligations']=={'O1':'FULFILLED','O2':'BREACHED'}
    report={'verified':True,'source_sha256':s['source_sha256'],'github_source_url':url,'transactions':txs,'agreement_id':s['agreement_id'],'request_id':s['request_id'],'decision_hash':previous,'outcome':r['status'],'evidence':evidence}
    save('verification.json',report)
    print(json.dumps(report,indent=2))
    return report
if __name__=='__main__':verify()
