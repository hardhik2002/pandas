import sys
tup_=(int(i) for i in input().split())
print(sys.getsizeof(tup_))
print(sys._sizeof_(tup_))


