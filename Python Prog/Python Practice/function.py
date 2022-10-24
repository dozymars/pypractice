from http.client import MOVED_PERMANENTLY, CannotSendHeader


def mean(list):
    the_mean = sum(list) / len(list)
    return the_mean
print(mean([2,5,8,9]))




#Cad to USDdollar calculation

def cad(amount):
    usd = 2.3 * amount
    return usd
receive = cad(300)
print(receive)


#calculate squre root of a value
def foo(num):
    formular = num**2
    return formular
print(foo(7))

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean
student_grades = {"marry": 9.1, "sim": 8.8, "john": 7.5}
to_list = student_grades.values()

print(mean([to_list]))


