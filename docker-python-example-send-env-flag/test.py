import argparse
parser = argparse.ArgumentParser()

parser.add_argument("-IMAGE", "--IMAGE_PATH", help="SET IMAGE PATH")
args = parser.parse_args()
print(args.IMAGE_PATH)