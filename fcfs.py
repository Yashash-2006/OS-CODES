import random
import matplotlib.pyplot as plt

# ---------- INPUT ----------
n = int(input("enter number of processes: "))
p = []

for i in range(n):
    at = random.randint(0, 10)
    bt = random.randint(1, 10)
    p.append([f'P{i+1}', at, bt])

p.sort(key=lambda x: x[1])  # sort by arrival time

time = 0
timeline = []
total_wt = 0
total_tat = 0

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
for i in range(n):
    pid, at, bt = p[i]
    if time < at:
        time = at
    ct = time + bt
    tat = ct - at
    wt = tat - bt

    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")

    total_wt += wt
    total_tat += tat
    
    timeline.append((pid, time, ct))
    time = ct

if n > 0:
    print(f"\nAverage Waiting Time: {total_wt / n:.2f}")
    print(f"Average Turnaround Time: {total_tat / n:.2f}")

fig, ax = plt.subplots()
for i in range(len(timeline)):
    pid, start, end = timeline[i]
    # Using numeric index 'i' maps perfectly to the range(len(timeline)) ticks 
    ax.barh(i, end - start, left=start, edgecolor='black')

ax.set_yticks(range(len(timeline)))
ax.set_yticklabels([t[0] for t in timeline])
ax.set_title("FCFS Scheduling Gantt Chart")
ax.set_xlabel("Time")
ax.set_ylabel("Processes")
plt.show()