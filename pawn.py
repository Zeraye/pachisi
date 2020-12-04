from variables import pawns

class Pawn:

    def __init__(self, color, pos_index, pos_place):
        self.color = color
        self.pos_index = pos_index
        self.pos_place = pos_place

    def get_pos_index(self):
        return self.pos_index

    def get_pos_place(self):
        return self.pos_place

    def get_color(self):
        return self.color

    def move(self, score):
        pass

    def delete(self):
        pawns.remove(self)
        del self
