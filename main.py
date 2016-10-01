#/usr/bin/env python2.7

from parser import Parser
from markov import MarkovChain
import argparse


def main():
    # Parse command line arguments.
    arg_parser = argparse \
        .ArgumentParser(description='Generate text using Markov Chains')
    arg_parser.add_argument('file_name', help='The name of the file to parse')
    args = arg_parser.parse_args()

    # Parse the file.
    parser = Parser(args.file_name)

    # Generate a Markov Chain from the parsed data.
    markov_chain = MarkovChain(parser.parsed_text)
    markov_chain.generate_text()

if __name__ == '__main__':
    main()

