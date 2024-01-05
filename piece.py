from abc import ABC, abstractmethod
from params import Color, Position


class Piece(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_colors(self):
        pass

    @abstractmethod
    def get_pos(self):
        pass

    @abstractmethod
    def set_colors(self, *args, **kwargs):
        pass

    @abstractmethod
    def set_pos(self, pos: Position):
        pass


class Center(Piece):
    def __init__(self, color_0: Color, pos: Position):
        self.color_0 = color_0
        self.pos = pos

    def get_colors(self):
        return [self.color_0]

    def get_pos(self):
        return self.pos

    def set_colors(self, color_0: Color):
        self.color_0 = color_0

    def set_pos(self, pos: Position):
        self.pos = pos


class Edge(Piece):
    def __init__(self, color_0: Color, color_1: Color, pos: Position):
        self.color_0 = color_0
        self.color_1 = color_1
        self.pos = pos

    def get_colors(self):
        return [self.color_0, self.color_1]

    def get_pos(self):
        return self.pos

    def set_colors(self, color_0: Color, color_1: Color):
        self.color_0 = color_0
        self.color_1 = color_1

    def set_pos(self, pos: Position):
        self.pos = pos


class Corner(Piece):
    def __init__(self, color_0: Color, color_1: Color, color_2: Color, pos: Position):
        self.color_0 = color_0
        self.color_1 = color_1
        self.color_2 = color_2
        self.pos = pos

    def get_colors(self):
        return [self.color_0, self.color_1, self.color_2]

    def get_pos(self):
        return self.pos

    def set_colors(self, color_0: Color, color_1: Color, color_2: Color):
        self.color_0 = color_0
        self.color_1 = color_1
        self.color_2 = color_2

    def set_pos(self, pos: Position):
        self.pos = pos
