#Mathew De La Cruz
def polygon (T,sides,size,c):
    angle=240/sides
    T.color(c)
    for times in range(sides):
        T.forward(size)
        T.left(angle)
    
