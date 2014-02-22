import imp
import string
import pygame

__all__ = ['Entity', 'Component', 'ScriptComponent']

class Entity():
  def __init__(self):
    self.pos = pygame.Rect(0., 0., 0., 0.)
    self._components = []
  
  def get_component(name):
    for c in _components:
      if c.__class__.__name__ == name:
        return c
    return None

  def components(self):
    return list(self._components)

  def add_component(self, component):
    self._components.append(component)
    component.owner = self

  def __getattr__(self, name):
    if string.find(name, 'c_') == 0:
      # find component
      for c in self._components:
        if c.__class__.__name__ == string.replace(name, 'c_', ''):
          return c
    else:
      # get from components
      for c in self._components:
        return _CallOnComponents(name, self._components)

class _CallOnComponents():
  def __init__(self, name, components):
    self.name = name
    self.components = components

  def __call__(self, *args):
    for c in self.components:
      func = getattr(c, self.name)
      func(*args)

class Component():
  def __init__(self):
    self.owner = None

  def act(self, delta):
    pass

  def draw(self, surface):
    pass

class ScriptComponent(Component):
  def __init__(self, modulename):
    Component.__init__(self)
    self._scriptmodule = imp.load_source('scripts.' + modulename, 'scripts/' +
        modulename + '.py')

  def act(self, delta):
    try:
      self._scriptmodule.act(self.owner, delta)
    except AttributeError as ae:
      pass # We don't care about missing functions

  def draw(self, surface):
    try:
      self._scriptmodule.draw(self.owner, surface)
    except AttributeError as ae:
      pass # We don't care about missing functions
