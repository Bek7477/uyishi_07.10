def bir_xil_ishora_qoshni(lst):
    for i in range(len(lst) - 1):
        if lst[i] * lst[i + 1] > 0:  
            print(lst[i], lst[i + 1])
            
lst = []
n = int(input("list uzunligini kiriting: "))
for i in range(n):
    qiymat = int(input(">>> "))
    lst.append(qiymat)

bir_xil_ishora_qoshni(lst)

