with open('data.txt') as f:
    lines = f.readlines()

lista = []

for line in lines:
    game = line.split(":")
    id_game = int(game[0].split(" ")[1])
    colors = {
        "blue":[],
        "red":[],
        "green":[]
    }
    sets = game[1].split(";")
    for set in sets:
        boxes = set.split(",")
        for box in boxes:
            value = box.split(" ")
            colors[value[2].replace("\n","")].append(int(value[1]))
    

    if max(colors["blue"]) <= 14 and max(colors["red"]) <= 12 and max(colors["green"]) <= 13:
        lista.append(id_game)

print(sum(lista))

