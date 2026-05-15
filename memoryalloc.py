import matplotlib.pyplot as plt

nb = int(input("Enter number of memory blocks: "))
block = list(map(int,input("Enter block sizes:\n").split()))

np = int(input("\nEnter number of processes: "))
process = list(map(int,input("Enter process sizes:\n").split()))

print("\n1. First Fit\n2. Best Fit\n3. Worst Fit")
choice = int(input("Enter choice: "))

alloc = [-1] * np

# Allocation Logic
for i in range(np):
    idx = -1

    # First Fit
    if choice == 1:
        for j in range(nb):
            if block[j] >= process[i]:
                idx = j
                break

    # Best Fit
    elif choice == 2:
        best = 999999
        for j in range(nb):
            if block[j] >= process[i] and block[j] < best:
                best = block[j]
                idx = j

    # Worst Fit
    elif choice == 3:
        worst = -1
        for j in range(nb):
            if block[j] >= process[i] and block[j] > worst:
                worst = block[j]
                idx = j

    # Allocation
    if idx != -1:
        alloc[i] = idx
        block[idx] -= process[i]

# Output Table
print("\nProcess\tSize\tBlock")

for i in range(np):
    print(f"P{i+1}\t{process[i]}\t",end="")
    if alloc[i] != -1:
        print(alloc[i]+1)
    else:
        print("Not Allocated")

# Graph
fig, ax = plt.subplots(figsize=(8,5))
for i in range(np):
    if alloc[i] != -1:
        ax.barh(alloc[i], process[i], color="blue")
        ax.text(process[i]/2, alloc[i], f"P{i+1}", ha="center", va="center", color="white")

ax.set_xlim(0,100)
ax.set_ylim(-1,nb)

ax.set_xlabel("Memory Size")
ax.set_ylabel("Blocks")

ax.set_title("Memory Allocation")

plt.show()