
import tkinter as tk
from block import Block
from blockchain1 import Blockchain
from gui import BlockchainGUI
if __name__ == '__main__':
    blockchain = Blockchain()
    gui = BlockchainGUI(blockchain)
    