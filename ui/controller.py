from . import box


class Controller(box.Box):
    def __init__(self, left, top, right, bottom, parent=None):
        super().__init__(left, top, right, bottom, parent)
        # buttons and stuff
        # we want a randomize button, a sort button, and a list of algorithms we can scroll down

