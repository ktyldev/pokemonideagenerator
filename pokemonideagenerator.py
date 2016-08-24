import sys
import argparse

from attributes import *


class PokemonIdea:
    def __init__(self):
        self.attributes = [
            PokemonType(),
            Colour(),
            Evolutions(),
            Size()
        ]

    def describe(self):
        """
        describe the idea!
        Should print out a bunch of information about this idea
        :return:
        """

        for attr in self.attributes:
            print(attr.describe())


def check_args(args=None):
    parser = argparse.ArgumentParser(description='Generate some Pokemon ideas')
    parser.add_argument('count', metavar='C', type=int, help='number of ideas to generate')
    return parser.parse_args(args)


def run(count):
    for i in range(0, count):
        print('Idea ID: ' + str(i))
        idea = PokemonIdea()
        idea.describe()
        print('')


if __name__ == '__main__':
    namespace = check_args(sys.argv[1:])
    run(namespace.count)


