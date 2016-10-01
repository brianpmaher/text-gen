#/usr/bin/env python2.7

import re as regex


class Parser():
    def __init__(self, file_name):
        self.parsed_text = []

        with open(file_name, 'r') as input_file:
            text_input = input_file.read()

            # Parse all text along with its punctuation.
            text_regex = r'[\w\,\.\/\?\;\:\'\"\\\!]+'
            self.parsed_text = regex.findall(text_regex, text_input)
