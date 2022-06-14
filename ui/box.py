from engine import handler, window, state, filehandler, user_input


BOX_TYPE = "box_type"


def add_box_to_state(left: float, top: float, right: float, bottom: float, parent = None, ctype=None):
    ctype = Box if ctype == None else ctype
    box = ctype(left, top, right, bottom, parent)
    state.CURRENT.add_persist_entity(box)
    return box


class Box(handler.PersistentObject):
    def __init__(self, left: float, top: float, right: float, bottom: float, parent = None):
        super().__init__()
        self.object_type = BOX_TYPE

        # simple OOP layout
        self.parent = parent
        self.frect = handler.Rect(left, top, right, bottom)
        self.rect = handler.Rect(0, 0, 0, 0)

        # properties
        self.dirty = True
        self.children = []
        self.fill_color = (0, 0, 0)
        self.surface = None

        # create
        self.create()

    def create(self):
        if self.parent:
            self.rect.pos = (self.parent.rect.x + self.parent.rect.w * self.frect.x, self.parent.rect.y + self.parent.rect.h * self.frect.y)
            self.rect.area = (self.parent.rect.w * (self.frect.w-self.frect.x), self.parent.rect.h * (self.frect.h - self.frect.y))
        else:
            self.rect.pos = (window.WIDTH * self.frect.x, window.HEIGHT * self.frect.y)
            self.rect.area = (window.WIDTH * (self.frect.w-self.frect.x), window.HEIGHT * (self.frect.h - self.frect.y))
        
        self.surface = filehandler.make_surface(int(self.rect.w), int(self.rect.h))
    
    def create_child(self, left: float, top: float, right: float, bottom: float, ctype=None):
        child = add_box_to_state(left, top, right, bottom, parent=self, ctype=ctype)
        self.children.append(child)
        return child
    
    def set_fill_color(self, color):
        self.fill_color = color
        self.dirty = True
    
    def update(self, dt):
        if self.dirty:
            self.dirty = False
            self.surface.fill(self.fill_color)
    
    def render(self):
        window.get_framebuffer_for_draw().blit(self.surface, self.rect.topleft)
    
    # utility functions
    def is_hovering(self):
        mpos = user_input.get_mouse_pos()
        if mpos[0] < self.rect.x or mpos[0] > self.rect.right:
            return False
        if mpos[1] < self.rect.y or mpos[1] > self.rect.bottom:
            return False
        return True
    
    def clicked(self):
        return self.is_hovering() & user_input.mouse_button_clicked(1)


