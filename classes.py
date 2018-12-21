class Agent:
    POSSIBLE_STATUS_EFFECTS = [
        'blinded',
        'charmed',
        'deafended',
        'fatigued',
        'frightened',
        'grappled',
        'incapacitated',
        'invisible',
        'paralyzed',
        'petrified',
        'poisoned',
        'prone',
        'restrained',
        'stunned',
        'unconcious',
        'exhaustion'
    ]

    def __init__(self, name, hp, ac, initiative):
        # Provided properties of Agent
        self.name = name
        self.total_hp = hp
        self.current_hp = hp
        self.armor_class = ac
        self.init = initiative
        self.alive = True
        self.concious = True
        self.failed_death_saves = 0

        # Dictionary of action names (keys) and sub-dictionaries containing action type and value
        self.actions = {}
        
        # list of strings representing status_effects
        self.status_effects = []

    def addAction(self, name, attack_mod, damage_mod):
        if name not in self.actions.keys():
            self.actions[name] = {'attack_mod': attack_mod, 'damage_mod': damage_mod}
        else:
            print("{} already exists in this character's list of actions.".format(name))

    def addStatusEffect(self, name):
        if name in self.POSSIBLE_STATUS_EFFECTS:
            self.status_effects.append(name)
        else:
            print("{} is not a possible status effect.".format(name))
    
    def takeDamage(self, value):
        self.current_hp -= value
        if not self.alive:
            print("{} is dead.".format(self.name))
        elif self.current_hp < (0 - self.total_hp):
            self.alive = False
        elif self.current_hp < 0:
            self.concious = False
    
    def kill(self):
        self.current_hp = 0
        self.concious = False
        self.alive = False
    
    def heal(self, value):
        if not self.alive:
            self.alive = True
            self.concious = True
            self.failed_death_saves = 0
            self.current_hp = 0 + value
        elif not self.concious:
            self.current_hp = 0 + value
            self.concious = True
            self.failed_death_saves = 0
        else:
            self.current_hp += value

    def stabilize(self):
        self.current_hp = 0
        self.failed_death_saves = 0

    def takeDeathSave(self):
        self.failed_death_saves += 1
        if self.failed_death_saves >= 3:
            self.alive = False

class Player(Agent):

    def __init__(self, name, _class, race, hp, ac, initiative):
        # Provided properties of Agent
        super().__init__(name, hp, ac, initiative)
        self._class = _class
        self.race = race


class Monster(Agent):

    def __init__(self, name, template, race, hp, ac, initiative):
        # Provided properties of Agent
        super().__init__(name, hp, ac, initiative)
        self.monster_race = race
        self.template = template

