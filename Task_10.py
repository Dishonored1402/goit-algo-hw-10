import pulp

problem = pulp.LpProblem("Maximize_Production", pulp.LpMaximize)

x1 = pulp.LpVariable("Lemonade", lowBound=0, cat='Continuous')
x2 = pulp.LpVariable("Juice", lowBound=0, cat='Continuous')

problem += x1 + x2, "Total_Production"

problem += 2 * x1 + x2 <= 100, "Water"
problem += x1 <= 50, "Sugar"
problem += x1 <= 30, "Lemon_Syrup"
problem += 2 * x2 <= 40, "Fruit_Puree"

problem.solve()

if pulp.LpStatus[problem.status] == 'Optimal':
    print(f"Максимальна кількість лимонаду, яку можна виготовити: {x1.varValue}")
    print(f"Максимальна кількість фруктового соку, яке можна виготовити: {x2.varValue}")
    print(f"Максимальна загальна кількість продуктів: {x1.varValue + x2.varValue}")
else:
    print("Неможливо знайти оптимальне рішення.")
