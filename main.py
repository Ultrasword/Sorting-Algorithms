import pygame

import engine
from engine import window, clock, user_input, handler, draw
from engine import filehandler, maths, animation, state, serialize
from engine import spritesheet, core_utils
from engine.globals import *

from ui import box, sorter, controller, button

# create essential instances
window.create_instance("Sorting", 1280, 720, f=pygame.RESIZABLE)
window.set_scaling(True)
# should use framebuffer!
window.change_framebuffer(1280, 720, pygame.SRCALPHA)

# ------------------------------ your code ------------------------------ #
FPS = 60 # change fps if needed
BACKGROUND = (0, 0, 0) # change background color if needed


HANDLER = state.State()
state.push_state(HANDLER)


MAIN = box.add_box_to_state(0, 0, 1, 1)

SORTER = MAIN.create_child(0.01, 0.01, 0.79, 0.99, ctype=sorter.Sorter)
SORTER.set_value_color((255, 0, 0))
SORTER.setup_sorter(100)
# randomize
SORTER.randomize()

CONTROLLER = MAIN.create_child(0.81, 0.01, 0.99, 0.99, ctype=controller.Controller)
CONTROLLER.set_fill_color((10, 10, 10))

def randomize(button):
    print("Randomizing")
    SORTER.randomize()

def sort(button):
    print("sort?")

RNG = CONTROLLER.create_child(0.1, 0.1, 0.4, 0.15, ctype=button.Button)
RNG.set_text("Randomize")
RNG.set_on_click(randomize)

SORT = CONTROLLER.create_child(0.5, 0.1, 0.8, 0.15, ctype=button.Button)
SORT.set_text("Sort!")
SORT.set_on_click(sort)

# ----------------------------------------------------------------------- #


clock.start(fps=FPS)
window.create_clock(clock.FPS)
running = True

while running:
    clock.update()

    # fill instance
    window.fill_buffer(BACKGROUND)

    # updates
    if state.CURRENT:
        state.CURRENT.update(clock.delta_time)

    # render
    window.push_buffer((0,0))

    # update display
    pygame.display.flip()

    # update keyboard and mouse
    user_input.update()
    # for loop through events
    for e in pygame.event.get():
        # handle different events
        if e.type == pygame.QUIT:
            running = False
        elif e.type == pygame.KEYDOWN:
            # keyboard press
            user_input.key_press(e)
        elif e.type == pygame.KEYUP:
            # keyboard release
            user_input.key_release(e)
        elif e.type == pygame.MOUSEMOTION:
            # mouse movement
            user_input.mouse_move_update(e)
        elif e.type == pygame.MOUSEBUTTONDOWN:
            # mouse press
            user_input.mouse_button_press(e)
        elif e.type == pygame.MOUSEBUTTONUP:
            # mouse release
            user_input.mouse_button_release(e)
        elif e.type == pygame.WINDOWRESIZED:
            # window resized
            window.handle_resize(e)
            user_input.update_ratio(window.WIDTH, window.HEIGHT, window.ORIGINAL_WIDTH, window.ORIGINAL_HEIGHT)
        elif e.type == pygame.WINDOWMAXIMIZED:
            # window maximized
            window.get_instance().fill(BACKGROUND)
            # re render all entities
            HANDLER.render_all()
            # push frame
            pygame.display.update()
            # prevent re push
            window.INSTANCE_CHANGED = False

     # update clock -- calculate delta time
    
    window.GLOBAL_CLOCK.tick(FPS)



pygame.quit()
