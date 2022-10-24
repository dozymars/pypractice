phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
cont = phone_numbers.items()
for num in cont:
    print(num)



phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for name, num in phone_numbers.items():
    print(f"this is the phone for {name}: {num}")



phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}
for num in phone_numbers.values():
    print(num.replace("+", "00"))