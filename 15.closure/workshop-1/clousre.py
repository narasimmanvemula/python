def get_fn():
    a = 1
    b = 2
    def get():
        print(a)
        print(b)
        return (a, b)
    return get

gfn = get_fn()
gfn.__code__.co_freevars
# ('a', 'b')
gfn.__closure__[0]
# <cell at 0x10849c4f8: int object at 0x1081907c0>
gfn.__closure__[0].cell_contents
# 1
gfn.__closure__[1].cell_contents
# 2