from crypto.BlockChain import BlockChain

class App:

    def __init__(self):
        self.chain = BlockChain()
    
    def chain(self):
        return self.chain

    def new_transaction(self):
        last = self.chain.latest
        last_proof = last.proof
        proof_num = self.chain.proof_of_work(last_proof)

        self.chain.new_data(sender = "0", recipient = "Austin", amount = 1)

        last_hash = last.compute_hash
        block = self.chain.construct_block(proof_num, last_hash)

    

# example of adding transactions to the chain

app = App()

chain = app.chain

for x in range(20):
    app.new_transaction()

print(chain.chain)
