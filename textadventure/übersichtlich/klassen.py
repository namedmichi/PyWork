import random
from dataclasses import dataclass


@dataclass
class Item:
    weight: int
    worth: int


@dataclass
class Weapon(Item):
    wad: int
    name: str

    def rand_weap(self):
        rand = random.randint(0, 2)
        if rand == 0:
            self.wad = 100
            self.weight = 10
            self.name = "Breitschwert"
        if rand == 1:
            self.wad = 20
            self.weight = 5
            self.name = "Schwert"
        if rand == 2:
            self.wad = 1
            self.weight = 1
            self.name = "Stick"


@dataclass
class Potion(Item):
    pass


@dataclass
class HealthPotion(Potion):

    regenerated_health: int
    qty: int


@dataclass
class FightPotion(Potion):

    extra_ad: int
    qty: int


@dataclass
class Character:
    hp: int
    ad: int
    name: int

    def get_hit(self, ad):
        self.hp = self.hp - ad
        if self.hp <= 0:
            self.die()

    def is_dead(self):
        return self.hp <= 0

    def die(self):
        print(self.name + " starb")


class Goblin(Character):
    def __init__(self):
        Character.__init__(self, 100, 10, "Goblin")


class Ork(Character):
    def __init__(self):
        Character.__init__(self, 300, 30, "Ork")


@dataclass
class wInventory:

    winv: list

    def check_winv(self, p, weapon):
        test = p.winv[0].name
        test2 = weapon.name
        if test2 == test:
            return False
        else:
            return True

    def check_emptywinv(self, p):
        test = p.winv[0].name
        if test == "":
            return True
        else:
            return False

    def winv_add(self, weapon,):
        self.winv[0] = weapon


@dataclass
class Inventory:
    inv: dict

    def check_winv(self, p):
        pass

    def check_emptyinv(self, p):
        pass

    def inv_add(self, object,):
        self.inv[object] = 1


@dataclass
class Player(Character, wInventory, Inventory):

    max_hp: int

    def die(self):
        exit("Tot.")

    def rest(self):
        self.hp = self.max_hp


@dataclass
class Field:
    enemies: list

    def print_state(self):
        print("Du schaust dich um und siehst ")
        for i in self.enemies:
            print(i.name)

    @staticmethod
    def gen_random():
        rand = random.randint(0, 2)
        if rand == 0:
            return Field([])
        if rand == 1:
            return Field([Ork()])
        if rand == 2:
            return Field([Goblin(), Goblin(), Ork()])


@dataclass
class Map:

    state: list
    width: int
    height: int

    def __post_init__(self):
        self.x = 0
        self.y = 0
        for i in range(self.width):
            fields = []
            for j in range(self.height):
                fields.append(Field.gen_random())
            self.state.append(fields)

    def print_state(self):
        self.state[self.x][self.y].print_state()

    def get_enemies(self):
        return self.state[self.x][self.y].enemies

    def forward(self):
        if self.x == len(self.state) - 1:
            print("Du siehst hohe Berge die du nicht erklimmen kannst")
        else:
            self.x = self.x + 1

    def backwards(self):
        if self.x == 0:
            print("Du siehst Klippen du die nicht runter kommst")
        else:
            self.x = self.x - 1

    def right(self):
        if self.y == len(self.state[self.x]) - 1:
            print("Du siehst hohe Berge die du nicht erklimmen kannst")
        else:
            self.y = self.y + 1

    def left(self):
        if self.y == 0:
            print("Du siehst Klippen du die nicht runter kommst")
        else:
            self.y = self.y - 1
