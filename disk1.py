import random
import matplotlib.pyplot as plt

def plot(order,title):
    plt.plot(order,marker='o')
    plt.title(title)
    plt.xlabel("Step")
    plt.ylabel("Cylinder")
    plt.show()

def fcfs(q, head):
    order=[head] + q[:]
    total=sum(abs(order[i+1]-order[i]) for i in range(len(order)-1))
    print("FCFS")
    print("Order of access:", order)
    print("Total head movement:", total)
    plot(order, "FCFS")

def sstf(q, head):
    req=q[:]
    curr=head
    order=[head]
    total=0
    while req:
        nearest = min(req, key=lambda x: abs(x-curr))
        total += abs(nearest-curr)
        curr = nearest
        order.append(curr)
        req.remove(nearest)
    print("SSTF")
    print("Order of access:", order)
    print("Total head movement:", total)
    plot(order, "SSTF")

def scan(q, head, direction):
    left=sorted([x for x in q if x<head])
    right=sorted([x for x in q if x>=head])
    order=[head]
    if direction=="left":
        order+=left[::-1]+right
    else:
        order+=right+left[::-1]
    total=sum(abs(order[i+1]-order[i])for i in range(len(order)-1))
    print("SCAN")
    print("Order of access:",order)
    print("Total head movement:",total)
    plot(order,"SCAN")  

n = int(input("Number of requests: "))
q = [random.randint(0, 199) for _ in range(n)]
head = random.randint(0, 199)
print("queue: ",q)
print("Initial head position: ",head)

ch=int(input("Choose algorithm (1/2/3): "))

if ch==1:
    fcfs(q,head)
elif ch==2:
    sstf(q,head)
elif ch==3:
    direction=input("Direction (left/right): ").lower()
    scan(q,head,direction)
else:
    print("Invalid choice!")

