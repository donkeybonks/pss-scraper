import urllib.request
from util import *
from xml.dom import minidom
from PIL import Image # pip install pillow

# Constants
SPRITES_URL = r'http://api2.pixelstarships.com/FileService/ListSprites'

class Sprite:
    def __init__(self, source):
        self.SpriteId = source.attributes['SpriteId'].value
        self.ImageFileId = source.attributes['ImageFileId'].value
        self.X = source.attributes['X'].value
        self.Y = source.attributes['Y'].value
        self.Width = source.attributes['Width'].value
        self.Height = source.attributes['Height'].value
        self.SpriteKey = source.attributes['SpriteKey'].value

    def __repr__(self):
        str = "{{ Sprite {0}: ".format(self.SpriteId)
        str += "ImageFileId='{0}', ".format(self.ImageFileId)
        str += "X='{0}', ".format(self.X)
        str += "Y='{0}', ".format(self.Y)
        str += "Width='{0}', ".format(self.Width)
        str += "Height='{0}', ".format(self.Height)
        str += "SpriteKey='{0}', ".format(self.SpriteKey)
        return str

    def id(self):
        return int(self.SpriteId)

    def file_id(self):
        return int(self.ImageFileId)

    def left(self):
        return int(self.X)

    def top(self):
        return int(self.Y)

    def width(self):
        return int(self.Width)

    def height(self):
        return int(self.Height)

    def key(self):
        return str(self.SpriteKey)

    # Using the passed file_dict, return the PIL image of this sprite
    def image(self, file_dict):
        url = file_dict[self.file_id()].remote_filename()
        img = Image.open(urllib.request.urlopen(url))
        left = self.left()
        upper = self.top()
        right = left + self.width()
        lower = upper + self.height()
        return img.crop((left, upper, right, lower))


# Load sprites from remote as a list
def load_sprites():
    with urllib.request.urlopen(SPRITES_URL) as response:
        source = response.read()
    source = source.decode("utf-8")
    xmldoc = minidom.parseString(source)
    for spr in xmldoc.getElementsByTagName('Sprite'):
        yield Sprite(spr)

# Return a dictionary of sprites loaded and keyed by id
def sprites_dictionary():
    sprites = load_sprites()
    return dict((spr.id(), spr) for spr in sprites)

# Save a sprite given the file dictionary to extract from
def save_sprite(sprite, file_dict):
    sprite.image(file_dict).save("sprites/" + sprite.key() + ".png")

