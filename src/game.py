PlayerList = None

def initPlayers():
    global PlayerList
    PlayerList = []

def createNewPlayer(name="", damage=0, defensePower=0):
    return {"name": name, "score": 0, "damage": damage, "health": 100, "defensePower": defensePower, "defense": False}

def addPlayer(player):
    global PlayerList
    PlayerList.append(player)

def removePlayer(name):
    global PlayerList
    adapemain = True
    for i in range(len(PlayerList)):
        if PlayerList[i]["name"] == name:
            adapemain = False
            PlayerList.pop(i)
    if adapemain:
        print("There is no player with that name!")

def setPlayer(player, key, value):
    player[key] = value

def attackPlayer(attacker, target):

    TargetDefense = target.get("defensePower")
    dmg = attacker.get("damage")
    GainingScore = 1

    if target["defense"]:
        dmg -= TargetDefense
        GainingScore -= (1 / target["defensePower"]) if target["defensePower"] > 0 else 0

    if dmg > 0:
        AttackerScore = round(attacker.get("score") + GainingScore, 2)
        TargetHP = target.get("health") - dmg
        setPlayer(target, "defense", False)
        setPlayer(target, "health", TargetHP)
        setPlayer(attacker, "score", AttackerScore)


def displayMatchResult():
    global PlayerList
    pplist = sorted(PlayerList, key=lambda x: (-x["score"], -x["health"])) 
    rank = 1

    for player in pplist:
        PlayerName = player["name"]
        PlayerScore = player["score"]
        PlayerHealth = player["health"]
        print(f"Rank {rank}: {PlayerName} | Score: {PlayerScore} | Health: {PlayerHealth}")
        rank += 1
