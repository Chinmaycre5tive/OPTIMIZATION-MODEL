from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

# Initialize the optimization model
model = LpProblem(name="product-mix-optimization", sense=LpMaximize)

# Define decision variables
x = LpVariable(name="Product_A", lowBound=0, cat="Continuous")
y = LpVariable(name="Product_B", lowBound=0, cat="Continuous")

# Add the objective function
model += 20 * x + 30 * y, "Total_Profit"

# Add constraints
model += (2 * x + 3 * y <= 100, "Labor_Constraint")
model += (x + y <= 40, "Material_Constraint")

# Solve the optimization problem
status = model.solve()

# Output results
print(f"Status: {model.status}, {LpStatus[model.status]}")
print(f"Optimal number of Product A to produce: {x.value()}")
print(f"Optimal number of Product B to produce: {y.value()}")
print(f"Maximum Profit: ${value(model.objective)}")
