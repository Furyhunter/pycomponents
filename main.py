#!/usr/bin/env python2
import sys
import pygame
import imp
from pygame import time, display
from pygame.locals import *

from entity import *

FPS=120


def main(args):
  pygame.init()
  surf = display.set_mode((320, 240))
  display.set_caption('Hi nerds')
  clock = time.Clock()
  entities = []


# Make entities
  e = Entity()
  e.add_component(ScriptComponent('testcomponent'))
  entities.append(e)

  while True:
    for event in pygame.event.get():
      if event.type == QUIT:
        pygame.quit()
        return 0
    update(entities, surf, 1./FPS)
    clock.tick(FPS)
    display.update()

def update(entities, surface, delta):
  for e in entities:
    e.act(delta)
  for e in entities:
    e.draw(surface)

if __name__ == '__main__':
  sys.exit(main(sys.argv))
