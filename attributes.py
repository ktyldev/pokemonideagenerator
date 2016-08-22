import random

# lists ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TYPES = [
    'normal', 'fire', 'fighting', 'water',
    'flying', 'grass', 'poison', 'electric',
    'ground', 'psychic', 'rock', 'ice',
    'bug', 'dragon', 'ghost', 'dark', 'steel',
    'fairy'
]
COLOURS = [
    'red', 'blue', 'green', 'yellow', 'brown',
    'black', 'white', 'pink', 'purple'
]
SIZES = [
    'really small', 'sorta small', 'human sized',
     'pretty big', 'fucken huge'
 ]


# static helpers ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
def one_or_two():
    """
    Returns either 1 or 2 as an int.
    :return:
    """
    return random.randint(1, 2)


class Attribute:
    def __init__(self, name, options):
        self.name = name
        self.list = options

    def random_choice(self):
        return str(random.choice(self.list))

    def get(self):
        return self.random_choice()

    def describe(self):
        return self.name + ': ' + self.get()


class PokemonType(Attribute):
    def __init__(self):
        super().__init__('Type', TYPES)

    def get(self):
        """
        Gets a random type combination. Returns a string.
        :return:
        """
        type_a = self.random_choice()
        type_b = None

        if one_or_two() > 1:
            candidate = self.random_choice()
            if candidate != type_a:
                type_b = candidate

        if type_b is not None:
            return str(type_a + '/' + type_b)
        else:
            return type_a


class Colour(Attribute):
    def __init__(self):
        super().__init__('Colour', COLOURS)


class Evolutions(Attribute):
    def __init__(self):
        super().__init__('Evolutions', [1, 2, 3, 4])


class Size(Attribute):
    def __init__(self):
        super().__init__('Size', SIZES)
