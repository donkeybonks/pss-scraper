import urllib.request
from util import *
from xml.dom import minidom

# Constants
ROOM_URL = r'http://api2.pixelstarships.com/RoomService/ListRoomDesigns2?languageKey=en'

class Room:
    def __init__(self, source):
        self.RoomDesignId = source.attributes['RoomDesignId'].value
        self.RoomName = source.attributes['RoomName'].value
        self.RoomShortName = source.attributes['RoomShortName'].value
        self.RoomType = source.attributes['RoomType'].value
        self.MineralCost = source.attributes['MineralCost'].value
        self.MaxSystemPower = source.attributes['MaxSystemPower'].value
        self.ConstructionTime = source.attributes['ConstructionTime'].value
        self.Capacity = source.attributes['Capacity'].value
        self.ReloadTime = source.attributes['ReloadTime'].value
        self.ImageSpriteId = source.attributes['ImageSpriteId'].value
        self.LogoSpriteId = source.attributes['LogoSpriteId'].value
        self.MaxPowerGenerated = source.attributes['MaxPowerGenerated'].value
        self.RandomImprovements = source.attributes['RandomImprovements'].value
        self.ImprovementAmounts = source.attributes['ImprovementAmounts'].value
        self.ManufactureCapacity = source.attributes['ManufactureCapacity'].value
        self.ManufactureRate = source.attributes['ManufactureRate'].value
        self.ManufactureType = source.attributes['ManufactureType'].value
        self.GasCost = source.attributes['GasCost'].value
        self.Level = source.attributes['Level'].value
        self.CategoryType = source.attributes['CategoryType'].value
        self.ConstructionSpriteId = source.attributes['ConstructionSpriteId'].value
        self.MinShipLevel = source.attributes['MinShipLevel'].value
        self.ItemRank = source.attributes['ItemRank'].value
        self.Rotate = source.attributes['Rotate'].value
        self.Rows = source.attributes['Rows'].value
        self.Columns = source.attributes['Columns'].value
        self.RoomDescription = source.attributes['RoomDescription'].value
        self.FlipOnEnemyShip = source.attributes['FlipOnEnemyShip'].value
        self.RootRoomDesignId = source.attributes['RootRoomDesignId'].value
        self.RefillUnitCost = source.attributes['RefillUnitCost'].value
        self.DefaultDefenceBonus = source.attributes['DefaultDefenceBonus'].value
        self.UpgradeFromRoomDesignId = source.attributes['UpgradeFromRoomDesignId'].value
        self.MissileDesignId = source.attributes['MissileDesignId'].value
        self.RaceId = source.attributes['RaceId'].value

    def __repr__(self):
        str = "{{ Room {0}: ".format(self.RoomDesignId)
        str += "RoomName='{0}', ".format(self.RoomName)
        str += "RoomShortName='{0}', ".format(self.RoomShortName)
        str += "RoomType='{0}', ".format(self.RoomType)
        str += "MineralCost='{0}', ".format(self.MineralCost)
        str += "MaxSystemPower='{0}', ".format(self.MaxSystemPower)
        str += "ConstructionTime='{0}', ".format(self.ConstructionTime)
        str += "Capacity='{0}', ".format(self.Capacity)
        str += "ReloadTime='{0}', ".format(self.ReloadTime)
        str += "ImageSpriteId='{0}', ".format(self.ImageSpriteId)
        str += "LogoSpriteId='{0}', ".format(self.LogoSpriteId)
        str += "MaxPowerGenerated='{0}', ".format(self.MaxPowerGenerated)
        str += "RandomImprovements='{0}', ".format(self.RandomImprovements)
        str += "ImprovementAmounts='{0}', ".format(self.ImprovementAmounts)
        str += "ManufactureCapacity='{0}', ".format(self.ManufactureCapacity)
        str += "ManufactureRate='{0}', ".format(self.ManufactureRate)
        str += "ManufactureType='{0}', ".format(self.ManufactureType)
        str += "GasCost='{0}', ".format(self.GasCost)
        str += "Level='{0}', ".format(self.Level)
        str += "CategoryType='{0}', ".format(self.CategoryType)
        str += "ConstructionSpriteId='{0}', ".format(self.ConstructionSpriteId)
        str += "MinShipLevel='{0}', ".format(self.MinShipLevel)
        str += "ItemRank='{0}', ".format(self.ItemRank)
        str += "Rotate='{0}', ".format(self.Rotate)
        str += "Rows='{0}', ".format(self.Rows)
        str += "Columns='{0}', ".format(self.Columns)
        str += "RoomDescription='{0}', ".format(self.RoomDescription)
        str += "FlipOnEnemyShip='{0}', ".format(self.FlipOnEnemyShip)
        str += "RootRoomDesignId='{0}', ".format(self.RootRoomDesignId)
        str += "RefillUnitCost='{0}', ".format(self.RefillUnitCost)
        str += "DefaultDefenceBonus='{0}', ".format(self.DefaultDefenceBonus)
        str += "UpgradeFromRoomDesignId='{0}', ".format(self.UpgradeFromRoomDesignId)
        str += "MissileDesignId='{0}', ".format(self.MissileDesignId)
        str += "RaceId='{0}' }}".format(self.RaceId)
        return str

    def name(self):
        return str(self.RoomName)

    def level(self):
        return int(self.Level)

    def capacity(self):
        return int(self.Capacity)

    def mineral_cost(self):
        return cost_with_units(int(self.MineralCost))

    def gas_cost(self):
        return cost_with_units(int(self.GasCost))

    def reload(self):
        return ticks_with_units_clarified(int(self.ReloadTime))

    def construction_time(self):
        return seconds_with_units(int(self.ConstructionTime))

    def rows(self):
        return int(self.Rows)

    def columns(self):
        return int(self.Columns)


def load_rooms():
    with urllib.request.urlopen(ROOM_URL) as response:
        source = response.read()
    source = source.decode("utf-8")
    xmldoc = minidom.parseString(source)
    for design in xmldoc.getElementsByTagName('RoomDesign'):
        yield Room(design)
