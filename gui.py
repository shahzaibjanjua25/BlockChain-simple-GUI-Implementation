import tkinter as tk
from block import Block
from blockchain1 import Blockchain
from tkinter import simpledialog, messagebox

class BlockchainGUI:
    def __init__(self, blockchain):
        self.blockchain = blockchain

        # Create the root window
        self.root = tk.Tk()
        self.root.title("Blockchain")

        # Create a frame for the image
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(padx=10, pady=10)

        # Load the image
        self.image = tk.PhotoImage(file="block-chain.png")

        # Create a label for the image
        self.image_label = tk.Label(self.top_frame, image=self.image)
        self.image_label.pack(side=tk.LEFT)

        # Create the frame for the canvas and scrollbar
        self.frame = tk.Frame(self.root)
        self.frame.pack(padx=10, pady=10)

        # Create the canvas for the blocks
        self.canvas = tk.Canvas(self.frame, width=600, height=500)
        self.canvas.pack(side=tk.LEFT, padx=10, pady=10)

        # Create the scrollbar for the canvas
        self.scrollbar = tk.Scrollbar(self.frame, orient=tk.VERTICAL, command=self.canvas.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Configure the canvas to work with the scrollbar
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        # Initialize the list of block frames
        self.block_frames = []

        # Draw the initial blocks on the canvas
        self.draw_blocks()

        # Create a frame to hold the "Add Block" button
        self.bottom_frame = tk.Frame(self.root)
        self.bottom_frame.pack(side=tk.BOTTOM, pady=10)

        # Create the "Add Block" button
        self.add_button = tk.Button(self.bottom_frame, text="Add Block", command=self.add_block, bg="green", fg="white", width=20, height=2)
        self.add_button.pack(pady=10)

        # Start the main event loop
        self.root.mainloop()

    def draw_blocks(self):
        # Clear the existing block frames
        for block_frame in self.block_frames:
            block_frame.destroy()

        self.block_frames = []

        # Draw each block in the blockchain
        for i, block in enumerate(self.blockchain.chain):
            # Create a frame for the block
            block_frame = tk.Frame(self.canvas, bg="#F0F0F0", bd=1, relief=tk.SOLID)
            block_frame.pack(side=tk.TOP, fill=tk.X, pady=5)

            # Add the block index label
            index_label = tk.Label(block_frame, text=f"Block {block.index}", font=("Arial", 12))
            index_label.pack(side=tk.LEFT, padx=10)

            # Add the block data label
            data_label = tk.Label(block_frame, text=block.data, font=("Arial", 12), bg="#F0F0F0")
            data_label.pack(side=tk.LEFT, padx=10, fill=tk.X, expand=True)

            # Add the "Delete" button
            delete_button = tk.Button(block_frame, text="Delete", command=lambda index=block.index: self.delete_block(index), bg="red", fg="white")
            delete_button.pack(side=tk.RIGHT, padx=10)

            # Add the "Modify" button
            modify_button = tk.Button(block_frame, text="Modify", command=lambda index=block.index: self.modify_block(index), bg="blue", fg="white")
            modify_button.pack(side=tk.RIGHT, padx=5)

            # Add the block frame to the list of block frames
            self.block_frames.append(block_frame)
        

        # Update the canvas to show the new blocks
        self.canvas.update_idletasks()
        
        # Set the scroll region of the canvas to fit the blocks
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
