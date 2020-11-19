# creating a block chain in python
# installed
# flask
# postman HTTP client

import datetime
import hashlib
import json
from flask import Flask, jsonify

# part-1 building a blockchain


class Blockchain:  # block chain class

    def __init__(self):  # class always start with init function and always take self argument
        self.chain = []  # initialize the blockchain list
        self.create_block(proof=1, previous_hash='0')  # create the genesis block

    def create_block(self, proof, previous_hash):  # create a new block with the help of proof, previous hash
        block = {'index': len(self.chain)+1,           # essential data of block will be saved in dictionary
                 'timestamp': str(datetime.datetime.now()),
                 'proof': proof,
                 'previous_hash': previous_hash,
                 }
        self.chain.append(block)  # append new block in chain
        return block

    def get_previous_block(self):  # get the last block of chain
        return self.chain[-1]

    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(str(new_proof**2 - previous_proof**2)).hexdigest()
            if hash_operation[:4] == '0000':
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    def hash(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(str(proof ** 2 - previous_proof ** 2)).hexdigest()
            if hash_operation[:4] != '0000':
                return False
            previous_block = block
            block_index +=1
        return True


# part-2 Mining our blockchain

