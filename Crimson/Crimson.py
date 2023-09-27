import pygame
import pygame_menu
import json
import random
import math
import sys

import Character
import UI

pygame.init()
pygame.font.SysFont(None, 30)
clock = pygame.time.Clock()
surface = pygame.display.set_mode((1000, 600))
moving_sprites = pygame.sprite.Group()
mount_olympus = pygame.image.load("./images/mount-olympus.png")
camelot = pygame.image.load("./images/camelot.png")
player_idle = [
                pygame.image.load("./sprites/player/idle/00.png"),
                pygame.image.load("./sprites/player/idle/01.png"),
                pygame.image.load("./sprites/player/idle/02.png"),
                pygame.image.load("./sprites/player/idle/03.png")
              ]

player_attack = [
                pygame.image.load("./sprites/player/attack/00.png"),
                pygame.image.load("./sprites/player/attack/01.png"),
                pygame.image.load("./sprites/player/attack/02.png"),
                pygame.image.load("./sprites/player/attack/03.png"),
                pygame.image.load("./sprites/player/attack/04.png")
              ]

player_heal = [
                pygame.image.load("./sprites/player/heal/00.png"),
                pygame.image.load("./sprites/player/heal/01.png"),
                pygame.image.load("./sprites/player/heal/02.png")
              ]

archer_idle = [
                pygame.image.load("./sprites/archer/idle/00.png"),
                pygame.image.load("./sprites/archer/idle/01.png"),
                pygame.image.load("./sprites/archer/idle/02.png"),
                pygame.image.load("./sprites/archer/idle/03.png")
              ]

archer_attack = [
                pygame.image.load("./sprites/archer/attack/00.png"),
                pygame.image.load("./sprites/archer/attack/01.png"),
                pygame.image.load("./sprites/archer/attack/02.png"),
                pygame.image.load("./sprites/archer/attack/03.png"),
                pygame.image.load("./sprites/archer/attack/04.png")
              ]

mage_idle = [
                pygame.image.load("./sprites/mage/idle/00.png"),
                pygame.image.load("./sprites/mage/idle/01.png"),
                pygame.image.load("./sprites/mage/idle/02.png"),
                pygame.image.load("./sprites/mage/idle/03.png")
              ]

mage_attack = [
                pygame.image.load("./sprites/mage/attack/00.png"),
                pygame.image.load("./sprites/mage/attack/01.png"),
                pygame.image.load("./sprites/mage/attack/02.png"),
                pygame.image.load("./sprites/mage/attack/03.png"),
                pygame.image.load("./sprites/mage/attack/04.png")
              ]

snake_idle = [
                pygame.image.load("./sprites/snake/idle/00.png"),
                pygame.image.load("./sprites/snake/idle/01.png"),
                pygame.image.load("./sprites/snake/idle/02.png"),
                pygame.image.load("./sprites/snake/idle/03.png")
              ]

snake_attack = [
                pygame.image.load("./sprites/snake/attack/00.png"),
                pygame.image.load("./sprites/snake/attack/01.png"),
                pygame.image.load("./sprites/snake/attack/02.png"),
                pygame.image.load("./sprites/snake/attack/03.png"),
                pygame.image.load("./sprites/snake/attack/04.png")
              ]

crow_idle = [
                pygame.image.load("./sprites/crow/idle/00.png"),
                pygame.image.load("./sprites/crow/idle/01.png"),
                pygame.image.load("./sprites/crow/idle/02.png"),
                pygame.image.load("./sprites/crow/idle/03.png")
              ]

crow_attack = [
                pygame.image.load("./sprites/crow/attack/00.png"),
                pygame.image.load("./sprites/crow/attack/01.png"),
                pygame.image.load("./sprites/crow/attack/02.png"),
                pygame.image.load("./sprites/crow/attack/03.png"),
                pygame.image.load("./sprites/crow/attack/04.png")
              ]

death_king_idle = [
                pygame.image.load("./sprites/death-king/idle/00.png"),
                pygame.image.load("./sprites/death-king/idle/01.png"),
                pygame.image.load("./sprites/death-king/idle/02.png"),
                pygame.image.load("./sprites/death-king/idle/03.png")
              ]

death_king_attack = [
                pygame.image.load("./sprites/death-king/attack/00.png"),
                pygame.image.load("./sprites/death-king/attack/01.png"),
                pygame.image.load("./sprites/death-king/attack/02.png"),
                pygame.image.load("./sprites/death-king/attack/03.png"),
                pygame.image.load("./sprites/death-king/attack/04.png")
              ]

evil_wizard_idle = [
                pygame.image.load("./sprites/evil-wizard/idle/00.png"),
                pygame.image.load("./sprites/evil-wizard/idle/01.png"),
                pygame.image.load("./sprites/evil-wizard/idle/02.png"),
                pygame.image.load("./sprites/evil-wizard/idle/03.png")
              ]

evil_wizard_attack = [
                pygame.image.load("./sprites/evil-wizard/attack/00.png"),
                pygame.image.load("./sprites/evil-wizard/attack/01.png"),
                pygame.image.load("./sprites/evil-wizard/attack/02.png"),
                pygame.image.load("./sprites/evil-wizard/attack/03.png"),
                pygame.image.load("./sprites/evil-wizard/attack/04.png")
              ]

def startGame():
    userData = open("UserData.json", "r")
    dataObj = json.load(userData)
    userData.close()

    if dataObj["newgame"] == "True":
        registerUser()
    else:
        loadGame()

def registerUser():
    global name
    name = ""

    def start_the_game():
        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        UserData.close()
        dataObj["name"] = name
        dataObj["newgame"] = "False"
        dataObj["characters"].append([name, 500, 500, "Protagonist"])
        dataObj["currentCharacter"] = [name, 500, 500, "Protagonist"]
        UserData = open("UserData.json", "w")
        json.dump(dataObj, UserData)
        UserData.close()
        loadGame()

    def setName(value):
        global name
        name = value;

    menu = pygame_menu.Menu('Welcome', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
    menu.add.text_input('Name: ', default='', onchange=setName)
    menu.add.vertical_margin(10)
    menu.add.button('Play', start_the_game).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('Quit', pygame_menu.events.EXIT).set_border(1, (255, 255, 255))
    menu.mainloop(surface)

def loadGame():

    #Battle Option
    def battle():

        def fight(title):
            UserData = open("UserData.json", "r")
            lootValue = random.randint(1,10)
            global shards
            shards = 0
            if 1 <= lootValue <= 5:
                shards = 1
            elif 6 <= lootValue <= 10:
                shards = 2
            dataObj = json.load(UserData)
            UserData.close()
            global enemyHealth
            global playerName
            global playerHealth
            global playerAttack
            global enemyAttack
            global enemy
            global enemyTitle
            global cont
            global player
            global background
            global powerUps
            global healingPotions
            playerName = str(dataObj["currentCharacter"][0])
            playerHealth = int(dataObj["currentCharacter"][1])
            playerAttack= int(dataObj["currentCharacter"][2])

            if dataObj["banner"] == "Mount Olympus":
                playerHealth += 50
            if dataObj["banner"] == "Camelot":
                playerAttack += 25

            powerUps = int(dataObj["inventory"]["Power Ups"])
            healingPotions = int(dataObj["inventory"]["Healing Potions"])
            if title == 'Mount Olympus':
                enemyList = [["crow", 1000, 100], ["death king", 4000, 400]]
                background = mount_olympus
            elif title == 'Camelot':
                enemyList = [["snake", 3000, 300], ["evil wizard", 9000, 1200]]
                background = camelot
            background = pygame.transform.scale(background, (1000, 600))
            randomNum = random.randint(0,3)
            enemyIndex = 0
            if randomNum == 0:
                enemyIndex = 1
            cont = False
            enemyTitle = enemyList[enemyIndex][0]
            enemyHealth = enemyList[enemyIndex][1]
            enemyAttack = enemyList[enemyIndex][2]
            width, height = pygame.display.get_surface().get_size()
            first = width / 4 / 2
            second = width / 4 + width / 4 / 2
            third = width * 2 / 4 + width / 4 / 2
            fourth = width * 3 / 4 + width / 4 / 2
            center = width / 2
            first_center = width / 4
            second_center = width / 2 + width / 4
            if enemyTitle == "snake":
                enemy = Character.Character(256, width * 2 / 4 + width / 8, 150, snake_idle, snake_attack)
            elif enemyTitle == "crow":
                enemy = Character.Character(256, width * 2 / 4 + width / 8, 150, crow_idle, crow_attack)
            elif enemyTitle == "death king":
                enemy = Character.Character(512, width * 2 / 4, -75, death_king_idle, death_king_attack)
            elif enemyTitle == "evil wizard":
                enemy = Character.Character(1048, width * 2 / 4 - width / 8, -200, evil_wizard_idle, evil_wizard_attack)
            if playerName == "Arthur":
                player = Character.Character(320, width / 8, 150, archer_idle, archer_attack)
            elif playerName == "Merlin":
                player = Character.Character(448, width / 8, 150, mage_idle, mage_attack)
            else:
                player = Character.Character(256, width / 8, 150, player_idle, player_attack, player_heal)
            moving_sprites.add(player)
            moving_sprites.add(enemy)
            attack_button = UI.Button(first - 50, 500, 150, 50, "Attack", (255, 0, 0))
            power_button = UI.Button(second - 50, 500, 150, 50, "Power", (0, 0, 255))
            heal_button = UI.Button(third - 50, 500, 150, 50, "Heal", (0, 255, 0))
            run_button = UI.Button(fourth - 50, 500, 150, 50, "Run", (0, 255, 255))
            enemy_label = UI.Label(center, 350, "Enemy: " + str(enemyTitle.title()))
            player_health = UI.Label(first_center, 400, "Player Health: " + str(playerHealth))
            enemy_health = UI.Label(second_center, 400, "Enemy Health: " + str(enemyHealth))

            powers_label = UI.Label(second, 450, "Power Ups: " + str(powerUps))
            potions_label = UI.Label(third, 450, "Healing Potions: " + str(healingPotions))

            def attackEnemy():
                global enemyHealth
                global playerHealth
                global playerAttack
                global enemyAttack
                global player
                global powerUps
                player.attack()
                enemy.attack()
                enemyHealth = enemyHealth - random.randint(playerAttack-50, playerAttack+50)
                playerHealth = playerHealth - random.randint(enemyAttack-20, enemyAttack+20)
                enemy_health.change_text("Enemy Health: " + str(enemyHealth))
                player_health.change_text("Player Health: " + str(playerHealth))

            def powerAttack():
                global enemyHealth
                global playerHealth
                global playerAttack
                global enemyAttack
                global player
                global powerUps
                if powerUps == 0:
                    return
                player.attack()
                enemy.attack()
                enemyHealth = enemyHealth - random.randint(int(playerAttack*1.5-50), int(playerAttack*1.5+50))
                playerHealth = playerHealth - random.randint(enemyAttack-20, enemyAttack+20)
                enemy_health.change_text("Enemy Health: " + str(enemyHealth))
                player_health.change_text("Player Health: " + str(playerHealth))
                powerUps -= 1
                powers_label.change_text("Power Ups: " + str(powerUps))

            def healPlayer():
                global enemyHealth
                global playerHealth
                global playerAttack
                global enemyAttack
                global healingPotions
                if healingPotions == 0 or playerHealth >= dataObj["currentCharacter"][1]:
                    return
                player.heal()
                enemy.attack()
                playerHealth = dataObj["currentCharacter"][1]
                enemy_health.change_text("Enemy Health: " + str(enemyHealth))
                player_health.change_text("Player Health: " + str(playerHealth))
                playerHealth = playerHealth - random.randint(enemyAttack-20, enemyAttack+20);
                enemy_health.change_text("Enemy Health: " + str(enemyHealth))
                player_health.change_text("Player Health: " + str(playerHealth))
                healingPotions -= 1
                potions_label.change_text("Healing Potions: " + str(healingPotions))

            def drawGame():
                attack_button.draw(surface)
                power_button.draw(surface)
                heal_button.draw(surface)
                run_button.draw(surface)
                enemy_label.draw(surface)
                enemy_health.draw(surface)
                player_health.draw(surface)
                powers_label.draw(surface)
                potions_label.draw(surface)

            def win(title):
                global menu
                global enemyTitle
                UserData = open("UserData.json", "r")
                dataObj = json.load(UserData)
                UserData.close()

                menu = pygame_menu.Menu(title, 1000, 600, theme=pygame_menu.themes.THEME_DARK)
                def continueGame():
                    global cont
                    cont = True
                menu.add.label("Victory").update_font({'size': 80})
                menu.add.vertical_margin(30)
                if title == "Mount Olympus":
                    menu.add.label("Gold +2,500")
                    if enemyTitle == "death king":
                        menu.add.label("Gold +10,000")
                        menu.add.label("%s Fragments +5" % (title))
                if title == "Camelot":
                    menu.add.label("Gold +5,000")
                    if enemyTitle == "evil wizard":
                        menu.add.label("Gold +20,000")
                        menu.add.label("%s Fragments +5" % (title))
                if shards == 1:
                    menu.add.label("%s Fragments +1" % (title))
                elif shards == 2:
                    menu.add.label("%s Fragments +2" % (title))
                menu.add.vertical_margin(50)
                menu.add.button('Continue', continueGame).set_border(1, (255, 255, 255))
                menu.mainloop(surface, disable_loop=True)
            def lose(title):
                global menu
                menu = pygame_menu.Menu(title, 1000, 600,theme=pygame_menu.themes.THEME_DARK)
                def continueGame():
                    global cont
                    cont = True
                menu.add.label("Defeat").update_font({'size': 80})
                menu.add.vertical_margin(10)
                menu.add.button('Continue', continueGame).set_border(1, (255, 255, 255))
                menu.mainloop(surface, disable_loop=True)
            def runAway():
                global enemyHealth
                global playerHealth
                global cont
                enemyHealth = 0
                playerHealth = 0
                cont = True
            menu.disable()
            while enemyHealth > 0 and playerHealth > 0:
                surface.blit(background, (0, 0))
                drawGame()
                for event in pygame.event.get():
                    mouse_position = pygame.mouse.get_pos()
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if attack_button.on_button(mouse_position):
                            attackEnemy()
                        elif power_button.on_button(mouse_position):
                            powerAttack()
                        elif heal_button.on_button(mouse_position):
                            healPlayer()
                        elif run_button.on_button(mouse_position):
                            runAway()
                moving_sprites.draw(surface)
                moving_sprites.update()
                pygame.display.update()
                clock.tick(10)
            moving_sprites.remove(player)
            moving_sprites.remove(enemy)
            menu.enable()
            dataObj["inventory"]["Healing Potions"] = healingPotions
            dataObj["inventory"]["Power Ups"] = powerUps
            UserData = open("UserData.json", "w")
            json.dump(dataObj, UserData)
            UserData.close()
            if playerHealth == 0 and enemyHealth == 0:
                pass
            elif enemyHealth <= 0:
                while cont == False:
                    win(title)
                menu.mainloop(surface, disable_loop=True)
                if title == "Mount Olympus":
                    dataObj["inventory"]["Gold"] += 2500
                    if enemyTitle == "death king":
                        dataObj["inventory"]["Gold"] += 10000
                        dataObj["inventory"]["%s Fragments" % (title)] += 5
                if title == "Camelot":
                    dataObj["inventory"]["Gold"] += 5000
                    if enemyTitle == "evil wizard":
                        dataObj["inventory"]["Gold"] += 20000
                        dataObj["inventory"]["%s Fragments" % (title)] += 5
                if shards == 1:
                    dataObj["inventory"]["%s Fragments" % (title)] += 1
                elif shards == 2:
                    dataObj["inventory"]["%s Fragments" % (title)] += 2
                UserData = open("UserData.json", "w")
                json.dump(dataObj, UserData)
                UserData.close()
            elif playerHealth <= 0:
                while cont == False:
                    lose(title)


        menu = pygame_menu.Menu('Select your destination', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
        menu.add.button('Mount Olympus', fight, 'Mount Olympus').set_border(1, (255, 255, 255))
        menu.add.vertical_margin(20)
        menu.add.button('Camelot', fight, 'Camelot').set_border(1, (255, 255, 255))
        menu.add.vertical_margin(20)
        menu.add.button('Back', loadGame).set_border(1, (255, 255, 255))
        menu.mainloop(surface)

    #Characters Option
    def viewCharacters():
        global hero_label
        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        UserData.close()
        charList = dataObj["characters"]
        def characterInfo(n):
            global hero_label
            dataObj["currentCharacter"] = charList[n]
            UserData = open("UserData.json", "w")
            json.dump(dataObj, UserData)
            UserData.close()
            hero_label.set_title("Current Hero: " + dataObj["currentCharacter"][0])
        menu = pygame_menu.Menu('Characters', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
        hero_label = menu.add.label("Current Hero: " + dataObj["currentCharacter"][0]).update_font({"size": 40})
        for i in range(len(charList)):
            menu.add.label("Name: " + charList[i][0] + ", Title: "+ charList[i][3])
            menu.add.label("Damage: " + str(charList[i][2]) + ", Health: " + str(charList[i][1]))
            menu.add.button('Choose', characterInfo, i).set_border(1, (255, 255, 255))
            menu.add.vertical_margin(20)
        menu.add.vertical_margin(30)
        menu.add.button("Back", loadGame).set_border(1, (255, 255, 255))
        menu.add.vertical_margin(50)
        menu.mainloop(surface)

    #Inventory Option
    def openInventory():
        menu = pygame_menu.Menu('Inventory', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        inventory = dataObj["inventory"]
        for item in inventory:
            menu.add.label(item + " x"+str(inventory[item]))
            menu.add.vertical_margin(5)
        menu.add.vertical_margin(50)
        menu.add.button("Back", loadGame).set_border(1, (255, 255, 255))
        menu.mainloop(surface)

    def goToShop():
        global shop_gold_label
        global shop_potions_label
        global shop_powers_label
        global shop_error
        def buyItem(item):
            global gold_label
            UserData = open("UserData.json", "r")
            dataObj = json.load(UserData)
            UserData.close()
            if item == "Healing Potions" and dataObj["inventory"]["Gold"] >= 1000:
                dataObj["inventory"]["Healing Potions"] += 1
                dataObj["inventory"]["Gold"] -= 1000
                shop_error.set_title("Bought 1 Healing Potions").update_font({"color": (0, 255, 0)})
            elif item == "Power Ups" and dataObj["inventory"]["Gold"] >= 2000:
                dataObj["inventory"]["Power Ups"] += 1
                dataObj["inventory"]["Gold"] -= 2000
                shop_error.set_title("Bought 1 Power Ups").update_font({"color": (0, 255, 0)})
            elif item == "Upgrade Health" and dataObj["inventory"]["Gold"] >= 5000:
                dataObj["currentCharacter"][1] += 100
                dataObj["inventory"]["Gold"] -= 5000
                shop_error.set_title("Your Hero's Health is Increased by 100").update_font({"color": (0, 255, 0)})
                for i in range(0, len(dataObj["characters"])):
                    if dataObj["characters"][i][0] == dataObj["currentCharacter"][0]:
                        dataObj["characters"][i][1] += 100
            elif item == "Upgrade Damage" and dataObj["inventory"]["Gold"] >= 5000:
                dataObj["currentCharacter"][2] += 50
                dataObj["inventory"]["Gold"] -= 5000
                shop_error.set_title("Your Hero's Damage is Increased by 50").update_font({"color": (0, 255, 0)})
                for i in range(0, len(dataObj["characters"])):
                    if dataObj["characters"][i][0] == dataObj["currentCharacter"][0]:
                        dataObj["characters"][i][2] += 50
            else:
                shop_error.set_title("Error: Not Enough Gold").update_font({"color": (255, 0, 0)})
            UserData = open("UserData.json", "w")
            json.dump(dataObj, UserData)
            UserData.close()
            shop_potions_label.set_title("Healing Potions: " + str(dataObj["inventory"]["Healing Potions"]))
            shop_powers_label.set_title("Power Ups: " + str(dataObj["inventory"]["Power Ups"]))
            shop_gold_label.set_title("Gold: " + str(dataObj["inventory"]["Gold"]))
        menu = pygame_menu.Menu('Shop', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        shop_gold_label = menu.add.label("Gold: " + str(dataObj["inventory"]["Gold"])).update_font({"size": 40})
        menu.add.vertical_margin(5)
        shop_potions_label = menu.add.label("Healing Potions: " + str(dataObj["inventory"]["Healing Potions"]))
        menu.add.vertical_margin(5)
        shop_powers_label = menu.add.label("Power Ups: " + str(dataObj["inventory"]["Power Ups"]))
        menu.add.vertical_margin(10)
        shop_error = menu.add.label("").update_font({"size": 24})
        menu.add.vertical_margin(40)
        menu.add.label("Healing Potion, Cost: 1000")
        menu.add.label("Description: Heal 100% of Health in Battle")
        menu.add.button('Buy', buyItem, "Healing Potions").set_border(1, (255, 255, 255))
        menu.add.vertical_margin(20)
        menu.add.label("Power Ups, Cost: 2000")
        menu.add.label("Description: Next Attack Deals 150% Damage")
        menu.add.button('Buy', buyItem, "Power Ups").set_border(1, (255, 255, 255))
        menu.add.vertical_margin(20)
        menu.add.label("Upgrade Health, Cost: 5000")
        menu.add.label("Description: Increase Health by 100 Permanently")
        menu.add.button('Buy', buyItem, "Upgrade Health").set_border(1, (255, 255, 255))
        menu.add.vertical_margin(20)
        menu.add.label("Upgrade Attack, Cost: 5000")
        menu.add.label("Description: Increase Attack Damage by 50 Permanently")
        menu.add.button('Buy', buyItem, "Upgrade Damage").set_border(1, (255, 255, 255))
        menu.add.vertical_margin(50)
        menu.add.button("Back", loadGame).set_border(1, (255, 255, 255))
        menu.add.vertical_margin(50)
        menu.mainloop(surface)

    #Select Banner and Summon Option
    def openBanner():
        global banner_label
        global banner_bonus_label
        def setBanner(value):
            UserData = open("UserData.json", "r")
            dataObj = json.load(UserData)
            UserData.close()
            dataObj["banner"] = value
            UserData = open("UserData.json", "w")
            json.dump(dataObj, UserData)
            UserData.close()
            bonus = ""
            if value == "Mount Olympus":
                bonus = "Gain 50 Health"
            elif value == "Camelot":
                bonus = "Gain 25 Damage"
            global banner_label
            global banner_bonus_label
            banner_label.set_title("Current Banner: " + value)
            banner_bonus_label.set_title("Current Bonus: " + bonus)
        menu = pygame_menu.Menu("Banner", 1000, 600, theme=pygame_menu.themes.THEME_DARK)
        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        UserData.close()
        banner = dataObj["banner"]
        bonus = ""
        if banner == "Mount Olympus":
            bonus = "Gain 50 Health"
        elif banner == "Camelot":
            bonus = "Gain 25 Damage"
        banner_label = menu.add.label("Current Banner: " + banner).update_font({"size": 40})
        banner_bonus_label = menu.add.label("Current Bonus: " + bonus)
        menu.add.vertical_margin(50)
        menu.add.label("Mount Olympus")
        menu.add.label("Description: Gain 50 Health")
        menu.add.button("Choose", setBanner, "Mount Olympus").set_border(1, (255, 255, 255))
        menu.add.vertical_margin(20)
        menu.add.label("Camelot")
        menu.add.label("Description: Gain 25 Damage")
        menu.add.button("Choose", setBanner, "Camelot").set_border(1, (255, 255, 255))
        menu.add.vertical_margin(50)
        menu.add.button("Back", loadGame).set_border(1, (255, 255, 255))
        menu.add.vertical_margin(50)
        menu.mainloop(surface)

    def summoningPortal():

        def summon():
            menu = pygame_menu.Menu("Summoning", 1000, 600, theme=pygame_menu.themes.THEME_DARK)
            UserData = open("UserData.json", "r")
            dataObj = json.load(UserData)
            UserData.close()
            mountOlympusFragments = dataObj["inventory"]["Mount Olympus Fragments"]
            camelotFragments = dataObj["inventory"]["Camelot Fragments"]
            if dataObj["banner"] == "Mount Olympus":
                if mountOlympusFragments >= 10:
                    dataObj["inventory"]["Mount Olympus Fragments"] = dataObj["inventory"]["Mount Olympus Fragments"]-10
                    summonList = [["Arthur", 1000, 1000, "Archer"]]
                    summonEntity = random.choice(summonList)
                    owned = []
                    for i in range(0, len(dataObj["characters"])):
                        owned.append(dataObj["characters"][i][0])
                    if (summonEntity[0] in owned) == False:
                        dataObj["characters"].append(summonEntity)
                        menu.add.label("Summoning Successful").update_font({"size": 40})
                        menu.add.vertical_margin(50)
                        menu.add.label("Name: " + summonEntity[0] + ", Title: " + summonEntity[3])
                        menu.add.label("Damage: " + str(summonEntity[1]) + ", Health: " + str(summonEntity[2]))
                    else:
                        menu.add.label("No Heroes Available to Summon").update_font({"size": 40})
                        menu.add.vertical_margin(10)
                        menu.add.label("Gold +25,000")
                        dataObj["inventory"]["Gold"] += 25000
                elif mountOlympusFragments < 10:
                    menu.add.label("Mount Olympus Fragments: " + str(dataObj["inventory"]["Mount Olympus Fragments"])).update_font({"size": 40})
                    menu.add.vertical_margin(50)
                    menu.add.label("Summoning requires 10 Mount Olympus Fragments")

            if dataObj["banner"] == "Camelot":
                if camelotFragments >= 10:
                    dataObj["inventory"]["Camelot Fragments"] = dataObj["inventory"]["Camelot Fragments"]-10
                    summonList = [["Merlin", 2000, 2000, "Mage"]]
                    summonEntity = random.choice(summonList)
                    owned = []
                    for i in range(0, len(dataObj["characters"])):
                        owned.append(dataObj["characters"][i][0])
                    if (summonEntity[0] in owned) == False:
                        dataObj["characters"].append(summonEntity)
                        menu.add.label("Summoning Successful").update_font({"size": 40})
                        menu.add.vertical_margin(50)
                        menu.add.label("Name: " + summonEntity[0] + ", Title: " + summonEntity[3])
                        menu.add.label("Damage: " + str(summonEntity[1]) + ", Health: " + str(summonEntity[2]))
                    else:
                        menu.add.label("No Heroes Available to Summon").update_font({"size": 40})
                        menu.add.vertical_margin(50)
                        menu.add.label("Gold +50,000")
                        dataObj["inventory"]["Gold"] += 50000
                elif camelotFragments < 10:
                    menu.add.label("Camelot Fragments: " + str(dataObj["inventory"]["Camelot Fragments"])).update_font({"size": 40})
                    menu.add.vertical_margin(10)
                    menu.add.label("Summoning requires 10 Camelot Fragments")

            UserData = open("UserData.json", "w")
            json.dump(dataObj, UserData)
            UserData.close()
            menu.add.vertical_margin(50)
            menu.add.button("Back", summoningPortal).set_border(1, (255, 255, 255))
            menu.mainloop(surface)

        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        UserData.close()
        menu = pygame_menu.Menu('Summoning Portal', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
        menu.add.label("Current Banner: " + dataObj["banner"]).update_font({"size": 40})
        menu.add.vertical_margin(50)
        menu.add.button('Summon', summon).set_border(1, (255, 255, 255))
        menu.add.vertical_margin(20)
        menu.add.button("Back", loadGame).set_border(1, (255, 255, 255))
        menu.mainloop(surface)

    def demoMode():
        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        UserData.close()
        dataObj["inventory"]["Gold"] += 1000000
        dataObj["inventory"]["Mount Olympus Fragments"] += 100
        dataObj["inventory"]["Camelot Fragments"] += 100
        UserData = open("UserData.json", "w")
        json.dump(dataObj, UserData)
        UserData.close()

    UserData = open("UserData.json", "r")
    dataObj = json.load(UserData)
    UserData.close()
    menu = pygame_menu.Menu('Crimson', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
    menu.add.label("Current Banner: " + dataObj["banner"])
    menu.add.button('Fight in Battle', battle).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('View Heroes', viewCharacters).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('Open Inventory', openInventory).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('Go to Shop', goToShop).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('Change Banner', openBanner).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('Summoning Portal', summoningPortal).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('Demo Mode', demoMode).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button('Exit', pygame_menu.events.EXIT).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.mainloop(surface)

def options():
    def resetGame(menu):
        UserData = open("UserData.json", "r")
        dataObj = json.load(UserData)
        dataObj["newgame"] = "True"
        dataObj["name"] = ""
        dataObj["banner"] = "Mount Olympus"
        dataObj["characters"] = []
        dataObj["currentCharacter"] = []
        dataObj["inventory"] = {'Gold': 0, 'Mount Olympus Fragments': 0, 'Camelot Fragments': 0, 'Healing Potions': 0, 'Power Ups': 0}
        UserData.close()
        UserData = open("UserData.json", "w")
        json.dump(dataObj, UserData)
        UserData.close()
        menu.disable()
    def backOption(menu):
        menu.disable()
    menu = pygame_menu.Menu('Options', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
    menu.add.button("Reset Game", resetGame, menu).set_border(1, (255, 255, 255))
    menu.add.vertical_margin(10)
    menu.add.button("Back", backOption, menu).set_border(1, (255, 255, 255))
    menu.mainloop(surface)

menu = pygame_menu.Menu('Crimson', 1000, 600, theme=pygame_menu.themes.THEME_DARK)
menu.add.button('Play', startGame).set_border(1, (255, 255, 255))
menu.add.vertical_margin(10)
menu.add.button('Options', options).set_border(1, (255, 255, 255))
menu.add.vertical_margin(10)
menu.add.button('Quit', pygame_menu.events.EXIT).set_border(1, (255, 255, 255))

menu.mainloop(surface)
