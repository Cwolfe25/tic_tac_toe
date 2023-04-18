
text = open('Bee_Movie.txt')
d = dict()
for word in text:
    d[word] = d.get(c,0) + 1
print(d)
