n=int(input("no. of processes: "))
m=int(input("no. of resources: "))

total = list(map(int, input("Total resources: ").split()))

print("enter max matrix: ")
maxm=[list(map(int,input().split())) for _ in range(n)]

print("enter allocation matrix: ")
alloc=[list(map(int,input().split())) for _ in range(n)]

need=[[maxm[i][j]-alloc[i][j] for j in range(m)]for i in range(n)]

available = []

for j in range(m):
    s=sum(abs(alloc[i][j]) for i in range(n))
    available.append(total[j]-s)

print("\n Available:", available)
work=available[:]
finish=[False]*n
safe=[]
    
while len(safe)<n:
    found=False
    for i in range(n):
        if not finish[i] and all(need[i][j]<=work[j] for j in range(m)):
            for j in range(m):
                work[j]+=alloc[i][j]
            safe.append(f'P{i+1}')
            finish[i]=True
            found=True
            break
    if not found:
        break
    if len(safe)==n:
        print("\nSafe Sequence:", " -> ".join(safe))
    else:
        print("\nSystem is in unsafe state")
        break

