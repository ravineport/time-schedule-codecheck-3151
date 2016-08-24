import argparse
from app.app import main

parser = argparse.ArgumentParser(description='Write description here')  
parser.add_argument('basic_arguments', nargs='*')

args = parser.parse_args()

main(args.basic_arguments, args)