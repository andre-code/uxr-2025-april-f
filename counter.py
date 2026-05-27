import sys

total = int(sys.argv[1]) if len(sys.argv) > 1 else 100

for i in range(1, total + 1):
    print(i)
