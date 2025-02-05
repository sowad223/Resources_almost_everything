import numpy as np
import random

def Chromosome_Representation(p_size,c_length):
  population_list = []
  for i in range(p_size):
    chromosome = ""
    for j in range(c_length):
      chromosome+=random.choice(["0","1"])
    population_list.append(chromosome)
  return population_list

"""### Fitness function"""

def fitness(chromosome, N, T):
    Course_overlapping_penalty = 0
    Course_consistency_penalty = 0
    current_slot= 0
    c_count = [0] * N
    c_assigned = 0
    for i in range(len(chromosome)):
        if chromosome[i] == '1':
            c_assigned += 1
            c_count[current_slot] += 1
        if current_slot== N - 1:
            if c_assigned > 1:
                Course_overlapping_penalty += c_assigned - 1
            c_assigned = 0
            current_slot= 0
        else:
            current_slot+= 1
    for i in c_count:
        if i != 1:
            Course_consistency_penalty += abs(i - 1)
    fitness = -(Course_overlapping_penalty + Course_consistency_penalty)
    return fitness

"""### Random Selection function"""

def selection(population):
    return random.sample(population, 2)

"""### Crossover function"""

def crossover(chromosome_1, chromosome_2):
    point = random.randint(1, len(chromosome_1) - 1)
    offspring_1 = chromosome_1[:point] + chromosome_2[point:]
    offspring_2 = chromosome_2[:point] + chromosome_1[point:]
    return offspring_1, offspring_2

"""###Mutation function"""

def mutation(chromosome):
    m_points = random.sample(range(len(chromosome)), 2)
    chromosome = list(chromosome)
    for i in range(len(chromosome)):
        if i in m_points:
            if chromosome[i] == '0':
                chromosome[i] = '1'
            else:
                chromosome[i] = '0'
    chromosome = ''.join(chromosome)
    return chromosome

"""### Genetic Algorithm Function"""

def GA(N, T, p_size, maximum_generations):
    c_length = N * T
    population = Chromosome_Representation(p_size, c_length)

    for i in range(maximum_generations):
        fitness_list = []
        for i in population:
            fitness_list.append(fitness(i, N, T))

        if max(fitness_list) == 0:
            best_fitness = max(fitness_list)
            c_best = population[fitness_list.index(best_fitness)]
            return c_best, best_fitness, population

        current_population_list = []
        for i in range(p_size//2):
            chromosome_1, chromosome_2 = selection(population)
            offspring_1, offspring_2 = crossover(chromosome_1, chromosome_2)
            current_population_list.append(mutation(offspring_1))
            current_population_list.append(mutation(offspring_2))

        population = current_population_list

    fitness_list = []
    for i in population:
        fitness_list.append(fitness(i, N, T))

    best_fitness = max(fitness_list)
    c_best = population[fitness_list.index(best_fitness)]
    return c_best, best_fitness, population

"""Running the Genetic Algorithm function"""

f = open("24141255_Showrin_CSE422_06_Lab_Assignment01_InputFile_Summer2024.txt", "r")
N, T = map(int, f.readline().strip().split(" "))
p_size = 10
maximum_generations = 50000

best_schedule, best_fitness, population = GA(N, T, p_size, maximum_generations)
print(best_schedule)
print(best_fitness)

"""**Part 2**"""

def two_point_crossover(chromosome_1, chromosome_2):
  c_length = len(chromosome_1)

  if c_length == 3:
    point_1 = 0
    point_2 = 2
  else:
    point_1 = random.randint(1,c_length - 2)
    point_2 = random.randint(point_1 + 1,c_length - 1)

  offspring_1 = chromosome_1[:point_1] + chromosome_2[point_1:point_2] + chromosome_1[point_2:]
  offspring_2 = chromosome_2[:point_1] + chromosome_1[point_1:point_2] + chromosome_2[point_2:]

  return offspring_1,offspring_2,point_1,point_2

best_schedule, best_fitness, population = GA(N, T, p_size, 1)
chromosome_1, chromosome_2 = selection(population)
offspring_1, offspring_2, point_1, point2 = two_point_crossover(chromosome_1, chromosome_2)

print(f"Offspring 1 is  {offspring_1}")
print(f"Offspring 2 is {offspring_2}")
