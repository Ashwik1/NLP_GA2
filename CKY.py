import argparse
import CNF
import nltk


class Set:
    def __init__(self, parent_set, child_set1, child_set2=None):
        self.parent_set = parent_set
        self.child_set1 = child_set1
        self.child_set2 = child_set2


class Parser:
    """
    Parse the given sentence in CNF grammar.
    """
    def __init__(self, grammar, sentence):
        """
        :param grammar: the grammar file
        :param sentence: the file of the sentence to be parsed
        """
        self.parse_table = None
        self.grammar = None
        self.change_grammar(grammar)
        self.complete_sentence(sentence)

    def complete_sentence(self, sentence):
        """
        :param sentence: the sentence to parse with self.grammar
        """
        with open(sentence) as fr:
            self.input = fr.readline().split()