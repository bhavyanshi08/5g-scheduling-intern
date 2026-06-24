print("Program started")
import random

ues = int(input("Enter number of UEs: "))
rbs = int(input("Enter number of Resource Blocks (RBs): "))
slots = int(input("Enter number of Time Slots: "))

allocation = []
avg_throughput = [1.0] * ues
ue_allocations = [0] * ues

for i in range(slots):
    row = []

    for j in range(rbs):
        current_throughput = [random.randint(1, 20) for _ in range(ues)]

        pf_metric = []

        for k in range(ues):
            pf_metric.append(current_throughput[k] / avg_throughput[k])

        selected_ue = pf_metric.index(max(pf_metric))

        row.append(selected_ue)
        ue_allocations[selected_ue] += 1

        avg_throughput[selected_ue] = (
            0.9 * avg_throughput[selected_ue]
            + 0.1 * current_throughput[selected_ue]
        )

    allocation.append(row)

print("\nProportional Fair Allocation Matrix:\n")

for idx, r in enumerate(allocation[:10]):
    print(f"Slot {idx + 1}: {r}")

print("\nValidation:")
print("Total Slots =", len(allocation))
print("RBs per Slot =", len(allocation[0]))
print("UE IDs Range = 0 to", ues - 1)

print("\nUE Allocation Counts:")

for i in range(ues):
    print(f"UE {i}: {ue_allocations[i]}")

print("\nFinal Average Throughputs:")

for i in range(ues):
    print(f"UE {i}: {avg_throughput[i]:.2f}")
