from cubescrambler import scrambler333
# import random


class Scrambler:
    def __init__(self):
        self.turns = []
        self.text = ''

        # self.base = ['R', 'U', 'F', 'L', 'D', 'B']
        # self.mdfr = ['', '\'', '2']

    def generate(self):
        # self.turns = []
        # self.text = ''
        #
        # count = random.randint(18, 21)
        # bl = random.randint(0, 5)
        #
        # for i in range(count):
        #     while True:
        #         bi = random.randint(0, 5)
        #         if bi % 3 != bl % 3:
        #             bl = bi
        #             break
        #     b = self.base[bi]
        #     m = self.mdfr[random.randint(0, 2)]
        #     t = b + m
        #
        #     self.turns.append(t)
        #     self.text += t + ' '

        self.text = scrambler333.get_WCA_scramble()
        self.turns = self.text.split()

        return self.turns, self.text
