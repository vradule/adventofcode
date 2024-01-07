def get_input(file_name):
    file = open(file_name, "r")
    return file.read().split("\n")


def is_possible(game):
    game = game.split(": ")[1]
    game = game.split("; ")
    for set in game:
        for pair in set.split(", "):
            count, color = pair.split(" ")
            count = int(count)
            if color == "red" and count > 12:
                return False
            if color == "green" and count > 13:
                return False
            if color == "blue" and count > 14:
                return False
    return True


def sum_of_possible(games):
    sum = 0
    for i, game in enumerate(games):
        if is_possible(game):
            sum += i + 1
    return sum


games = get_input("example1.txt")
assert is_possible(games[0]) == True
assert is_possible(games[1]) == True
assert is_possible(games[2]) == False
assert is_possible(games[3]) == False
assert is_possible(games[4]) == True
assert sum_of_possible(games) == 8

games = get_input("input.txt")
res = sum_of_possible(games)
print(res)


def fewest_power(game):
    game = game.split(": ")[1]
    game = game.split("; ")
    colors = {"red": 0, "green": 0, "blue": 0}
    for set in game:
        for pair in set.split(", "):
            count, color = pair.split(" ")
            count = int(count)
            if(colors[color] < count): colors[color] = count
    prod = 1
    for v in colors.values():
        prod *= v
    return prod


def sum_of_fewest_power(games):
    sum = 0
    for game in games:
        sum += fewest_power(game)
    return sum


games = get_input("example1.txt")
assert fewest_power(games[0]) == 48
assert fewest_power(games[1]) == 12
assert fewest_power(games[2]) == 1560
assert fewest_power(games[3]) == 630
assert fewest_power(games[4]) == 36
assert sum_of_fewest_power(games) == 2286

games = get_input("input.txt")
res = sum_of_fewest_power(games)
print(res)