import random
import matplotlib.pyplot as plt

n = int(input("Enter number of processes: "))
p = []

for i in range(n):
    at = random.randint(0, 5)
    bt = random.randint(1, 10)
    pr = random.randint(1, 5)  # priority
    p.append([f'P{i+1}', at, bt, pr, bt])  # last = remaining time

time = 0
timeline = []   
total_wt = 0
total_tat = 0
completed = 0
start_time = 0
current = None
ct = {}

while completed < n:
    idx = -1
    best_pr = 9999
    for i in range(n):
        pid, at, bt, pr, rt = p[i]
        # Need to ensure the process hasn't finished yet (rt > 0)
        if at <= time and pr < best_pr and rt > 0:
            best_pr = pr
            idx = i
            
    if idx == -1:
        if current is not None:
            timeline.append((current, start_time, time))
            current = None
        time += 1
        continue
    pid, at, bt, pr, rt = p[idx]    

    # If process changes → store previous block
    if current != pid:
        if current is not None:
            timeline.append((current, start_time, time))
        current = pid
        start_time = time
        
    # Execute for 1 unit
    p[idx][4] -= 1
    time += 1
    
    # If completed
    if p[idx][4] == 0:
        ct[pid] = time
        completed += 1
        
# Add last process to timeline
if current is not None:
    timeline.append((current, start_time, time))

if n > 0:
    print("\nPID\tAT\tBT\tPR\tCT\tTAT\tWT")
    for pid, at, bt, pr, _ in p:
        completion = ct[pid]
        tat = completion - at
        wt = tat - bt
        print(f"{pid}\t{at}\t{bt}\t{pr}\t{completion}\t{tat}\t{wt}")
        total_wt += wt
        total_tat += tat
    print(f"\nAverage Waiting Time: {total_wt/n:.2f}")
    print(f"Average Turnaround Time: {total_tat/n:.2f}")

fig, ax = plt.subplots()
for i in range(len(timeline)):
    pid, start, end = timeline[i]       
    ax.barh(i, end-start, left=start, edgecolor='black')    
ax.set_yticks(range(len(timeline)))
ax.set_yticklabels([t[0] for t in timeline])    
ax.set_title("Priority Preemptive Scheduling Gantt Chart")
ax.set_xlabel("Time")
ax.set_ylabel("Processes")
plt.show()