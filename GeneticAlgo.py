import random

population_size = 10
target_value = 255
max_generation = 25
generation = 0


def fitness_check(x):
    return abs(x**2 + 45 - target_value)


def initialize_population():
    return [random.uniform(0, 50) for _ in range(population_size)]


def mutate(x, mutation_rate=0.1):
    if random.random() < mutation_rate:
        return random.uniform(0, 50)
    return x


def crossover(parent1, parent2):
    return (parent1 + parent2) / 2


population = initialize_population()

while generation < max_generation:
    fitness_scores = [(fitness_check(num), num) for num in population]
    fitness_scores.sort()

    top_5 = fitness_scores[:5]

    if top_5[0][0] <= 5:
        print(
            f"Solution found in generation {generation} and the number is {top_5[0][1]}")
        break

    offspring = [mutate(crossover(random.choice(top_5)[1], random.choice(top_5)[
                        1])) for _ in range(population_size - 1)]

    offspring.append(top_5[0][1])

    population = offspring
    generation += 1
