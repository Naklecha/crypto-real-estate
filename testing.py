from web3 import Web3

rpc = "http://127.0.0.1:8545"

web3 = Web3(Web3.HTTPProvider(rpc))

abi = '[{"constant":true,"inputs":[],"name":"check","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"address"}],"name":"wallet","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"landCount","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"","type":"uint256"}],"name":"land_record","outputs":[{"name":"region","type":"uint256"},{"name":"x","type":"uint256"},{"name":"y","type":"uint256"},{"name":"owner","type":"address"},{"name":"price","type":"uint256"},{"name":"status","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":false,"inputs":[{"name":"region","type":"uint256"},{"name":"x","type":"uint256"},{"name":"y","type":"uint256"}],"name":"initLand","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[],"name":"doneInit","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"landid","type":"uint256"},{"name":"price","type":"uint256"}],"name":"buyLand","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":false,"inputs":[{"name":"landid","type":"uint256"},{"name":"price","type":"uint256"}],"name":"sellLand","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"}]'
admin_acc = '0xB0BE5EFDe83490f0d8fC64120461660098AE7599'
admin_pvtkey = '25d9479cd21fb800522f8e0c74513f0730f7afac9f3ac7a23d8ad69b7103be52'

contract_addr = "0x8fDd21C593c5693788E0248b4C86bB66375f8dA7"
contract = web3.eth.contract(address=contract_addr, abi=abi)

print(contract.caller().check())

id = 0
for region in range(4):
    for x in range(10):
        for y in range(10):
            id += 1
            print(id,"/",4*10*10)
            transaction  = contract.functions.initLand(region,x,y).buildTransaction()
            transaction['nonce'] = web3.eth.getTransactionCount(admin_acc)

            signed_tx = web3.eth.account.signTransaction(transaction, admin_pvtkey)
            tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

            print(tx_hash)
print("Done")

transaction  = contract.functions.doneInit().buildTransaction()
transaction['nonce'] = web3.eth.getTransactionCount(admin_acc)

signed_tx = web3.eth.account.signTransaction(transaction, admin_pvtkey)
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

print(tx_hash)



