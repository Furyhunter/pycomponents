# pycomponents

I got bored Friday night, and decided to learn Python. And then I found out
about metaprogramming, and made this. So I guess this is kind of cool.

Usage, or something:

```
from entity import *

e = Entity()
c = ScriptComponent('testcomponent')
e.add_component(ScriptComponent('testcomponent'))

e.act(1)

if e.c_ScriptComponent === c:
    print 'It works!'

```
