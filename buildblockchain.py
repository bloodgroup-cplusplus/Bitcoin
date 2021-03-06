"""" we'll shall start by first defining what our blocks will look like.
In blockchain, each block is stored with a timestamp and, optionally, an index. In snakeCoin, We're
going to store both. And to help ensure integrity throughout the blockchain, each block
will have a self-identifying hash. Like Bitcoin, each block's hash will be a cryptographic has of the block's index,
timestamp, data the has of the previous block


"""

import datetime as date
import hashlib as hasher


class Block :
    def __init__(self,index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data =data
        self.prvious_hash = previous_hash
        self.has = self.hash_block()



    def hash_block(self):
        sha = hasher.sha256()
        sha.update(str(self.index) + str(self.timestamp)+ str(self.data) + str( self.prvious_hash))
        return sha.hexdigest()



def create_genesis_block():
    # manually construct a block with index zero and arbitrary previous hash


    return Block(0,date.datetime.now(),"Genesis Block", "0")




def next_block(last_block):
    this_index = last_block.index+1
    this_timestamp = date.datetime.now()
    this_data = "Second Bailout for the Banks " + str(this_index)
    this_hash = last_block.hash()
    return Block(this_index, this_timestamp, this_data,this_hash)



# Create the blockchain and add the genesis block
blockchain = [create_genesis_block()]
previous_block = blockchain[0]

# How many blocks should we add to the chain
# after the genesis block
num_of_blocks_to_add = 20

# Add blocks to the chain
for i in range(0, num_of_blocks_to_add):
  block_to_add = next_block(previous_block)
  blockchain.append(block_to_add)
  previous_block = block_to_add
  # Tell everyone about it!
  print ("Block #{} has been added to the blockchain!".format(block_to_add.index))
  print ("Hash: {}\n".format(block_to_add.hash))


