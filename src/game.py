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
        GainingScore -= 0.2

    if dmg > 0:
        AttackerScore = attacker.get("score") + GainingScore
        TargetHP = target.get("health") - dmg
        setPlayer(target, "defense", False)
        setPlayer(target, "health", TargetHP)
        setPlayer(attacker, "score", AttackerScore)


def displayMatchResult():
    global PlayerList
    pplist = PlayerList.copy()

    for i in range(len(PlayerList)):

        PlayerScoreList = []
        PlayerHealthList = []

        for player in pplist:
            PlayerScoreList.append(player["score"])
            PlayerHealthList.append(player["health"])

        MaxScore = max(PlayerScoreList)
        if PlayerScoreList.count(MaxScore) > 1:
          MaxIndex = []
          MaxHealth = 0
          for j in range(len(PlayerScoreList)):
            if PlayerScoreList[j] == MaxScore:
              MaxIndex.append(j)

          for index in MaxIndex:
            MaxHealth = max(pplist[index]["health"], MaxHealth)

          for k in MaxIndex:
            if pplist[k]["health"] == MaxHealth:
                PlayerName = pplist[k]["name"]
                PlayerScore = pplist[k]["score"]
                PlayerHealth = pplist[k]["health"]

                print(f"Rank {i+1}: {PlayerName} | Score: {PlayerScore} | Health: {PlayerHealth}")
                pplist.pop(k)
                MaxIndex.remove(k)
        else:
          MaxIndex = PlayerScoreList.index(MaxScore)
          PlayerName = pplist[MaxIndex]["name"]
          PlayerScore = pplist[MaxIndex]["score"]
          PlayerHealth = pplist[MaxIndex]["health"]

          print(f"Rank {i+1}: {PlayerName} | Score: {PlayerScore} | Health: {PlayerHealth}")
          pplist.pop(MaxIndex)