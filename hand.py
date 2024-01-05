from abc import ABC, abstractmethod
from params import Position


class Hand(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def turn(self, pieces, index, direction):
        pass

    @abstractmethod
    def reset_pos(self, pieces):
        pass

    @abstractmethod
    def reset_color_edge(self, pieces, index):
        pass

    @abstractmethod
    def reset_color_corner(self, pieces, index, direction):
        pass

    @abstractmethod
    def R(self, pieces):
        pass

    @abstractmethod
    def Rp(self, pieces):
        pass

    @abstractmethod
    def U(self, pieces):
        pass

    @abstractmethod
    def Up(self, pieces):
        pass

    @abstractmethod
    def F(self, pieces):
        pass

    @abstractmethod
    def Fp(self, pieces):
        pass

    @abstractmethod
    def L(self, pieces):
        pass

    @abstractmethod
    def Lp(self, pieces):
        pass

    @abstractmethod
    def D(self, pieces):
        pass

    @abstractmethod
    def Dp(self, pieces):
        pass

    @abstractmethod
    def B(self, pieces):
        pass

    @abstractmethod
    def Bp(self, pieces):
        pass

    @abstractmethod
    def R2(self, pieces):
        pass

    @abstractmethod
    def U2(self, pieces):
        pass

    @abstractmethod
    def F2(self, pieces):
        pass

    @abstractmethod
    def L2(self, pieces):
        pass

    @abstractmethod
    def D2(self, pieces):
        pass

    @abstractmethod
    def B2(self, pieces):
        pass


class Default(Hand):
    def __init__(self):
        self.pos = [Position.dfl, Position.df, Position.dfr,
                    Position.dl, Position.d, Position.dr,
                    Position.dbl, Position.db, Position.dbr,
                    Position.fl, Position.f, Position.fr,
                    Position.l, None, Position.r,
                    Position.bl, Position.b, Position.br,
                    Position.ufl, Position.uf, Position.ufr,
                    Position.ul, Position.u, Position.ur,
                    Position.ubl, Position.ub, Position.ubr]

        # 24 25 26        ubl ub ubr
        # 21 22 23         ul  u  ur
        # 18 19 20        ufl uf ufr

        # 15 16 17         bl  b  br
        # 12 na 14          l      r
        #  9 10 11         fl  f  fr

        #  0  1  2        dfl df dfr
        #  3  4  5         dl  d  dr
        #  6  7  8        dbl db dbr

    def turn(self, pieces, index, direction):
        if direction == 0:
            pieces[index[0]], pieces[index[1]], pieces[index[2]], pieces[index[3]] = \
                pieces[index[3]], pieces[index[0]], pieces[index[1]], pieces[index[2]]
        else:
            pieces[index[0]], pieces[index[1]], pieces[index[2]], pieces[index[3]] = \
                pieces[index[1]], pieces[index[2]], pieces[index[3]], pieces[index[0]]

    def reset_pos(self, pieces):
        for i in range(27):
            if pieces[i] is not None:
                if pieces[i].get_pos() != self.pos[i]:
                    pieces[i].set_pos(self.pos[i])

    def reset_color_edge(self, pieces, index):
        for i in index:
            color_t = pieces[i].get_colors()
            pieces[i].set_colors(color_t[1], color_t[0])

    def reset_color_corner(self, pieces, index, direction):
        for i in index:
            color_t = pieces[i].get_colors()
            if direction == 0:
                pieces[i].set_colors(color_t[1], color_t[0], color_t[2])
            elif direction == 1:
                pieces[i].set_colors(color_t[0], color_t[2], color_t[1])
            else:
                pieces[i].set_colors(color_t[2], color_t[1], color_t[0])

    def R(self, pieces):
        self.turn(pieces, [5, 11, 23, 17], 0)
        self.turn(pieces, [2, 20, 26, 8], 0)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [2, 20, 26, 8], 0)

    def Rp(self, pieces):
        self.turn(pieces, [5, 11, 23, 17], 1)
        self.turn(pieces, [2, 20, 26, 8], 1)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [2, 20, 26, 8], 0)

    def U(self, pieces):
        self.turn(pieces, [19, 21, 25, 23], 0)
        self.turn(pieces, [18, 24, 26, 20], 0)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [18, 24, 26, 20], 1)

    def Up(self, pieces):
        self.turn(pieces, [19, 21, 25, 23], 1)
        self.turn(pieces, [18, 24, 26, 20], 1)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [18, 24, 26, 20], 1)

    def F(self, pieces):
        self.turn(pieces, [1, 9, 19, 11], 0)
        self.turn(pieces, [0, 18, 20, 2], 0)
        self.reset_pos(pieces)
        self.reset_color_edge(pieces, [1, 9, 19, 11])
        self.reset_color_corner(pieces, [0, 18, 20, 2], 2)

    def Fp(self, pieces):
        self.turn(pieces, [1, 9, 19, 11], 1)
        self.turn(pieces, [0, 18, 20, 2], 1)
        self.reset_pos(pieces)
        self.reset_color_edge(pieces, [1, 9, 19, 11])
        self.reset_color_corner(pieces, [0, 18, 20, 2], 2)

    def L(self, pieces):
        self.turn(pieces, [3, 9, 21, 15], 1)
        self.turn(pieces, [0, 18, 24, 6], 1)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [0, 18, 24, 6], 0)

    def Lp(self, pieces):
        self.turn(pieces, [3, 9, 21, 15], 0)
        self.turn(pieces, [0, 18, 24, 6], 0)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [0, 18, 24, 6], 0)

    def D(self, pieces):
        self.turn(pieces, [1, 5, 7, 3], 0)
        self.turn(pieces, [0, 2, 8, 6], 0)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [0, 2, 8, 6], 1)

    def Dp(self, pieces):
        self.turn(pieces, [1, 5, 7, 3], 1)
        self.turn(pieces, [0, 2, 8, 6], 1)
        self.reset_pos(pieces)
        self.reset_color_corner(pieces, [0, 2, 8, 6], 1)

    def B(self, pieces):
        self.turn(pieces, [7, 17, 25, 15], 0)
        self.turn(pieces, [6, 8, 26, 24], 0)
        self.reset_pos(pieces)
        self.reset_color_edge(pieces, [7, 17, 25, 15])
        self.reset_color_corner(pieces, [6, 8, 26, 24], 2)

    def Bp(self, pieces):
        self.turn(pieces, [7, 17, 25, 15], 1)
        self.turn(pieces, [6, 8, 26, 24], 1)
        self.reset_pos(pieces)
        self.reset_color_edge(pieces, [7, 17, 25, 15])
        self.reset_color_corner(pieces, [6, 8, 26, 24], 2)

    def R2(self, pieces):
        self.R(pieces)
        self.R(pieces)

    def U2(self, pieces):
        self.U(pieces)
        self.U(pieces)

    def F2(self, pieces):
        self.F(pieces)
        self.F(pieces)

    def L2(self, pieces):
        self.L(pieces)
        self.L(pieces)

    def D2(self, pieces):
        self.D(pieces)
        self.D(pieces)

    def B2(self, pieces):
        self.B(pieces)
        self.B(pieces)

    def scramble(self, pieces, turns):
        for t in turns:
            if t == 'R':
                self.R(pieces)
            elif t == 'R\'':
                self.Rp(pieces)
            elif t == 'R2':
                self.R2(pieces)
            elif t == 'U':
                self.U(pieces)
            elif t == 'U\'':
                self.Up(pieces)
            elif t == 'U2':
                self.U2(pieces)
            elif t == 'F':
                self.F(pieces)
            elif t == 'F\'':
                self.Fp(pieces)
            elif t == 'F2':
                self.F2(pieces)
            elif t == 'L':
                self.L(pieces)
            elif t == 'L\'':
                self.Lp(pieces)
            elif t == 'L2':
                self.L2(pieces)
            elif t == 'D':
                self.D(pieces)
            elif t == 'D\'':
                self.Dp(pieces)
            elif t == 'D2':
                self.D2(pieces)
            elif t == 'B':
                self.B(pieces)
            elif t == 'B\'':
                self.Bp(pieces)
            elif t == 'B2':
                self.B2(pieces)


class CrossAI(Hand):
    def reset_color_corner(self, pieces, index, direction):
        pass

    def reset_pos(self, pieces):
        pass

    def __init__(self):
        self.r = [2, 5, 10, 7]
        self.u = [8, 9, 11, 10]
        self.f = [0, 4, 8, 5]
        self.l = [1, 6, 9, 4]
        self.d = [0, 2, 3, 1]
        self.b = [3, 6, 11, 7]

    def turn(self, state, index, direction):
        s = state.copy()
        if direction == 0:
            s[index[0]], s[index[1]], s[index[2]], s[index[3]] = \
                s[index[3]], s[index[0]], s[index[1]], s[index[2]]
        else:
            s[index[0]], s[index[1]], s[index[2]], s[index[3]] = \
                s[index[1]], s[index[2]], s[index[3]], s[index[0]]
        return s

    def reset_color_edge(self, state, index):
        s = state.copy()
        for i in index:
            if s[i] is not None:
                x = list(s[i])
                x[1] = 1 - x[1]
                s[i] = (x[0], x[1])
        return s

    def get_pos(self, state):
        pos = []
        for i in range(12):
            if state[i] is not None:
                pos.append(i)
        return pos

    def R(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.r])
        s = self.turn(state, self.r, 0)
        return s, ['R'], c

    def Rp(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.r])
        s = self.turn(state, self.r, 1)
        return s, ['R\''], c

    def U(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.u])
        s = self.turn(state, self.u, 0)
        return s, ['U'], c

    def Up(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.u])
        s = self.turn(state, self.u, 1)
        return s, ['U\''], c

    def F(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.f])
        s = self.turn(state, self.f, 0)
        s = self.reset_color_edge(s, self.f)
        return s, ['F'], c

    def Fp(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.f])
        s = self.turn(state, self.f, 1)
        s = self.reset_color_edge(s, self.f)
        return s, ['F\''], c

    def L(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.l])
        s = self.turn(state, self.l, 0)
        return s, ['L'], c

    def Lp(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.l])
        s = self.turn(state, self.l, 1)
        return s, ['L\''], c

    def D(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.d])
        s = self.turn(state, self.d, 0)
        return s, ['D'], c

    def Dp(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.d])
        s = self.turn(state, self.d, 1)
        return s, ['D\''], c

    def B(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.b])
        s = self.turn(state, self.b, 1)
        s = self.reset_color_edge(s, self.b)
        return s, ['B'], c

    def Bp(self, state):
        pos = self.get_pos(state)
        c = 5 - len([v for v in pos if v in self.b])
        s = self.turn(state, self.b, 0)
        s = self.reset_color_edge(s, self.b)
        return s, ['B'], c

    def R2(self, state):
        s, _, _ = self.R(state)
        s, _, c = self.R(s)
        return s, ['R2'], c

    def U2(self, state):
        s, _, _ = self.U(state)
        s, _, c = self.U(s)
        return s, ['U2'], c

    def F2(self, state):
        s, _, _ = self.F(state)
        s, _, c = self.F(s)
        return s, ['F2'], c

    def L2(self, state):
        s, _, _ = self.L(state)
        s, _, c = self.L(s)
        return s, ['L2'], c

    def D2(self, state):
        s, _, _ = self.D(state)
        s, _, c = self.D(s)
        return s, ['D2'], c

    def B2(self, state):
        s, _, _ = self.B(state)
        s, _, c = self.B(s)
        return s, ['B2'], c
