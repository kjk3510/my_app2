__author__ = 'Administrator'


import game_framework
import Player
import mainGame
from Ui import *
from pico2d import *

ui = None
name = "SelectState"
image = None
character = None
#def getUI():
#    global ui
 #   return ui

def enter():
    global image, ui
    image = load_image('selected.png')


def exit():
    global image
    del(image)


def handle_events():
    events = get_events()
    global x, y, PlayerName, ui
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()

        elif event.type == SDL_MOUSEMOTION:
            x, y = event.x, 800 - event.y

        elif event.type == SDL_MOUSEBUTTONDOWN:
            x, y = event.x, 800 - event.y
            if x > 61 and x < 220 and y > 296 and y < 488:
                ui = UI("Sunny")
                print("2", ui.name)
                #game_framework.push_state(mainGame)
                game_framework.change_state(mainGame)
            if x > 280 and x < 437 and y > 296 and y < 488:
                ui = UI("Raby")
                #game_framework.push_state(mainGame)
                game_framework.change_state(mainGame)
                #game_framework.change_state(main_raby)

        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            #elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            #    game_framework.change_state(main_sunny)


def draw():
    clear_canvas()
    image.draw_to_origin(0, 0, 500, 800)
    update_canvas()






def update():
    pass


def pause():
    pass


def resume():
    pass

