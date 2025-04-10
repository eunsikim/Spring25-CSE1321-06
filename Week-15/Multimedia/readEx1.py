with open("Week-15/Multimedia/saveFile.txt", mode="r", encoding="utf-8") as save:
    lines = save.readlines()

    data = []

    for line in lines:
        data.append(line.strip())

    player_name = data[0]
    last_lvl = int(data[1])
    player_hp = int(data[2])


    print(f"Player Name: {player_name}")
    print(f"Loading level: {last_lvl}")
    print(f"Player HP: {player_hp}")

with open("Week-15/Multimedia/saveFile2.txt", mode="w", encoding="utf-8") as save:
    player_name = "John Doe"
    last_lvl = 2
    player_hp = 100

    data = [f"{player_name}\n", f"{str(last_lvl)}\n", f"{str(player_hp)}\n"]

    save.writelines(data)
