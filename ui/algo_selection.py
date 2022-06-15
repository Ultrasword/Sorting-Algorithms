from . import box

import importlib.util
import os


class AlgoSelection(box.Box):
    def __init__(self, left, top, right, bottom, parent=None):
        super().__init__(left, top, right, bottom, parent)
        # algorithms :)
        # load all from algorithms folder at start
        self.algorithms = []
        for file in os.listdir("algorithms"):
            # load python script
            spec = importlib.util.spec_from_file_location("data", "algorithms/" + file)
            mod = importlib.util.module_from_spec(spec)
            algo = mod.setup()
            self.algorithms.append(algo)
            # add children
            


