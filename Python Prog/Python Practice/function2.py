def foo(agc):
    b = len(agc)
    if b >= 8:
        print("True") 
    else:
        print("False")
foo("mypass")


def foo(agc):
    b = len(agc)
    if b >= 8:
        return True 
    else:
        return False
foo("mypass")

def temp(val):
    if val > 25:
        return "Hot"
    elif 15 > val < 25:
        return "Warm"
    else:
        return "Cold"
foo(10)