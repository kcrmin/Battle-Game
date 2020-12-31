import random
import time

# Unit Class
class unit():
    def __init__(self, name, classjob):
        self.name = name
        self.classjob = classjob
        self.rank = 1
        self.frozen_count = 0
        self.dead_count = 0
    
    # create / rank up and statistics
    def rank_up(self):
        # Warrior class
        if int(self.classjob) == 1:
            if int(self.rank) == 1:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 50
                self.ATK = 8
                self.DEF = 3
                self.SS_Heal = False
                self.SS_Poison = False
                print("(Level {0})\nName = \"{1}\"\nClass = Warrior\nHP = {2}\nATK = {3}\nDEF = {4}".format(self.rank, self.name, self.HP, self.ATK, self.DEF))
            elif int(self.rank) == 2:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 60
                self.ATK = 9
                self.DEF = 4
                self.SS_Heal = False
                self.SS_Poison = False
                print("\n\n==============================LEVEL UP==============================")
                print("(Level {0})\nName = \"{1}\"\nClass = Warrior\nHP = {2}\nATK = {3}\nDEF = {4}".format(self.rank, self.name, self.HP, self.ATK, self.DEF))
                print("====================================================================\n\n")
                to_continue = input("Press \'Enter\' to continue...")
            elif int(self.rank) == 3:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 70
                self.ATK = 10
                self.DEF = 5
                self.SS_Heal = False
                self.SS_Poison = False
                print("\n\n==============================LEVEL UP==============================")
                print("(Level {0})\nName = \"{1}\"\nClass = Warrior\nHP = {2}\nATK = {3}\nDEF = {4}".format(self.rank, self.name, self.HP, self.ATK, self.DEF))
                print("====================================================================\n\n")
                to_continue = input("Press \'Enter\' to continue...")
            else:
                pass
        # Tanker class
        elif int(self.classjob) == 2:
            if int(self.rank) == 1:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 60
                self.ATK = 5
                self.DEF = 5
                self.SS_Heal = False
                self.SS_Poison = False
                print("(Level {0})\nName = \"{1}\"\nClass = Tanker\nHP = {2}\nATK = {3}\nDEF = {4}".format(self.rank, self.name, self.HP, self.ATK, self.DEF))
            elif int(self.rank) == 2:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 70
                self.ATK = 6
                self.DEF = 6
                self.SS_Heal = False
                self.SS_Poison = False
                print("\n\n==============================LEVEL UP==============================")
                print("(Level {0})\nName = \"{1}\"\nClass = Tanker\nHP = {2}\nATK = {3}\nDEF = {4}".format(self.rank, self.name, self.HP, self.ATK, self.DEF))
                print("====================================================================\n\n")
                to_continue = input("Press \'Enter\' to continue...")
            elif int(self.rank) == 3:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 80
                self.ATK = 8
                self.DEF = 8
                self.SS_Heal = False
                self.SS_Poison = False
                print("\n\n==============================LEVEL UP==============================")
                print("(Level {0})\nName = \"{1}\"\nClass = Tanker\nHP = {2}\nATK = {3}\nDEF = {4}".format(self.rank, self.name, self.HP, self.ATK, self.DEF))
                print("====================================================================\n\n")
                to_continue = input("Press \'Enter\' to continue...")
            else:
                pass
        # Wizard class
        elif int(self.classjob) == 3:
            if int(self.rank) == 1:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 40
                self.ATK = 3
                self.DEF = 2
                self.SS_Heal = 5
                self.SS_Poison = 3
                print("(Level: {0})\nName = \"{1}\"\nClass = Wizard\nHP = {2}\nATK = {3}\nDEF = {4}\n(Spells)\nHeal = {5}\nPoison = {6}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison))
            elif int(self.rank) == 2:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 50
                self.ATK = 4
                self.DEF = 3
                self.SS_Heal = 8
                self.SS_Poison = 5
                print("\n\n==============================LEVEL UP==============================")
                print("(Level: {0})\nName = \"{1}\"\nClass = Wizard\nHP = {2}\nATK = {3}\nDEF = {4}\n(Spells)\nHeal = {5}\nPoison = {6}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison))
                print("====================================================================\n\n")
                to_continue = input("Press \'Enter\' to continue...")
            elif int(self.rank) == 3:
                self.alive = True
                self.frozen = False
                self.poisoned = False
                self.EXP = 0
                self.HP = 60
                self.ATK = 5
                self.DEF = 4
                self.SS_Heal = 10
                self.SS_Poison = 8
                print("\n\n==============================LEVEL UP==============================")
                print("(Level: {0})\nName = \"{1}\"\nClass = Wizard\nHP = {2}\nATK = {3}\nDEF = {4}\n(Spells)\nHeal = {5}\nPoison = {6}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison))
                print("====================================================================\n\n")
                to_continue = input("Press \'Enter\' to continue...")
            else:
                pass
        else:
            pass

    def create_unit(self):
        self.rank_up()

    # Attacks
    def random_bonus_damage(self):
        Bonus_Damage = random.randrange(-2, 6)
        return Bonus_Damage

    def damage_calculation(self, ATK):
        Bonus_Damage = self.random_bonus_damage()
        total_damage = ATK - self.DEF + Bonus_Damage
        if int(total_damage) <= 0:
            total_damage = 0
        else:
            pass
        return total_damage

    def attack(self, total_damage, killed):
        # if the attack killed the target (50% more EXP)
        if killed == True:
            total_damage *= 1.5
            total_damage = int(total_damage)
            self.EXP += total_damage
        # if the total_damage point is more than 10 (20% more EXP)
        elif int(total_damage) > 10:
            total_damage *= 1.2
            total_damage = int(total_damage)
            self.EXP += total_damage
        else:
            self.EXP += total_damage

    def attacked(self, ATK):
        total_damage = self.damage_calculation(ATK)
        if int(self.HP) <= int(total_damage):
            self.HP = 0
            self.alive = False
            self.killed = True
        else:
            self.HP -= total_damage
            self.EXP += self.DEF
            self.killed = False
        return total_damage, self.killed

    # Spells
    def cure(self):
        self.EXP += 5

    def cured(self):
        self.poisoned = False

    def heal(self):
        self.EXP += 5

    def healed(self, heal_amount):
        self.HP += heal_amount

    def CS_Poison(self):
        self.EXP += 5

    def CS_Freeze(self):
        self.EXP += 5
    
    def SC_Poisoned(self, poison_amount):
        self.poisoned = True
        self.poison_amount = poison_amount

    def SC_Frozen(self):
        self.frozen = True
        self.frozen_count = 0

    # Check
    def check_EXP(self):
        if int(self.rank) >= 3:
            self.EXP = 0
            self.rank = 3
        elif int(self.EXP) >= 50:
            self.rank += 1
            self.rank_up()
            myFile = open("GameLog.txt", "a")
            now = time.localtime()
            timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
            myFile.write("\n\nUnit \"{0}\" LEVEL UP!\n".format(self.name))
            self.txt_status(myFile)
            myFile.write("\n\n")
            myFile.close()
        else:
            pass

    def check_alive(self):
        if int(self.dead_count) == 0:
            if int(self.HP) <= 0:
                self.HP = 0
                self.alive = False
                self.dead_count += 1
                print("\n{0} IS NOW DEAD.".format(self.name))
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n\nUnit \"{0}\" IS NOW DEAD\n".format(self.name))
                myFile.write("\n")
                myFile.close()
                to_continue = input("Press \'Enter\' to continue...")
        elif int(self.dead_count) >= 1:
            if int(self.HP) <= 0:
                self.HP = 0
                self.alive = False

    def check_Frozen(self):
        if int(self.frozen_count) == 0:
            self.frozen_count += 1
        elif int(self.frozen_count) == 1:
            self.frozen = False
        else:
            pass

    def check_Poison(self):
        if self.poisoned == True:
            self.HP -= self.poison_amount
        else:
            pass

    def check_status(self):
        self.check_EXP()
        self.check_Frozen()
        self.check_Poison()
        self.check_alive()

    def status(self):
        return self.name, self.rank, self.classjob, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison, self.EXP, self.frozen, self.poisoned, self.alive

    def print_status(self, number):
        if int(self.classjob) == 1:
            print("({0}) (Level {1}) / \"{2}\" / Warrior / HP = {3} / ATK = {4} / DEF = {5} / EXP = {6} / Poisoned = {7} / Frozen = {8}".format(number, self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 2:
            print("({0}) (Level {1}) / \"{2}\" / Tanker / HP = {3} / ATK = {4} / DEF = {5} / EXP = {6} / Poisoned = {7} / Frozen = {8}".format(number, self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 3:
            print("({0}) (Level {1}) / \"{2}\" / Wizard / HP = {3} / ATK = {4} / DEF = {5} / Heal Spell = {6} / Poison Spell = {7} / EXP = {8} / Poisoned = {9} / Frozen = {10}".format(number, self.rank, self.name, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison, self.EXP, self.poisoned, self.frozen))
        else:
            pass

    def print_status_last(self):
        if int(self.classjob) == 1:
            print("(Level {0}) / \"{1}\" / Warrior / HP = {2} / ATK = {3} / DEF = {4} / EXP = {5} / Poisoned = {6} / Frozen = {7}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 2:
            print("(Level {0}) / \"{1}\" / Tanker / HP = {2} / ATK = {3} / DEF = {4} / EXP = {5} / Poisoned = {6} / Frozen = {7}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 3:
            print("(Level {0}) / \"{1}\" / Wizard / HP = {2} / ATK = {3} / DEF = {4} / Heal Spell = {5} / Poison Spell = {6} / EXP = {7} / Poisoned = {8} / Frozen = {9}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison, self.EXP, self.poisoned, self.frozen))
        else:
            pass

    def txt_status(self, myFile):
        if int(self.classjob) == 1:
            myFile.write("(Level {0}) / \"{1}\" / Warrior / HP = {2} / ATK = {3} / DEF = {4} / EXP = {5} / Poisoned = {6} / Frozen = {7}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 2:
            myFile.write("(Level {0}) / \"{1}\" / Tanker / HP = {2} / ATK = {3} / DEF = {4} / EXP = {5} / Poisoned = {6} / Frozen = {7}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 3:
            myFile.write("(Level {0}) / \"{1}\" / Wizard / HP = {2} / ATK = {3} / DEF = {4} / Heal Spell = {5} / Poison Spell = {6} / EXP = {7} / Poisoned = {8} / Frozen = {9}".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison, self.EXP, self.poisoned, self.frozen))

    def txt_status_last(self, myFile):
        if int(self.classjob) == 1:
            myFile.write("(Level {0}) / \"{1}\" / Warrior / HP = {2} / ATK = {3} / DEF = {4} / EXP = {5} / Poisoned = {6} / Frozen = {7}\n".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 2:
            myFile.write("(Level {0}) / \"{1}\" / Tanker / HP = {2} / ATK = {3} / DEF = {4} / EXP = {5} / Poisoned = {6} / Frozen = {7}\n".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.EXP, self.poisoned, self.frozen))
        elif int(self.classjob) == 3:
            myFile.write("(Level {0}) / \"{1}\" / Wizard / HP = {2} / ATK = {3} / DEF = {4} / Heal Spell = {5} / Poison Spell = {6} / EXP = {7} / Poisoned = {8} / Frozen = {9}\n".format(self.rank, self.name, self.HP, self.ATK, self.DEF, self.SS_Heal, self.SS_Poison, self.EXP, self.poisoned, self.frozen))

##############################################################################################################


def classjob_txt(classjob):
    if int(classjob) == 1:
        class_txt = "Warrior"
    elif int(classjob) == 2:
        class_txt = "Tanker"
    elif int(classjob) == 3:
        class_txt = "Wizard"
    return class_txt

def name_input(name_list, count_num):
    unit_name = input("\nEnter a name for the unit #{0} (Blue Team): ".format(count_num))
    while (unit_name in name_list) or (unit_name.strip() == ""):
        print("\n====================An Error has occurred please enter a valid input====================")
        unit_name = input("\nEnter a name for the unit #{0} (Blue Team): ".format(count_num))
    name_list.append(unit_name)
    return unit_name, name_list

# Print Event Log
def print_event_blue(u1, u2, total_damage, SS_Heal, move, turns):
    print("\nBLUE TEAM MOVE")
    u1_name, u1_rank, u1_classjob, u1_HP, u1_ATK, u1_DEF, u1_SS_Heal, u1_SS_Poison, u1_EXP, u1_frozen, u1_poisoned, u1_alive = u1.status()
    u2_name, u2_rank, u2_classjob, u2_HP, u2_ATK, u2_DEF, u2_SS_Heal, u2_SS_Poison, u2_EXP, u2_frozen, u2_poisoned, u2_alive = u2.status()
    myFile = open("GameLog.txt", "a")
    now = time.localtime()
    timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    myFile.write("\n{0} Blue Team # {1} Turn".format(timestamp, turns))
    myFile.write("\nUnit Selected: ")
    u1.txt_status(myFile)
    myFile.write("\nTarget Unit: ")
    u2.txt_status(myFile)
    if int(move) == 1:
        print("Unit \"{0}\" attacked unit \"{1}\" with a total damage of {2}".format(u1_name, u2_name, total_damage))
        myFile.write("\nUnit \"{0}\" attacked unit \"{1}\" with a total damage of {2}\n".format(u1_name, u2_name, total_damage))
    elif int(move) == 2:
        print("Unit \"{0}\" cast a poison spell to unit \"{1}\"".format(u1_name, u2_name))
        myFile.write("\nUnit \"{0}\" cast a poison spell to unit \"{1}\"\n".format(u1_name, u2_name))
    elif int(move) == 3:
        print("Unit \"{0}\" cast a freeze spell to unit \"{1}\"".format(u1_name, u2_name))
        myFile.write("\nUnit \"{0}\" cast a freeze spell to unit \"{1}\"\n".format(u1_name, u2_name))
    elif int(move) == 4:
        print("Unit \"{0}\" healed unit \"{1}\". + {2} HP".format(u1_name, u2_name, SS_Heal))
        myFile.write("\nUnit \"{0}\" healed unit \"{1}\". + {2} HP\n".format(u1_name, u2_name, SS_Heal))
    elif int(move) == 5:
        print("Unit \"{0}\" cured unit \"{1}\" from the poison".format(u1_name, u2_name))
        myFile.write("\nUnit \"{0}\" cured unit \"{1}\" from the poison\n".format(u1_name, u2_name)) 
    to_continue = input("Press \'Enter\' to continue...")
    myFile.close()

def print_event_red(u1, u2, total_damage, SS_Heal, move, turns):
    print("\nRED TEAM MOVE")
    u1_name, u1_rank, u1_classjob, u1_HP, u1_ATK, u1_DEF, u1_SS_Heal, u1_SS_Poison, u1_EXP, u1_frozen, u1_poisoned, u1_alive = u1.status()
    u2_name, u2_rank, u2_classjob, u2_HP, u2_ATK, u2_DEF, u2_SS_Heal, u2_SS_Poison, u2_EXP, u2_frozen, u2_poisoned, u2_alive = u2.status()
    myFile = open("GameLog.txt", "a")
    now = time.localtime()
    timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    myFile.write("\n{0} Red Team # {1} Turn".format(timestamp, turns))
    myFile.write("\nUnit Selected: ")
    u1.txt_status(myFile)
    myFile.write("\nTarget Unit: ")
    u2.txt_status(myFile)
    if int(move) == 1:
        print("Unit \"{0}\" attacked unit \"{1}\" with a total damage of {2}".format(u1_name, u2_name, total_damage))
        myFile.write("\nUnit \"{0}\" attacked unit \"{1}\" with a total damage of {2}\n".format(u1_name, u2_name, total_damage))
    elif int(move) == 2:
        print("Unit \"{0}\" cast a poison spell to unit \"{1}\"".format(u1_name, u2_name))
        myFile.write("\nUnit \"{0}\" cast a poison spell to unit \"{1}\"\n".format(u1_name, u2_name))
    elif int(move) == 3:
        print("Unit \"{0}\" cast a freeze spell to unit \"{1}\"".format(u1_name, u2_name))
        myFile.write("\nUnit \"{0}\" cast a freeze spell to unit \"{1}\"\n".format(u1_name, u2_name))
    elif int(move) == 4:
        print("Unit \"{0}\" healed unit \"{1}\". + {2} HP".format(u1_name, u2_name, SS_Heal))
        myFile.write("\nUnit \"{0}\" healed unit \"{1}\". + {2} HP\n".format(u1_name, u2_name, SS_Heal))
    elif int(move) == 5:
        print("Unit \"{0}\" cured unit \"{1}\" from the poison".format(u1_name, u2_name))
        myFile.write("\nUnit \"{0}\" cured unit \"{1}\" from the poison\n".format(u1_name, u2_name)) 
    to_continue = input("Press \'Enter\' to continue...")
    myFile.close()

# reset available/alive units
def reset_available():
    a1_available = False
    a2_available = False
    a3_available = False
    b1_available = False
    b2_available = False
    b3_available = False
    return (a1_available, a2_available, a3_available, b1_available, b2_available, b3_available)

def reset_alive():
    a1_alive = False
    a2_alive = False
    a3_alive = False
    b1_alive = False
    b2_alive = False
    b3_alive = False
    return a1_alive, a2_alive, a3_alive, b1_alive, b2_alive, b3_alive

# Input Clarifier
# Function to Clarify the Number of Units Input (1, 2, or 3)
def unit_num_input():
    unit_num = input("\nChoose the number of unit(s) you want to play with\n(1) 1 vs 1\n(2) 2 vs 2\n(3) 3 vs 3\nPlease enter the option you want to choose: ")
    while not unit_num.isdigit() or int(unit_num) <= 0 or int(unit_num) >= 4:
        print("\n====================An Error has occurred please enter a valid input====================")
        unit_num = input("\nChoose the number of unit(s) you want to play with\n(1) 1 vs 1\n(2) 2 vs 2\n(3) 3 vs 3\nPlease enter the option you want to choose: ")
    if int(unit_num) == 1:
        print("\n========================================1 vs 1========================================")
    elif int(unit_num) == 2:
        print("\n========================================2 vs 2========================================")
    elif int(unit_num) == 3:
        print("\n========================================3 vs 3========================================")
    else:
        pass
    return unit_num

# Function to Clarify the Unit Class Input (1 = Warrior, 2 = Tanker, 3 = Wizard)
def unit_class_input(unit_name):
    unit_class = input("\nChoose the class of unit \"{0}\"\n(1) = Warrior\n(2) = Tanker\n(3) = Wizard\nPlease enter the option you want to choose: ".format(unit_name))
    while not unit_class.isdigit() or int(unit_class) <= 0 or int(unit_class) >= 4:
        print("\n====================An Error has occurred please enter a valid input====================")
        unit_class = input("\nChoose the class of unit \"{0}\"\n(1) = Warrior\n(2) = Tanker\n(3) = Wizard\nPlease enter the option you want to choose: ".format(unit_name))
    return unit_class

# Function to Clarify the uvu and uva input (1 or 2)
def uvu_vs_uva_input():
    game_mode = input("\nWelcome to the Python Game!\n(1) User vs User\n(2) User vs AI \nPlease enter the option you want to choose: ")
    while not game_mode.isdigit() or int(game_mode) <= 0 or int(game_mode) >= 3:
        print("\n====================An Error has occurred please enter a valid input====================")
        game_mode = input("Welcome to the Python Game!\n(1) User vs User\n(2) User vs AI \nPlease enter the option you want to choose: ")
    return game_mode

# Random Generator  
# Function to generate random move
def random_move_generator():
    random_move = random.randrange(1, 3)
    return random_move

# Function for the random class 
def random_class_generator():
    unit_class = random.randrange(1, 4)
    return unit_class

# Function for the random name
def random_name_generator():
    alphabets = "abcdefghijklmnopqrstuvwxyz"
    random_name = ""
    for i in range(2):
        random_name += random.choice(alphabets)
    for i in range(3):
        random_name += str(random.randrange(10))
    return random_name

# User Choice of Unit Number (a is friendly unit, b is enemy unit)
def unit_choice(game_mode):
    name_list = []
    unit_num = int(unit_num_input())
    if int(unit_num) == 1:
        myFile = open("GameLog.txt", "a")
        now = time.localtime()
        timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        myFile.write("{0} Chose 1 vs 1\n\n".format(timestamp))
        myFile.close()
    elif int(unit_num) == 2:
        myFile = open("GameLog.txt", "a")
        now = time.localtime()
        timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        myFile.write("{0} Chose 2 vs 2\n\n".format(timestamp))
        myFile.close()
    elif int(unit_num) == 3:
        myFile = open("GameLog.txt", "a")
        now = time.localtime()
        timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
        myFile.write("{0} Chose 3 vs 3\n\n".format(timestamp))
        myFile.close()
    count_blue_num = 1
    count_red_num = 1
    # User vs User
    if game_mode == 1:
        # Blue Team
        for a in range(unit_num):
            # First Loop
            if count_blue_num == 1:
                unit_name, name_list = name_input(name_list, count_blue_num)
                class_input = unit_class_input(unit_name)
                a1 = unit(unit_name, class_input)
                print("\n=========================(Blue Team) Unit {0}=========================".format(count_blue_num))
                a1.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Blue Team Unit 1 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("=====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_blue_num += 1
            # Second Loop
            elif count_blue_num == 2:
                unit_name, name_list = name_input(name_list, count_blue_num)
                class_input = unit_class_input(unit_name)
                a2 = unit(unit_name, class_input)
                print("\n=========================(Blue Team) Unit {0}=========================".format(count_blue_num))
                a2.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Blue Team Unit 2 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("=====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_blue_num += 1
            # Third Loop
            elif count_blue_num == 3:
                unit_name, name_list = name_input(name_list, count_blue_num)
                class_input = unit_class_input(unit_name)
                a3 = unit(unit_name, class_input)
                print("\n=========================(Blue Team) Unit {0}=========================".format(count_blue_num))
                a3.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Blue Team Unit 3 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("=====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_blue_num += 1
            else:
                pass
        # Red Team
        for b in range(unit_num):
            # First Loop
            if count_red_num == 1:
                unit_name, name_list = name_input(name_list, count_red_num)
                class_input = unit_class_input(unit_name)
                b1 = unit(unit_name, class_input)
                print("\n=========================(Red Team) Unit {0}=========================".format(count_red_num))
                b1.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Red Team Unit 1 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_red_num += 1
            # Second Loop
            elif count_red_num == 2:
                unit_name, name_list = name_input(name_list, count_red_num)
                class_input = unit_class_input(unit_name)
                b2 = unit(unit_name, class_input)
                print("\n=========================(Red Team) Unit {0}=========================".format(count_red_num))
                b2.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Red Team Unit 2 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_red_num += 1
            # Third Loop
            elif count_red_num == 3:
                unit_name, name_list = name_input(name_list, count_red_num)
                class_input = unit_class_input(unit_name)
                b3 = unit(unit_name, class_input)
                print("\n=========================(Red Team) Unit {0}=========================".format(count_red_num))
                b3.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Red Team Unit 3 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_blue_num += 1
            else:
                pass
        # Missing Unit Return
        if unit_num == 1:
            a2 = 0
            a3 = 0
            b2 = 0
            b3 = 0
        elif unit_num == 2:
            a3 = 0
            b3 = 0
        elif unit_num == 3:
            pass
        else:
            pass
        return a1, a2, a3, b1, b2, b3, unit_num
    # User vs AI
    elif game_mode == 2:
        # Blue Team
        for a in range(unit_num):
            # First Loop
            if count_blue_num == 1:
                unit_name, name_list = name_input(name_list, count_blue_num)
                class_input = unit_class_input(unit_name)
                a1 = unit(unit_name, class_input)
                print("\n=========================(Blue Team) Unit {0}=========================".format(count_blue_num))
                a1.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Blue Team Unit 1 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("=====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_blue_num += 1
            # Second Loop
            elif count_blue_num == 2:
                unit_name, name_list = name_input(name_list, count_blue_num)
                class_input = unit_class_input(unit_name)
                a2 = unit(unit_name, class_input)
                print("\n=========================(Blue Team) Unit {0}=========================".format(count_blue_num))
                a2.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Blue Team Unit 2 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("=====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_blue_num += 1
            # Third Loop
            elif count_blue_num == 3:
                unit_name, name_list = name_input(name_list, count_blue_num)
                class_input = unit_class_input(unit_name)
                a3 = unit(unit_name, class_input)
                print("\n=========================(Blue Team) Unit {0}=========================".format(count_blue_num))
                a3.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Blue Team Unit 3 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("=====================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_blue_num += 1
            else:
                pass
        # Red Loop
        for b in range(unit_num):
            # First Loop
            if count_red_num == 1:
                unit_name = random_name_generator()
                class_input = random_class_generator()
                b1 = unit(unit_name, class_input)
                print("\n=========================(Red Team) Unit {0}=========================".format(count_red_num))
                b1.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Red Team Unit 1 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("===================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_red_num += 1
            # Second Loop
            elif count_red_num == 2:
                unit_name = random_name_generator()
                class_input = random_class_generator()
                b2 = unit(unit_name, class_input)
                print("\n=========================(Red Team) Unit {0}=========================".format(count_red_num))
                b2.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Red Team Unit 2 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("===================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_red_num += 1
            # Third Loop
            elif count_red_num == 3:
                unit_name = random_name_generator()
                class_input = random_class_generator()
                b3 = unit(unit_name, class_input)
                print("\n=========================(Red Team) Unit {0}=========================".format(count_red_num))
                b3.create_unit()
                class_txt = classjob_txt(class_input)
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("{0} Red Team Unit 3 is created (\"{1}\", {2})\n\n".format(timestamp, unit_name, class_txt))
                myFile.close()
                print("===================================================================")
                to_continue = input("Press \'Enter\' to continue...")
                count_red_num += 1
            else:
                pass
        # Missing Unit Return
        if unit_num == 1:
            a2 = 0
            a3 = 0
            b2 = 0
            b3 = 0
        elif unit_num == 2:
            a3 = 0
            b3 = 0
        elif unit_num == 3:
            pass
        else:
            pass
        return a1, a2, a3, b1, b2, b3, unit_num
    else:
        pass

# Functions to run user_moves
# Functions to chose the unit to use
def input_1(u1, AD):
    print("\n==================================(Available Unit List)==================================")
    u1.print_status(1)
    if int(AD) == 1:
        unit_selected = input("Please choose the unit you want to use: ")
    elif int(AD) == 2:
        unit_selected = input("Please choose the unit you want to attack: ")
    elif int(AD) == 3:
        unit_selected = input("Please choose the unit you want to help: ")
    else:
        pass
    while not unit_selected.isdigit() or not int(unit_selected) == 1:
        print("\n====================An Error has occurred please enter a valid input====================")
        print("==================================(Available Unit List)==================================")
        u1.print_status(1)
        if int(AD) == 1:
            unit_selected = input("Please choose the unit you want to use: ")
        elif int(AD) == 2:
            unit_selected = input("Please choose the unit you want to attack: ")
        elif int(AD) == 3:
            unit_selected = input("Please choose the unit you want to help: ")
        else:
            pass
    return unit_selected

def input_2(u2, AD):
    print("\n==================================(Available Unit List)==================================")
    u2.print_status(2)
    if int(AD) == 1:
        unit_selected = input("Please choose the unit you want to use: ")
    elif int(AD) == 2:
        unit_selected = input("Please choose the unit you want to attack: ")
    elif int(AD) == 3:
        unit_selected = input("Please choose the unit you want to help: ")
    else:
        pass
    while not unit_selected.isdigit() or not int(unit_selected) == 2:
        print("\n====================An Error has occurred please enter a valid input====================")
        print("==================================(Available Unit List)==================================")
        u2.print_status(2)
        if int(AD) == 1:
            unit_selected = input("Please choose the unit you want to use: ")
        elif int(AD) == 2:
            unit_selected = input("Please choose the unit you want to attack: ")
        elif int(AD) == 3:
            unit_selected = input("Please choose the unit you want to help: ")
        else:
            pass
    return unit_selected

def input_3(u3, AD):
    print("\n==================================(Available Unit List)==================================")
    u3.print_status(3)
    if int(AD) == 1:
        unit_selected = input("Please choose the unit you want to use: ")
    elif int(AD) == 2:
        unit_selected = input("Please choose the unit you want to attack: ")
    elif int(AD) == 3:
        unit_selected = input("Please choose the unit you want to help: ")
    else:
        pass
    while not unit_selected.isdigit() or not int(unit_selected) == 3:
        print("\n====================An Error has occurred please enter a valid input====================")
        print("==================================(Available Unit List)==================================")
        u3.print_status(3)
        if int(AD) == 1:
            unit_selected = input("Please choose the unit you want to use: ")
        elif int(AD) == 2:
            unit_selected = input("Please choose the unit you want to attack: ")
        elif int(AD) == 3:
            unit_selected = input("Please choose the unit you want to help: ")
        else:
            pass
    return unit_selected

def input_12(u1, u2, AD):
    print("\n==================================(Available Unit List)==================================")
    u1.print_status(1)
    u2.print_status(2)
    if int(AD) == 1:
        unit_selected = input("Please choose the unit you want to use: ")
    elif int(AD) == 2:
        unit_selected = input("Please choose the unit you want to attack: ")
    elif int(AD) == 3:
        unit_selected = input("Please choose the unit you want to help: ")
    else:
        pass
    while not unit_selected.isdigit() or not (int(unit_selected) == 1 or int(unit_selected) == 2):
        print("\n====================An Error has occurred please enter a valid input====================")
        print("==================================(Available Unit List)==================================")
        u1.print_status(1)
        u2.print_status(2)
        if int(AD) == 1:
            unit_selected = input("Please choose the unit you want to use: ")
        elif int(AD) == 2:
            unit_selected = input("Please choose the unit you want to attack: ")
        elif int(AD) == 3:
            unit_selected = input("Please choose the unit you want to help: ")
        else:
            pass
    return unit_selected

def input_23(u2, u3, AD):
    print("\n==================================(Available Unit List)==================================")
    u2.print_status(2)
    u3.print_status(3)
    if int(AD) == 1:
        unit_selected = input("Please choose the unit you want to use: ")
    elif int(AD) == 2:
        unit_selected = input("Please choose the unit you want to attack: ")
    elif int(AD) == 3:
        unit_selected = input("Please choose the unit you want to help: ")
    else:
        pass
    while not unit_selected.isdigit() or not (int(unit_selected) == 2 or int(unit_selected) == 3):
        print("\n====================An Error has occurred please enter a valid input====================")
        print("==================================(Available Unit List)==================================")
        u2.print_status(2)
        u3.print_status(3)
        if int(AD) == 1:
            unit_selected = input("Please choose the unit you want to use: ")
        elif int(AD) == 2:
            unit_selected = input("Please choose the unit you want to attack: ")
        elif int(AD) == 3:
            unit_selected = input("Please choose the unit you want to help: ")
        else:
            pass
    return unit_selected

def input_13(u1, u3, AD):
    print("\n==================================(Available Unit List)==================================")
    u1.print_status(1)
    u3.print_status(3)
    if int(AD) == 1:
        unit_selected = input("Please choose the unit you want to use: ")
    elif int(AD) == 2:
        unit_selected = input("Please choose the unit you want to attack: ")
    elif int(AD) == 3:
        unit_selected = input("Please choose the unit you want to help: ")
    else:
        pass
    while not unit_selected.isdigit() or not (int(unit_selected) == 1 or int(unit_selected) == 3):
        print("\n====================An Error has occurred please enter a valid input====================")
        print("==================================(Available Unit List)==================================")
        u1.print_status(1)
        u3.print_status(3)
        if int(AD) == 1:
            unit_selected = input("Please choose the unit you want to use: ")
        elif int(AD) == 2:
            unit_selected = input("Please choose the unit you want to attack: ")
        elif int(AD) == 3:
            unit_selected = input("Please choose the unit you want to help: ")
        else:
            pass
    return unit_selected

def input_123(u1, u2, u3, AD):
    print("\n==================================(Available Unit List)==================================")
    u1.print_status(1)
    u2.print_status(2)
    u3.print_status(3)
    if int(AD) == 1:
        unit_selected = input("Please choose the unit you want to use: ")
    elif int(AD) == 2:
        unit_selected = input("Please choose the unit you want to attack: ")
    elif int(AD) == 3:
        unit_selected = input("Please choose the unit you want to help: ")
    else:
        pass
    while not unit_selected.isdigit() or not (int(unit_selected) == 1 or int(unit_selected) == 2 or int(unit_selected) == 3):
        print("\n====================An Error has occurred please enter a valid input====================")
        print("==================================(Available Unit List)==================================")
        u1.print_status(1)
        u2.print_status(2)
        u3.print_status(3)
        if int(AD) == 1:
            unit_selected = input("Please choose the unit you want to use: ")
        elif int(AD) == 2:
            unit_selected = input("Please choose the unit you want to attack: ")
        elif int(AD) == 3:
            unit_selected = input("Please choose the unit you want to help: ")
        else:
            pass
    return unit_selected

def wizard_choose_move():
    wizard_move = input("\nChoose the unit's move\n(1) Attack\n(2) Poison\n(3) Freeze\n(4) Heal\n(5) Cure\nPlease enter the option you want to choose: ")
    while not wizard_move.isdigit() or int(wizard_move) <= 0 or int(wizard_move) >= 6:
        print("\n====================An Error has occurred please enter a valid input====================")
        wizard_move = input("Choose the unit's move\n(1) Attack\n(2) Poison\n(3) Freeze\n(4) Heal\n(5) Cure\nPlease enter the option you want to choose: ")
    return wizard_move

def wizard_choose_unit(u1_alive, u2_alive, u3_alive, u1, u2, u3, AD):
    # when 3 units are alive (u1, u2, u3)
    if (u1_alive == True) and (u2_alive == True) and (u3_alive == True):
        target_unit_selected = input_123(u1, u2, u3, AD)
    # when 2 units are alive (u1, u2)
    elif (u1_alive == True) and (u2_alive == True):
        target_unit_selected = input_12(u1, u2, AD)
    # when 2 units are alive (u2, u3)
    elif (u2_alive == True) and (u3_alive == True):
        target_unit_selected = input_23(u2, u3, AD)
    # when 2 units are alive (u1, u3)
    elif (u1_alive == True) and (u3_alive == True):
        target_unit_selected = input_13(u1, u3, AD)
    # when 1 unit is alive (u1)
    elif u1_alive == True:
        target_unit_selected = input_1(u1, AD)
    # when 1 unit is alive (u2)
    elif u2_alive == True:
        target_unit_selected = input_2(u2, AD)
    # when 1 unit is alive (u3)
    elif u3_alive == True:
        target_unit_selected = input_3(u3, AD)
    # when 0 unit is alive
    else:
        target_unit_selected = 0
    return target_unit_selected

def choose_unit(u1_available, u2_available, u3_available, u1, u2, u3, AD):
    # when 3 units are available (u1, u2, u3)
    if (u1_available == True) and (u2_available == True) and (u3_available == True):
        unit_selected = input_123(u1, u2, u3, AD)
    # when 2 units are available (u1, u2)
    elif (u1_available == True) and (u2_available == True):
        unit_selected = input_12(u1, u2, AD)
    # when 2 units are available (u2, u3)
    elif (u2_available == True) and (u3_available == True):
        unit_selected = input_23(u2, u3, AD)
    # when 2 units are available (u1, u3)
    elif (u1_available == True) and (u3_available == True):
        unit_selected = input_13(u1, u3, AD)
    # when 1 unit is available (u1)
    elif u1_available == True:
        unit_selected = input_1(u1, AD)
    # when 1 unit is available (u2)
    elif u2_available == True:
        unit_selected = input_2(u2, AD)
    # when 1 unit is available (u3)
    elif u3_available == True:
        unit_selected = input_3(u3, AD)
    # when 0 unit is available
    else:
        unit_selected = 0
    return unit_selected

# Advanced AI moves
def AI_moves(a1, a2, a3, b1, b2, b3, unit_num, turns):
    if int(unit_num) == 1:
        # attributes
        a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
        b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
        # b1 unit's move
        if (b1_alive == True) and (b1_frozen == False):
            # Warrior and Tanker moves
            if int(b1_classjob) == 1 or int(b1_classjob) == 2:
                # attack the opponent with the lowest health
                if a1_alive == True:
                    total_damage, killed = a1.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a1, total_damage, 0, 1, turns)
            # Wizard moves
            elif int(b1_classjob) == 3:
                # Heal if the friendly unit has less than 10 HP point
                if (int(b1_HP) <= 10) and (b1_alive == True):
                    b1.healed(int(b1_SS_Heal))
                    b1.heal()
                    print_event_red(b1, b1, 0, b1_SS_Heal, 4, turns)
                # Cure if the friendly unit is poisoned
                elif (b1_poisoned == True) and (b1_alive == True):
                    b1.cured()
                    b1.cure()
                    print_event_red(b1, b1, 0, 0, 5, turns)
                # If the oponent unit has more than 30 HP than cast a spell (freeze or poison)
                # attack a1 unit if it has more than 30 HP
                elif (int(a1_HP) >= 30) and (a1_poisoned == False) and (a1_frozen == False):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a1.SC_Poisoned(int(b1_SS_Poison))
                        b1.CS_Poison()
                        print_event_red(b1, a1, 0, 0, 2, turns)
                    elif int(random_move) == 2:
                        a1.SC_Frozen()
                        b1.CS_Freeze()
                        print_event_red(b1, a1, 0, 0, 3, turns)    
                # attack the opponent with the lowest health
                elif a1_alive == True:
                    total_damage, killed = a1.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a1, 0, 0, 1, turns)
    elif int(unit_num) == 2:
        # attributes
        a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
        a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
        b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
        b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
        # b1 unit's move
        if (b1_alive == True) and (b1_frozen == False):
            # Warrior and Tanker moves
            if int(b1_classjob) == 1 or int(b1_classjob) == 2:
                # attack the opponent with the lowest health
                if (int(a1_HP) < int(a2_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a1, total_damage, 0, 1, turns)
                elif (int(a2_HP) < int(a1_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a2, total_damage, 0, 1, turns)
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a1, total_damage, 0, 1, turns)
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a2, total_damage, 0, 1, turns)
            # Wizard moves
            elif int(b1_classjob) == 3:
                # Heal if the friendly unit has less than 10 HP point
                if (int(b2_HP) <= 10) and (b2_alive == True):
                    b2.healed(int(b1_SS_Heal))
                    b1.heal()
                    print_event_red(b1, b2, 0, b1_SS_Heal, 4, turns)
                # Cure if the friendly unit is poisoned
                elif (b1_poisoned == True) and (b1_alive == True):
                    b1.cured()
                    b1.cure()
                    print_event_red(b1, b1, 0, 0, 5, turns)
                elif (b2_poisoned == True) and (b2_alive == True):
                    b2.cured()
                    b1.cure()
                    print_event_red(b1, b2, 0, 0, 5, turns)
                # If the oponent unit has more than 30 HP than cast a spell (freeze or poison)
                # attack a1 unit if it has more than 30 HP
                elif (int(a1_HP) >= 30) and (a1_poisoned == False) and (a1_frozen == False):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a1.SC_Poisoned(int(b1_SS_Poison))
                        b1.CS_Poison()
                        print_event_red(b1, a1, 0, 0, 2, turns)
                    elif int(random_move) == 2:
                        a1.SC_Frozen()
                        b1.CS_Freeze()
                        print_event_red(b1, a1, 0, 0, 3, turns)
                # attack a2 unit if it has more than 30 HP
                elif (int(a2_HP) >= 30) and (a2_poisoned == False) and (a2_frozen == False):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a2.SC_Poisoned(int(b1_SS_Poison))
                        b1.CS_Poison()
                        print_event_red(b1, a2, 0, 0, 2, turns)
                    elif int(random_move) == 2:
                        a2.SC_Frozen()
                        b1.CS_Freeze()
                        print_event_red(b1, a2, 0, 0, 3, turns)
                # attack the opponent with the lowest health
                elif (int(a1_HP) < int(a2_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a1, total_damage, 0, 1, turns)
                elif (int(a2_HP) < int(a1_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a2, total_damage, 0, 1, turns)
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a1, total_damage, 0, 1, turns)
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a2, total_damage, 0, 1, turns)
        # b2 unit's move
        elif (b2_alive == True and b2_frozen == False):
            # Warrior and Tanker moves
            if int(b2_classjob) == 1 or int(b2_classjob) == 2:
                # attack the opponent with the lowest health
                if (int(a1_HP) < int(a2_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a2, total_damage, 0, 1, turns)
                elif (int(a2_HP) < int(a1_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a2, total_damage, 0, 1, turns)
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a1, total_damage, 0, 1, turns)
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a2, total_damage, 0, 1, turns)
            # Wizard moves
            elif int(b2_classjob) == 3:
                # Heal if the friendly unit has less than 10 HP point
                if (int(b1_HP) <= 10) and (b1_alive == True):
                    b1.healed(int(b2_SS_Heal))
                    b2.heal()
                    print_event_red(b2, b1, 0, b2_SS_Heal, 4, turns)
                # Cure if the friendly unit is poisoned
                elif (b1_poisoned == True) and (b1_alive == True):
                    b1.cured()
                    b2.cure()
                    print_event_red(b2, b1, 0, 0, 5, turns)
                elif (b2_poisoned == True) and (b2_alive == True):
                    b2.cured()
                    b2.cure()
                    print_event_red(b2, b2, 0, 0, 5, turns)
                # If the oponent unit has more than 30 HP than cast a spell (freeze or poison)
                # attack a1 unit if it has more than 30 HP
                elif (int(a1_HP) >= 30) and ((a1_poisoned == False) and (a1_frozen == False)):
                    random_move = random_move_generator()
                    if (int(random_move) == 1):
                        a1.SC_Poisoned(int(b2_SS_Poison))
                        b2.CS_Poison()
                        print_event_red(b2, a1, 0, 0, 2, turns)
                    elif (int(random_move) == 2):
                        a1.SC_Frozen()
                        b2.CS_Freeze()
                        print_event_red(b2, a1, 0, 0, 3, turns)
                # attack a2 unit if it has more than 30 HP
                elif (int(a2_HP) >= 30) and (a2_poisoned == False) and (a2_frozen == False):
                    random_move = random_move_generator()
                    if (int(random_move) == 1):
                        a2.SC_Poisoned(int(b2_SS_Poison))
                        b2.CS_Poison()
                        print_event_red(b2, a2, 0, 0, 2, turns)
                    elif (int(random_move) == 2):
                        a2.SC_Frozen()
                        b2.CS_Freeze()
                        print_event_red(b2, a2, 0, 0, 3, turns)           
                # attack the opponent with the lowest health
                elif (int(a1_HP) < int(a2_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a1, total_damage, 0, 1, turns)
                elif (int(a2_HP) < int(a1_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a2, total_damage, 0, 1, turns)
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a1, total_damage, 0, 1, turns)
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a2, total_damage, 0, 1, turns)
    elif int(unit_num) == 3:
        a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
        a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
        a3_name, a3_rank, a3_classjob, a3_HP, a3_ATK, a3_DEF, a3_SS_Heal, a3_SS_Poison, a3_EXP, a3_frozen, a3_poisoned, a3_alive = a3.status()
        b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
        b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
        b3_name, b3_rank, b3_classjob, b3_HP, b3_ATK, b3_DEF, b3_SS_Heal, b3_SS_Poison, b3_EXP, b3_frozen, b3_poisoned, b3_alive = b3.status()
        # b1 unit's move
        if (b1_alive == True) and (b1_frozen == False):
            # Warrior and Tanker moves
            if int(b1_classjob) == 1 or int(b1_classjob) == 2:
                # attack the opponent with the lowest health
                if (int(a1_HP) < int(a2_HP)) and (int(a1_HP) < int(a3_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a1, total_damage, 0, 1, turns)
                elif (int(a2_HP) < int(a1_HP)) and (int(a2_HP) < int(a3_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a2, total_damage, 0, 1, turns)
                elif (int(a3_HP) < int(a1_HP)) and (int(a3_HP) < int(a2_HP)) and (a3_alive == True):
                    total_damage, killed = a3.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a3, total_damage, 0, 1, turns)
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a1, total_damage, 0, 1, turns)
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a2, total_damage, 0, 1, turns)
                    elif a3_alive == True:
                        total_damage, killed = a3.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a3, total_damage, 0, 1, turns)
            # Wizard moves
            elif int(b1_classjob) == 3:
                # Heal if the friendly unit has less than 10 HP point
                if (int(b2_HP) <= 10) and (b2_alive == True):
                    b2.healed(int(b1_SS_Heal))
                    b1.heal()
                    print_event_red(b1, b2, 0, b1_SS_Heal, 4, turns)
                elif (int(b3_HP) <= 10) and (b3_alive == True):
                    b3.healed(int(b1_SS_Heal))
                    b1.heal()
                    print_event_red(b1, b3, 0, b1_SS_Heal, 4, turns)
                # Cure if the friendly unit is poisoned
                elif (b1_poisoned == True) and (b1_alive == True):
                    b1.cured()
                    b1.cure()
                    print_event_red(b1, b1, 0, 0, 5, turns)
                elif (b2_poisoned == True) and (b2_alive == True):
                    b2.cured()
                    b1.cure()
                    print_event_red(b1, b2, 0, 0, 5, turns)
                elif (b3_poisoned == True) and (b3_alive == True):
                    b3.cured()
                    b1.cure()
                    print_event_red(b1, b3, 0, 0, 5, turns)
                # If the oponent unit has more than 30 HP than cast a spell (freeze or poison)
                # attack a1 unit if it has more than 30 HP
                elif (int(a1_HP) >= 30) and (a1_poisoned == False) and (a1_frozen == False):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a1.SC_Poisoned(int(b1_SS_Poison))
                        b1.CS_Poison()
                        print_event_red(b1, a1, 0, 0, 2, turns)
                    elif int(random_move) == 2:
                        a1.SC_Frozen()
                        b1.CS_Freeze()
                        print_event_red(b1, a1, 0, 0, 3, turns)
                # attack a2 unit if it has more than 30 HP
                elif (int(a2_HP) >= 30) and (a2_poisoned == False) and (a2_frozen == False):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a2.SC_Poisoned(int(b1_SS_Poison))
                        b1.CS_Poison()
                        print_event_red(b1, a2, 0, 0, 2, turns) 
                    elif int(random_move) == 2:
                        a2.SC_Frozen()
                        b1.CS_Freeze()
                        print_event_red(b1, a2, 0, 0, 3, turns) 
                # attack a3 unit if it has more than 30 HP
                elif (int(a3_HP) >= 30) and ((a3_poisoned == False) and (a3_frozen == False)):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a3.SC_Poisoned(int(b1_SS_Poison))
                        b1.CS_Poison()
                        print_event_red(b1, a3, 0, 0, 2, turns) 
                    elif int(random_move) == 2:
                        a3.SC_Frozen()
                        b1.CS_Freeze()
                        print_event_red(b1, a3, 0, 0, 3, turns) 
                # attack the opponent with the lowest health
                elif (int(a1_HP) < int(a2_HP)) and (int(a1_HP) < int(a3_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a1, total_damage, 0, 1, turns) 
                elif (int(a2_HP) < int(a1_HP)) and (int(a2_HP) < int(a3_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a2, total_damage, 0, 1, turns) 
                elif (int(a3_HP) < int(a1_HP)) and (int(a3_HP) < int(a2_HP)) and (a3_alive == True):
                    total_damage, killed = a3.attacked(int(b1_ATK))
                    b1.attack(int(total_damage), killed)
                    print_event_red(b1, a3, total_damage, 0, 1, turns) 
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a3, total_damage, 0, 1, turns) 
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a2, total_damage, 0, 1, turns) 
                    elif a3_alive == True:
                        total_damage, killed = a3.attacked(int(b1_ATK))
                        b1.attack(int(total_damage), killed)
                        print_event_red(b1, a3, total_damage, 0, 1, turns)    
        # b2 unit's move
        elif (b2_alive == True and b2_frozen == False):
            # Warrior and Tanker moves
            if int(b2_classjob) == 1 or int(b2_classjob) == 2:
                # attack the opponent with the lowest health
                if (int(a1_HP) < int(a2_HP)) and (int(a1_HP) < int(a3_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b1, a1, total_damage, 0, 1, turns) 
                elif (int(a2_HP) < int(a1_HP)) and (int(a2_HP) < int(a3_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b1, a2, total_damage, 0, 1, turns) 
                elif (int(a3_HP) < int(a1_HP)) and (int(a3_HP) < int(a2_HP)) and (a3_alive == True):
                    total_damage, killed = a3.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a3, total_damage, 0, 1, turns) 
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a1, total_damage, 0, 1, turns) 
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a2, total_damage, 0, 1, turns) 
                    elif a3_alive == True:
                        total_damage, killed = a3.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a3, total_damage, 0, 1, turns) 
            # Wizard moves
            elif int(b2_classjob) == 3:
                # Heal if the friendly unit has less than 10 HP point
                if (int(b1_HP) <= 10) and (b1_alive == True):
                    b1.healed(int(b2_SS_Heal))
                    b2.heal()
                    print_event_red(b2, b1, 0, b2_SS_Heal, 5, turns) 
                elif (int(b3_HP) <= 10) and (b3_alive == True):
                    b3.healed(int(b2_SS_Heal))
                    b2.heal()
                    print_event_red(b2, b3, 0, b2_SS_Heal, 4, turns) 
                # Cure if the friendly unit is poisoned
                elif (b1_poisoned == True) and (b1_alive == True):
                    b1.cured()
                    b2.cure()
                    print_event_red(b2, b1, 0, 0, 5, turns)
                elif (b2_poisoned == True) and (b2_alive == True):
                    b2.cured()
                    b2.cure()
                    print_event_red(b2, b2, 0, 0, 5, turns)
                elif (b3_poisoned == True) and (b3_alive == True):
                    b3.cured()
                    b2.cure()
                    print_event_red(b2, b3, 0, 0, 5, turns) 
                # If the oponent unit has more than 30 HP than cast a spell (freeze or poison)
                # attack a1 unit if it has more than 30 HP
                elif (int(a1_HP) >= 30) and ((a1_poisoned == False) and (a1_frozen == False)):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a1.SC_Poisoned(int(b2_SS_Poison))
                        b2.CS_Poison()
                        print_event_red(b2, a1, 0, 0, 2, turns) 
                    elif int(random_move) == 2:
                        a1.SC_Frozen()
                        b2.CS_Freeze()
                        print_event_red(b2, a1, 0, 0, 3, turns) 
                # attack a2 unit if it has more than 30 HP
                elif (int(a2_HP) >= 30) and (a2_poisoned == False) and (a2_frozen == False):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a2.SC_Poisoned(int(b2_SS_Poison))
                        b2.CS_Poison()
                        print_event_red(b2, a2, 0, 0, 2, turns) 
                    elif int(random_move) == 2:
                        a2.SC_Frozen()
                        b2.CS_Freeze()
                        print_event_red(b2, a2, 0, 0, 3, turns) 
                # attack a3 unit if it has more than 30 HP
                elif (int(a3_HP) >= 30) and ((a3_poisoned == False) and (a3_frozen == False)):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a3.SC_Poisoned(int(b2_SS_Poison))
                        b2.CS_Poison()
                        print_event_red(b2, a3, 0, 0, 2, turns) 
                    elif int(random_move) == 2:
                        a3.SC_Frozen()
                        b2.CS_Freeze()
                        print_event_red(b2, a3, 0, 0, 3, turns) 
                # attack the opponent with the lowest health
                elif (int(a1_HP) < int(a2_HP)) and (int(a1_HP) < int(a3_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a1, total_damage, 0, 1, turns) 
                elif (int(a2_HP) < int(a1_HP)) and (int(a2_HP) < int(a3_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a2, total_damage, 0, 1, turns) 
                elif (int(a3_HP) < int(a1_HP)) and (int(a3_HP) < int(a2_HP)) and (a3_alive == True):
                    total_damage, killed = a3.attacked(int(b2_ATK))
                    b2.attack(int(total_damage), killed)
                    print_event_red(b2, a3, total_damage, 0, 1, turns) 
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a1, total_damage, 0, 1, turns) 
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a2, total_damage, 0, 1, turns) 
                    elif a3_alive == True:
                        total_damage, killed = a3.attacked(int(b2_ATK))
                        b2.attack(int(total_damage), killed)
                        print_event_red(b2, a3, total_damage, 0, 1, turns) 
        # b3 unit's move
        elif (b3_alive == True and b3_frozen == False):
            # Warrior and Tanker moves
            if int(b3_classjob) == 1 or int(b3_classjob) == 2:
                # attack the opponent with the lowest health
                if (int(a1_HP) < int(a2_HP)) and (int(a1_HP) < int(a3_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b3_ATK))
                    b3.attack(int(total_damage), killed)
                    print_event_red(b3, a1, total_damage, 0, 1, turns) 
                elif (int(a2_HP) < int(a1_HP)) and (int(a2_HP) < int(a3_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b3_ATK))
                    b3.attack(int(total_damage), killed)
                    print_event_red(b3, a2, total_damage, 0, 1, turns) 
                elif (int(a3_HP) < int(a1_HP)) and (int(a3_HP) < int(a2_HP)) and (a3_alive == True):
                    total_damage, killed = a3.attacked(int(b3_ATK))
                    b3.attack(int(total_damage), killed)
                    print_event_red(b3, a3, total_damage, 0, 1, turns) 
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b3_ATK))
                        b3.attack(int(total_damage), killed)
                        print_event_red(b3, a1, total_damage, 0, 1, turns) 
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b3_ATK))
                        b3.attack(int(total_damage), killed)
                        print_event_red(b3, a2, total_damage, 0, 1, turns) 
                    elif a3_alive == True:
                        total_damage, killed = a3.attacked(int(b3_ATK))
                        b3.attack(int(total_damage), killed)
                        print_event_red(b3, a3, total_damage, 0, 1, turns) 
            # Wizard moves
            elif int(b3_classjob) == 3:
                # Heal if the friendly unit has less than 10 HP point
                if (int(b1_HP) <= 10) and (b1_alive == True):
                    b1.healed(int(b3_SS_Heal))
                    b3.heal()
                    print_event_red(b3, b1, 0, b3_SS_Heal, 4, turns)
                elif (int(b2_HP) <= 10) and (b2_alive == True):
                    b2.healed(int(b3_SS_Heal))
                    b3.heal()
                    print_event_red(b3, b2, 0, b3_SS_Heal, 4, turns) 
                # Cure if the friendly unit is poisoned
                elif (b1_poisoned == True) and (b1_alive == True):
                    b1.cured()
                    b3.cure()
                    print_event_red(b3, b1, 0, 0, 5, turns) 
                elif (b2_poisoned == True) and (b2_alive == True):
                    b2.cured()
                    b3.cure()
                    print_event_red(b3, b2, 0, 0, 5, turns)
                elif (b3_poisoned == True) and (b3_alive == True):
                    b3.cured()
                    b3.cure()
                    print_event_red(b3, b3, 0, 0, 5, turns)
                # If the oponent unit has more than 30 HP than cast a spell (freeze or poison)
                # attack a1 unit if it has more than 30 HP
                elif (int(a1_HP) >= 30) and ((a1_poisoned == False) and (a1_frozen == False)):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a1.SC_Poisoned(int(b3_SS_Poison))
                        b3.CS_Poison()
                        print_event_red(b3, a1, 0, 0, 2, turns) 
                    elif int(random_move) == 2:
                        a1.SC_Frozen()
                        b3.CS_Freeze()
                        print_event_red(b3, a1, 0, 0, 3, turns) 
                # attack a2 unit if it has more than 30 HP
                elif (int(a2_HP) >= 30) and ((a2_poisoned == False) and (a2_frozen == False)):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a2.SC_Poisoned(int(b3_SS_Poison))
                        b3.CS_Poison()
                        print_event_red(b3, a2, 0, 0, 2, turns)
                    elif int(random_move) == 2:
                        a2.SC_Frozen()
                        b3.CS_Freeze()
                        print_event_red(b3, a2, 0, 0, 3, turns)
                # attack a3 unit if it has more than 30 HP
                elif (int(a3_HP) >= 30) and ((a3_poisoned == False) and (a3_frozen == False)):
                    random_move = random_move_generator()
                    if int(random_move) == 1:
                        a3.SC_Poisoned(int(b3_SS_Poison))
                        b3.CS_Poison()
                        print_event_red(b3, a3, 0, 0, 2, turns)
                    elif int(random_move) == 2:
                        a3.SC_Frozen()
                        b3.CS_Freeze()
                        print_event_red(b3, a3, 0, 0, 3, turns)
                # attack the opponent with the lowest health
                elif (int(a1_HP) < int(a2_HP)) and (int(a1_HP) < int(a3_HP)) and (a1_alive == True):
                    total_damage, killed = a1.attacked(int(b3_ATK))
                    b3.attack(int(total_damage), killed)
                    print_event_red(b3, a1, total_damage, 0, 1, turns)
                elif (int(a2_HP) < int(a1_HP)) and (int(a2_HP) < int(a3_HP)) and (a2_alive == True):
                    total_damage, killed = a2.attacked(int(b3_ATK))
                    b3.attack(int(total_damage), killed)
                    print_event_red(b3, a2, total_damage, 0, 1, turns)
                elif (int(a3_HP) < int(a1_HP)) and (int(a3_HP) < int(a2_HP)) and (a3_alive == True):
                    total_damage, killed = a3.attacked(int(b3_ATK))
                    b3.attack(int(total_damage), killed)
                    print_event_red(b3, a3, total_damage, 0, 1, turns)
                # if all the oponents have a same amount of health, than randomly attack one
                else:
                    if a1_alive == True:
                        total_damage, killed = a1.attacked(int(b3_ATK))
                        b3.attack(int(total_damage), killed)
                        print_event_red(b3, a1, total_damage, 0, 1, turns)
                    elif a2_alive == True:
                        total_damage, killed = a2.attacked(int(b3_ATK))
                        b3.attack(int(total_damage), killed)
                        print_event_red(b3, a2, total_damage, 0, 1, turns)
                    elif a3_alive == True:
                        total_damage, killed = a3.attacked(int(b3_ATK))
                        b3.attack(int(total_damage), killed)
                        print_event_red(b3, a3, total_damage, 0, 1, turns)

# User Moves
def user_moves(a1, a2, a3, b1, b2, b3, unit_num, BR, turns):
    a1_available, a2_available, a3_available, b1_available, b2_available, b3_available = reset_available()
    a1_alive, a2_alive, a3_alive, b1_alive, b2_alive, b3_alive = reset_alive()
    if int(BR) == 1:
        # 1 vs 1
        if int(unit_num) == 1:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            if ((a1_alive == True) and (a1_frozen == False)):
                a1_available = True
            if b1_alive == True:
                b1_available = True
            unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 1)
            if int(unit_selected) == 1:
                if int(a1_classjob) == 1 or int(a1_classjob) == 2:
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                elif int(a1_classjob) == 3:
                    pass
                else:
                    pass
            else:
                pass
        # 2 vs 2
        elif int(unit_num) == 2:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            if ((a1_alive == True) and (a1_frozen == False)):
                a1_available = True
            if ((a2_alive == True) and (a2_frozen == False)):
                a2_available = True
            if b1_alive == True:
                b1_available = True
            if b2_alive == True:
                b2_available = True
            unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 1)    
            if int(unit_selected) == 1:
                if int(a1_classjob) == 1 or int(a1_classjob) == 2:
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                elif int(a1_classjob) == 3:
                    pass
                else:
                    pass
            elif int(unit_selected) == 2:
                if int(a2_classjob) == 1 or int(a2_classjob) == 2:
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                elif int(a2_classjob) == 3:
                    pass
                else:
                    pass
            else:
                pass
        # 3 vs 3
        elif int(unit_num) == 3:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            a3_name, a3_rank, a3_classjob, a3_HP, a3_ATK, a3_DEF, a3_SS_Heal, a3_SS_Poison, a3_EXP, a3_frozen, a3_poisoned, a3_alive = a3.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            b3_name, b3_rank, b3_classjob, b3_HP, b3_ATK, b3_DEF, b3_SS_Heal, b3_SS_Poison, b3_EXP, b3_frozen, b3_poisoned, b3_alive = b3.status()
            if ((a1_alive == True) and (a1_frozen == False)):
                a1_available = True
            if ((a2_alive == True) and (a2_frozen == False)):
                a2_available = True
            if ((a3_alive == True) and (a3_frozen == False)):
                a3_available = True
            if b1_alive == True:
                b1_available = True
            if b2_alive == True:
                b2_available = True
            if b3_alive == True:
                b3_available = True
            unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 1)
            if int(unit_selected) == 1:
                if int(a1_classjob) == 1 or int(a1_classjob) == 2:
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                elif int(a1_classjob) == 3:
                    pass
                else:
                    pass
            elif int(unit_selected) == 2:
                if int(a2_classjob) == 1 or int(a2_classjob) == 2:
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                elif int(a2_classjob) == 3:
                    pass
                else:
                    pass
            elif int(unit_selected) == 3:
                if int(a3_classjob) == 1 or int(a3_classjob) == 2:
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                elif int(a3_classjob) == 3:
                    pass
                else:
                    pass
            else:
                pass
        ################################################################################################################
        # a1 attacks
        if int(unit_selected) == 1:
            if int(a1_classjob) == 1 or int(a1_classjob) == 2:
                if int(target_unit_selected) == 1:
                    total_damage, killed = b1.attacked(a1_ATK)
                    a1.attack(total_damage, killed)
                    print_event_blue(a1, b1, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 2:
                    total_damage, killed = b2.attacked(a1_ATK)
                    a1.attack(total_damage, killed)
                    print_event_blue(a1, b2, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 3:
                    total_damage, killed = b3.attacked(a1_ATK)
                    a1.attack(total_damage, killed)
                    print_event_blue(a1, b3, total_damage, 0, 1, turns)
                else:
                    pass
            elif int(a1_classjob) == 3:
                wizard_move = wizard_choose_move()
                if (int(wizard_move) == 1) or (int(wizard_move) == 2) or (int(wizard_move) == 3):
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                    if int(wizard_move) == 1:
                        if int(target_unit_selected) == 1:
                            total_damage, killed = b1.attacked(a1_ATK)
                            a1.attack(total_damage, killed)
                            print_event_blue(a1, b1, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 2:
                            total_damage, killed = b2.attacked(a1_ATK)
                            a1.attack(total_damage, killed)
                            print_event_blue(a1, b2, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 3:
                            total_damage, killed = b3.attacked(a1_ATK)
                            a1.attack(total_damage, killed)
                            print_event_blue(a1, b3, total_damage, 0, 1, turns)
                        else:
                            pass
                    elif int(wizard_move) == 2:
                        if int(target_unit_selected) == 1:
                            b1.SC_Poisoned(a1_SS_Poison)
                            a1.CS_Poison()
                            print_event_blue(a1, b1, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 2:
                            b2.SC_Poisoned(a1_SS_Poison)
                            a1.CS_Poison()
                            print_event_blue(a1, b2, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 3:
                            b3.SC_Poisoned(a1_SS_Poison)
                            a1.CS_Poison()
                            print_event_blue(a1, b3, 0, 0, 2, turns)
                        else:
                            pass
                    elif int(wizard_move) == 3:
                        if int(target_unit_selected) == 1:
                            b1.SC_Frozen()
                            a1.CS_Freeze
                            print_event_blue(a1, b1, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 2:
                            b2.SC_Frozen()
                            a1.CS_Freeze
                            print_event_blue(a1, b2, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 3:
                            b3.SC_Frozen()
                            a1.CS_Freeze
                            print_event_blue(a1, b3, 0, 0, 3, turns)
                        else:
                            pass
                    else:
                        pass
                elif int(wizard_move) == (4 or 5):
                    target_unit_selected = wizard_choose_unit(a1_alive, a2_alive, a3_alive, a1, a2, a3, 3)
                    if int(wizard_move) == 4:
                        if int(target_unit_selected) == 1:
                            a1.healed(a1_SS_Heal)
                            a1.heal()
                            print_event_blue(a1, a1, 0, a1_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 2:
                            a2.healed(a1_SS_Heal)
                            a1.heal()
                            print_event_blue(a1, a2, 0, a1_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 3:
                            a3.healed(a1_SS_Heal)
                            a1.heal()
                            print_event_blue(a1, a3, 0, a1_SS_Heal, 4, turns)
                        else:
                            pass
                    elif int(wizard_move) == 5:
                        if int(target_unit_selected) == 1:
                            a1.cured()
                            a1.cure()
                            print_event_blue(a1, a1, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 2:
                            a2.cure()
                            a1.cured()
                            print_event_blue(a1, a2, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 3:
                            a3.cured()
                            a1.cure()
                            print_event_blue(a1, a3, 0, 0, 5, turns)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        ################################################################################################################
        # a2 attacks
        elif int(unit_selected) == 2:
            if int(a2_classjob) == 1 or int(a2_classjob) == 2:
                if int(target_unit_selected) == 1:
                    total_damage, killed = b1.attacked(a2_ATK)
                    a2.attack(total_damage, killed)
                    print_event_blue(a2, b1, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 2:
                    total_damage, killed = b2.attacked(a2_ATK)
                    a2.attack(total_damage, killed)
                    print_event_blue(a2, b2, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 3:
                    total_damage, killed = b3.attacked(a2_ATK)
                    a2.attack(total_damage, killed)
                    print_event_blue(a2, b3, total_damage, 0, 1, turns)
                else:
                    pass
            elif int(a2_classjob) == 3:
                wizard_move = wizard_choose_move()
                if (int(wizard_move) == 1) or (int(wizard_move) == 2) or (int(wizard_move) == 3):
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                    if int(wizard_move) == 1:
                        if int(target_unit_selected) == 1:
                            total_damage, killed = b1.attacked(a2_ATK)
                            a2.attack(total_damage, killed)
                            print_event_blue(a2, b1, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 2:
                            total_damage, killed = b2.attacked(a2_ATK)
                            a2.attack(total_damage, killed)
                            print_event_blue(a2, b2, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 3:
                            total_damage, killed = b3.attacked(a2_ATK)
                            a2.attack(total_damage, killed)
                            print_event_blue(a2, b3, total_damage, 0, 1, turns)
                        else:
                            pass
                    elif int(wizard_move) == 2:
                        if int(target_unit_selected) == 1:
                            b1.SC_Poisoned(a2_SS_Poison)
                            a2.CS_Poison()
                            print_event_blue(a2, b1, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 2:
                            b2.SC_Poisoned(a2_SS_Poison)
                            a2.CS_Poison()
                            print_event_blue(a2, b2, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 3:
                            b3.SC_Poisoned(a2_SS_Poison)
                            a2.CS_Poison()
                            print_event_blue(a2, b3, 0, 0, 2, turns)
                        else:
                            pass
                    elif int(wizard_move) == 3:
                        if int(target_unit_selected) == 1:
                            b1.SC_Frozen()
                            a2.CS_Freeze
                            print_event_blue(a2, b1, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 2:
                            b2.SC_Frozen()
                            a2.CS_Freeze
                            print_event_blue(a2, b2, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 3:
                            b3.SC_Frozen()
                            a2.CS_Freeze
                            print_event_blue(a2, b3, 0, 0, 3, turns)
                        else:
                            pass
                    else:
                        pass
                elif int(wizard_move) == (4 or 5):
                    target_unit_selected = wizard_choose_unit(a1_alive, a2_alive, a3_alive, a1, a2, a3, 3)
                    if int(wizard_move) == 4:
                        if int(target_unit_selected) == 1:
                            a1.healed(a2_SS_Heal)
                            a2.heal()
                            print_event_blue(a2, a1, 0, a2_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 2:
                            a2.healed(a2_SS_Heal)
                            a2.heal()
                            print_event_blue(a2, a2, 0, a2_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 3:
                            a3.healed(a2_SS_Heal)
                            a2.heal()
                            print_event_blue(a2, a3, 0, a2_SS_Heal, 4, turns)
                        else:
                            pass
                    elif int(wizard_move) == 5:
                        if int(target_unit_selected) == 1:
                            a1.cured()
                            a2.cure()
                            print_event_blue(a2, a1, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 2:
                            a2.cure()
                            a2.cured()
                            print_event_blue(a2, a2, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 3:
                            a3.cured()
                            a2.cure()
                            print_event_blue(a2, a3, 0, 0, 5, turns)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        ################################################################################################################
        # a3 attacks
        elif int(unit_selected) == 3:
            if int(a3_classjob) == 1 or int(a3_classjob) == 2:
                if int(target_unit_selected) == 1:
                    total_damage, killed = b1.attacked(a3_ATK)
                    a3.attack(total_damage, killed)
                    print_event_blue(a3, b1, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 2:
                    total_damage, killed = b2.attacked(a3_ATK)
                    a3.attack(total_damage, killed)
                    print_event_blue(a3, b2, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 3:
                    total_damage, killed = b3.attacked(a3_ATK)
                    a3.attack(total_damage, killed)
                    print_event_blue(a3, b3, total_damage, 0, 1, turns)
                else:
                    pass
            elif int(a3_classjob) == 3:
                wizard_move = wizard_choose_move()
                if (int(wizard_move) == 1) or (int(wizard_move) == 2) or (int(wizard_move) == 3):
                    target_unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 2)
                    if int(wizard_move) == 1:
                        if int(target_unit_selected) == 1:
                            total_damage, killed = b1.attacked(a3_ATK)
                            a3.attack(total_damage, killed)
                            print_event_blue(a3, b1, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 2:
                            total_damage, killed = b2.attacked(a3_ATK)
                            a3.attack(total_damage, killed)
                            print_event_blue(a3, b2, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 3:
                            total_damage, killed = b3.attacked(a3_ATK)
                            a3.attack(total_damage, killed)
                            print_event_blue(a3, b3, total_damage, 0, 1, turns)
                        else:
                            pass
                    elif int(wizard_move) == 2:
                        if int(target_unit_selected) == 1:
                            b1.SC_Poisoned(a3_SS_Poison)
                            a3.CS_Poison()
                            print_event_blue(a3, b1, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 2:
                            b2.SC_Poisoned(a3_SS_Poison)
                            a3.CS_Poison()
                            print_event_blue(a3, b2, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 3:
                            b3.SC_Poisoned(a3_SS_Poison)
                            a3.CS_Poison()
                            print_event_blue(a3, b3, 0, 0, 2, turns)
                        else:
                            pass
                    elif int(wizard_move) == 3:
                        if int(target_unit_selected) == 1:
                            b1.SC_Frozen()
                            a3.CS_Freeze
                            print_event_blue(a3, b1, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 2:
                            b2.SC_Frozen()
                            a3.CS_Freeze
                            print_event_blue(a3, b2, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 3:
                            b3.SC_Frozen()
                            a3.CS_Freeze
                            print_event_blue(a3, b3, 0, 0, 3, turns)
                        else:
                            pass
                    else:
                        pass
                elif int(wizard_move) == (4 or 5):
                    target_unit_selected = wizard_choose_unit(a1_alive, a2_alive, a3_alive, a1, a2, a3, 3)
                    if int(wizard_move) == 4:
                        if int(target_unit_selected) == 1:
                            a1.healed(a3_SS_Heal)
                            a3.heal()
                            print_event_blue(a3, a1, 0, a3_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 2:
                            a2.healed(a3_SS_Heal)
                            a3.heal()
                            print_event_blue(a3, a2, 0, a3_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 3:
                            a3.healed(a3_SS_Heal)
                            a3.heal()
                            print_event_blue(a3, a3, 0, a3_SS_Heal, 4, turns)
                        else:
                            pass
                    elif int(wizard_move) == 5:
                        if int(target_unit_selected) == 1:
                            a1.cured()
                            a3.cure()
                            print_event_blue(a3, a1, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 2:
                            a2.cure()
                            a3.cured()
                            print_event_blue(a3, a2, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 3:
                            a3.cured()
                            a3.cure()
                            print_event_blue(a3, a3, 0, 0, 5, turns)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    elif int(BR) == 2:
        # 1 vs 1
        if int(unit_num) == 1:
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            if ((b1_alive == True) and (b1_frozen == False)):
                b1_available = True
            if a1_alive == True:
                a1_available = True
            unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 1)
            if int(unit_selected) == 1:
                if int(b1_classjob) == 1 or int(b1_classjob) == 2:
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                elif int(b1_classjob) == 3:
                    pass
                else:
                    pass
            else:
                pass
        # 2 vs 2
        elif int(unit_num) == 2:
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            if ((b1_alive == True) and (b1_frozen == False)):
                b1_available = True
            if ((b2_alive == True) and (b2_frozen == False)):
                b2_available = True
            if a1_alive == True:
                a1_available = True
            if a2_alive == True:
                a2_available = True
            unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 1)    
            if int(unit_selected) == 1:
                if int(b1_classjob) == 1 or int(b1_classjob) == 2:
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                elif int(b1_classjob) == 3:
                    pass
                else:
                    pass
            elif int(unit_selected) == 2:
                if int(b2_classjob) == 1 or int(b2_classjob) == 2:
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                elif int(b2_classjob) == 3:
                    pass
                else:
                    pass
            else:
                pass
        # 3 vs 3
        elif int(unit_num) == 3:
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            b3_name, b3_rank, b3_classjob, b3_HP, b3_ATK, b3_DEF, b3_SS_Heal, b3_SS_Poison, b3_EXP, b3_frozen, b3_poisoned, b3_alive = b3.status()
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            a3_name, a3_rank, a3_classjob, a3_HP, a3_ATK, a3_DEF, a3_SS_Heal, a3_SS_Poison, a3_EXP, a3_frozen, a3_poisoned, a3_alive = a3.status()
            if ((b1_alive == True) and (b1_frozen == False)):
                b1_available = True
            if ((b2_alive == True) and (b2_frozen == False)):
                b2_available = True
            if ((b3_alive == True) and (b3_frozen == False)):
                b3_available = True
            if a1_alive == True:
                a1_available = True
            if a2_alive == True:
                a2_available = True
            if a3_alive == True:
                a3_available = True
            unit_selected = choose_unit(b1_available, b2_available, b3_available, b1, b2, b3, 1)
            if int(unit_selected) == 1:
                if int(b1_classjob) == 1 or int(b1_classjob) == 2:
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                elif int(b1_classjob) == 3:
                    pass
                else:
                    pass
            elif int(unit_selected) == 2:
                if int(b2_classjob) == 1 or int(b2_classjob) == 2:
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                elif int(b2_classjob) == 3:
                    pass
                else:
                    pass
            elif int(unit_selected) == 3:
                if int(b3_classjob) == 1 or int(b3_classjob) == 2:
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                elif int(b3_classjob) == 3:
                    pass
                else:
                    pass
            else:
                pass
        ################################################################################################################
        # b1 attacks
        if int(unit_selected) == 1:
            if int(b1_classjob) == 1 or int(b1_classjob) == 2:
                if int(target_unit_selected) == 1:
                    total_damage, killed = a1.attacked(b1_ATK)
                    b1.attack(total_damage, killed)
                    print_event_red(b1, a1, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 2:
                    total_damage, killed = a2.attacked(b1_ATK)
                    b1.attack(total_damage, killed)
                    print_event_red(b1, a2, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 3:
                    total_damage, killed = a3.attacked(b1_ATK)
                    b1.attack(total_damage, killed)
                    print_event_red(b1, a3, total_damage, 0, 1, turns)
                else:
                    pass
            elif int(b1_classjob) == 3:
                wizard_move = wizard_choose_move()
                if (int(wizard_move) == 1) or (int(wizard_move) == 2) or (int(wizard_move) == 3):
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                    if int(wizard_move) == 1:
                        if int(target_unit_selected) == 1:
                            total_damage, killed = a1.attacked(b1_ATK)
                            b1.attack(total_damage, killed)
                            print_event_red(b1, a1, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 2:
                            total_damage, killed = a2.attacked(b1_ATK)
                            b1.attack(total_damage, killed)
                            print_event_red(b1, a2, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 3:
                            total_damage, killed = a3.attacked(b1_ATK)
                            b1.attack(total_damage, killed)
                            print_event_red(b1, a3, total_damage, 0, 1, turns)
                        else:
                            pass
                    elif int(wizard_move) == 2:
                        if int(target_unit_selected) == 1:
                            a1.SC_Poisoned(b1_SS_Poison)
                            b1.CS_Poison()
                            print_event_red(b1, a1, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 2:
                            a2.SC_Poisoned(b1_SS_Poison)
                            b1.CS_Poison()
                            print_event_red(b1, a2, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 3:
                            a3.SC_Poisoned(b1_SS_Poison)
                            b1.CS_Poison()
                            print_event_red(b1, a3, 0, 0, 2, turns)
                        else:
                            pass
                    elif int(wizard_move) == 3:
                        if int(target_unit_selected) == 1:
                            a1.SC_Frozen()
                            b1.CS_Freeze
                            print_event_red(b1, a1, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 2:
                            a2.SC_Frozen()
                            b1.CS_Freeze
                            print_event_red(b1, a2, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 3:
                            a3.SC_Frozen()
                            b1.CS_Freeze
                            print_event_red(b1, a3, 0, 0, 3, turns)
                        else:
                            pass
                    else:
                        pass
                elif int(wizard_move) == (4 or 5):
                    target_unit_selected = wizard_choose_unit(b1_alive, b2_alive, b3_alive, b1, b2, b3, 3)
                    if int(wizard_move) == 4:
                        if int(target_unit_selected) == 1:
                            b1.healed(b1_SS_Heal)
                            b1.heal()
                            print_event_red(b1, b1, 0, b1_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 2:
                            b2.healed(b1_SS_Heal)
                            b1.heal()
                            print_event_red(b1, b2, 0, b1_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 3:
                            b3.healed(b1_SS_Heal)
                            b1.heal()
                            print_event_red(b1, b3, 0, b1_SS_Heal, 4, turns)
                        else:
                            pass
                    elif int(wizard_move) == 5:
                        if int(target_unit_selected) == 1:
                            b1.cured()
                            b1.cure()
                            print_event_red(b1, b1, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 2:
                            b2.cure()
                            b1.cured()
                            print_event_red(b1, b2, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 3:
                            b3.cured()
                            b1.cure()
                            print_event_red(b1, b3, 0, 0, 5, turns)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        ################################################################################################################
        # b2 attacks
        elif int(unit_selected) == 2:
            if int(b2_classjob) == 1 or int(b2_classjob) == 2:
                if int(target_unit_selected) == 1:
                    total_damage, killed = a1.attacked(b2_ATK)
                    b2.attack(total_damage, killed)
                    print_event_red(b2, a1, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 2:
                    total_damage, killed = a2.attacked(b2_ATK)
                    b2.attack(total_damage, killed)
                    print_event_red(b2, a2, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 3:
                    total_damage, killed = a3.attacked(b2_ATK)
                    b2.attack(total_damage, killed)
                    print_event_red(b2, a3, total_damage, 0, 1, turns)
                else:
                    pass
            elif int(b2_classjob) == 3:
                wizard_move = wizard_choose_move()
                if (int(wizard_move) == 1) or (int(wizard_move) == 2) or (int(wizard_move) == 3):
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                    if int(wizard_move) == 1:
                        if int(target_unit_selected) == 1:
                            total_damage, killed = a1.attacked(b2_ATK)
                            b2.attack(total_damage, killed)
                            print_event_red(b2, a1, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 2:
                            total_damage, killed = a2.attacked(b2_ATK)
                            b2.attack(total_damage, killed)
                            print_event_red(b2, a2, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 3:
                            total_damage, killed = a3.attacked(b2_ATK)
                            b2.attack(total_damage, killed)
                            print_event_red(b2, a3, total_damage, 0, 1, turns)
                        else:
                            pass
                    elif int(wizard_move) == 2:
                        if int(target_unit_selected) == 1:
                            a1.SC_Poisoned(b2_SS_Poison)
                            b2.CS_Poison()
                            print_event_red(b2, a1, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 2:
                            a2.SC_Poisoned(b2_SS_Poison)
                            b2.CS_Poison()
                            print_event_red(b2, a2, 0, 0, 2, turns)
                        elif int(target_unit_selected) == 3:
                            a3.SC_Poisoned(b2_SS_Poison)
                            b2.CS_Poison()
                            print_event_red(b2, a3, 0, 0, 2, turns)
                        else:
                            pass
                    elif int(wizard_move) == 3:
                        if int(target_unit_selected) == 1:
                            a1.SC_Frozen()
                            b2.CS_Freeze
                            print_event_red(b2, a1, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 2:
                            a2.SC_Frozen()
                            b2.CS_Freeze
                            print_event_red(b2, a2, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 3:
                            a3.SC_Frozen()
                            b2.CS_Freeze
                            print_event_red(b2, a3, 0, 0, 3, turns)
                        else:
                            pass
                    else:
                        pass
                elif int(wizard_move) == (4 or 5):
                    target_unit_selected = wizard_choose_unit(b1_alive, b2_alive, b3_alive, b1, b2, b3, 3)
                    if int(wizard_move) == 4:
                        if int(target_unit_selected) == 1:
                            b1.healed(b2_SS_Heal)
                            b2.heal()
                            print_event_red(b2, b1, 0, b2_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 2:
                            b2.healed(b2_SS_Heal)
                            b2.heal()
                            print_event_red(b2, b2, 0, b2_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 3:
                            b3.healed(b2_SS_Heal)
                            b2.heal()
                            print_event_red(b2, b3, 0, b2_SS_Heal, 4, turns)
                        else:
                            pass
                    elif int(wizard_move) == 5:
                        if int(target_unit_selected) == 1:
                            b1.cured()
                            b2.cure()
                            print_event_red(b2, b1, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 2:
                            b2.cure()
                            b2.cured()
                            print_event_red(b2, b2, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 3:
                            b3.cured()
                            b2.cure()
                            print_event_red(b2, b3, 0, 0, 5, turns)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        ################################################################################################################
        # b3 attacks
        elif int(unit_selected) == 3:
            if int(b3_classjob) == 1 or int(b3_classjob) == 2:
                if int(target_unit_selected) == 1:
                    total_damage, killed = a1.attacked(b3_ATK)
                    b3.attack(total_damage, killed)
                    print_event_red(b3, a1, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 2:
                    total_damage, killed = a2.attacked(b3_ATK)
                    b3.attack(total_damage, killed)
                    print_event_red(b3, a2, total_damage, 0, 1, turns)
                elif int(target_unit_selected) == 3:
                    total_damage, killed = a3.attacked(b3_ATK)
                    b3.attack(total_damage, killed)
                    print_event_red(b3, a3, total_damage, 0, 1, turns)
                else:
                    pass
            elif int(b3_classjob) == 3:
                wizard_move = wizard_choose_move()
                if (int(wizard_move) == 1) or (int(wizard_move) == 2) or (int(wizard_move) == 3):
                    target_unit_selected = choose_unit(a1_available, a2_available, a3_available, a1, a2, a3, 2)
                    if int(wizard_move) == 1:
                        if int(target_unit_selected) == 1:
                            total_damage, killed = a1.attacked(b3_ATK)
                            b3.attack(total_damage, killed)
                            print_event_red(b3, a1, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 2:
                            total_damage, killed = a2.attacked(b3_ATK)
                            b3.attack(total_damage, killed)
                            print_event_red(b3, a2, total_damage, 0, 1, turns)
                        elif int(target_unit_selected) == 3:
                            total_damage, killed = a3.attacked(b3_ATK)
                            b3.attack(total_damage, killed)
                            print_event_red(b3, a3, total_damage, 0, 1, turns)
                        else:
                            pass
                    elif int(wizard_move) == 2:
                        if int(target_unit_selected) == 1:
                            a1.SC_Poisoned(b3_SS_Poison)
                            b3.CS_Poison()
                            print_event_red(b3, a1, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 2:
                            a2.SC_Poisoned(b3_SS_Poison)
                            b3.CS_Poison()
                            print_event_red(b3, a2, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 3:
                            a3.SC_Poisoned(b3_SS_Poison)
                            b3.CS_Poison()
                            print_event_red(b3, a3, 0, 0, 2, turns)
                        else:
                            pass
                    elif int(wizard_move) == 3:
                        if int(target_unit_selected) == 1:
                            a1.SC_Frozen()
                            b3.CS_Freeze
                            print_event_red(b3, a1, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 2:
                            a2.SC_Frozen()
                            b3.CS_Freeze
                            print_event_red(b3, a2, 0, 0, 3, turns)
                        elif int(target_unit_selected) == 3:
                            a3.SC_Frozen()
                            b3.CS_Freeze
                            print_event_red(b3, a3, 0, 0, 3, turns)
                        else:
                            pass
                    else:
                        pass
                elif int(wizard_move) == (4 or 5):
                    target_unit_selected = wizard_choose_unit(b1_alive, b2_alive, b3_alive, b1, b2, b3, 3)
                    if int(wizard_move) == 4:
                        if int(target_unit_selected) == 1:
                            b1.healed(b3_SS_Heal)
                            b3.heal()
                            print_event_red(b3, b1, 0, b3_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 2:
                            b2.healed(b3_SS_Heal)
                            b3.heal()
                            print_event_red(b3, b2, 0, b3_SS_Heal, 4, turns)
                        elif int(target_unit_selected) == 3:
                            b3.healed(b3_SS_Heal)
                            b3.heal()
                            print_event_red(b3, b3, 0, b3_SS_Heal, 4, turns)
                        else:
                            pass
                    elif int(wizard_move) == 5:
                        if int(target_unit_selected) == 1:
                            b1.cured()
                            b3.cure()
                            print_event_red(b3, b1, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 2:
                            b2.cure()
                            b3.cured()
                            print_event_red(b3, b2, 0, 0, 5, turns)
                        elif int(target_unit_selected) == 3:
                            b3.cured()
                            b3.cure()
                            print_event_red(b3, b3, 0, 0, 5, turns)
                        else:
                            pass
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass

# Switch Turns
def switch_turns(turn):
    if turn == "blue_team":
        turn = "red_team"
    elif turn == "red_team":
        turn = "blue_team"
    return turn


##############################################################################################################


# game loop for uvu
def game_loop_uvu(game_mode):
    myFile = open("GameLog.txt", "a")
    now = time.localtime()
    timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    myFile.write("{0} Chose User vs User\n\n".format(timestamp))
    myFile.close()
    a1, a2, a3, b1, b2, b3, unit_num = unit_choice(game_mode)
    game_loop = True
    turn = "red_team"
    count_blue = 1
    count_red = 1
    # UVA 1 vs 1
    if int(unit_num) == 1:
        while game_loop == True:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            turn = switch_turns(turn)
            if turn == "blue_team":
                print("\n==================================# {0} Turn (Blue Team)==================================".format(count_blue))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 1, count_blue)
                count_blue += 1
            elif turn == "red_team":
                print("\n===================================# {0} Turn (Red Team)===================================".format(count_red))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 2, count_red)
                count_red += 1
            
            # check_status
            a1.check_status()
            b1.check_status()

            # Game Over
            if a1_alive == False:
                game_loop = False
                print("Blue Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} RED TEAM WON!!".format(timestamp))
            elif b1_alive == False:
                game_loop = False
                print("Red Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} BLUE TEAM WON!!".format(timestamp))
        myFile.write("\nBlue Team Current Status\n")
        a1.txt_status_last(myFile)
        myFile.write("Red Team Current Status\n")
        b1.txt_status_last(myFile)
        myFile.close()
        print("Blue Team Current Status")
        a1.print_status_last()
        print("Red Team Current Status")
        b1.print_status_last()
        to_end = input("Press \'Enter\' to end...")

    # UVA 2 vs 2
    elif int(unit_num) == 2:
        while game_loop == True:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            turn = switch_turns(turn)
            if turn == "blue_team":
                print("\n==================================# {0} Turn (Blue Team)==================================".format(count_blue))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 1, count_blue)
                count_blue += 1
            elif turn == "red_team":
                print("\n===================================# {0} Turn (Red Team)===================================".format(count_red))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 2, count_red)
                count_red += 1
                

            # check_status
            a1.check_status()
            a2.check_status()
            b1.check_status()
            b2.check_status()

            # Game Over
            if (a1_alive == False) and (a2_alive == False):
                game_loop = False
                print("Blue Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} RED TEAM WON!!".format(timestamp))
            elif (b1_alive == False) and (b2_alive == False):
                game_loop = False
                print("Red Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} BLUE TEAM WON!!".format(timestamp))
        myFile.write("\nBlue Team Current Status\n")
        a1.txt_status_last(myFile)
        a2.txt_status_last(myFile)
        myFile.write("Red Team Current Status\n")
        b1.txt_status_last(myFile)
        b2.txt_status_last(myFile)
        myFile.close()
        print("Blue Team Current Status")
        a1.print_status_last()
        a2.print_status_last()
        print("Red Team Current Status")
        b1.print_status_last()
        b2.print_status_last()
        to_end = input("Press \'Enter\' to end...")

    # UVA 3 vs 3
    elif int(unit_num) == 3:
        while game_loop == True:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            a3_name, a3_rank, a3_classjob, a3_HP, a3_ATK, a3_DEF, a3_SS_Heal, a3_SS_Poison, a3_EXP, a3_frozen, a3_poisoned, a3_alive = a3.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            b3_name, b3_rank, b3_classjob, b3_HP, b3_ATK, b3_DEF, b3_SS_Heal, b3_SS_Poison, b3_EXP, b3_frozen, b3_poisoned, b3_alive = b3.status()
            turn = switch_turns(turn)
            if turn == "blue_team":
                print("\n==================================# {0} Turn (Blue Team)==================================".format(count_blue))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 1, count_blue)
                count_blue += 1
            elif turn == "red_team":
                print("\n===================================# {0} Turn (Red Team)===================================".format(count_red))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 2, count_red)
                count_red += 1
            
            # check_status
            a1.check_status()
            a2.check_status()
            a3.check_status()
            b1.check_status()
            b2.check_status()
            b3.check_status()

            # Game Over
            if (a1_alive == False) and (a2_alive == False) and (a3_alive == False):
                game_loop = False
                print("Blue Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} RED TEAM WON!!".format(timestamp))
            elif (b1_alive == False) and (b2_alive == False) and (b3_alive == False):
                game_loop = False
                print("Red Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} BLUE TEAM WON!!".format(timestamp))
        myFile.write("\nBlue Team Current Status\n")
        a1.txt_status_last(myFile)
        a2.txt_status_last(myFile)
        a3.txt_status_last(myFile)
        myFile.write("Red Team Current Status\n")
        b1.txt_status_last(myFile)
        b2.txt_status_last(myFile)
        b3.txt_status_last(myFile)
        myFile.close()
        print("Blue Team Current Status")
        a1.print_status_last()
        a2.print_status_last()
        a3.print_status_last()
        print("Red Team Current Status")
        b1.print_status_last()
        b2.print_status_last()
        b3.print_status_last()
        to_end = input("Press \'Enter\' to end...")
    else:
        pass

# game loop for uva
def game_loop_uva(game_mode):
    myFile = open("GameLog.txt", "a")
    now = time.localtime()
    timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    myFile.write("{0} Chose User vs AI\n\n".format(timestamp))
    myFile.close()
    a1, a2, a3, b1, b2, b3, unit_num = unit_choice(game_mode)
    game_loop = True
    turn = "red_team"
    count_blue = 1
    count_red = 1
    # UVA 1 vs 1
    if int(unit_num) == 1:
        while game_loop == True:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            turn = switch_turns(turn)
            if turn == "blue_team":
                print("\n==================================# {0} Turn (Blue Team)==================================".format(count_blue))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 1, count_blue)
                count_blue += 1
            elif turn == "red_team":
                print("\n===================================# {0} Turn (Red Team)===================================".format(count_red))
                AI_moves(a1, a2, a3, b1, b2, b3, unit_num, count_red)
                count_red += 1
            
            # check_status
            a1.check_status()
            b1.check_status()

            # Game Over
            if a1_alive == False:
                game_loop = False
                print("Blue Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} RED TEAM WON!!".format(timestamp))
            elif b1_alive == False:
                game_loop = False
                print("Red Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} BLUE TEAM WON!!".format(timestamp))
        myFile.write("\nBlue Team Current Status\n")
        a1.txt_status_last(myFile)
        myFile.write("Red Team Current Status\n")
        b1.txt_status_last(myFile)
        myFile.close()
        print("Blue Team Current Status")
        a1.print_status_last()
        print("Red Team Current Status")
        b1.print_status_last()
        to_end = input("Press \'Enter\' to end...")
            
    # UVA 2 vs 2
    elif int(unit_num) == 2:
        while game_loop == True:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            turn = switch_turns(turn)
            if turn == "blue_team":
                print("\n==================================# {0} Turn (Blue Team)==================================".format(count_blue))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 1, count_blue)
                count_blue += 1
            elif turn == "red_team":
                print("\n===================================# {0} Turn (Red Team)===================================".format(count_red))
                AI_moves(a1, a2, a3, b1, b2, b3, unit_num, count_red)
                count_red += 1

            # check_status
            a1.check_status()
            a2.check_status()
            b1.check_status()
            b2.check_status()

            # Game Over
            if (a1_alive == False) and (a2_alive == False):
                game_loop = False
                print("Blue Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} RED TEAM WON!!".format(timestamp))
            elif (b1_alive == False) and (b2_alive == False):
                game_loop = False
                print("Red Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} BLUE TEAM WON!!".format(timestamp))
        myFile.write("\nBlue Team Current Status\n")
        a1.txt_status_last(myFile)
        a2.txt_status_last(myFile)
        myFile.write("Red Team Current Status\n")
        b1.txt_status_last(myFile)
        b2.txt_status_last(myFile)
        myFile.close()
        print("Blue Team Current Status")
        a1.print_status_last()
        a2.print_status_last()
        print("Red Team Current Status")
        b1.print_status_last()
        b2.print_status_last()
        to_end = input("Press \'Enter\' to end...")

    # UVA 3 vs 3
    elif int(unit_num) == 3:
        while game_loop == True:
            a1_name, a1_rank, a1_classjob, a1_HP, a1_ATK, a1_DEF, a1_SS_Heal, a1_SS_Poison, a1_EXP, a1_frozen, a1_poisoned, a1_alive = a1.status()
            a2_name, a2_rank, a2_classjob, a2_HP, a2_ATK, a2_DEF, a2_SS_Heal, a2_SS_Poison, a2_EXP, a2_frozen, a2_poisoned, a2_alive = a2.status()
            a3_name, a3_rank, a3_classjob, a3_HP, a3_ATK, a3_DEF, a3_SS_Heal, a3_SS_Poison, a3_EXP, a3_frozen, a3_poisoned, a3_alive = a3.status()
            b1_name, b1_rank, b1_classjob, b1_HP, b1_ATK, b1_DEF, b1_SS_Heal, b1_SS_Poison, b1_EXP, b1_frozen, b1_poisoned, b1_alive = b1.status()
            b2_name, b2_rank, b2_classjob, b2_HP, b2_ATK, b2_DEF, b2_SS_Heal, b2_SS_Poison, b2_EXP, b2_frozen, b2_poisoned, b2_alive = b2.status()
            b3_name, b3_rank, b3_classjob, b3_HP, b3_ATK, b3_DEF, b3_SS_Heal, b3_SS_Poison, b3_EXP, b3_frozen, b3_poisoned, b3_alive = b3.status()
            turn = switch_turns(turn)
            if turn == "blue_team":
                print("\n==================================# {0} Turn (Blue Team)==================================".format(count_blue))
                user_moves(a1, a2, a3, b1, b2, b3, unit_num, 1, count_blue)
                count_blue += 1
            elif turn == "red_team":
                print("\n===================================# {0} Turn (Red Team)===================================".format(count_red))
                AI_moves(a1, a2, a3, b1, b2, b3, unit_num, count_red)
                count_red += 1
            
            # check_status
            a1.check_status()
            a2.check_status()
            a3.check_status()
            b1.check_status()
            b2.check_status()
            b3.check_status()

            # Game Over
            if (a1_alive == False) and (a2_alive == False) and (a3_alive == False):
                game_loop = False
                print("Blue Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} RED TEAM WON!!".format(timestamp))
            elif (b1_alive == False) and (b2_alive == False) and (b3_alive == False):
                game_loop = False
                print("Red Team No Unit alive... GAME OVER")
                myFile = open("GameLog.txt", "a")
                now = time.localtime()
                timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
                myFile.write("\n{0} BLUE TEAM WON!!".format(timestamp))
        myFile.write("\nBlue Team Current Status\n")
        a1.txt_status_last(myFile)
        a2.txt_status_last(myFile)
        a3.txt_status_last(myFile)
        myFile.write("Red Team Current Status\n")
        b1.txt_status_last(myFile)
        b2.txt_status_last(myFile)
        b3.txt_status_last(myFile)
        myFile.close()
        print("Blue Team Current Status")
        a1.print_status_last()
        a2.print_status_last()
        a3.print_status_last()
        print("Red Team Current Status")
        b1.print_status_last()
        b2.print_status_last()
        b3.print_status_last()
        to_end = input("Press \'Enter\' to end...")
    else:
        pass

# Main Function
def main():
    myFile = open("GameLog.txt", "w")
    now = time.localtime()
    timestamp = "(%04d-%02d-%02d %02d:%02d:%02d)" % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)
    myFile.write("{0} Game Started\n\n".format(timestamp))
    myFile.close()
    game_mode = int(uvu_vs_uva_input())
    if game_mode == 1:
        print("\n===================================User vs User mode===================================")
        game_loop_uvu(game_mode)
    elif game_mode == 2:
        print("\n====================================User vs AI mode====================================")
        game_loop_uva(game_mode)
    else:
        pass

# Call Main Function
main()
