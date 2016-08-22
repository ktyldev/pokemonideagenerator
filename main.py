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


for i in range(0, 10):
    print('Idea ID: ' + str(i))
    idea = PokemonIdea()
    idea.describe()
    print('')
