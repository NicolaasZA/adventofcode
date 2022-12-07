def readInput(pathToFile: str) -> list[str]:
    result = []
    with open(pathToFile) as fi:
        result = fi.readlines()
    return result


def flatten(_: list[str]):
    return "/".join(_) + '/'


sizes = {}
folders: list[str] = []
files: list[str] = []
cpath: list[str] = ['', ]

for com in readInput('input.txt'):
    com = com.replace("\n", "")
    if com.startswith("$ "):
        # this is a command
        parts = com.replace("$ ", "").split(" ")

        if parts[0] == "cd":
            if parts[1] == '/':
                cpath = ['', ]
            elif parts[1] == '.':
                pass
            elif parts[1] == '..':
                if len(cpath) > 1:
                    cpath.pop()
            else:
                cpath.append(parts[1])
                filepath = flatten(cpath)

                if filepath not in folders:
                    folders.append(filepath)
                    sizes[filepath] = 0

        else:
            pass

    elif com.startswith("dir "):
        # this is an ls output, folder
        filepath = flatten(cpath)

        if filepath not in folders:
            folders.append(filepath)
            sizes[filepath] = 0
    else:
        # this is an ls output, file
        parts = com.split(" ")
        filepath = flatten(cpath) + parts[1]
        if filepath not in files:
            files.append(filepath)
        sizes[filepath] = int(parts[0], base=10)

# Calculate folder sizes
for folder in folders:
    for fl in files:
        if fl.startswith(folder):
            sizes[folder] += sizes[fl]


# PART 1
total = 0
for p in folders:
    if sizes[p] <= 100000:
        total += sizes[p]

print("part one:", total)


# PART 2
need_to_get_rid_of = sizes['/'] - (70000000 - 30000000)

best_path = folders[0]
for p in folders:
    if (sizes[p] < sizes[best_path]) and (sizes[p] >= need_to_get_rid_of):
        best_path = p

print(f"part two: {sizes[best_path]} at '{best_path}'")
