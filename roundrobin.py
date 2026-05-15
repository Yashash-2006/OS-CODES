import random
import matplotlib.pyplot as plt
from collections import deque

n = int(input("Enter number of processes: "))
tq = int(input("Enter Time Quantum: "))
p = []

# Input (random AT & BT)
for i in range(n):
    at = random.randint(0, 5)
    bt = random.randint(1, 10)
    p.append([f'P{i+1}', at, bt, bt])  # last = remaining time
# Sort by Arrival Time
p.sort(key=lambda x: x[1])

time = 0
queue = deque()
i = 0
timeline = []
ct = {}
total_wt = total_tat = 0

while True:
    # Add arrived processes to queue
    while i < n and p[i][1] <= time:
        queue.append(i)
        i += 1

    if not queue:
        if i < n:
            time = p[i][1]
            continue
        else:
            break

    idx = queue.popleft()
    pid, at, bt, rt = p[idx]

    start = time

    # Execute for time quantum or remaining time
    if rt > tq:
        time += tq
        p[idx][3] -= tq
    else:
        time += rt
        p[idx][3] = 0
        ct[pid] = time

    timeline.append((pid, start, time))
    # Add newly arrived processes during execution
    while i < n and p[i][1] <= time:
        queue.append(i)
        i += 1

    # If not completed → push back to queue
    if p[idx][3] > 0:
        queue.append(idx)

# Output
print("\nPID\tAT\tBT\tCT\tTAT\tWT")

for pid, at, bt, _ in p:
    completion = ct[pid]
    tat = completion - at
    wt = tat - bt
    total_tat += tat
    total_wt += wt
    print(pid, at, bt, completion, tat, wt, sep="\t")
print("\nAvg WT:", total_wt/n)
print("Avg TAT:", total_tat/n)

fig, ax = plt.subplots()
for i in range(len(timeline)):
    pid, start, end = timeline[i]       
    ax.barh(i, end-start, left=start, edgecolor='black')    
ax.set_yticks(range(len(timeline)))
ax.set_yticklabels([t[0] for t in timeline])    
ax.set_title("Round Robin Scheduling Gantt Chart")      
ax.set_xlabel("Time")
ax.set_ylabel("Processes")
plt.show()

