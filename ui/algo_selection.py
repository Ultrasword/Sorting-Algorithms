from . import box, button

import importlib.util
import os


class AlgoSelection(box.Box):
    def __init__(self, left, top, right, bottom, parent=None):
        super().__init__(left, top, right, bottom, parent)
        # algorithms :)
        # load all from algorithms folder at start
        self.algorithms = {}
        self.sorter_object = []
    
    def set_sorter_object(self, sorter):
        self.sorter_object = sorter

    def _on_click(self, button):
        self.sorter_object.set_algorithm(self.algorithms[button.text])
        print("set algo to ", button.text)

    def setup(self):
        left = 0
        top = 0
        width = 0.5
        height = 0.2
        for file in os.listdir("algorithms"):
            if not file.endswith(".py"):
                continue
            # load python script
            mod = importlib.import_module("algorithms." + file[:-3])
            algo = mod.setup()
            algo.set_dataset(self.sorter_object)
            # add children
            but = self.create_child(left, top, left+width, top+height, ctype=button.Button)
            but.set_text(mod.NAME)
            self.algorithms[mod.NAME] = algo
            but.set_on_click(self._on_click)
            left += width
            if left >= 1:
                left = 0
                top += height
    
    def update(self, dt):
        if self.dirty:
            self.dirty = False
            self.surface.fill(self.fill_color)
            self.render_children()


