import urllib.request
import io
import imageio # pip install imageio
from util import *
from xml.dom import minidom

# Constants
ANIMATIONS_URL = r'http://api2.pixelstarships.com/AnimationService/ListAnimations'
DURATION_PER_SECOND = 40

class Animation:
    def __init__(self, source):
        self.AnimationId = source.attributes['AnimationId'].value
        self.Key = source.attributes['Key'].value
        self.AnimationSprites = source.attributes['AnimationSprites'].value
        self.Duration = source.attributes['Duration'].value

    def __repr__(self):
        str = "{{ Animation {0}: ".format(self.AnimationId)
        str += "Key='{0}', ".format(self.Key)
        str += "AnimationSprites='{0}', ".format(self.AnimationSprites)
        str += "Duration='{0}' }}".format(self.Duration)
        return str

    def id(self):
        return int(self.AnimationId)

    def key(self):
        return str(self.Key)

    def sprites(self):
        return map(int, str(self.AnimationSprites).split(","))

    def frameno(self):
        return len(str(self.AnimationSprites).split(","))

    def duration(self):
        return int(self.Duration)

    def duration_seconds(self):
        return self.duration() / DURATION_PER_SECOND


# Load animations from remote as a list
def load_animations():
    with urllib.request.urlopen(ANIMATIONS_URL) as response:
        source = response.read()
    source = source.decode("utf-8")
    xmldoc = minidom.parseString(source)
    for file in xmldoc.getElementsByTagName('Animation'):
        yield Animation(file)

# Return a dictionary of animations loaded and keyed by id
def animations_dictionary():
    anims = load_animations()
    return dict((anim.id(), anim) for anim in anims)

# Saves this animation as a gif
def save_animation(animation, sprite_dict, file_dict):
    sprites = []
    anim_sprites = animation.sprites();
    meta = {'duration': animation.duration_seconds() / animation.frameno()}
    # GIF-FI is the only one that works properly
    with imageio.get_writer("animations/" + animation.key() + ".gif", mode='I', format="GIF-FI") as writer:
        for sprite_id in anim_sprites:
            img = sprite_dict[sprite_id].image(file_dict)
            img = img.convert("RGBA")
            with io.BytesIO() as output:
                img.save(output, format="PNG")
                writer.append_data(imageio.imread(output.getvalue(), format="PNG"), meta)
