__author__ = 'WilsonKoder'

import os, sys, math, pygame, pygame.mixer
import random
from pygame.locals import *
#import euclid #from http://pyeuclid.googlecode.com/svn/trunk/euclid.py

#defining some colors
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
blue = 0, 255, 0
green = 0, 0, 255

colors = [black, red, blue, green]

gravity = pygame.math.Vector2(0, 80.0)
drag = 0
initial_velocity = 20

#define screen size
window_size = (800, 600)

#setup window
screen = pygame.display.set_mode(window_size)

class baseCircle:

    def __init__(self, position, size, color = (255, 255, 255), velocity = pygame.math.Vector2(0, 0), accel = pygame.math.Vector2(0, 0), width = 1):
        self.position = position
        self.size = size
        self.color = color
        self.width = width
        self.velocity = velocity
        self.accel = accel

    def display(self):
        rx, ry = int(self.position.x), int(self.position.y)
        pygame.draw.circle(screen, self.color, (rx, ry), self.size, self.width)

    def move(self):
        self.position += self.velocity * dtime
        self.velocity += self.accel * dtime
        self.position += self.velocity * drag * dtime
        self.bounce()

    def change_velocity(self, velocity):
        self.velocity = velocity

    def bounce(self):
        if self.position.x <= self.size:
            self.position.x = 2 * self.size - self.position.x
            self.velocity = self.velocity.reflect(pygame.math.Vector2(1, 0))

        elif self.position.x >= window_size[0] - self.size:
            self.position.x = 2 * (window_size[0] - self.size) - self.position.x
            self.velocity = self.velocity.reflect(pygame.math.Vector2(1, 0))

        elif self.position.y <= self.size:
            self.position.y = 2 * self.size - self.position.y
            self.velocity = self.velocity.reflect(pygame.math.Vector2(0, 1))

        elif self.position.y >= window_size[1] - self.size:
            self.position.y = 2 * (window_size[1] - self.size) - self.position.y
            self.velocity = self.velocity.reflect(pygame.math.Vector2(0, 1))

    #Collisions Broke. Will fix soon.

    #def surface_distance(self, other, time):
        #radiiAB = self.size + other.size
        #posA = self.position + self.velocity * time + 0.5 * (self.accel * (time ** 2))
        #posB = other.position + other.velocity * time + 0.5 * (other.accel * (time ** 2))
        #posAB = pygame.math.Vector2().__abs__(posA) - pygame.math.Vector2().__abs__(posB)
        #return posAB - radiiAB

    #def collide(self, other):
        #if self.surface_distance(other, dtime) <= 0:
            #collision_vector = self.position - other.position
            #collision_vector.normalize()
            #self.velocity = self.velocity.reflect(collision_vector)





def get_random_velocity():
    new_angle = random.uniform(0, math.pi * 2)
    new_x = math.sin(new_angle)
    new_y = math.cos(new_angle)
    new_vector = pygame.math.Vector2(new_x, new_y)
    new_vector *= initial_velocity
    return new_vector





#get clock
clock = pygame.time.Clock()
#setting window title
pygame.display.set_caption("Koding Physics Demo")

max_circles = 10
circles = []

for n in range(max_circles):
    size = random.randint(10, 20)
    x = random.randint(size, window_size[0] - size)
    y = random.randint(size, window_size[1] - size)
    color = random.choice(colors)
    velocity = get_random_velocity()
    circle = baseCircle(pygame.math.Vector2(x, y), size, color, velocity, gravity)
    circles.append(circle)

#fps stuff
fps_limit = 60
running = True

while running:
    #limit fps
    dtime_ms = clock.tick(fps_limit)
    dtime = dtime_ms / 1000
    direction_tick = 0
    direction_tick += dtime


    #check events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.lock()
    #clear the screen
    screen.fill(white)

    for i, circle in enumerate(circles):
        circle.move()
        for circle2 in circles[i+1:]:
            circle.collide(circle2)
        circle.display()


    screen.unlock()
    #display everything on the screen
    pygame.display.flip()

print("Game Over")
pygame.quit()
sys.exit()