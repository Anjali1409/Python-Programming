n=int(input())
f=[1,1]
for i in range(n):
    f.append(f[i-1]+f[i-2])
print(f)
