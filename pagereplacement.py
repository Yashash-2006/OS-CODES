import random
import matplotlib.pyplot as plt

n = int(input("pages: "))
f=int(input("frames: "))
algo=input("algorithm (fifo/lru/optimal): ").lower()
pages=[random.randint(1,9) for _ in range(n)]

history=[]
faults=0
frames=[]
recent={}

for i in range(n):
    p=pages[i]
    recent[p]=i
    if p not in frames:
        faults+=1
        if len(frames)<f:
            frames.append(p)
        else:
            if algo=="fifo":
                frames.pop(0)
            elif algo=="lru":
                victim=min(frames,key=lambda x: recent[x])
                frames.remove(victim)
            elif algo=="optimal":
                future=pages[i+1:]
                victim=max(frames,key=lambda x: future.index(x) if x in future else 999)
                frames.remove(victim)
            frames.append(p)
    history.append(frames[:])
print(f"Page Faults: {faults}")
print(f"faults: {faults}")
print(f"hits: {n - faults}")

table=[]
for i in range(f):
    row=[]
    for h in history:
        row.append(h[i] if i<len(h) else None)
    table.append(row)

plt.figure(figsize=(10,5))
plt.axis('off')
plt.title(f"{algo.upper()} Page Replacement")
plt.table(cellText=table, colLabels=[f"Step {i+1}" for i in range(n)], rowLabels=[f"Frame {i+1}" for i in range(f)], loc='center')
plt.show()

