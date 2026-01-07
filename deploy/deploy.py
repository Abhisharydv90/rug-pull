import os
from web3 import Web3
import json

def deploy_contract():
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{os.environ["INFURA_PROJECT_ID"]}'))
    acct = w3.eth.account.from_key(os.environ["DEPLOYER_PRIVATE_KEY"])
    
    with open('contract.json', 'r') as f:
        contract_data = json.load(f)
    
    contract = w3.eth.contract(
        abi=contract_data['abi'],
        bytecode=contract_data['bytecode']
    )
    
    tx = contract.constructor().build_transaction({
        'from': acct.address,
        'gas': 2000000
    })
    
    signed = acct.sign_transaction(tx)
    tx_hash = w3.eth.send_raw_transaction(signed.rawTransaction)
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    
    print(f"Contract deployed at: {receipt.contractAddress}")
    with open('contract_address.txt', 'w') as f:
        f.write(receipt.contractAddress)

if __name__ == "__main__":
    deploy_contract()
