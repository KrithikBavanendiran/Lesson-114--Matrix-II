x=[]
row=int(input("Enter the number for rows and columns: "))

for i in range(row):
    r=[]
    for j in range(row):
        no=int(input(f"Enter the value for {[i],[j]}: "))
        r.append(no)
    x.append(r)

print(f"The {row}x{row} matrix is: ")
for n in x:
    print(n)

ax=0

for i in range(len(x)):
    for j in range(len(x[0])):
        ax=ax+x[j][i]
    print(ax, end=" ")
    ax=0