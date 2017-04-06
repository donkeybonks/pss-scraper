import urllib.request
from util import *
from xml.dom import minidom

# Constants
CRAFTS_URL = r'http://api2.pixelstarships.com/RoomService/ListCraftDesigns'

class Craft:
    def __init__(self, source):
        self.CraftDesignId = source.attributes['CraftDesignId'].value
        self.CraftName = source.attributes['CraftName'].value
        self.FlightSpeed = source.attributes['FlightSpeed'].value
        self.Reload = source.attributes['Reload'].value
        self.SpriteId = source.attributes['SpriteId'].value
        self.MissileDesignId = source.attributes['MissileDesignId'].value
        self.Volley = source.attributes['Volley'].value
        self.VolleyDelay = source.attributes['VolleyDelay'].value
        self.Hp = source.attributes['Hp'].value

    def __repr__(self):
        str = "{{ Craft {0}: ".format(self.CraftDesignId)
        str += "CraftName='{0}', ".format(self.CraftName)
        str += "FlightSpeed='{0}', ".format(self.FlightSpeed)
        str += "Reload='{0}', ".format(self.Reload)
        str += "SpriteId='{0}', ".format(self.SpriteId)
        str += "MissileDesignId='{0}', ".format(self.MissileDesignId)
        str += "Volley='{0}', ".format(self.Volley)
        str += "VolleyDelay='{0}', ".format(self.VolleyDelay)
        str += "Hp='{0}' }}".format(self.Hp)
        return str

    def id(self):
        return int(self.CraftDesignId)

    def name(self):
        return str(self.CraftName)

    def speed(self):
        return int(self.FlightSpeed)

    def reload(self):
        return int(self.Reload)

    def sprite_id(self):
        return int(self.SpriteId)

    def missile_id(self):
        return int(self.MissileDesignId)

    def hp(self):
        return int(self.Hp)


# Load crafts from remote as a list
def load_crafts():
    with urllib.request.urlopen(CRAFTS_URL) as response:
        source = response.read()
    source = source.decode("utf-8")
    xmldoc = minidom.parseString(source)
    for design in xmldoc.getElementsByTagName('CraftDesign'):
        yield Craft(design)

# Return a dictionary of crafts loaded and keyed by id
def crafts_dictionary():
    crafts = load_crafts()
    return dict((craft.id(), craft) for craft in crafts)

