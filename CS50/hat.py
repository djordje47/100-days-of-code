import random


class Hat:
    houses = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    @classmethod
    def sort(cls, name: str):
        print(cls.think(cls))
        print(name, 'is in', random.choice(cls.houses))

    # Returns string
    def think(self) -> str:
        print(self)
        return 'hmmmmm....'


def main():
    Hat.sort('Harry')


if __name__ == '__main__':
    main()
