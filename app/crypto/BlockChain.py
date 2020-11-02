import hashlib

from .Block import Block

class BlockChain(object):

    # for now we're just going to store this in memory, I eventually want to actually have a built chain once we work out how to handle everything
    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()
    
    # method to construct the intial block of the block chain
    def construct_genesis(self):
        self.construct_block(proof = 0, prev_hash = 0)
    
    # method to construct a new block in the chain
    def construct_block(self, proof, prev_hash):
        # construct a new block object with all of the necessary variables
        new_block = Block(index = len(self.chain), proof = proof, prev_hash = prev_hash, data = self.current_data)

        # clear the current data array
        self.current_data = []

        # append the block to the chain and return it
        self.chain.append(new_block)
        return new_block

    # method to check the integrity of the block chain
    @staticmethod
    def confirm_validity(block, prev_block):
        # check if the previous blocks index with one additive is the same as the current block's index
        if(prev_block.index + 1 != block.index):
            return False
        # check if the previous block's hash is equal to the current block's previous hash
        elif prev_block.compute_hash != block.prev_hash:
            return False
        # verify that the pow has been checked
        elif not BlockChain.verifying_proof(block.proof, prev_block.proof):
            return False
        # check if the current block was created before the previous one
        elif block.timestamp <= prev_block.timestamp:
            return False
        # if none of the conditionals are met, the validity is proved
        return True
    
    @staticmethod
    # method to varifying that the "miner" did the work necessary. discourages simply generating new blocks easily
    def proof_of_work(last_proof):
        
        # the number of proof verifying proof is on
        proof_num = 0

        # while the proof hasn't been verified or completed, keep adding and looping
        while BlockChain.verifying_proof(proof_num, last_proof) is False:
            proof_num += 1
        
        # return the final number
        return proof_num

    def new_data(self, sender, recipient, amount):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantitiy': amount
        })
        return True

    @staticmethod
    def verifying_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()

        return guess_hash[:4] == "0000"
    
    # Method that declares new transactions on the chain
    def get_data(self, sender, receiver, amount):
        self.current_data_.append({
            'sender': sender,
            'receiver': receiver,
            'amount': amount
        })
        return True
    
    # method to award a user for validating transactions
    def mine(self, miner, reward):
        self.new_data(sender = "0", receiver=miner, quantity=reward)

    @property
    def latest(self):
        return self.chain[-1]