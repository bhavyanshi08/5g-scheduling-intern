ues=5
rbs=10
slots=100
allocation=[]
for i in range(slots):
    row=[]
    for j in range(rbs):
        ue=j%ues
        row.append(ue)
    allocation.append(row)
for r in allocation:
    print(r)