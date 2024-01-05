from hand import CrossAI
from queue import PriorityQueueWithFunction


class Solver:
    def __init__(self):
        self.state = [('B', 0), ('O', 0), ('R', 0), ('G', 0),
                      None, None, None, None,
                      None, None, None, None]
        self.goal = [('B', 0), ('O', 0), ('R', 0), ('G', 0),
                     None, None, None, None,
                     None, None, None, None]
        self.hand = CrossAI()

        #      11                 ?0
        #   9      10         ?0     ?0
        #       8                 ?0
        #   6       7         ?0     ?0
        #
        #   4       5         ?0     ?0
        #       0                 B0
        #   1       2         O0     R0
        #       3                 G0

    def set_state(self, state):
        self.state = state

    def heuristic(self, state):
        d = 0

        for i in range(12):
            if state[i] is not None:
                color = state[i][0]
                pos = state[i][1]

                if color == 'B':
                    if pos == 0 and (i == 1 or i == 2 or i == 3 or i == 8) or \
                            pos == 1 and (i == 4 or i == 5):
                        d += 1
                    elif pos == 1 and (i == 0 or i == 3 or i == 8 or i == 11):
                        d += 3
                    else:
                        if not (pos == 0 and i == 0):
                            d += 2
                elif color == 'R':
                    if pos == 0 and (i == 0 or i == 1 or i == 3 or i == 10 or
                                     i == 5 or i == 7):
                        d += 1
                    elif pos == 1 and (i == 1 or i == 2 or i == 9 or i == 10):
                        d += 3
                    else:
                        if not (pos == 0 and i == 2):
                            d += 2
                elif color == 'G':
                    if pos == 0 and (i == 0 or i == 1 or i == 2 or i == 11) or \
                            pos == 1 and (i == 6 or i == 7):
                        d += 1
                    elif pos == 1 and (i == 0 or i == 3 or i == 8 or i == 11):
                        d += 3
                    else:
                        if not (pos == 0 and i == 3):
                            d += 2
                else:
                    if pos == 0 and (i == 0 or i == 2 or i == 3 or i == 9 or
                                     i == 4 or i == 6):
                        d += 1
                    elif pos == 1 and (i == 1 or i == 2 or i == 9 or i == 10):
                        d += 3
                    else:
                        if not (pos == 0 and i == 1):
                            d += 2
        return d

    def get_successors(self, state):
        available = []
        pos = []
        successors = []

        r = [2, 5, 10, 7]
        u = [8, 9, 11, 10]
        f = [0, 4, 8, 5]
        l = [1, 6, 9, 4]
        d = [0, 2, 3, 1]
        b = [3, 6, 11, 7]

        for i in range(12):
            if state[i] is not None:
                pos.append(i)

        if len([v for v in pos if v in r]) != 0:
            available.append('R')
            available.append('R\'')
            available.append('R2')
        if len([v for v in pos if v in u]) != 0:
            available.append('U')
            available.append('U\'')
            available.append('U2')
        if len([v for v in pos if v in f]) != 0:
            available.append('F')
            available.append('F\'')
            available.append('F2')
        if len([v for v in pos if v in l]) != 0:
            available.append('L')
            available.append('L\'')
            available.append('L2')
        if len([v for v in pos if v in d]) != 0:
            available.append('D')
            available.append('D\'')
            available.append('D2')
        if len([v for v in pos if v in b]) != 0:
            available.append('B')
            available.append('B\'')
            available.append('B2')

        for t in available:
            if t == 'R':
                s, _, c = self.hand.R(state)
            elif t == 'R\'':
                s, _, c = self.hand.Rp(state)
            elif t == 'R2':
                s, _, c = self.hand.R2(state)
            elif t == 'U':
                s, _, c = self.hand.U(state)
            elif t == 'U\'':
                s, _, c = self.hand.Up(state)
            elif t == 'U2':
                s, _, c = self.hand.U2(state)
            elif t == 'F':
                s, _, c = self.hand.F(state)
            elif t == 'F\'':
                s, _, c = self.hand.Fp(state)
            elif t == 'F2':
                s, _, c = self.hand.F2(state)
            elif t == 'L':
                s, _, c = self.hand.L(state)
            elif t == 'L\'':
                s, _, c = self.hand.Lp(state)
            elif t == 'L2':
                s, _, c = self.hand.L2(state)
            elif t == 'D':
                s, _, c = self.hand.D(state)
            elif t == 'D\'':
                s, _, c = self.hand.Dp(state)
            elif t == 'D2':
                s, _, c = self.hand.D2(state)
            elif t == 'B':
                s, _, c = self.hand.B(state)
            elif t == 'B\'':
                s, _, c = self.hand.Bp(state)
            else:
                s, _, c = self.hand.B2(state)
            successors.append([s, [t], c])

        return successors

    def search(self):
        s = self.state.copy()
        fringe = PriorityQueueWithFunction(
            lambda x: x[2] + self.heuristic(x[0])
        )
        fringe.push((s, [], 0))
        mark_list = []

        while not fringe.isEmpty():
            (s, p, c) = fringe.pop()
            if self.heuristic(s) == 0:
                text = ''
                for t in p:
                    text = text + t + ' '
                return text

            if s not in mark_list:
                mark_list.append(s)
                successors = self.get_successors(s)

                for successor in successors:
                    fringe.push((successor[0], p + successor[1], c + successor[2]))
