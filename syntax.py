import nltk
from nltk.parse import CoreNLPParser

# Initialize the parser
parser = CoreNLPParser(url='http://localhost:9000')

# Define the sentence to be parsed
sentence = "John is a computer scientist"

# Parse the sentence into a parse tree
tree = next(parser.parse(sentence.split()))

# Print the parse tree
print(tree)
