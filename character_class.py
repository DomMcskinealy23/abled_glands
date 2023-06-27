class Character():
    def __init__(self, **kwargs):
        self.profession = ""
        self.charisma = ""
        self.combat = ""
        self.magic = ""
        self.sancity = ""
        self.scouting = ""
        self.thievery = ""
    
    def print_attributes(self):
         s = f"""
            Profession = {self.profession}
            Charisma = {self.charisma}
            Combat = {self.combat}
            Magic = {self.magic}
            Sancity = {self.sancity}
            Scouting = {self.scouting}
            Thievery = {self.thievery}
         """
         return s


def loadClass(player, profession, charisma, combat, magic, sancity, scouting, thievery):
        player.profession=profession,
        player.charisma=charisma,
        player.combat=combat,
        player.magic=magic,
        player.sancity=sancity,
        player.scouting=scouting,
        player.thievery=thievery


player = Character()
loadClass(player, "jdjdjdf", 2, 2, 2, 2, 2, 2)
print(player.print_attributes())