import streamlit as st
import pulp

# Function to solve the maximization problem
def solve_maximization_problem(objective_coeffs, constraints):
    # Create the problem variable to contain the problem data
    prob = pulp.LpProblem("Maximization_Problem", pulp.LpMaximize)

    # Create decision variables
    vars = {f'x{i}': pulp.LpVariable(f'x{i}', lowBound=0) for i in range(1, len(objective_coeffs) + 1)}

    # Objective function: Maximize the objective
    prob += pulp.lpSum([vars[f'x{i}'] * coeff for i, coeff in enumerate(objective_coeffs, 1)])

    # Constraints
    for constraint in constraints:
        lhs = pulp.lpSum([vars[f'x{i}'] * coeff for i, coeff in enumerate(constraint['coeffs'], 1)])
        if constraint['type'] == '<=':
            prob += lhs <= constraint['rhs']
        elif constraint['type'] == '>=':
            prob += lhs >= constraint['rhs']
        elif constraint['type'] == '=':
            prob += lhs == constraint['rhs']

    # Solve the problem
    prob.solve()

    # Extract results
    result = {
        'Status': pulp.LpStatus[prob.status],
        'Variables': {v.name: v.varValue for v in prob.variables()},
        'Objective': pulp.value(prob.objective)
    }

    return result

# Streamlit UI
st.title("Maximization Problem Solver")

st.sidebar.header("Input Parameters")

# Input number of variables and constraints
num_vars = st.sidebar.number_input("Number of Variables", min_value=1, max_value=10, value=2)
num_constraints = st.sidebar.number_input("Number of Constraints", min_value=1, max_value=10, value=2)

st.header("Objective Function Coefficients")
objective_coeffs = []
for i in range(1, num_vars + 1):
    coeff = st.number_input(f"Coefficient of x{i}", value=1.0)
    objective_coeffs.append(coeff)

st.header("Constraints")
constraints = []
for j in range(1, num_constraints + 1):
    constraint = {}
    constraint['coeffs'] = [st.number_input(f"Coefficient of x{i} in constraint {j}", value=1.0) for i in range(1, num_vars + 1)]
    constraint['type'] = st.selectbox(f"Constraint {j} type", ('<=', '>=', '='), index=0)
    constraint['rhs'] = st.number_input(f"Right-hand side of constraint {j}", value=1.0)
    constraints.append(constraint)

if st.button("Solve"):
    result = solve_maximization_problem(objective_coeffs, constraints)
    
    st.subheader("Result")
    st.write(f"Status: {result['Status']}")
    st.write(f"Objective Value: {result['Objective']}")
    
    st.subheader("Variable Values")
    for var, value in result['Variables'].items():
        st.write(f"{var}: {value}")

# To run the app, use the command: streamlit run app.py
