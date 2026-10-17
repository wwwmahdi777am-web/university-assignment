import sys

year = int(sys.argv[1])

if year % 400 == 0:
    print("sal kabise")
elif year % 100 == 0:
    print("sal kabise nist")
elif year % 4 == 0:
    print("sal kabise")
else:
    print("sal kabise nist")