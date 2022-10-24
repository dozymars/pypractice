def temp(val):
    if val > 25:
        return "Hot"
    elif 15 > val < 25:
        return "Warm"
    else:
        return "Cold"
print(temp(10))