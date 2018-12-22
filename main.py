from classes import Agent, Player, Monster
from tracker import Tracker
import os

def printAgents(agents):
    for agent in agents:
        print('{}'.format('-'*40))
        print("{} || HP: {}/{} | AC: {} | Init: {} | Alive: {} | Concious: {} | FDS: {}\n".format(agent.name, agent.current_hp, agent.total_hp, agent.armor_class, agent.init, agent.alive, agent.concious, agent.failed_death_saves))
        print("Active Status Effects: {}".format(agent.status_effects))
        print('{}'.format('-'*40))

p1 = Player('Joshua Weber','Rogue','Dwarf',20,12,3)
p2 = Player('Julie Weber','Paladin','Halfling',30,17,1)
m1 = Monster('Werewolf','Humanoid','x',30,12,2)
players = [p1,p2]
monsters = [m1]
game = Tracker(players,monsters)
printAgents(players)
p1.current_hp -= 8
printAgents(players)
p1.takeDeathSave()
printAgents(players)

print(isinstance(p1, Player))

x = {'a':1, 'b':10, 'c':3}

x.pop('a')

print('{}'.format('-_-'*20))

initiative_rolls = {p1.name: 14, p2.name: 12, m1.name: 17}

game.determine_intiative(initiative_rolls)