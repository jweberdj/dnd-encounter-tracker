import operator
from classes import Agent, Player, Monster

class Tracker:

    def __init__(self, players, monsters):
        self.players = players
        self.monsters = monsters

        self.round_count = 0
        self.initiative_queue = []

    def determine_intiative(self, agent_rolls):
        # `agent_rolls` should be a dict type with keys('Agent_object' : 'roll_value')
        while len(agent_rolls) != 0:
            max_dict_obj = max(agent_rolls.items())
            if isinstance(agent_rolls[max_dict_obj[0]], Player):
                self.initiative_queue.append(self.players(max_dict_obj[0]))
            else:
                self.initiative_queue.append(self.monsters(max_dict_obj[0]))
            agent_rolls.pop(max_dict_obj[0])
        print(self.initiative_queue)