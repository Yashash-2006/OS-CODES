import random
import matplotlib.pyplot as plt

def plot(order,title):
    plt.plot(order,marker='o')
    plt.title(title)
    plt.xlabel("Step")
    plt.ylabel("Cylinder")
    plt.show()

def cscan(q, head, max_cyl):
    left=sorted([x for x in q if x<head])
    right=sorted([x for x in q if x>=head])
    order=[head] + right + [max_cyl] + [0] + left
    total=sum(abs(order[i+1]-order[i]) for i in range(len(order)-1))
    print("C-SCAN")
    print("Order of access:", order)
    print("Total head movement:", total)
    plot(order, "C-SCAN")

def look(q, head, direction):
    left=sorted([x for x in q if x<head])
    right=sorted([x for x in q if x>=head])
    order=[head]
    if direction=="left":
        order+=left[::-1]+right
    else:
        order+=right+left[::-1]
    total=sum(abs(order[i+1]-order[i]) for i in range(len(order)-1))
    print("LOOK")
    print("Order of access:", order)
    print("Total head movement:", total)
    plot(order, "LOOK")

def clook(q, head, direction):
    left=sorted([x for x in q if x<head])
    right=sorted([x for x in q if x>=head])
    order=[head]+right+left
    total=sum(abs(order[i+1]-order[i]) for i in range(len(order)-1))
    print("C-LOOK")
    print("Order of access:", order)
    print("Total head movement:", total)
    plot(order, "C-LOOK")
n = int(input("Number of requests: "))
q = [random.randint(0, 199) for _ in range(n)]
head = random.randint(0, 199)
print("queue: ",q)
print("Initial head position: ",head)

ch=int(input("Choose algorithm (1/2/3): "))

if ch==1:
    cscan(q,head,max_cyl=199)
elif ch==2:
    direction=input("Direction (left/right): ").lower()
    look(q,head,direction)
elif ch==3:
    direction=input("Direction (left/right): ").lower()
    clook(q,head,direction)
else:
    print("Invalid choice!")

