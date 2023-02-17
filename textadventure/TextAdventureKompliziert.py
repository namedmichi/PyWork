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

    def winv_add(
        self,
        weapon,
    ):
        self.winv[0] = weapon


@dataclass
class Inventory:
    inv: dict

    def check_winv(self, p):
        pass

    def check_emptyinv(self, p):
        pass

    def inv_add(
        self,
        object,
    ):
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


def forward(p, m):
    m.forward()


def right(p, m):
    m.right()


def left(p, m):
    m.left()


def backwards(p, m):
    m.backwards()


def save():
    pass


def load():
    pass


def show_inv(p, m):
    print(p.inv)


def quit_game(p, m):
    print("Du begehst selbstmord und verlässt die Welt.")
    exit(0)


def print_help(p, m):
    print(Commands.keys())


def heal(p, m):
    quantatiy = p.inv["HealthPotion"].qty
    if quantatiy >= 1:
        p.hp += p.inv["HealthPotion"].regenerated_health
        print("Du wurdest geheilt", p.hp)
        p.inv["HealthPotion"].qty = p.inv["HealthPotion"].qty - 1
    else:
        print("Keine Tränke mehr vorhanden")


def fight_potion(p, m):
    quantatiy = p.inv["FightPotion"].qty
    if quantatiy >= 1:
        p.ad += p.inv["FightPotion"].extra_ad
        print("Du fühlst dich stärker")
        p.inv["FightPotion"].qty = p.inv["FightPotion"].qty - 1
    else:
        print("Keine Tränke mehr vorhanden")


def fight(p, m):
    enemies = m.get_enemies()
    while len(enemies) > 0:
        enemies[0].get_hit(p.ad + p.winv[0].wad)
        if enemies[0].is_dead():
            enemies.remove(enemies[0])
            rand = random.randint(0, 3)
            if rand == 0:
                print("Heiltrank gefunden")
                p.inv["HealthPotion"].qty += 1
            if rand == 2:
                global dro_weapon
                dro_weapon = Weapon(1, 1, 1, "pre")
                dro_weapon.rand_weap()
                print(dro_weapon.name)
                inpu = str(
                    input(
                        "Du hast eine Waffe gefunden willst du sie aufheben?"))
                if inpu == "ja":
                    if p.check_emptywinv(p):
                        p.winv_add(dro_weapon)
                        print(dro_weapon.name, " aufgehoben")
                    elif p.check_winv(p, dro_weapon):
                        print("Du hast noch ein " + p.winv[0].name +
                              ",willst du die neue Waffe aufheben ")
                        ipu = str(input(""))
                        if ipu == "ja":
                            p.winv_add(dro_weapon)
                            print(dro_weapon.name, " aufgehoben")
                    else:
                        print("Du hast diese Waffe bereits")

        for i in enemies:
            p.get_hit(i.ad)
            print("Du bist verwundet und hast " + str(p.hp) + " hp left")
    else:
        if not p.ad == puad:
            p.ad = puad
            print("Du wirst schwächer")


def game_start(p):
    p.inv["HealthPotion"] = HealthPotion(1, 20, 100, 1)
    p.inv["FightPotion"] = FightPotion(1, 50, 100, 2)
    p.winv = [Weapon(0, 0, 0, "")]


def rest(p, m):
    p.rest()


Commands = {
    'help': print_help,
    'quit': quit_game,
    'forward': forward,
    'right': right,
    'left': left,
    'backwards': backwards,
    'fight': fight,
    'save': save,
    'load': load,
    'rest': rest,
    "heal": heal,
    "show_inv": show_inv,
    "fight_potion": fight_potion
}

if __name__ == '__main__':
    name = input("Name eingaben")
    p = Player({}, [], 500, 100, name, 500)
    puad = p.ad
    map = Map([], 5, 5)
    print("(gib help ein um alle verfügbaren befehle zu sehen)\n")
    game_start(p)
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Commands:
            Commands[command[0]](p, map)
            print("\n")
        else:
            print("Du gehst im Kreis und weist nicht was du tust.")
        map.print_state()
