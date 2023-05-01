import tkinter as tk
from block import Block
from blockchain1 import Blockchain
from tkinter import simpledialog

class BlockchainGUI:
    def __init__(self, blockchain):
        self.blockchain = blockchain

        self.root = tk.Tk()
        self.root.title("Blockchain")

        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(self.frame, width=500, height=500)
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.block_frames = []

        self.add_button = tk.Button(self.root, text="Add Block", command=self.add_block)
        self.add_button.pack(padx=10, pady=10)


        self.draw_blocks()

        self.root.mainloop()

    def draw_blocks(self):
        for block_frame in self.block_frames:
            block_frame.destroy()

        self.block_frames = []

        for i, block in enumerate(self.blockchain.chain):
            block_frame = tk.Frame(self.canvas)
            block_frame.pack(side=tk.TOP, fill=tk.X)

            index_label = tk.Label(block_frame, text=f"Block {block.index}")
            index_label.pack(side=tk.LEFT, padx=10)

            data_label = tk.Label(block_frame, text=block.data)
            data_label.pack(side=tk.LEFT, padx=10)

            delete_button = tk.Button(block_frame, text="Delete", command=lambda index=block.index: self.delete_block(index))
            delete_button.pack(side=tk.RIGHT, padx=10)

            modify_button = tk.Button(block_frame, text="Modify", command=lambda index=block.index: self.modify_block(index))
            modify_button.pack(side=tk.RIGHT)

            self.block_frames.append(block_frame)

        self.canvas.update_idletasks()

        self.canvas.configure(scrollregion=self.canvas.bbox(tk.ALL))

    def add_block(self):
        data = tk.simpledialog.askstring("Add Block", "Enter data for new block:")
        if data:
            self.blockchain.add_block(data)
            self.draw_blocks()

    def delete_block(self, index):
        result = tk.messagebox.askquestion("Delete Block", f"Are you sure you want to delete block {index}?")
        if result == "yes":
            self.blockchain.delete_block(index)
            self.draw_blocks()

    def modify_block(self, index):
        data = tk.simpledialog.askstring("Modify Block", "Enter new data for block:")
        if data:
            self.blockchain.modify_block(index, data)
            self.draw_blocks()
