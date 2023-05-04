import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str, help='your name')
parser.add_argument('--age', type=int, help='your age')
parser.add_argument('--gender', type=str, help='your gender')

args = parser.parse_args()

print('Name:', args.name)
print('Age:', args.age)
print('Gender:', args.gender)
