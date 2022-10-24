class Bed:
    def __init__(self, size, shape):
        self.size = size
        self.shape = shape
my = Bed("queen", "round")

print(my.size)
print(my.shape)


def bell(mem):
    if mem > 4:
        print("five is less than 4")

bell(5)


def bell(cad):
    usd = cad * 1.3
    return usd
    
print(bell(1000))
