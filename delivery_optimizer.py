# delivery_optimizer.py
import math
import random
import copy
import tkinter as tk
from typing import List, Tuple

class Vehicle:
    def __init__(self, capacity):
        self.capacity = capacity
        self.packages = []

    def load_package(self, package):
        self.packages.append(package)

    def total_weight(self):
        return sum(p.weight for p in self.packages)

    def is_overloaded(self):
        return self.total_weight() > self.capacity


class Package:
    def __init__(self, x, y, weight, priority):
        self.x = x
        self.y = y
        self.weight = weight
        self.priority = priority

    def location(self):
        return (self.x, self.y)


def total_distance(vehicle: Vehicle):
    dist = 0
    last = (0, 0)
    for p in vehicle.packages:
        dist += euclidean_distance(last, p.location())
        last = p.location()
    dist += euclidean_distance(last, (0, 0))
    return dist

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)



def overall_cost(vehicles: List[Vehicle]):
    return sum(total_distance(v) for v in vehicles)

def genetic_algorithm(packages, num_vehicles, capacity, generations=500, pop_size=50, mutation_rate=0.05):
    packages = sorted(packages, key=lambda p: p.priority)  # Priority sorting
    population = initialize_population(packages, num_vehicles, capacity, pop_size)
    for _ in range(generations):
        population.sort(key=overall_cost)
        new_population = population[:10]  # elite

        while len(new_population) < pop_size:
            parent = copy.deepcopy(random.choice(population[:20]))
            if random.random() < mutation_rate:
                mutate(parent)
            if not any(v.is_overloaded() for v in parent):
                new_population.append(parent)

        population = new_population
    return population[0]

def simulated_annealing(packages, num_vehicles, capacity, init_temp=1000, cooling_rate=0.95):
    vehicles = [Vehicle(capacity) for _ in range(num_vehicles)]
    packages = sorted(packages, key=lambda p: p.priority)  # Priority sorting

    i = 0
    for p in packages:
        vehicles[i % num_vehicles].load_package(p)
        i += 1

    current_solution = copy.deepcopy(vehicles)
    best_solution = copy.deepcopy(vehicles)
    temp = init_temp

    while temp > 1:
        for _ in range(100):
            new_solution = copy.deepcopy(current_solution)
            v1, v2 = random.sample(new_solution, 2)
            if not v1.packages or not v2.packages:
                continue
            i = random.randint(0, len(v1.packages) - 1)
            j = random.randint(0, len(v2.packages) - 1)
            v1.packages[i], v2.packages[j] = v2.packages[j], v1.packages[i]

            if any(v.is_overloaded() for v in new_solution):
                continue

            cost_diff = overall_cost(new_solution) - overall_cost(current_solution)
            if cost_diff < 0 or random.random() < math.exp(-cost_diff / temp):
                current_solution = new_solution
                if overall_cost(current_solution) < overall_cost(best_solution):
                    best_solution = current_solution

        temp *= cooling_rate

    return best_solution

def initialize_population(packages, num_vehicles, capacity, population_size):
    population = []
    for _ in range(population_size):
        random.shuffle(packages)
        vehicles = [Vehicle(capacity) for _ in range(num_vehicles)]
        i = 0
        for p in packages:
            vehicles[i % num_vehicles].load_package(p)
            i += 1
        population.append(vehicles)
    return population

def mutate(solution):
    v1, v2 = random.sample(solution, 2)
    if v1.packages and v2.packages:
        i = random.randint(0, len(v1.packages) - 1)
        j = random.randint(0, len(v2.packages) - 1)
        v1.packages[i], v2.packages[j] = v2.packages[j], v1.packages[i]




def load_from_file(filename: str):
    packages = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        if not lines:
            raise ValueError("Input file is empty")

        
        num_vehicles, capacity = map(int, lines[0].strip().split())

  
        for line in lines[1:]:
            if not line.strip():
                continue
            x, y, weight, priority = map(float, line.strip().split())
            weight = float(weight)
            priority = int(priority)
            if weight <= capacity:
                packages.append(Package(x, y, weight, priority))
            else:
                print(f"Skipping package at ({x}, {y}) — weight exceeds capacity.")
    return num_vehicles, int(capacity), packages


car_positions = []

def run():
    filename = "test.txt"
    algo = input("Choose algorithm (1 = Simulated Annealing, 2 = Genetic Algorithm): ").strip()

    num_vehicles, capacity, packages = load_from_file(filename)

    if algo == '1':
        solution = simulated_annealing(packages, num_vehicles, capacity)
    else:
        solution = genetic_algorithm(packages, num_vehicles, capacity)

    for i, v in enumerate(solution):
        print(f"\nVehicle {i+1} (Total Weight: {v.total_weight():.2f} kg, Distance: {total_distance(v):.2f} km):")
        for p in v.packages:
            print(f"  - Dest: ({p.x},{p.y}) | Weight: {p.weight}kg | Priority: {p.priority}")
            #print(f"{p.x},{p.y}")
            car_positions.append((p.x,p.y))

    draw_cars(car_positions)
   
    root.mainloop()  

   
            
           ##################GUI PART#################
SCALE = 6  

def draw_cars(car_positions):
    canvas.delete("all")  
    for x, y in car_positions:
        draw_car(x, y)

def draw_car(x, y):
    x *= SCALE
    y *= SCALE
    car_width = 10
    car_height = 20
    canvas.create_rectangle(x, y, x + car_width, y + car_height, fill='blue')
    canvas.create_text(x + car_width / 2, y - 10, text=f"({x:.1f}, {y:.1f})", font=("Arial", 9))
 
root = tk.Tk()
root.title("Car Position Viewer")
canvas_width = 1000
canvas_height = 900
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="Black")
canvas.pack(padx=10, pady=10)



if __name__ == '__main__':
    run()