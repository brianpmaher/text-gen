#/usr/bin/env python2.7

import random
import sys


class MarkovChain():
    def __init__(self, parsed_text):
        self.chain = {}

        words_count = 0
        for i in range(len(parsed_text) - 2):
            word1 = parsed_text[i]
            word2 = parsed_text[i+1]
            product = parsed_text[i+2]
            pair = word1 + ' ' + word2

            if pair in self.chain:
                if product in self.chain[pair]:
                    self.chain[pair][product] += 1
                else:  # product has not been seen yet, create it
                    self.chain[pair][product] = 1  # start the count at 1
            else:  # pair had not been seen yet, create it
                self.chain[pair] = { product: 1 }
            words_count += 1

        print 'words: ' + str(words_count)


    def generate_text(self, word_count=100):
        # Get all starting pairs.
        start_pairs = []
        for pair in self.chain:
            if pair[0].isupper():
                start_pairs.append(pair)
        
        pair = start_pairs[random.randint(0, len(start_pairs)-1)]
        sys.stdout.write(pair)

        for _i in range(word_count):
            if '!' in pair or '?' in pair or '.' in pair:
                break
            if pair in self.chain:
                random_product_number = \
                    random.randint(0, len(self.chain[pair])-1)
                product_count = 0
                for product in self.chain[pair]:
                    if product_count == random_product_number:
                        selected_product = product
                        break
                    product_count += 1
                pair = pair.split(' ')[1] + ' ' + selected_product
                sys.stdout.write(' ' + selected_product)
        sys.stdout.write('\n')


