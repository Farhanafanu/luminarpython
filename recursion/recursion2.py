def rec_fibnoci(n):
    if n<=1:
        return n
    else:
        return rec_fibnoci(n-1)+rec_fibnoci(n-2)
nturms=10
print("fibinoci sequence")
for i in range(nturms):
    print(rec_fibnoci(i))