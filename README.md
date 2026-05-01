# 🚚 Optimization Strategies for Local Package Delivery Operations

> **ENCS3340 – Artificial Intelligence | Project #1** | Faculty of Engineering & Technology, Electrical & Computer Engineering Department  
> **Birzeit University**

---

## 👥 Authors

| Name | Student ID |
|------|-----------|
| Yousef Shanti | 1221137 |

**Instructors:** Dr. Yazan Abu Farha & Dr. Samah Alaydi  
**Submission Date:** May 04, 2025

---

## 📌 Overview

This project applies two **metaheuristic optimization algorithms** to solve the **Vehicle Routing Problem (VRP)** with capacity constraints and prioritized packages:

- 🌡️ **Simulated Annealing (SA)**
- 🧬 **Genetic Algorithm (GA)**

The goal is to minimize total delivery distance while respecting vehicle weight limits and ensuring high-priority packages are handled first.

---

## 📐 Problem Formulation

### Objectives
- ✅ No vehicle exceeds its weight capacity
- ✅ Total distance traveled by all vehicles is minimized
- ✅ High-priority packages are considered first

### Package Definition
Each package is defined by:
- A **destination** (2D coordinate)
- A **weight** in kilograms
- A **priority** (1 = highest, 5 = lowest)

### Vehicle Definition
Each vehicle:
- Has a **fixed weight capacity**
- Starts and ends at the **origin (0, 0)**
- Cost = total **Euclidean distance** from origin → deliveries → origin

---

## ⚙️ Algorithms

### 🌡️ Simulated Annealing (SA)

Inspired by the metallurgical annealing process — starts with high "temperature" for broad exploration, then cools to converge on an optimal solution.

| Component | Detail |
|-----------|--------|
| Initial Solution | Round-robin assignment of packages across vehicles |
| Neighbor Generation | Swap two packages between two random vehicles |
| Acceptance | Worse solutions accepted with decreasing probability as temperature drops |

### 🧬 Genetic Algorithm (GA)

Mimics biological evolution through selection, mutation, and reproduction over generations.

| Component | Detail |
|-----------|--------|
| Initialization | Random shuffling with round-robin assignment |
| Selection | Elitism — top-performing solutions carried forward |
| Mutation | Swapping packages between vehicles |
| Reproduction | Cloning elite or top-ranking individuals |

---

## 🛡️ Constraint Handling

### Vehicle Capacity
Packages exceeding the maximum vehicle capacity are **excluded** and the user is notified.

### Priority Handling
All packages are **sorted by priority (ascending)** before assignment — ensures priority-1 packages are assigned first.

### Overload Prevention
After every mutation or neighbor generation, a **validity check** ensures no vehicle is overloaded. Invalid solutions are discarded.

---

## 🔧 Parameter Tuning

### Simulated Annealing

| Parameter | Value | Notes |
|-----------|-------|-------|
| Initial Temperature | 1000 | High value allows broad early exploration |
| Cooling Rate | 0.95 | Lower (0.90) = faster but suboptimal; Higher (0.98) = better quality but slower |

### Genetic Algorithm

| Parameter | Value | Notes |
|-----------|-------|-------|
| Population Size | 50 | Balances diversity and computation time |
| Mutation Rate | 0.05 | Lower = stagnation; Higher = disrupts good solutions |
| Elite Retention | Top 10 | Preserves best candidates each generation |

---

## 🧪 Test Cases & Observations

### Test Case 1: Feasibility Check
- **Input:** 3 vehicles, capacity 100kg, 10 packages
- **Algorithm:** Simulated Annealing
- **Result:** All packages assigned within capacity; routes visualized per vehicle
- <img width="626" height="479" alt="Screenshot 2026-05-01 at 5 52 43 PM" src="https://github.com/user-attachments/assets/5afcbb94-38b1-4ef9-8af5-b288809860e3" />


### Test Case 2: Priority Biasing
- **Input:** 2 vehicles, some packages marked as priority 1
- **Algorithm:** Genetic Algorithm
- **Result:** Priority-1 packages correctly assigned before lower-priority ones

### Test Case 3: Overcapacity Packages
- **Input:** One package with 150kg weight, vehicle capacity 100kg
- **Result:** Package skipped with message `"Skipping package — weight exceeds capacity"`; remaining packages routed normally

### Test Case 4: SA vs GA Scalability
- **Observation:** SA produced shorter total distances for **small datasets**; GA scaled better for **large inputs** due to population diversity

---

## 📊 Algorithm Comparison

| Criteria | Simulated Annealing | Genetic Algorithm |
|----------|--------------------|--------------------|
| Best for | Small datasets | Large datasets |
| Implementation | Simpler, more intuitive | More flexible, scalable |
| Convergence | Faster for small inputs | Better coverage for large inputs |
| Diversity | Single solution path | Population-based diversity |

---

## 📝 Conclusion

Both SA and GA provide viable solutions to the VRP with capacity and priority constraints.

> **SA** is simpler and often more intuitive, while **GA** offers more flexibility and scalability for large datasets. Prioritizing high-importance packages and enforcing strict capacity checks ensured the reliability and practical relevance of the system.

---

## 🛠️ Tech Stack

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-green)
![NumPy](https://img.shields.io/badge/NumPy-Computation-lightblue?logo=numpy)

---

*Faculty of Engineering & Technology – Birzeit University*
