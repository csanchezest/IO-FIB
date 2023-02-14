x = {1:2,2:3,3:4,4:2,5:3,6:4,7:5,8:1,9:2,10:3,11:1,12:2,13:3,14:4,15:2.5,16:2,17:3,18:4,19:5,20:3,21:4,22:1,23:3,24:4}
y = {1:1,2:1,3:1,4:2,5:2,6:2,7:2,8:3,9:3,10:3,11:4,12:4,13:4,14:4,15:5  ,16:6,17:6,18:6,19:6,20:7,21:7,22:8,23:8,24:8}
links=[(1,2),(2,1),(1,4),(4,1),(2,3),(3,2),(3,6),(6,3),(3,7),(7,3),(4,5),(5,4),(4,9),(9,4),(5,10),(10,5),(5,6),(6,5),(6,14),(14,6),(7,14),(14,7),(7,19),(19,7),(8,9),(9,8),(8,11),(11,8),(9,12),(12,9),(9,10),(10,9),(10,13),(13,10),(11,22),(22,11),(11,12),(12,11),(12,15),(15,12),(12,13),(13,12),(13,14),(14,13),(13,15),(15,13),(13,17),(17,13),(14,18),(18,14),(15,16),(16,15),(16,17),(17,16),(16,22),(22,16),(17,18),(18,17),(17,20),(20,17),(18,21),(21,18),(19,24),(24,19),(20,22),(22,20),(20,23),(23,20),(20,21),(21,20),(21,24),(24,21),(22,23),(23,22),(23,24),(24,23)]
reds = set([(22,23), (23,22), (21,18), (21,24), (19,7), (3,6), (1,4), (4,5), (4,9), (10,5), (14,13), (16,15), (15,13)])

for i,j in links:
    cost = 95 + (x[i]-x[j]) ** 2 + (y[i] - y[j]) ** 2
    if (i,j) in reds:
        cost *= 1.75
    print(i, j, cost)
