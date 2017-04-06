import urllib.request
from util import *
from xml.dom import minidom

# Constants
BACKGROUNDS_URL = r'http://api2.pixelstarships.com/BackgroundService/ListBackgrounds'

class Background:
    def __init__(self, source):
        self.BackgroundId = source.attributes['BackgroundId'].value
        self.BackgroundSpriteId = source.attributes['BackgroundSpriteId'].value
        self.FarObjectSpriteId = source.attributes['FarObjectSpriteId'].value
        self.MediumObjectSpriteId = source.attributes['MediumObjectSpriteId'].value
        self.CloseObjectSpriteId = source.attributes['CloseObjectSpriteId'].value
        self.BackgroundEffectType = source.attributes['BackgroundEffectType'].value
        self.BackgroundType = source.attributes['BackgroundType'].value

    def __repr__(self):
        str = "{{ Background {0}: ".format(self.BackgroundId)
        str += "BackgroundSpriteId='{0}', ".format(self.BackgroundSpriteId)
        str += "FarObjectSpriteId='{0}', ".format(self.FarObjectSpriteId)
        str += "MediumObjectSpriteId='{0}', ".format(self.MediumObjectSpriteId)
        str += "CloseObjectSpriteId='{0}', ".format(self.CloseObjectSpriteId)
        str += "BackgroundEffectType='{0}', ".format(self.BackgroundEffectType)
        str += "BackgroundType='{0}' }}".format(self.BackgroundType)
        return str

    def id(self):
        return int(self.BackgroundId)

    def sprite_id(self):
        return int(self.BackgroundSpriteId)


# Load crafts from remote as a list
def load_backgrounds():
    with urllib.request.urlopen(BACKGROUNDS_URL) as response:
        source = response.read()
    source = source.decode("utf-8")
    xmldoc = minidom.parseString(source)
    for bg in xmldoc.getElementsByTagName('Background'):
        yield Background(bg)

# Return a dictionary of crafts loaded and keyed by id
def backgrounds_dictionary():
    bgs = load_backgrounds()
    return dict((bg.id(), bg) for bg in bgs)

