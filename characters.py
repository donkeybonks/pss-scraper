import urllib.request
from util import *
from xml.dom import minidom

# Constants
CHARACTERS_URL = r'http://api2.pixelstarships.com/CharacterService/ListAllCharacterDesigns2?languageKey=en'

class CharacterPart:
    def __init__(self, source):
        self.CharacterPartId = source.attributes['CharacterPartId'].value
        self.CharacterPartName = source.attributes['CharacterPartName'].value
        self.CharacterPartType = source.attributes['CharacterPartType'].value
        self.StandardSpriteId = source.attributes['StandardSpriteId'].value
        self.StandardFileId = source.attributes['StandardFileId'].value
        self.ActionFileId = source.attributes['ActionFileId'].value
        self.StandardFileId = source.attributes['StandardFileId'].value
        self.StandardBorderFileId = source.attributes['StandardBorderFileId'].value
        self.ActionBorderFileId = source.attributes['ActionBorderFileId'].value
        self.ActionSpriteId = source.attributes['ActionSpriteId'].value
        self.StandardBorderSpriteId = source.attributes['StandardBorderSpriteId'].value
        self.ActionBorderSpriteId = source.attributes['ActionBorderSpriteId'].value

    def __repr__(self):
        str = "{{ CharacterPart {0}: ".format(self.CharacterPartId)
        str += "CharacterPartName='{0}', ".format(self.CharacterPartName)
        str += "CharacterPartType='{0}', ".format(self.CharacterPartType)
        str += "StandardSpriteId='{0}', ".format(self.StandardSpriteId)
        str += "StandardFileId='{0}', ".format(self.StandardFileId)
        str += "StandardBorderFileId='{0}', ".format(self.StandardBorderFileId)
        str += "ActionBorderFileId='{0}', ".format(self.ActionBorderFileId)
        str += "ActionSpriteId='{0}', ".format(self.ActionSpriteId)
        str += "StandardBorderSpriteId='{0}', ".format(self.StandardBorderSpriteId)
        str += "ActionBorderSpriteId='{0}' }}".format(self.ActionBorderSpriteId)
        return str

    def id(self):
        return int(self.CharacterPart)

    def name(self):
        return str(self.CharacterPartName)

    def type(self):
        return str(self.CharacterPartType)

    def sprite_id(self):
        return int(self.StandardSpriteId)

    def file_id(self):
        return int(self.StandardFileId)

    def border_id(self):
        return int(self.StandardBorderFileId)

    def action_sprite_id(self):
        return int(self.ActionSpriteId)

    def action_file_id(self):
        return int(self.ActionFileId)

    def action_border_id(self):
        return int(self.ActionBorderSpriteId)

# Load character parts from <CharacterPart> tags on the given root node
def load_character_parts(source):
    for part in source.getElementsByTagName('CharacterPart'):
        yield CharacterPart(part)


class Character:
    def __init__(self, source):
        self.parts = list(load_character_parts(source))
        self.CharacterDesignId = source.attributes['CharacterDesignId'].value
        self.CharacterDesignName = source.attributes['CharacterDesignName'].value
        self.CharacterHeadPartId = source.attributes['CharacterHeadPartId'].value
        self.CharacterBodyPartId = source.attributes['CharacterBodyPartId'].value
        self.GenderType = source.attributes['GenderType'].value
        self.RaceType = source.attributes['RaceType'].value
        self.Hp = source.attributes['Hp'].value
        self.Pilot = source.attributes['Pilot'].value
        self.Attack = source.attributes['Attack'].value
        self.FireResistance = source.attributes['FireResistance'].value
        self.Repair = source.attributes['Repair'].value
        self.Weapon = source.attributes['Weapon'].value
        self.Shield = source.attributes['Shield'].value
        self.Engine = source.attributes['Engine'].value
        self.Research = source.attributes['Research'].value
        self.Level = source.attributes['Level'].value
        self.WalkingSpeed = source.attributes['WalkingSpeed'].value
        self.GasCost = source.attributes['GasCost'].value
        self.MineralCost = source.attributes['MineralCost'].value
        self.MinShipLevel = source.attributes['MinShipLevel'].value
        self.FinalHp = source.attributes['FinalHp'].value
        self.FinalPilot = source.attributes['FinalPilot'].value
        self.FinalAttack = source.attributes['FinalAttack'].value
        self.FinalRepair = source.attributes['FinalRepair'].value
        self.FinalWeapon = source.attributes['FinalWeapon'].value
        self.FinalShield = source.attributes['FinalShield'].value
        self.FinalEngine = source.attributes['FinalEngine'].value
        self.FinalResearch = source.attributes['FinalResearch'].value
        self.CharacterLegPartId = source.attributes['CharacterLegPartId'].value
        self.Rarity = source.attributes['Rarity'].value
        self.ProgressionType = source.attributes['ProgressionType'].value
        self.CharacterDesignDescription = source.attributes['CharacterDesignDescription'].value
        self.XpRequirementScale = source.attributes['XpRequirementScale'].value
        self.MaxCharacterLevel = source.attributes['MaxCharacterLevel'].value
        self.SpecialAbilityType = source.attributes['SpecialAbilityType'].value
        self.SpecialAbilityArgument = source.attributes['SpecialAbilityArgument'].value
        self.SpecialAbilityFinalArgument = source.attributes['SpecialAbilityFinalArgument'].value
        self.ProfileSpriteId = source.attributes['ProfileSpriteId'].value
        self.RunSpeed = source.attributes['RunSpeed'].value
        self.TrainingCapacity = source.attributes['TrainingCapacity'].value
        self.EquipmentMask = source.attributes['EquipmentMask'].value
        self.TapSoundFileId = source.attributes['TapSoundFileId'].value
        self.ActionSoundFileId = source.attributes['ActionSoundFileId'].value

    def __repr__(self):
        str = "{{ Character {0}: ".format(self.CharacterDesignId)
        str += "CharacterDesignName='{0}', ".format(self.CharacterDesignName)
        str += "CharacterHeadPartId='{0}', ".format(self.CharacterHeadPartId)
        str += "CharacterBodyPartId='{0}', ".format(self.CharacterBodyPartId)
        str += "GenderType='{0}', ".format(self.GenderType)
        str += "RaceType='{0}', ".format(self.RaceType)
        str += "Hp='{0}', ".format(self.Hp)
        str += "Pilot='{0}', ".format(self.Pilot)
        str += "Attack='{0}', ".format(self.Attack)
        str += "FireResistance='{0}', ".format(self.FireResistance)
        str += "Repair='{0}', ".format(self.Repair)
        str += "Weapon='{0}', ".format(self.Weapon)
        str += "Shield='{0}', ".format(self.Shield)
        str += "Engine='{0}', ".format(self.Engine)
        str += "Research='{0}', ".format(self.Research)
        str += "Level='{0}', ".format(self.Level)
        str += "WalkingSpeed='{0}', ".format(self.WalkingSpeed)
        str += "GasCost='{0}', ".format(self.GasCost)
        str += "MineralCost='{0}', ".format(self.MineralCost)
        str += "MinShipLevel='{0}', ".format(self.MinShipLevel)
        str += "FinalHp='{0}', ".format(self.FinalHp)
        str += "FinalPilot='{0}', ".format(self.FinalPilot)
        str += "FinalAttack='{0}', ".format(self.FinalAttack)
        str += "FinalRepair='{0}', ".format(self.FinalRepair)
        str += "FinalWeapon='{0}', ".format(self.FinalWeapon)
        str += "FinalShield='{0}', ".format(self.FinalShield)
        str += "FinalEngine='{0}', ".format(self.FinalEngine)
        str += "FinalResearch='{0}', ".format(self.FinalResearch)
        str += "CharacterLegPartId='{0}', ".format(self.CharacterLegPartId)
        str += "Rarity='{0}', ".format(self.Rarity)
        str += "ProgressionType='{0}', ".format(self.ProgressionType)
        str += "CharacterDesignDescription='{0}', ".format(self.CharacterDesignDescription)
        str += "XpRequirementScale='{0}', ".format(self.XpRequirementScale)
        str += "MaxCharacterLevel='{0}', ".format(self.MaxCharacterLevel)
        str += "SpecialAbilityType='{0}', ".format(self.SpecialAbilityType)
        str += "SpecialAbilityArgument='{0}', ".format(self.SpecialAbilityArgument)
        str += "SpecialAbilityFinalArgument='{0}', ".format(self.SpecialAbilityFinalArgument)
        str += "ProfileSpriteId='{0}', ".format(self.ProfileSpriteId)
        str += "RunSpeed='{0}', ".format(self.RunSpeed)
        str += "TrainingCapacity='{0}', ".format(self.TrainingCapacity)
        str += "EquipmentMask='{0}', ".format(self.EquipmentMask)
        str += "TapSoundFileId='{0}', ".format(self.TapSoundFileId)
        str += "ActionSoundFileId='{0}' }}".format(self.ActionSoundFileId)
        return str

    def id(self):
        return int(self.CharacterDesignId)


# Load characters from remote as a list
def load_characters():
    with urllib.request.urlopen(CHARACTERS_URL) as response:
        source = response.read()
    source = source.decode("utf-8")
    xmldoc = minidom.parseString(source)
    for design in xmldoc.getElementsByTagName('CharacterDesign'):
        yield Character(design)

# Return a dictionary of characters loaded and keyed by id
def characters_dictionary():
    chars = load_characters()
    return dict((char.id(), char) for char in chars)

