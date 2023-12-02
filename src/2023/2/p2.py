from p1 import read


def get_power(game: str) -> int:
    shows = game.split(':')[1].split(';')
    red, green, blue = 0, 0, 0
    for show in shows:
        cubes = [x.strip(' ') for x in show.strip(' ').split(',')]
        for cube in cubes:
            count = int(cube.split(' ')[0])
            if cube.endswith('red') and count > red:
                red = count
            elif cube.endswith('green') and count > green:
                green = count
            elif cube.endswith('blue') and count > blue:
                blue = count
    return red * green * blue


games = read('input.txt')
powers = [get_power(g) for g in games]
print('part 2:', sum(powers))
