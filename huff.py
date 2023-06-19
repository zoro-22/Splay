class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None


def build_huffman_tree(characters, frequencies):
    nodes = [HuffmanNode(char, freq) for char, freq in zip(characters, frequencies)]

    while len(nodes) > 1:
        nodes = sorted(nodes, key=lambda x: x.freq)
        left_node = nodes[0]
        right_node = nodes[1]
        merged_freq = left_node.freq + right_node.freq
        merged_node = HuffmanNode(None, merged_freq)
        merged_node.left = left_node
        merged_node.right = right_node
        nodes = nodes[2:]
        nodes.append(merged_node)

    return nodes[0]


def build_codeword_table(huffman_tree_root):
    codeword_table = {}

    def traverse(node, codeword):
        if node.char:
            codeword_table[node.char] = codeword
        else:
            traverse(node.left, codeword + '0')
            traverse(node.right, codeword + '1')

    traverse(huffman_tree_root, '')
    return codeword_table

def compress(data, codeword_table):
    compressed_data = ''.join(codeword_table[char] for char in data)
    return compressed_data

# Get user input
num_characters = int(input("Enter the number of characters: "))

characters = []
frequencies = []

for i in range(num_characters):
    char = input(f"Character {i+1}: ")
    freq = int(input("Frequency: "))
    characters.append(char)
    frequencies.append(freq)

message = input("Enter the message to be encoded: ")

# Build Huffman tree and codeword table
huffman_tree_root = build_huffman_tree(characters, frequencies)
codeword_table = build_codeword_table(huffman_tree_root)
print(codeword_table)
# Compress the message
compressed_data = compress(message, codeword_table)
print("Compressed data:", compressed_data)

