def tuition_cost(tuition, rate, years):
    for i in range(years):
        tuition *= 1 + rate
    return tuition

def total_cost(tuition, rate, years, duration):
    future_tuition = tuition_cost(tuition, rate, years)
    total = 0
    for i in range(duration):
        total += future_tuition
        future_tuition *= 1 + rate
    return total

tuition = 10000
rate = 0.05
years = 10
duration = 4

future_tuition = tuition_cost(tuition, rate, years)
print("Tuition in", years, "years: $", future_tuition)

total = total_cost(tuition, rate, years, duration)
print("Total cost of", duration, "years worth of tuition starting", years, "years from now: $", total)
