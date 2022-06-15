from . import box
from engine import filehandler


FONT_PATH = "assets/CALIBRI.TTF"
FONT_SIZE = 14


def default_function(button):
    print(button.text)


class Button(box.Box):
    def __init__(self, left, top, right, bottom, parent=None):
        super().__init__(left, top, right, bottom, parent)
        # add text
        self.text = ""
        self.text_rect = None
        self.text_render = None
        self.text_color = (0, 0, 0)
        self.set_fill_color((255, 255, 255))
        self.on_click = default_function

    def set_text(self, text: str):
        self.text = text
        self.dirty = True
        # render the text
        self.text_render = filehandler.get_font(FONT_PATH).get_font_size(FONT_SIZE).render(self.text, True, self.text_color)
        self.text_rect = self.text_render.get_rect()
        self.text_rect.center = (self.rect.w//2, self.rect.h//2)
    
    def set_on_click(self, _on_click):
        self.on_click = _on_click
    
    def update(self, dt):
        if self.dirty:
            self.dirty = False
            self.surface.fill(self.fill_color)
            self.render_children()
            # render the text in the center
            if self.text_render:
                self.surface.blit(self.text_render, self.text_rect)
                print("rendere to ", self.text_rect)
        if self.clicked():
            self.on_click(self)

