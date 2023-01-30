def future_tuition(tuition, rate, years):
    for i in range(years):
        tuition *= (1 + rate / 100)
    return tuition

tuition = 10000
rate = 5
years = 10
future_tuition = future_tuition(tuition, rate, years)
print(f"Tuition in {years} years: ${future_tuition:.2f}")

years = 4
total_cost = future_tuition(tuition, rate, years) * years
print(f"Total cost of {years} years' worth of tuition starting {years} years from now: ${total_cost:.2f}")