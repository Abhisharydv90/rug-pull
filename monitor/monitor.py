import os
from web3 import Web3
import time

def check_investors():
    w3 = Web3(Web3.HTTPProvider(f'https://mainnet.infura.io/v3/{os.environ["INFURA_PROJECT_ID"]}'))
    
    with open('contract_address.txt', 'r') as f:
        contract_address = f.read().strip()
    
    while True:
        contract = w3.eth.contract(address=contract_address, abi=rug_pull_abi)
        balance = contract.functions.totalInvestments().call()
        
        if balance > 0:
            print(f"Investors detected: {balance}")
            contract.functions.emergencyWithdraw().transact()
            break
        
        time.sleep(1)  # Fast polling

if __name__ == "__main__":
    check_investors()
