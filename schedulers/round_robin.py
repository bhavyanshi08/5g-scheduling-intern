ues = int(input("Enter number of UEs: "))
rbs = int(input("Enter number of Resource Blocks (RBs): "))
slots = int(input("Enter number of Time Slots: "))
allocation = []
for i in range(slots):
    row = []
    for j in range(rbs):
        ue = (i + j) % ues
        row.append(ue)
    allocation.append(row)
print("\nRound Robin Allocation Matrix:\n")
for idx, r in enumerate(allocation):
    print(f"Slot {idx + 1}: {r}")
