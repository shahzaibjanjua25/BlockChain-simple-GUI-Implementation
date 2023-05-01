import hashlib
import json
from time import time
import tkinter as tk
from block import Block
class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        new_block = Block(len(self.chain), time(), data, self.get_latest_block().hash)
        self.chain.append(new_block)

    def delete_block(self, block_index):
        if block_index <= 0 or block_index >= len(self.chain):
            return False
        self.chain.pop(block_index)
        for i in range(block_index, len(self.chain)):
            self.chain[i].index -= 1
        return True

    def modify_block(self, block_index, new_data):
        if block_index <= 0 or block_index >= len(self.chain):
            return False
        self.chain[block_index].data = new_data
        self.chain[block_index].hash = self.chain[block_index].calculate_hash()
        return True

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
        return True
