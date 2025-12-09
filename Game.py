#importing stuff
import random
import time
import json
import os
from nerdland import agni
import Enemy
import toolstats

#clear console function
def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

first = input("hello world")
clear()
#intro stuff
decideLoad = True
cheatCode = False
print(
    "By pressing the enter key, you agree to the following:\n\n1.We do not have the braincells to steal your information (nor do we have any braincells to begin with, much less to make a neural connection)\n\n2.Not to mess with any variables in the code(Garett the carrot who looks like a ferrett, I'm looking at you...)\n\n3.That this program is superior to all other programs made by the coding club\n\n4.That :\n\nHis Rubik’s cube spins, the colors a blur\nAll the tabs of GitHub make his computer start to stir\nHe merged his life with a Python file,\nSaid, “return True” — and grinned with a smile\nYet everything he does, won't make a conversation worthwhile\n\nAgni's addicted to his Rubik's cube\nAnd now he's yapping about computers too\nI show him python code\nAnd then his brain goes rogue\nTelling me everything I didn't really care about\n\nHe talks in syntax, sleeps in stacks\nHas a monitor glow that never slacks\nIf you ask him out, he’ll probably say\nHold on, I gotta debug some shaders today\n\nAgni's addicted to his Rubik's cube\nAnd now he's yapping about computers too\nI show him python code\nAnd then his brain goes rogue\nTelling me everything I didn't really care about\n\nOh, Agni's been nerding\nBut his mind is blurring\nHe doesn't know what he's saying\nBut I'm praying\nThat Jonah will come and shut him up\n\nAgni's been on a roll\nHe's still tryna reach his goal\nHis skull's an empty hole\nNothing but code left in his soul\n\nAgni's addicted to his Rubik's cube\nAnd now he's yapping about computers too\nI show him python code\nAnd then his brain goes rogue\nTelling me everything I didn't really care about-Xavier Ko\n\n5.To ignore the grammar mistakes created by the code\n\n6.Not to annoy the developer with any of its 1000+ bugs\n\n7.That the developer is superior to you in coding in all aspects of coding (exceptions include every single coding language)\n\n\nIf you do not agree with any of the above, then plz... uh... press enter? \n"
)
intro = input("\nI agree, press (space) if you don't want to load a save file")
print("Loading the actual program...")

#wipe progress and cheat code
if (intro == " "):
    decideLoad = False
elif(intro=="pres"):
    decideLoad = False
    cheatCode = True
clear()


#saving your progress
def save_game(depth, playerHealth, damageBoost, armorBoost, luckBoost,
              foodInInven, sword, armor, pArmorBoost, pAttackBoost, pLuckBoost,
              enemies, allEnemies, coins, swordId, armorId, artifacts):
    game_state = {
        "depth": depth,
        "playerHealth": playerHealth,
        "damageBoost": damageBoost,
        "armorBoost": armorBoost,
        "luckBoost": luckBoost,
        "food": foodInInven,
        "sword": sword,
        "armor": armor,
        "pAttackBoost": pAttackBoost,
        "pArmorBoost": pArmorBoost,
        "pLuckBoost": pLuckBoost,
        "enemies": enemies,
        "allEnemies": allEnemies,
        "coins": coins,
        "swordId": swordId,
        "armorId": armorId,
        "artifacts": artifacts,
    }

    try:
        with open("save.json", "w") as f:
            json.dump(game_state, f)
    except e:
        print("Error saving game:", e)


def load_game():
    if not os.path.exists("save.json"):
        return None  # nothing to load

    try:
        with open("save.json", "r") as f:
            return json.load(f)
    except e:
        print("Error loading game:", e)

    return None


#player stats and stat boosts
playerHealth = 100
playerArmor = 0
playerDamage = 0
damageBoost = 0
armorBoost = 0
pArmorBoost = 0
pAttackBoost = 0
pLuckBoost = 0
sword = "wood"
armor = "none"

swordId = 0
armorId = -1

#enemy stuff
enemies = []
displayEnemies = []
allEnemies = [["zombie", 50], ["skeleton", 75]]
lowestPossibleCost = 50

#food
foodInInven = []
displayFood = foodInInven
allFood = [
    "pomegranate", "pancakes", "apple sauce", "pizza", "rice",
    "chicken tikka masala", "heal pot"
]

#dungeon features
depth = 0
totalEnemyWeight = 100

#for the funnies
happenings = [
    " Your soul is falling apart, one piece at a time ",
    " Your blade sings through the air... ",
    " In the distance, you hear someone shout: FIREBOLT!!!!!!! ... ",
    " Sweat begins to form on you forehead... ", " The air grows tense... ",
    " You feel like eating something... ",
    " You think, (How do zombies drop chicken???)...", " Your arm sores... ",
    " Your life flashes in front of your eyes... ",
    " all you days in the academy come back to you... ",
    " Your mind spins... ",
    " You hear battle music playing in the background... by a lute?!?!?!?",
    " It appears as if there was someone who just swam past you... ",
    " The earth shakes... ", " You hear a faint whisper... ",
    " In a rigged game, your mind is the only fair advantage... ",
    " In retrospect, the ground you stood on never existed in the first place... ",
    " Strength isn't necessary for those whith nothing to lose... ", 
    " You remember the unfullfilled promises you made",
    " It all came down to that moment"
]

#dungeon room types
curDungeonType = "normal"
allDungeonType = [
    "normal", "cold", "hot", "poison", "trapped", "dark", "spawner"
]

#loot stuff
luck = 0
luckBoost = 0
allLoot = ["sword", "armor", "boost"]
swordTypes = [
    "wood", "hardwood", "stone", "iron", "steel", "tungsten", "obsidian",
    "diamond"
]
armorTypes = [
    "paper", "leather", "chainmail", "iron", "steel", "tungsten", "diamond"
]

#artifacts
artifactsOnDisplay = []
artifacts = []
allArtifacts = [
    ["Poisoned dagger", 500, "Deal 3 extra damage","uncommon"],
    ["Iron totem", 200,"Revive self from death once to 100 hp, gives you 100 armor for 1 turn","uncommon"], 
    ["Totem of undying", 150, "revive self from death once to 100 hp","common"],
    ["Serrrated edge", 200, "Injures enemies, making them deal 1 less damage","common"],
    ["Shield of the gods", 300,"has a 10% chance to make your armor 100 for 1 turn","rare"], 
    ["Final hit", 150, "deals 1 damage to an enemy if it is at 1 hp","common"],
    ["Last stand", 550,"Increases your armor by 10 for 1 turn, has a 60% chance to activate, increases damage by 5","epic"],
    ["Free fall", 400,"When you enter the dungeon, you will start with a random amount of depth between 1 and 10","rare"],
    ["Wheel of fortune", 350,"Your armor becomes a random number between 0 and 110 for 1 turn when you are attacked","uncommon"], 
    ["Greed", 300, "Gives you money when you move down in depth","common"],
    ["Aged wine", 200, "passively gives you 10 hp every depth","common"],
    ["Payback", 400,"Deals damage to the enemy that attacked you","rare"],
    ["Bomb", 300, "Has a 10% chance to deal 5 damage to all enemies when you attack","rare"],
    ["Drill",1000, "Drills you down 1-10 levels everytime you go down a level",'legendary'],
    ["Four - leaf clover", 600, "Boosts luck by 1 when you progress down a floor","epic"],
    ["Aceticm",500,"On death, you will recieve 10 times the amount of depth you traveled in coins","epic"],
    ["Cunfuzianism",1500,"May the roll of the dice play in your favor....","legendary"],
]
commonArtifacts = []
uncommonArtifacts = []
rareArtifacts = []
epicArtifacts = []
legendaryArtifacts = []
rarities = []
#space filler when you already bought that artifact
trash = ["Trash",1000,"One man's trash is also usually another man's trash"]
artifactSlots = 4

#stuff for the scenes and hub
scene = 0
coins = 0
if(cheatCode):
    coins = 1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
chosenFood = "nothing"
foodCost = 0

#load save file?
if (decideLoad):
    loaded = load_game()
    if loaded:
        if loaded["playerHealth"] > 0:
            depth = loaded["depth"]
            playerHealth = loaded["playerHealth"]
            armorBoost = loaded["armorBoost"]
            damageBoost = loaded["damageBoost"]
            foodInInven = loaded["food"]
            sword = loaded["sword"]
            armor = loaded["armor"]
            pAttackBoost = loaded["pAttackBoost"]
            pArmorBoost = loaded["pArmorBoost"]
            pLuckBoost = loaded["pLuckBoost"]
            enemies = loaded["enemies"]
            allEnemies = loaded["allEnemies"]
            coins = loaded["coins"]
            swordId = loaded["swordId"]
            armorId = loaded["armorId"]
            artifacts = loaded["artifacts"]
            print("Save file loaded! Returning to depth", str(depth - 1))
        else:
            print("Save file found, but you died. Starting a new game.")
    else:
        print(
            "No save file found. Starting a new game. (If you're on KA the save doesn't work, please make a replit account)"
        )

#getting the base stats of the player and boosting them
def getPlayerDamage():
    global sword
    return random.randint(toolstats.swordStats[sword]["min"], toolstats.swordStats[sword]["max"])
def getPlayerArmor():
    global armor
    return toolstats.armorStats[armor]
def boostStats():
    global playerDamage, playerArmor, luck
    global damageBoost, armorBoost, luckBoost
    global pAttackBoost, pArmorBoost, pLuckBoost

    baseDamage = getPlayerDamage()
    baseArmor = getPlayerArmor()

    playerDamage = baseDamage + damageBoost + pAttackBoost
    playerArmor = baseArmor + armorBoost + pArmorBoost
    luck = luckBoost + pLuckBoost

#appending all artifacts to their respective rarity lists
def classifyArtifacts():
    commonArtifacts.clear()
    uncommonArtifacts.clear()
    rareArtifacts.clear()
    epicArtifacts.clear()
    legendaryArtifacts.clear()
    for artifact in allArtifacts:
        if(artifact[3] == "common"):
            commonArtifacts.append(artifact)
        elif(artifact[3] == "uncommon"):
            uncommonArtifacts.append(artifact)
        elif(artifact[3] == "rare"):
            rareArtifacts.append(artifact)
        elif(artifact[3] == "epic"):
            epicArtifacts.append(artifact)
        elif(artifact[3] == "legendary"):
            legendaryArtifacts.append(artifact)
        else:
            print("Error: artifact "+artifact[0]+" has no rarity")
classifyArtifacts()

#rolling for new arifacts in shop
def rollForArtifacts():
    global allArtifacts
    global rarities
    global artifacts
    global commonArtifacts
    global uncommonArtifacts
    global rareArtifacts
    global epicArtifacts
    global legendaryArtifacts
    global artifactsOnDisplay
    global artifactSlots
    artifactsOnDisplay.clear()
    rarities.clear()
    for i in range(artifactSlots-1):
        rarities.append(random.randint(0, 100))
    for rarity in rarities:
        if (rarity < 50):
            if(len(commonArtifacts)>0):
                artifactsOnDisplay.append(commonArtifacts[random.randint(0, len(commonArtifacts) - 1)])
            else:   
                artifactsOnDisplay.append(trash)
        elif (rarity < 80):
            if(len(uncommonArtifacts)>0):
                artifactsOnDisplay.append(uncommonArtifacts[random.randint(0, len(uncommonArtifacts) - 1)])
            else:   
                artifactsOnDisplay.append(trash)
        elif (rarity < 95):
            if(len(rareArtifacts)>0):
                artifactsOnDisplay.append(rareArtifacts[random.randint(0, len(rareArtifacts) - 1)])
            else:   
                artifactsOnDisplay.append(trash)
        elif (rarity < 99):
            if(len(epicArtifacts)>0):
                artifactsOnDisplay.append(epicArtifacts[random.randint(0, len(epicArtifacts) - 1)])
            else:   
                artifactsOnDisplay.append(trash)
        else:
            if(len(legendaryArtifacts)>0):
                artifactsOnDisplay.append(legendaryArtifacts[random.randint(0, len(legendaryArtifacts) - 1)])
            else:
                artifactsOnDisplay.append(trash)

#will check iin certain instances if the player has certain artifacts and will do certain things
def onPlayerAttack(choice):
    global playerDamage
    global enemies
    global allArtifacts
    global artifacts
    for artifact in artifacts:
        if (artifact[0] == "Poisoned dagger"):
            playerDamage += 3
            print("Your dagger poisened the enemy")
        if (artifact[0] == "Serrtated edge"):
            enemies[choice].damage -= 1
            print("Your edge injured the enemy")
        if (artifact[0] == "Last stand"):
            playerDamage += 5
            print("Your last stand boosted your damage")
        if (artifact[0] == "Final hit"):
            if (enemies[choice].health - playerDamage == 1):
                playerDamage += 1
                print("Your final hit dealt 1 extra damage")
        if(artifact[0] == "Bomb"):
            if (random.randint(0, 10) <= 1):
                for enemy in enemies:
                    enemy.health -= 5
                    print("Your bomb blew up")
def onEnemyAttack(damage, enemy):
    global playerHealth
    global enemies
    global playerArmor
    global allArtifacts
    global artifacts
    givenArmor = 0
    for artifact in artifacts:
        if (artifact[0] == "Shield of the gods"):
            if (random.randint(0, 10) <= 1):
                playerArmor = 100
                print("Your shield of the gods activated")
        if (artifact[0] == "Last stand"):
            if (random.randint(0, 10) < 6):
                playerArmor += 10
                print("Your last stand boosted your armor")
        if (artifact[0] == "Wheel of fortune"):
            givenArmor = random.randint(0, 110)
            playerArmor = givenArmor
            print("Your wheel of fortune gave "+str(givenArmor)+"armor boost")
        if (artifact[0] == "Payback"):
            print("Payback dealt 2 damage to the enemies")
            enemy.health -= 2
def onPlayerDeath():
    global playerHealth
    global playerArmor
    global artifacts
    global allArtifacts
    global depth
    global coins
    for artifact in artifacts:
        if (artifact[0] == "Totem of undying"):
            playerHealth = 100
            print("Your totem popped")
            artifacts.remove(artifact)
        if (artifact[0] == "Iron totem"):
            playerHealth = 100
            playerArmor = 100
            print("Your iron totem popped")
            artifacts.remove(artifact)
        if(artifact[0] == "Aceticm"):
            coins+=10*depth
            print("You recieve what you deserved...")
def onPlayerMoveDownDepth():
    global playerHealth
    global coins
    global allArtifacts
    global artifacts
    global depth
    global luckBoost
    extraCoins = 0
    for artifact in artifacts:
        if (artifact[0] == "greed"):
            extraCoins = random.randint(1, 10)
            coins += extraCoins
            print("Your greed gave you "+str(extraCoins)+" extra coins")
        if (artifact[0] == "Aged wine"):
            print("Your aged wine healed you 10 hp")
            playerHealth += 10
        if(artifact[0] == "Drill"):
            amountDrilled = random.randint(0,10)
            depth-=amountDrilled
            print("Your drill drilled you down "+amountDrilled+" depth!")
        if(artifact[0] == "Four - leaf clover"):
            luckBoost += 1
            print("You feel a little luckier...")
def onPlayerEnterDungeon():
    global depth
    global allArtifacts
    global artifacts
    fallAmt = 0
    for artifact in artifacts:
        if (artifact[0] == "Free fall"):
            if(depth<1):
                fallAmt = random.randint(1, 10)
                depth = fallAmt
                print("Your free fall dropped you "+str(fallAmt)+" extra depth")
        if(artifact[0] == "Cunfuzianism"):
            enemies.append(Enemy("sushi,steve,baoism"))
            artifacts.remove(artifact)

#calculating damage of player with armor
def damagePlayer(damage):
    global playerHealth
    global playerArmor
    reductionAmount = playerArmor / 100
    subtractAmount = round(reductionAmount * damage)
    playerHealth -= damage - subtractAmount
    return damage - subtractAmount

#spawning enemies from the given list
def spawnEnemies():
    global totalEnemyWeight
    global depth
    global enemies
    global allEnemies
    global lowestPossibleCost
    depth += 1
    for i in range(len(allEnemies)):
        if (allEnemies[i][1] < lowestPossibleCost):
            lowestPossibleCost = allEnemies[i][1]

    while (totalEnemyWeight >= lowestPossibleCost):
        spawnEnemy = random.randint(0, len(allEnemies) - 1)
        enemies.append(Enemy.Enemy(allEnemies[spawnEnemy][0]))
        totalEnemyWeight -= allEnemies[spawnEnemy][1]

#getting enemies from the enemies list to print them
def getEnemies():
    displayEnemies.clear()
    for i in range(len(enemies)):
        displayEnemies.append(enemies[i].type)

#randomize the dungeon room type 10% of the time
def randomDungeonType():
    global curDungeonType
    if (random.randint(0, 10) <= 1):
        curDungeonType = allDungeonType[random.randint(0, len(allDungeonType))]
    else:
        curDungeonType = "normal"

#for the lore of the game
def getHappening():
    global happenings
    return happenings[random.randint(0, len(happenings) - 1)]

#deciding if the enemy will drop food
def decideGiveFood(value):
    global allFood
    global foodInInven
    if (random.randint(0, 10) < value):
        givenFood = allFood[random.randint(0, len(allFood) - 1)]
        foodInInven.append(givenFood)
        return givenFood
    return "nothing"

#deciding what loot the player will get when the progres down a depth
def giveLoot():
    global luck
    global allLoot
    global swordTypes
    global armorTypes
    global depth
    global damageBoost
    global armorBoost
    global luckBoost
    global pArmorBoost
    global pAttackBoost
    global pLuckBoost

    lootRand = random.randint(0, 100)
    if (lootRand < 70):
        lootRand = random.randint(0, 100)
        if (lootRand < 33):
            lootRand = random.randint(1, 5 + round(luck/2))
            if (random.randint(0, 10) < 7):
                luckBoost = 0
            damageBoost += lootRand
            if (random.randint(0, 10) < 7):
                luckBoost = 0
            return "attack boost"
        elif (lootRand < 66):
            lootRand = random.randint(1, 5 + round(luck/2))
            armorBoost += lootRand
            if (random.randint(0, 10) < 7):
                luckBoost = 0
            return "defense boost"
        elif (lootRand < 99):
            lootRand = random.randint(1, 5 + round(luck/2))
            luckBoost += lootRand
            if (random.randint(0, 10) < 7):
                luckBoost = 0
            return "luck boost"
        else:
            lootRand = random.randint(1, 5 + round(luck/2))
            luckBoost += lootRand
            armorBoost += lootRand
            damageBoost += lootRand
            if (random.randint(0, 10) < 7):
                luckBoost = 0
            return "Every boost"
    elif (lootRand < 80):
        lootRand = random.randint(1, 2 + round(luck/2))
        pAttackBoost += lootRand
        if (random.randint(0, 10) < 7):
            luckBoost = 0
        return "permenant attack boost"
    elif (lootRand < 90):
        lootRand = random.randint(1, 2 + round(luck/2))
        pArmorBoost += lootRand
        if (random.randint(0, 10) < 7):
            luckBoost = 0
        return "permenant defense boost"
    elif (lootRand < 100):
        lootRand = random.randint(1, 3 + round(luck/2))
        pLuckBoost += lootRand
        if (random.randint(0, 10) < 7):
            luckBoost = 0
        return "permenant luck boost"
    else:
        lootRand = random.randint(0, max(100 * depth + luck, 100))
        damageBoost += lootRand
        if (random.randint(0, 10) < 7):
            luckBoost = 0
        return (" ...something")

#spawning new enemies when the player progresses down a depth
def newChallengerApproaches():
    global depth
    global allEnemies
    match (depth):
        case 5:
            allEnemies.append(["black_furry_ball", 20])
        case 10:
            enemies.append(Enemy.Enemy("BOSS:_gaurd_of_the_abandoned_mines"))
        case 11:
            allEnemies.append(["wood_golem", 75])
        case 15:
            allEnemies.append(["black_spikey_ball", 30])
        case 20:
            enemies.append(Enemy.Enemy("BOSS:_gaurd_of_the_deep_mines"))
        case 21:
            allEnemies.append(["ghost", 100])
        case 25:
            allEnemies.append(["goblin", 100])
        case 30:
            enemies.append(Enemy.Enemy("BOSS:_gaurd_of_the_black_markets"))
        case 31:
            allEnemies.append(["shape_shifter", 150])
        case 35:
            allEnemies.append(["slime", 50])
        case 40:
            enemies.append(Enemy.Enemy("BOSS:_champion_of_the_arena"))
        case 41:
            allEnemies.append(["stone_golem", 100])
        case 45:
            allEnemies.append(["obsidian_golem", 150])
        
        case 51:
            allEnemies.append(["powerful_spikey_ball", 50])
            
        case 100:
            print(
                "\n\nThe air, now heavy, feels familiar and terrifying. It's as if the world was telling you that it is over...\n\n"
            )
            allEnemies = []
            allEnemies.append(["SELF", 6000])


#the main game loop
while True:
    # a switch case for the scenes
    match (scene):
        # the starting scene for the game, introduces the game and the controls
        case 0:
            print(
                "Hello, welcome to my semester 1 CC project!\n\nThis game is based on a dungeon crawler, where you attempt to get as deep as possible into the depths of the dungeon.\n\nWhen playing, you will be able to choose multiple actions, such as attacking, eating food obtained from enemies, and a variety of actions that will boost your stats.\n\nOnce you die, you will be transported to the hub, where you can buy better equipment with coins obtained from the enemies, and then return to the dungeon.\n\nDon't worry about losing your progress, there is a save feature that works on replit!(or do worry if you're on KA)\nThere will be a guide in the next scene, to acess it press 6 after you press enter\n\n "
            )
            next = input("Press enter to continue")
            #rolls for artifacts here to prevent errors
            rollForArtifacts()
            scene = 2
        #the dungeon scene, where the player fights enemies and progresses down a depth
        case 1:
            # rolls for artifacts when you enter the dungeon
            artifactsOnDisplay = []
            rollForArtifacts()
            # another loop if the player is alive
            while (playerHealth > 0):
                # checks if the player has defeated all the enemies on the current depth
                if (len(enemies) < 1):
                    # tries to trigger artifacts that the player has
                    onPlayerMoveDownDepth()
                    # saving the game
                    print("Game saved.")
                    save_game(depth, playerHealth, damageBoost, armorBoost,
                              luckBoost, foodInInven, sword, armor,
                              pArmorBoost, pAttackBoost, pLuckBoost, enemies,
                              allEnemies, coins, swordId, armorId, artifacts)
                    # checks if a new enemy should appear
                    newChallengerApproaches()
                    # calculates the total weight of the enemies, the more weight the more enemies
                    totalEnemyWeight = 100 + (depth * (depth) / 2) + 5 * depth
                    # spawning enemies
                    spawnEnemies()
                    getEnemies()
                    # gives loot to the player if they progress down a depth
                    if (depth != 0):
                        print("\n\nYou advanced to depth " + str(depth - 1) +
                              " .You recieved " + giveLoot() + ".")
                    time.sleep(4)
                # checks if the player has food in their inventory
                if (len(foodInInven) < 1):
                    displayFood = "nothing"
                #start of the loop code

                clear()
                boostStats()
                # prints the player's stats and the enemies' stats
                show = " , ".join(displayEnemies)
                displayFood = " ,".join(foodInInven)
                print("\nYou are at a depth of " + str(depth - 1) +
                      " into the dungeon.\n\nYou have " + str(playerHealth) +
                      " hp left, with a attack boost of " + str(damageBoost) +
                      " + (" + str(pAttackBoost) + "), and a armor boost of " +
                      str(armorBoost) + " + (" + str(pArmorBoost) + ")%\n\n" +
                      str(getHappening()) +
                      "\n\nThe opposing team consists of:\n" + str(show) +
                      "\n\nYour inventory has " + displayFood +
                      "\n1.Attack\n2.Action\n3.Items\n4.Mercy\n5.Exit Dungeon")
                time.sleep(0.5)
                # the player's actions
                decision = input("\nWhat do you do?(type in number)")
                match (decision):
                    # attacking the enemy
                    case "1":
                        show = " , ".join(displayEnemies)
                        print(
                            "which enemy do you want to attack?(type in number please)\n"
                            + str(show))
                        decision = input(
                            "\nWhich enemy do you attack?(type in number)")
                        # catches if the player inputs a non integer to prevent errors
                        try:
                            decision = int(decision)

                        except ValueError:
                            print("TYPE AN INTEGER PLEASE FROM 1 TO " +
                                  str(len(enemies)))

                        # checks if the player inputs a valid enemy
                        else:
                            choice = int(decision) - 1
                            if choice < 0 or choice >= len(enemies):
                                print(
                                    "Invalid enemy, type the number of an available enemy"
                                )
                            else:
                                # attacks the enemy and deals damage
                                boostStats()
                                onPlayerAttack(choice)
                                enemies[choice].health -= playerDamage
                                print("You dealt " + str(playerDamage) +
                                      " damage to the " + enemies[choice].type)

                                # has a chance to reset the damage boost
                                if random.randint(0, 10) < 7:
                                    damageBoost = 0
                                    
                    # actions that the player can take
                    case "2":
                        print(
                            "1. Survey surroundings\n2. Meditate\n3. Sharpen Weapon(s)"
                        )
                        decision = input("\nWhat do you do?(type in number)")
                        match (decision):
                            # inspects the dungeon room, doesn't do anything (yet...)
                            case "1":
                                print("You inspect the dungeon room...\n")

                                time.sleep(1)

                                match (curDungeonType):
                                    case "normal":
                                        print("Everything seems fine.")
                                    case "cold":
                                        print("You can see icicles forming.")
                                    case "hot":
                                        print("Eveything is slightly red.")
                                    case "poison":
                                        print("The air seems to be green.")
                                    case "trapped":
                                        print(
                                            "The air is thick with suspense.")
                                    case "dark":
                                        print(
                                            "You can't see anything, it's too dark."
                                        )
                                    case "spawner":
                                        print(
                                            "Wait, did another monster just apperar?!?"
                                        )

                                time.sleep(2)
                            # meditating to boost aromr
                            case "2":
                                print("You rethink your life choices...\n")

                                time.sleep(3)

                                armorBoost += random.randint(1, 20)
                                print(
                                    "Your armor amount increased temporarily by "
                                    + str(armorBoost) + "% !")
                                time.sleep(2)
                            # sharpening weapons to boost damage
                            case "3":
                                print("You sharpen your weapons...\n")
                                time.sleep(2)
                                damageBoost = round(random.randint(1, 2 * round(luck/2)))
                                print(
                                    "Your damage has been temporarily boosted by "
                                    + str(damageBoost) + " !")
                                time.sleep(2)
                    #the player eats something from their inventory
                    case "3":
                        print(
                            "You rummage around in you backpack for some food..."
                        )
                        time.sleep(1)
                        # if they have food in their inventory, they can eat it
                        if (len(foodInInven) > 0):
                            print("You have " + " ,".join(foodInInven) + " .")
                            decision = input(
                                "\nWhat do you eat?(type in number)")
                            # catches if the player inputs a non integer to prevent errors
                            try:
                                decision = int(decision)
                            except ValueError:
                                print(
                                    "PLEASE\n\n\n\nTYPE\n\n\n\nIN\n\n\n\nINTEGER\n\n\n\nFORMAT"
                                )
                                time.sleep(10)
                            # if they input a non - valid number, it will catch it
                            else:
                                if (int(decision) > len(foodInInven)
                                        or int(decision) < 0):
                                    print(
                                        "Please input number(non 0 or negatives, 1-9)"
                                    )
                                # adding the player's health based on the food they ate
                                else:
                                    match (foodInInven[decision - 1]):
                                        case "pomegranate":
                                            playerHealth += 40
                                        case "pancakes":
                                            playerHealth += 50
                                        case "apple sauce":
                                            playerHealth += 20
                                        case "pizza":
                                            playerHealth += 40
                                        case "rice":
                                            playerHealth += 10
                                            #for the rice farmers
                                            if (random.randint(0, 10) <= 2):
                                                playerHealth += 200
                                        case "chicken tikka masala":
                                            playerHealth += 25
                                        case "heal pot":
                                            playerHealth += 90
                                            #d6 for extra heal, plus some base heal
                                            playerHealth += random.randint(
                                                1 * 10, 6 * 10)
                                    time.sleep(0.5)
                                    print("You ate a " +
                                          foodInInven[int(decision) - 1])
                                    foodInInven.pop(int(decision) - 1)
                        else:
                            print("You don't have anything to eat")
                        time.sleep(1)
                        
                    #the player begs for mercy, has a chance to do different things
                    case "4":
                        print("You beg for mercy of the enemies...")
                        time.sleep(2)
                        if (random.randint(0, 10) < 6):
                            print("\nThey ignore your pleas")
                        elif (random.randint(0, 10) < 4):
                            print("\nThey decide to commit autothysis")
                            for enemy in enemies:
                                enemy.health = 0
                            damagePlayer(20 * len(enemies))
                        else:
                            print("\nThey take damage due to sympathy")
                            for enemy in enemies:
                                enemy.health -= 5
                        time.sleep(2)
                    #the player exits the dungeon, resetting all their stats and progress
                    case "5":
                        
                        playerHealth = 0
                        depth = 0
                        allEnemies = [["zombie", 50], ["skeleton", 75]]
                        enemies = []
                        damageBoost = 0
                        armorBoost = 0
                        luckBoost = 0
                        foodInInven = []
                        pArmorBoost = 0
                        pAttackBoost = 0
                        pLuckBoost = 0
                        
                        print("You exit the dungeon...")
                        time.sleep(2)
                        scene = 2
                    case _:
                        print(
                            "\nPlease type one of the availible options(numbers)"
                        )
                    

                #enemy stuff
                for enemy in enemies[:]:
                    # only attack if the enemy is alive
                    if enemy.health <= 0:
                        continue
                    onEnemyAttack(enemy.damage, enemy)
                    enemy.attack(damagePlayer)
                    # if the player dies, it will trigger the onPlayerDeath function
                    if (playerHealth <= 0):
                        onPlayerDeath()
                    time.sleep(0.5)
                    # has a chance to reset the armor boost
                    if random.randint(0, 10) < 7:
                        armorBoost = 0

                dead_enemies = [e for e in enemies if e.health <= 0]
                for e in dead_enemies:
                    # gives the player coins and food based on the enemy they killed
                    coins += e.cost
                    print("A " + e.type + " died. You got " +
                          decideGiveFood(e.value) + " from it and " +
                          str(e.cost) + " coins.")

                enemies = [e for e in enemies if e.health > 0]
                displayEnemies = [e.type for e in enemies]
                getEnemies()

                time.sleep(2.5)

            clear()
            print("You died. Your final depth is: " + str(depth))
            time.sleep(5)
            cont = input("Type anything to continue")
            scene = 2
            playerHealth = 100
            depth = 0
            allEnemies = [["zombie", 50], ["skeleton", 75]]
            enemies = []
            damageBoost = 0
            armorBoost = 0
            luckBoost = 0
            foodInInven = []
            pArmorBoost = 0
            pAttackBoost = 0
            pLuckBoost = 0
            save_game(depth, playerHealth, damageBoost, armorBoost, luckBoost,
                      foodInInven, sword, armor, pArmorBoost, pAttackBoost,
                      pLuckBoost, enemies, allEnemies, coins, swordId, armorId,
                      artifacts)
        # the hub
        case 2:
            clear()
            print(
                "Welcome to the hub!\n\nYou have " + str(coins) +
                " coins.\n\n1.Buy Sword\n2.Buy Armor\n3.Buy food & stat boosts\n4.Buy artifacts\n5.Enter Dungeon\n6.Guide"
            )
            decision = input("\nWhat do you do?(type in number)")
            match (decision):
                # buying swords
                case "1":
                    clear()
                    if(swordId+1<len(swordTypes)):
                        print("You have " + str(coins) +
                              " coins. To buy the next sword, you need " +
                              str(30 * swordId + 20) + " coins.\n\n1.Buy " +
                              swordTypes[swordId + 1] + " Sword\n2.Back")
                        decision = input("\nWhat do you do?(type in number)")
                        match (decision):
                            # checks if the player has enough coins to buy the sword
                            case "1":
                                if (coins >= 30 * swordId + 20):
                                    coins -= 30 * swordId + 20
                                    swordId += 1
                                    sword = swordTypes[swordId]
                                    time.sleep(1)
                                    print("\nYou bought a " + swordTypes[swordId] +
                                          " sword!")
                                    time.sleep(2)
                                else:
                                    print("\nYou don't have enough coins...")
                                    time.sleep(2)
                            # returns to the hub
                            case "2":
                                print("Returning to hub...")
                                time.sleep(2)
                    else:
                        print("You bought all the swords...")
                        time.sleep(2)
                # buying armor
                case "2":
                    clear()
                    if(armorId+1<len(armorTypes)):
                        print("You have " + str(coins) +
                              " coins. To buy the next armor, you need " +
                              str(40 * armorId + 50) + " coins.\n\n1.Buy " +
                              armorTypes[armorId + 1] + " Armor\n2.Back")
                        decision = input("\nWhat do you do?(type in number)")
                        match (decision):
                            # checks if the player has enough coins to buy the armor
                            case "1":
                                if (coins >= 40 * armorId + 50):
                                    coins -= 40 * armorId + 50
                                    armorId += 1
                                    armor = armorTypes[armorId]
                                    time.sleep(1)
                                    print("\nYou bought " + armorTypes[armorId] +
                                          " armor!")
                                    time.sleep(2)
                                else:
                                    print("\nYou don't have enough coins...")
                                    time.sleep(2)
                            # returns to the hub
                            case "2":
                                print("Returning to hub...")
                                time.sleep(2)
                    else:
                        print("You bought all the armor...")
                        time.sleep(2)
                # buying food and stat boosts
                case "3":
                    clear()
                    print("You have " + str(coins) +
                          " coins.\n\n1.Buy food\n2.Buy stat boosts\n3.Back")
                    decision = input("\nWhat do you do?(type in number)")
                    match (decision):
                        # buying food
                        case "1":
                            clear()
                            print(
                                "You have " + str(coins) +
                                " coins.\n\n1.Buy pomegranate(30 coins)\n2.Buy pancakes(10 coins)\n3.Buy apple sauce(5 coins)\n4.Buy pizza(25 coins)\n5.Buy rice(10 coins)\n6.Buy chicken tikka masala(20 coins)\n7.Buy heal pot(50 coins)\n8.Back"
                            )
                            # checks which food the player wants to buy
                            decision = input(
                                "\nWhat do you do?(type in number)")
                            match (decision):
                                case "1":
                                    chosenFood = "pomegranate"
                                    foodCost = 30
                                case "2":
                                    chosenFood = "pancakes"
                                    foodCost = 10
                                case "3":
                                    chosenFood = "apple sauce"
                                    foodCost = 5
                                case "4":
                                    chosenFood = "pizza"
                                    foodCost = 25
                                case "5":
                                    chosenFood = "rice"
                                    foodCost = 10
                                case "6":
                                    chosenFood = "chicken tikka masala"
                                    foodCost = 20
                                case "7":
                                    chosenFood = "heal pot"
                                    foodCost = 50
                                case "8":
                                    chosenFood = "nothing"
                                    print("Returning to hub...")
                                    time.sleep(2)
                            if (chosenFood != "nothing"):
                                # how many of the food the player wants to buy
                                number = input(
                                    "\nHow many do you want to buy?(type in number)"
                                )
                                if ((int(number) * foodCost) <= coins):
                                    coins -= int(number) * foodCost
                                    for i in range(int(number)):
                                        foodInInven.append(chosenFood)
                                    print("You bought " + str(number) + " " +
                                          chosenFood + "(s)")
                                    time.sleep(2)
                                else:
                                    print("You don't have enough coins...")
                                    time.sleep(2)
                        # buying stat boosts
                        case "2":
                            clear()
                            print(
                                "You have " + str(coins) +
                                " coins.\n\n1.Buy attack boost(10 coins)\n2.Buy armor boost(10 coins)\n3.Buy luck boost(10 coins)\n4.Buy permenant attack boost(100 coins)\n5.Buy permanant armor boost(50 coins)\n6.Buy permenant luck boost(200 coins)\n7.Back"
                            )
                            # which stat boost the player wants to buy
                            decision = input(
                                "\nWhat do you do?(type in number)")
                            match (decision):
                                case "1":
                                    if (coins >= 10):
                                        coins -= 10
                                        damageBoost += 10
                                        print("You bought a attack boost!")
                                        time.sleep(2)
                                    else:
                                        print("You don't have enough coins...")
                                        time.sleep(2)
                                case "2":
                                    if (coins >= 10):
                                        coins -= 10
                                        armorBoost += 10
                                        print("You bought a armor boost!")
                                        time.sleep(2)
                                    else:
                                        print("You don't have enough coins...")
                                        time.sleep(2)
                                case "3":
                                    if (coins >= 10):
                                        coins -= 10
                                        luckBoost += 10
                                        print("You bought a luck boost!")
                                        time.sleep(2)
                                    else:
                                        print("You don't have enough coins...")
                                        time.sleep(2)
                                case "4":
                                    if (coins >= 100):
                                        coins -= 100
                                        pAttackBoost += 1
                                        print(
                                            "You bought a permenant attack boost!"
                                        )
                                        time.sleep(2)
                                    else:
                                        print("You don't have enough coins...")
                                        time.sleep(2)
                                case "5":
                                    if (coins >= 50):
                                        coins -= 50
                                        pArmorBoost += 1
                                        print(
                                            "You bought a permenant armor boost!"
                                        )
                                        time.sleep(2)
                                    else:
                                        print("You don't have enough coins...")
                                        time.sleep(2)
                                case "6":
                                    if (coins >= 200):
                                        coins -= 200
                                        pLuckBoost += 1
                                        print(
                                            "You bought a permenant luck boost!"
                                        )
                                        time.sleep(2)
                                    else:
                                        print("You don't have enough coins...")
                                        time.sleep(2)
                                case "7":
                                    print("Returning to hub...")
                                    time.sleep(2)
                        # returns to the hub
                        case "3":
                            print("Returning to hub...")
                            time.sleep(2)
                # buying artifacts
                case "4":
                    clear()
                    for i in range(len(artifactsOnDisplay)):
                        # prints the artifacts on display
                        print("\n"+str(i+1)+".Buy " + artifactsOnDisplay[i][0] + "  ("+artifactsOnDisplay[i][2]+"). costs " + str(artifactsOnDisplay[i][1]) + " coins")
                    # buying an extra artifact slot or returning to the hub
                    print("\n\n"+str(len(artifactsOnDisplay)+1)+".Buy artifact slot(100 coins)\n\n"+str(len(artifactsOnDisplay)+2)+".Back")
                    decision = input("\nWhat do you do?(type in number)")
                    d = int(decision)
                    if(d>=len(artifactsOnDisplay)+2):
                        print("Returning to hub...")
                        time.sleep(2)
                    elif(d==len(artifactsOnDisplay)+1):
                        if(coins>=100):
                            coins -= 100
                            artifactSlots+=1
                            rollForArtifacts()
                            print("Rerolled artifacts and added an extra slot!")
                            time.sleep(2)
                    # buying an artifact
                    else:
                        if(coins>=artifactsOnDisplay[d-1][1]):
                            coins -= artifactsOnDisplay[d-1][1]
                            artifacts.append(artifactsOnDisplay[d-1])
                            print("You bought a " +artifactsOnDisplay[d-1][0] + "!")
        
                            #removing the artifact that you bought from the shop
                            for i in range(len(allArtifacts)):
                                if(allArtifacts[i]==artifactsOnDisplay[d-1]):
                                    allArtifacts.pop(i)
                                    break
        
                            classifyArtifacts()
                            rollForArtifacts()
        
                            time.sleep(2)
                        # if the player doesn't have enough coins
                        else:
                            print("You don't have enough coins...")
                            time.sleep(2)
        
                # entering the dungeon
                case "5":
                    print("You enter the dungeon...")
                    time.sleep(2)
                    scene = 1
                    onPlayerEnterDungeon()
                # the guide
                case "6":
                    print(agni)
                    back = input("\n\nPress enter to return to the hub")
                    
