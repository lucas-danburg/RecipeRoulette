def get_lines(filename):
    file = open(filename, 'r')
    html = []
    for line in file:
        html.append(line)
    file.close()
    return html

def digit(items):
    ref = {'½': 0.5, '¾': 0.75, '¼': 0.25, '⅓': 0.3, '⅛': 0.125, '⅝': 0.625, '⅔': 0.6, '⅜': 0.375, '⅞': 0.875}
    new = []
    for item in items:
        if item in ref:
            new.append(ref[item])
        else:
            new.append(item)
    return new

lines = digit(get_lines('ingredients.txt'))
file = open('ing.txt', 'a')
for line in lines:
    line = line.strip('\n')
    file.write(line + '\n')
file.close()
