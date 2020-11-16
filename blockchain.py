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

# part-2 Mining our blockchain