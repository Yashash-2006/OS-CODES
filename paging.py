import math

def bits(x):
    b=0
    while(1<<b)<x:
        b+=1
    return b

ps=int(input("Process Size: "))
pg=int(input("Page Size: "))
nf=int(input("No. of Frames: "))

np = math.ceil(ps/pg)
print(f"Number of Pages: {np}")
if np > nf:
    print("Not enough frames for all pages!")
    exit()

pt=[]
print("Enter page table: ")
for i in range(np):
    pt.append(int(input(f"Page {i+1}: ")))

    offset_bits=bits(pg)
    page_bits=bits(np)
    frame_bits=bits(nf)

print("Logical -> Physical Address")
for la in range(ps):
    page=la//pg
    offset=la%pg
    frame=pt[page]
    pa=frame*pg+offset
    print(f"LA:{la}->Page:{page},Offset:{offset}->Frame:{frame},PA:{pa}")