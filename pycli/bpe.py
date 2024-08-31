"""
This module contains the functionality to perform byte-pair encoding (BPE) on a given text. 

It supports both reading in directly from stdin as well as passing a file. 

The result of both is the same, a BPE encoded text printed to stdout. Using stdout in this fashion allows you to pipe the output to another command or redirect it to a file.

As an example, you can run the following command to encode a text file:
    
    $ python -m pycli bpe text.txt -v 50

This will encode the text in `text.txt` using a vocabulary size of 50 using the BPE algorithm. The result will be printed to stdout.

See more about the algorithm at https://en.wikipedia.org/wiki/Byte_pair_encoding
"""

import sys
import os
import transformers
from argparse import Namespace, _SubParsersAction
from collections import defaultdict

# Transformers is very verbose. We only want to log errors.
transformers.utils.logging.set_verbosity("CRITICAL")


class BPE:
    def __init__(self, args: Namespace):
        self.files = args.files
        self.vocab_size = args.vocab_size
        self.vocab_file = args.vocab_file

    @staticmethod
    def register_subcommand(subparser: _SubParsersAction):
        parser = subparser.add_parser(name="bpe")
        parser.add_argument("files", type=str, nargs="*", default=sys.stdin)
        parser.add_argument("-vs", dest="vocab_size", type=int, required=True)
        parser.add_argument("-vf", dest="vocab_file", type=str, required=True)

        parser.set_defaults(func=BPE)

    def run(self):
        checkpoint = "gpt2"
        tokenizer = transformers.AutoTokenizer.from_pretrained(checkpoint)
        text = None
        with open(self.files[0], "r") as f:
            text = f.read()

        vocab = None
        with open(self.vocab_file, "r", encoding="utf-8") as f:
            vocab = f.read()

        # pretokenize the string
        tokens = tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(vocab)

        # Using the words from tokens where tokens is a tuple of (word, offset) compute the frequency of the words
        word_freq = defaultdict(int)
        for word, offset in tokens:
            word_freq[word] += 1

        alphabet = []
        # get a list of unique characters from all words - this is the initial vocab
        for word in word_freq.keys():
            for c in word:
                if c in alphabet:
                    continue
                alphabet.append(c)

        vocab = ["<|endoftext|>"] + alphabet.copy()

        # Split each word into individual characters - necessary to begin building up the merge rules
        splits = {word: list(word) for word in word_freq.keys()}

        merges = {}
        while len(vocab) < self.vocab_size:
            try:
                pair_freq = self.compute_pair_frequencies(word_freq, splits)
                freq_pair = self.most_freq(pair_freq)
                if freq_pair is None:
                    break
                splits = self.merge(freq_pair, splits, word_freq)
                merges[freq_pair] = freq_pair[0] + freq_pair[1]
                vocab.append(freq_pair[0] + freq_pair[1])
            except Exception as e:
                print(e)
                break

        print(self.tokenize(text, merges))

    def merge(self, pair, splits, word_freq):
        a = pair[0]
        b = pair[1]
        for word in word_freq.keys():
            split = splits[word]

            if len(split) == 1:
                continue

            i = 0
            while i < len(split) - 1:
                if split[i] == a and split[i + 1] == b:
                    split = split[:i] + [a + b] + split[i + 2 :]
                else:
                    i += 1
            splits[word] = split
        return splits

    def compute_pair_frequencies(self, word_freq, splits):
        """
        Compute the frequencies of pairs of characters in words.

        Args:
            word_freq (dict): A dictionary containing words as keys and their corresponding frequencies as values.
            splits (dict): A dictionary containing words as keys and their corresponding splits as values.

        Returns:
            dict: A dictionary containing pairs of characters as keys and their frequencies as values.
        """
        pair_freq = defaultdict(int)
        # for the word and their corresponding frequency
        for word, freq in word_freq.items():
            # get the splits of that word
            split = splits[word]

            # if the split is just the length of one, then continue
            if len(split) == 1:
                continue

            # otherwise iterate over the split, getting each pair of characters
            for i in range(len(split) - 1):
                pair = (split[i], split[i + 1])
                # then add it to the pair_freq dict
                pair_freq[pair] += freq

        return pair_freq

    def most_freq(self, pair_freq):
        """
        Finds the most frequent pair in the given pair frequency dict.

        Args:
            pair_freq (dict): A dict of pairs (tuple) and their corresponding frequencies (int).

        Returns:
            tuple: The most frequent pair.

        """
        max_pair_size = 0
        max_pair = None
        for pair, freq in pair_freq.items():
            if freq > max_pair_size:
                max_pair_size = freq
                max_pair = pair

        return max_pair

    def tokenize(self, text, merges):
        checkpoint = "gpt2"
        tokenizer = transformers.AutoTokenizer.from_pretrained(checkpoint)
        tokens = tokenizer.backend_tokenizer.pre_tokenizer.pre_tokenize_str(text)
        pre_tok_text = [word for word, _ in tokens]
        splits = [list(word) for word in pre_tok_text]
        for pair, word in merges.items():
            for idx, split in enumerate(splits):
                i = 0
                while i < len(split) - 1:
                    if split[i] == pair[0] and split[i + 1] == pair[1]:
                        split = split[:i] + [pair[0] + pair[1]] + split[i + 2 :]
                    else:
                        i += 1
                splits[idx] = split

        return sum(splits, [])
