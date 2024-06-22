import statistics

ensino_fundamental = [1,8,9,10,3,5,8,8,9]

variancia = statistics.variance(ensino_fundamental)
print(f"Variância: {variancia:.2f}")

import statistics

ensino_medio = list(range(1,151))

variancia = statistics.variance(ensino_medio)
print(f"Variância: {variancia:.2f}")
