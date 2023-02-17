import random


class Item:
    def __init__(self, weigth, worth):
        self.weight = weigth
        self.worth = worth


class Weapon(Item):
    def __init__(self, wad, weight, worth, name):
        Item.__init__(self, weight, worth)
        self.wad = wad
        self.name = name

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


class Potion(Item):
    def __init__(self, weight, worth):
        Item.__init__(self, weight, worth)


class HealthPotion(Potion):

    def __init__(self, weight, worth,  regenerated_health, qty):
        Item.__init__(self, weight, worth)
        self.regenerated_health = regenerated_health
        self.qty = qty


class FightPotion(Potion):

    def __init__(self, weight, worth,  extra_ad, qty):
        Item.__init__(self, weight, worth)
        self.extra_ad = extra_ad
        self.qty = qty


class Character:
    def __init__(self, hp, ad, name):
        self.hp = hp
        self.ad = ad
        self.name = name

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


class wInventory:
    def __init__(self):
        self.winv = [Weapon(0, 0, 0, "")]

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


class Inventory:
    def __init__(self):
        self.inv = {}
        self.inv["HealthPotion"] = HealthPotion(1, 20, 100, 1)
        self.inv["FightPotion"] = FightPotion(1, 50, 100, 2)

    def check_winv(self, p):
        pass

    def check_emptyinv(self, p):
        pass

    def inv_add(self, object,):
        self.inv[object] = 1


class Player(Character, wInventory, Inventory):
    def __init__(self, name, hp, ad):
        Character.__init__(self, hp, ad, name)
        wInventory.__init__(self)
        Inventory.__init__(self)
        self.max_hp = hp

    def die(self):
        exit("Tot.")

    def rest(self):
        self.hp = self.max_hp


class Field:
    def __init__(self, enemies):
        self.enemies = enemies

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


class Map:
    def __init__(self, width, height):
        self.state = []
        self.x = 0
        self.y = 0
        for i in range(width):
            fields = []
            for j in range(height):
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
    print("Du begehst selbstmord und verlasst die Welt.")
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
                    input("Du hast eine Waffe gefunden willst du sie aufheben?"))
                if inpu == "ja":
                    if p.check_emptywinv(p):
                        p.winv_add(dro_weapon)
                        print(dro_weapon.name, " aufgehoben")
                    elif p.check_winv(p, dro_weapon):
                        print(
                            "Du hast noch ein " + p.winv[0].name + ",willst du die neue Waffe aufheben ")
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
        p.ad = puad


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
    p = Player(name, 500, 100)
    puad = p.ad
    map = Map(5, 5)
    print("(gib help ein um alle verfügbaren befehle zu sehen)\n")
    while True:
        command = input(">").lower().split(" ")  # pickup
        if command[0] in Commands:
            Commands[command[0]](p, map)
            print("\n")
        else:
            print("Du gehst im Kreis und weist nicht was du tust.")
        map.print_state()
