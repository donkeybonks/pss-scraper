import pprint
from xml.dom import minidom
from multiprocessing.dummy import Pool as ThreadPool

from rooms import *
from characters import *
from files import *
from sprites import *
from animations import *

# Read room data
rooms = list(load_rooms())
characters = characters_dictionary()
files = files_dictionary()
sprites = sprites_dictionary()
animations = animations_dictionary()

print("Rooms: {0} total".format(len(rooms)))
print("Characters: {0} total".format(len(characters)))
print("Files: {0} total".format(len(files)))
print("Animations: {0} total".format(len(animations)))

pprint.pprint(rooms)
pprint.pprint(characters)
pprint.pprint(sprites)
pprint.pprint(animations)

print("Saving animations ..")

def save_sprite_lambda(anim):
    print("Saving {0}...".format(anim.key()))
    save_animation(anim, sprites, files)

pool = ThreadPool(30)
pool.map(save_sprite_lambda, animations.values())
pool.close()
pool.join()

#for anim in animations.values():
#    print("Saving {0}...".format(anim.key()))
#    save_animation(anim, sprites, files)


#print("Saving files ..")

#def save_file_lambda(file):
#    print("Saving {0}...".format(file.filename()))
#    save_file(file)

#pool = ThreadPool(30)
#pool.map(save_file_lambda, files)
#pool.close()
#pool.join()
