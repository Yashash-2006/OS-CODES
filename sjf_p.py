### PREEMPTIVE SJF (SRTF) ###
import random
import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))
p = []

# Input (random AT & BT)
for i in range(n):
    at = random.randint(0, 5)
    bt = random.randint(1, 10)
    p.append([f'P{i+1}', at, bt, bt])  # last = remaining time
time = 0
completed = 0
timeline = []
current = None
start_time = 0
ct = {}
total_wt = total_tat = 0

while completed < n:
    idx = -1
    min_rt = 9999

    # Find process with minimum remaining time
    for i in range(n):
        pid, at, bt, rt = p[i]
        if at <= time and rt > 0:
            if rt < min_rt:
                min_rt = rt
                idx = i

    if idx == -1:
        time += 1
        continue

    pid, at, bt, rt = p[idx]

    # If process changes → store previous block
    if current != pid:
        if current is not None:
            timeline.append((current, start_time, time))
        current = pid
        start_time = time

    # Execute for 1 unit
    p[idx][3] -= 1
    time += 1

    # If completed
    if p[idx][3] == 0:
        ct[pid] = time
        completed += 1

    timeline.append((current, start_time, time))

if n > 0:
    print("\nPID\tAT\tBT\tCT\tTAT\tWT")
    for pid, at, bt, _ in p:
        completion = ct[pid]
        tat = completion - at
        wt = tat - bt
        total_tat += tat
        total_wt += wt
        print(pid, at, bt, completion, tat, wt, sep="\t")
        
    print(f"\nAvg WT: {total_wt/n:.2f}")
    print(f"Avg TAT: {total_tat/n:.2f}")

fig, ax = plt.subplots()
for i in range(len(timeline)):  
    pid, start, end = timeline[i]
    ax.barh(i, end-start, left=start, edgecolor='black')    
ax.set_yticks(range(len(timeline)))
ax.set_yticklabels([t[0] for t in timeline])    
ax.set_title("SJF Preemptive Scheduling Gantt Chart")
ax.set_xlabel("Time")
ax.set_ylabel("Processes")
plt.show()