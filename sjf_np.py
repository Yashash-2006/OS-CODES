import random 
import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))
p = []

for i in range(n):
    at = random.randint(0, 10)
    bt = random.randint(1, 10)
    p.append([f'P{i+1}', at, bt])

time=0
timeline = []
total_wt = 0    
total_tat = 0
completed=0
visited = [False]*n

print("\nPID\tAT\tBT\tCT\tTAT\tWT")
while completed < n:
    idx=-1
    min_bt=9999
    for i in range(n):
        if not visited[i] and p[i][1]<=time:
            if p[i][2]<min_bt:
                min_bt=p[i][2]
                idx=i

    if idx==-1:
        time+=1     
        continue

    pid, at, bt = p[idx]
    ct = time + bt
    tat = ct - at
    wt = tat - bt
    print(f"{pid}\t{at}\t{bt}\t{ct}\t{tat}\t{wt}")
    total_wt += wt
    total_tat += tat    
    timeline.append((pid, time, ct))
    time = ct
    visited[idx] = True
    completed += 1

print(f"\nAverage Waiting Time: {total_wt/n:.2f}")
print(f"Average Turnaround Time: {total_tat/n:.2f}")

fig, ax = plt.subplots()
for i in range(len(timeline)):
    pid, start, end = timeline[i]
    ax.barh(i, end-start, left=start, edgecolor='black')
ax.set_yticks(range(len(timeline)))
ax.set_yticklabels([t[0] for t in timeline])    
ax.set_title("SJF Non-Preemptive Scheduling Gantt Chart")

plt.show()