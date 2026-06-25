# 📊 Week-5: Multi-Load Scheduler Evaluation

## 🎯 Objective

Evaluate the performance of Deep Reinforcement Learning (DQN) against traditional scheduling algorithms under different network load conditions.

### Scenarios Tested

* 🔹 5 UEs (Low Load)
* 🔹 15 UEs (Medium Load)
* 🔹 30 UEs (High Load)

### Performance Metrics

* 📈 Throughput
* ⏱️ Latency
* ⚖️ Jain's Fairness Index

---

## 🏆 DQN Results

| Scenario | Throughput |  Latency | Fairness |
| -------- | ---------: | -------: | -------: |
| 5 UEs    |   16950.00 | 56400.00 |   0.2000 |
| 15 UEs   |   16630.00 | 67140.00 |   0.0667 |
| 30 UEs   |   18370.00 | 63080.00 |   0.0333 |

---

## 🔄 Round Robin (RR) Results

| Scenario | Throughput | Latency | Fairness |
| -------- | ---------: | ------: | -------: |
| 5 UEs    |     259.67 |  543.69 |   0.7799 |
| 15 UEs   |     754.09 | 1517.71 |   0.7591 |
| 30 UEs   |    1511.66 | 2999.18 |   0.7579 |

---

## ⚖️ Proportional Fair (PF) Results

| Scenario | Throughput | Latency | Fairness |
| -------- | ---------: | ------: | -------: |
| 5 UEs    |     104.02 |  182.95 |   0.6615 |
| 15 UEs   |     194.27 |  305.74 |   0.5513 |
| 30 UEs   |     308.55 |  470.55 |   0.4430 |

---

## 📌 Key Observations

✅ DQN maintained the highest throughput across all load scenarios.

✅ Round Robin consistently achieved the highest fairness.

✅ Proportional Fair provided a balance between throughput and fairness.

✅ Increasing network load reduced fairness for DQN while RR remained stable.

---

