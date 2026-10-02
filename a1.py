x=[[1,2,3],[4,5,6],[7,8,9]]
print("Original matrix before transposing: ")
for n in x:
    print(n)

tx=[[0,0,0],[0,0,0],[0,0,0]]
for i in range (len(x)):
    for j in range(len(x[0])):
        tx[i][j]=x[j][i]

print("Altered matrix after transposing: ")
for m in tx:
    print(m)