from classes import Agent, Player, Monster

p1 = Player('Joshua Weber','Rogue','Dwarf',20,12,3)
print(p1.name)
p1.current_hp -= 8
print(p1.current_hp)
print(p1.POSSIBLE_STATUS_EFFECTS)
p1.takeDeathSave(True)