def point(x,y):
    def set_x(new_x):
        nonlocal x 
        x = new_x
    
    def set_y(new_y):
        nonlocal y
        y = new_y
    
    def get():
        print(x,y)

    point.set_x = set_x
    point.set_y = set_y
    point.get = get
    return point

p = point(2, 3)
print(p)
p.set_x(5)
p.get()

p.set_y(5)
p.get()
