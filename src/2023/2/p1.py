def read(file_to_use):
    lines: list[str] = []
    with open(file_to_use, 'r') as file:
        lines = file.readlines()
    return list(map(lambda x: x.replace('\n', '').replace('\r', ''), lines))


def is_possible(game: str) -> int:
    gameid = int(game.split(':')[0].replace('Game ', ''))
    shows = game.split(':')[1].split(';')
    for show in shows:
        cubes = [x.strip(' ') for x in show.strip(' ').split(',')]
        for cube in cubes:
            count = int(cube.split(' ')[0])
            if cube.endswith('red') and count > 12:
                return 0
            elif cube.endswith('green') and count > 13:
                return 0
            elif cube.endswith('blue') and count > 14:
                return 0
    # print(shows)
    return gameid

if __name__ == '__main__':
    games = read('input.txt')
    possibles = [is_possible(g) for g in games]
    print('part 1:', sum(possibles))
