import turtle

zelva = Turtle('triangle')

wn = Screen()
wn.setup(700, 700)

def stisknutiKlavesyNahoru():
    zelva.forward(10)

def stisknutiKlavesyDoprava():
    zelva.right(10)

def stisknutiKlavesyDoleva():
    zelva.left(10)

def stisknutiKlavesyDolu():
    zelva.down(10)

wn.onkeypress(stisknutiKlavesyNahoru, 'Up')
wn.onkeypress(stisknutiKlavesyDolu, 'Down')
wn.onkeypress(stisknutiKlavesyDoprava, 'Right')
wn.onkeypress(stisknutiKlavesyDoleva, 'Left')

wn.listen()

wn.mainloop()