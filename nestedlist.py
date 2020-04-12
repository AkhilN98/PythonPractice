n=int(input())
ar={}
val_ar=[]
for i in range(0,n):
    tmp_name=input()
    tmp_marks=float(input())
    ar[tmp_name]=tmp_marks
    val_ar.append(tmp_marks)
#print(ar)
#print(val_ar)

set_ar = set(val_ar)
#print(set_ar)
val_ar = list(set_ar)
val_ar.sort()
second_low = val_ar[1]
last_ar = []
for x in ar:
    if second_low == ar[x]:
        last_ar.append(x)

last_ar.sort()
for z in last_ar:
    print(z)