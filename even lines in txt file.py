f = open('dataset_31_6.txt','r')
g = open('dataset_31_6a.txt','w')
i = 1
for line in f:
    if i % 2 == 0:
        g.write(line)
    i += 1
f.close()
g.close()
