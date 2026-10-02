x=[[1,2,3],[4,5,6],[7,8,9]]

print("Original matrix before adding: ")
for m in x:
    print(m)

ax=0

for i in range(len(x)):
    for j in range(len(x[0])):
        ax=ax+x[j][i]
    print(ax, end=" ")
    ax=0
