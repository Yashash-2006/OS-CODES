import random

n = int(input("Disk size: "))
disk = [random.choice([0,1]) for _ in range(n)]

print("\nDisk:", disk)

print("\n1.Sequential")
print("2.Linked")
print("3.Indexed")

ch = int(input("Choice: "))

files = int(input("No. of files: "))

for f in range(1, files+1):
    size = random.randint(1,5)
    print(f"\nFile F{f} Size:", size)
    free = [i for i in range(n) if disk[i] == 0]
    # Sequential
    if ch == 1:
        ok = False
        for i in range(n-size+1):
            if all(disk[j]==0 for j in range(i,i+size)):
                for j in range(i,i+size):
                    disk[j] = 1

                print("Blocks:", list(range(i,i+size)))
                ok = True
                break

        if not ok:
            print("Allocation Failed")

    # Linked
    elif ch == 2:
        if len(free) < size:
            print("Allocation Failed")

        else:
            blocks = random.sample(free, size)
            for b in blocks:
                disk[b] = 1

            print("Linked:", " -> ".join(map(str,blocks)))

    # Indexed
    elif ch == 3:
        if len(free) < size+1:
            print("Allocation Failed")

        else:
            index = free[0]
            data = random.sample(free[1:], size)
            disk[index] = 1
            for b in data:
                disk[b] = 1

            print("Index Block:", index)
            print("Data Blocks:", data)

    print("Disk:", disk)