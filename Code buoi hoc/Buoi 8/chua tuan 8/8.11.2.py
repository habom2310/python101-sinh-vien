def khong_dq(n):
    F=[0,1,1,2]
    if n < 4:
        return F[n]
    else:
        for i in range(4,n+1):
            value = F[i-1] + F[i-2] + F[i-3]
            F.append(value)
        return F[n]

n= int(input("nhập n:"))

print(f"số Tribonacci thứ {n} là:",khong_dq(n))
