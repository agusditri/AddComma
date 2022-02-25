file = open(r"C:\Users\agust\OneDrive\Escritorio\Python\Advent2021\input.txt", "r+")
lines = file.readlines()
file.seek(0)
file.truncate(0)
file.flush()

for line in range(len(lines)):
    lines[line] = '"' + lines[line].replace("\n", '",\n' )
    file.write(str(lines[line]))
file.write('"')
file.close()
