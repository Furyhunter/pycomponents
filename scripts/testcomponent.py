awesome = 0

def act(e, delta):
  global awesome
  e.pos.x += 1
  awesome += 1
  if awesome == 50:
    pass

  if awesome % 100 == 0:
    print 'awesome'

#def draw(e, surface):
#  pass
