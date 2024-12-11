from src import game as m

m.initPlayers()

ambalika = m.createNewPlayer(name="ambalika", damage=0, defensePower=0)
salya = m.createNewPlayer(name="salya", damage=0, defensePower=0)
byasa = m.createNewPlayer(name="byasa", damage=0, defensePower=0)
surasena = m.createNewPlayer(name="surasena", damage=0, defensePower=0)
sahadeva = m.createNewPlayer(name="sahadeva", damage=0, defensePower=0)
wredokara = m.createNewPlayer(name="wredokara", damage=0, defensePower=0)

#menambahkan pemain ke dalam game
m.addPlayer(ambalika)
m.addPlayer(salya)
m.addPlayer(byasa)
m.addPlayer(surasena)
m.addPlayer(sahadeva)
m.addPlayer(wredokara)

#membagi pemain menjadi 2 tim secara acak

AllPlayerIndex = [0, 1, 2, 3, 4, 5]
# random.shuffle(AllPlayerIndex)
#TerroristTeam = [AllPlayerIndex[0:3]]
#CounterTerroristTeam = [AllPlayerIndex[3:]]
TerroristTeam = [1, 4, 0]
CounterTerroristTeam = [2, 5, 3]

print("Terrorist Team:")
for T in TerroristTeam:
  print(PlayerList[T]["name"])

print("Counter Terrorist Team:")
for CT in CounterTerroristTeam:
  print(PlayerList[CT]["name"])

#membuat atribut player
playerattribute = []
for player in PlayerList:
  playerattribute.append({"name": player["name"], "weapon": [], "weaponnow": "-", "currency": 800})

def setplayerattr(player_name, key, value):
    for attr in playerattribute:
        if attr["name"] == player_name:
            attr[key] = value

#memulai round pertama
print("Round 1")
print("Buying Phase 20 Second")

#membuat list dictionary weapon
Weapon = [{"name": "Ak47", "dmg/mag":1080, "firetime": 3, "price": 2700},
          {"name": "Glock0-18", "dmg/mag":600, "firetime": 3, "price":200},
          {"name": "M4A4", "dmg/mag":990, "firetime": 2.7, "price":3000},
          {"name": "USP-S", "dmg/mag":420, "firetime": 2, "price":200},
          {"name": "P90", "dmg/mag":1300, "firetime": 3.5, "price":2350},
          {"name": "AUG", "dmg/mag":840, "firetime": 3, "price":3300},
          {"name": "AWP", "dmg/mag":575, "firetime": 3.4, "price":4750},
          {"name": "Desert Eagle", "dmg/mag":371, "firetime": 1.6, "price":700},
          {"name": "XM1014", "dmg/mag":840, "firetime": 2.5, "price":2000},
          {"name": "Negev", "dmg/mag":5250, "firetime": 11.5, "price":1700}]

#membuat hubungan player dengan weapon
def Player_Weapon(playername, weaponname):
    for human in playerattribute:
        if human["name"] == playername:
            human["weapon"].append(weaponname)

#membuat hubungan pemain dengan armor
def Player_Armor(player, Armor=False):
  if Armor:
    m.setPlayer(player, "defense", True)

Player_Weapon("ambalika", "USP-S")
Player_Armor(ambalika, Armor = True)
Player_Weapon("salya", "Desert Eagle")
Player_Armor(salya, Armor = False)
Player_Weapon("byasa", "Glock0-18")
Player_Armor(byasa, Armor = True)
Player_Weapon("surasena", "Desert Eagle")
Player_Armor(surasena, Armor = False)
Player_Weapon("sahadeva", "Desert Eagle")
Player_Armor(sahadeva, Armor = False)
Player_Weapon("wredokara", "Desert Eagle")
Player_Armor(wredokara, Armor = False)

#membuat damage pemain tergantung dengan weaponnya
def PlayerUseWeapon(playername, weaponname):
  global PlayerList, Weapon
  weapon_data = next((w for w in Weapon if w["name"] == weaponname), None)
  if weapon_data is None:
      print(f"Weapon {weaponname} Tidak ditemukan!")
      return
  dps = round(weapon_data["dmg/mag"] / weapon_data["firetime"], 2)

  for human in range(len(PlayerList)):
    if PlayerList[human]["name"] == playername:
      PlayerList[human]["damage"] = dps

PlayerUseWeapon("ambalika", "USP-S")
PlayerUseWeapon("salya", "Desert Eagle")
PlayerUseWeapon("byasa", "Glock0-18")
PlayerUseWeapon("surasena", "Desert Eagle")
PlayerUseWeapon("sahadeva", "Desert Eagle")
PlayerUseWeapon("wredokara", "Desert Eagle")

#membuat fungsi untuk detail penyerangan
def DetailAttack(attacker, target, time, headshot=False):
  damage = attacker.get("damage")
  dmg = damage * time
  if headshot:
    dmg*=3
  if target["defense"]:
    m.setPlayer(target, "defensePower", dmg/2)
  m.setPlayer(attacker, "damage", dmg)
  m.attackPlayer(attacker, target)
  m.setPlayer(attacker, "damage", damage)
  print(f"pemain {attacker['name']} menyerang pemain {target['name']} selama {time} detik")
  if target.get("health") <= 0:
    print(f"pemain {target['name']} telah tereliminasi")
    m.setPlayer(target, "health", 0)

#memulai pertandingan
print("Round Begin!")

DetailAttack(salya, wredokara, 0.5)
DetailAttack(surasena, ambalika, 0.2, headshot = True)
m.displayMatchResult()
DetailAttack(wredokara, salya, 0.3)
DetailAttack(byasa, sahadeva, 1)
m.displayMatchResult()

print("pertandingan telah berakhir")
