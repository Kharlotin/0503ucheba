from 2modul.pypro import a
n = a
if n>0 and n<13:
    if n<3 or n==12:
        print("Winter")
    elif n>=3 or n<6:
        print("Vesna")
    elif n>=6 or n<9:
        print("Leto")
    elif n>3 or n<6:
        print("Osen")
else:
    print("error")
