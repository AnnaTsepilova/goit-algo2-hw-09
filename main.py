import random
import math


# Функція Сфери для мінімізації
def sphere_function(x):
    return sum(xi ** 2 for xi in x)


# Алгоритм підйому на гору
def hill_climbing(func, bounds, iterations=1000, epsilon=1e-6):
    # Ініціалізація початкової точки випадковими значеннями в межах bounds
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        # Генерація сусідньої точки шляхом додавання випадкового зсуву
        neighbor = [current[i] + random.uniform(-0.1, 0.1) for i in range(len(bounds))]
        # Переконання, що сусідня точка знаходиться в межах bounds
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        neighbor_value = func(neighbor)

        # Перевірка умови зупинки, якщо зміна значення функції менша за epsilon
        if abs(current_value - neighbor_value) < epsilon:
            break

        # Оновлення поточної точки, якщо знайдено краще значення
        if neighbor_value < current_value:
            current, current_value = neighbor, neighbor_value

    return current, current_value


# Алгоритм випадкового локального пошуку
def random_local_search(func, bounds, iterations=1000, epsilon=1e-6):
    # Ініціалізація найкращої точки випадковими значеннями в межах bounds
    best = [random.uniform(b[0], b[1]) for b in bounds]
    best_value = func(best)

    for _ in range(iterations):
        # Генерація випадкової точки в межах bounds
        candidate = [random.uniform(b[0], b[1]) for b in bounds]
        candidate_value = func(candidate)

        # Перевірка умови зупинки, якщо зміна значення функції менша за epsilon
        if abs(best_value - candidate_value) < epsilon:
            break

        # Оновлення найкращої точки, якщо знайдено краще значення
        if candidate_value < best_value:
            best, best_value = candidate, candidate_value

    return best, best_value


# Алгоритм імітації відпалу
def simulated_annealing(func, bounds, iterations=1000, temp=1000, cooling_rate=0.95, epsilon=1e-6):
    # Ініціалізація початкової точки випадковими значеннями в межах bounds
    current = [random.uniform(b[0], b[1]) for b in bounds]
    current_value = func(current)

    for _ in range(iterations):
        # Зменшення температури
        temp *= cooling_rate
        # Перевірка умови зупинки, якщо температура менша за epsilon
        if temp < epsilon:
            break

        # Генерація сусідньої точки шляхом додавання випадкового зсуву
        neighbor = [current[i] + random.uniform(-0.1, 0.1) for i in range(len(bounds))]
        # Переконання, що сусідня точка знаходиться в межах bounds
        neighbor = [max(min(neighbor[i], bounds[i][1]), bounds[i][0]) for i in range(len(bounds))]
        neighbor_value = func(neighbor)

        # Прийняття сусідньої точки залежно від значення функції або випадковості, обумовленої температурою
        if neighbor_value < current_value or random.uniform(0, 1) < math.exp((current_value - neighbor_value) / temp):
            current, current_value = neighbor, neighbor_value

    return current, current_value


if __name__ == "__main__":
    # Межі змінних для функції
    bounds = [(-5, 5), (-5, 5)]

    # Виконання алгоритму підйому на гору
    print("Hill Climbing:")
    hc_solution, hc_value = hill_climbing(sphere_function, bounds)
    print("Розв'язок:", hc_solution, "Значення:", hc_value)

    # Виконання алгоритму випадкового локального пошуку
    print("\nRandom Local Search:")
    rls_solution, rls_value = random_local_search(sphere_function, bounds)
    print("Розв'язок:", rls_solution, "Значення:", rls_value)

    # Виконання алгоритму імітації відпалу
    print("\nSimulated Annealing:")
    sa_solution, sa_value = simulated_annealing(sphere_function, bounds)
    print("Розв'язок:", sa_solution, "Значення:", sa_value)
