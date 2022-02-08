def checkKey(dict, key):
    if key in dict.keys():
        return True
    else:
        return False
d = {}
with open('Stopwords.txt') as f:
    line = f.readline()
    while line:
        line = f.readline()
        line = line.replace('\n', '')
        d[line] = 0

        