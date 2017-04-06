import pprint
from xml.dom import minidom
from multiprocessing.dummy import Pool as ThreadPool

from rooms import *
from characters import *
from files import *
from sprites import *
from animations import *
from crafts import *
from backgrounds import *

# Read room data
rooms = list(load_rooms())
characters = characters_dictionary()
files = files_dictionary()
sprites = sprites_dictionary()
animations = animations_dictionary()
crafts = crafts_dictionary()
backgrounds = backgrounds_dictionary()

print("Rooms: {0} total".format(len(rooms)))
print("Characters: {0} total".format(len(characters)))
print("Files: {0} total".format(len(files)))
print("Animations: {0} total".format(len(animations)))
print("Crafts: {0} total".format(len(crafts)))

#print.pprint(rooms)
#pprint.pprint(characters)
pprint.pprint(backgrounds)
#pprint.pprint(animations)

#print("Saving animations ..")

#def save_sprite_lambda(anim):
#    print("Saving {0}...".format(anim.key()))
#    save_animation(anim, sprites, files)

#pool = ThreadPool(30)
#pool.map(save_sprite_lambda, animations.values())
#pool.close()
#pool.join()

#for anim in animations.values():
#    print("Saving {0}...".format(anim.key()))
#    save_animation(anim, sprites, files)


#print("Saving files ..")

#def save_file_lambda(file):
#    print("Saving {0}...".format(file.filename()))
#    save_file(file)

#pool = ThreadPool(30)
#pool.map(save_file_lambda, files.values())
#pool.close()
#pool.join()

#print("Saving sprites ..")

#def save_sprite_lambda(sprite):
#    print("Saving {0}...".format(sprite.key()))
#    save_sprite(sprite, files)

#pool = ThreadPool(30)
#pool.map(save_sprite_lambda, sprites.values())
#pool.close()
#pool.join()
