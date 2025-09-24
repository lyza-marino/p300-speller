'''Visual Oddball program'''

import pygame as pg
import matplotlib as plt
import random
from muselsl import stream, list_muses, view, record

pg.init()

window_width = 1920
window_height = 1080
window_center_x = window_width / 2
window_center_y = window_height / 2
window = pg.display.set_mode((window_width, window_height))
trials = 5

star = [
    (window_center_x, window_center_y - 100),
    (window_center_x + 25, window_center_y - 25),
    (window_center_x + 100, window_center_y),
    (window_center_x + 25, window_center_y + 25),
    (window_center_x + 50, window_center_y + 100),
    (window_center_x, window_center_y + 50),
    (window_center_x - 50, window_center_y + 100),
    (window_center_x - 25, window_center_y + 25),
    (window_center_x - 100, window_center_y),
    (window_center_x - 25, window_center_y - 25)
    ]

#colors
gray = (105, 105, 105)
red = 'red'
#def random_shape_count():
for i in range(1, trials+1):
    window.fill((gray))
    pg.draw.line(window, 'black', 
                (window_center_x, window_center_y + 20), 
                (window_center_x, window_center_y - 20), 
                5)
    pg.draw.line(window, 'black',
                (window_center_x + 20, window_center_y), 
                (window_center_x - 20, window_center_y), 
                5)
    pg.display.flip()
    pg.time.wait(250)        
    
    total_shapes = int((random.random() * 15) + 1)
    for i in range(total_shapes):
        window.fill((gray))
        pg.display.update()
        pg.time.wait(250)
        
        pg.event.get()
        
        pg.draw.rect(window, 'cyan', (
            window_center_x - window_width/18, 
            window_center_y - window_height/24,   
            window_width/9, window_height/12
        ))
        pg.display.update()
        pg.time.wait(500)
        pg.event.get()

        window.fill(gray)
        pg.display.update()
        pg.event.get()


    
    pg.time.wait(250)
    pg.draw.polygon(window, red, star)
    pg.display.update()
    pg.time.wait(250)

    button_press = False
    while not button_press:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
                button_press = True

pg.quit()    


