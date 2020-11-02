# import the necessary libs
import hashlib
import time

# Constructing a block of the blockchain.
class Block(object):
    
    # pull all of the data in the constructor for further calculations
    def __init__(self, index, proof, prev_hash, data, timestamp = None):
        self.index = index
        self.proof = proof
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()
    
    # compute a hash with the given block data
    def compute_hash():
        # construct the string with our data
        block = "{}{}{}{}{}".format(self.index, self.proof, self.prev_hash, self.data, self.timestamp)
        # generate and return the block's hash
        return hashlib.sha256(block.encode()).hexdigest()

    # python equiv of toString()
    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof, self.prev_hash, self.data, self.timestamp)
        
    
