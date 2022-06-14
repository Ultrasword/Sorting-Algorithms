from . import box
from engine import draw

from random import sample


class Sorter(box.Box):
    def __init__(self, left, top, right, bottom, parent=None):
        super().__init__(left, top, right, bottom, parent)
        # algorithm stuff
        self.value_count = 0
        self.values = []
        self.value_color = (255, 255, 255)
        self.value_width = 0
        self.padding = (5, 5)
    
    def setup_sorter(self, value_count: int):
        self.value_count = value_count
        self.values = [(self.rect.h-self.padding[1]*2) * (i/value_count) for i in range(value_count)]
        self.value_width = (self.rect.w-self.padding[0] * 2) // self.value_count

    def set_value_color(self, color):
        self.value_color = color
    
    def update(self, dt):
        if self.dirty:
            self.dirty = False
            self.surface.fill(self.fill_color)
            # now we draw the values
            for i in range(self.value_count):
                x, y = i * self.value_width, self.rect.h - self.values[i]
                w, h = self.value_width, self.rect.h
                draw.DRAW_RECT(self.surface, self.value_color, (x, y, w, h))

    def randomize(self):
        self.dirty = True
        old = self.values.copy()
        self.values = [i for i in sample(old, self.value_count)]

