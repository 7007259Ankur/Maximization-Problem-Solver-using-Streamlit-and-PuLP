### Example Inputs

#### Objective Function

Maximize \( Z = 3x1 + 5x2 \)

#### Constraints

1. \( 2x1 + 3x2 <= 12 \)
2. \( 4x1 + x2 <= 8 \)

### Corresponding Inputs in the Streamlit App

1. **Number of Variables**: 2
2. **Number of Constraints**: 2

#### Objective Function Coefficients:

- Coefficient of \( x1 \): 3
- Coefficient of \( x2 \): 5

#### Constraints:

- **Constraint 1**:
  - Coefficient of \( x1 \) in constraint 1: 2
  - Coefficient of \( x2 \) in constraint 1: 3
  - Constraint 1 type: \( \<=\)
  - Right-hand side of constraint 1: 12
- **Constraint 2**:
  - Coefficient of \( x1 \) in constraint 2: 4
  - Coefficient of \( x2 \) in constraint 2: 1
  - Constraint 2 type: \( <=\)
  - Right-hand side of constraint 2: 8

### Running the Solver

Click the "Solve" button in the Streamlit app.

### Expected Output

The solver will process these inputs and provide the following output:

- **Status**: Optimal
- **Objective Value**: 13.0

#### Variable Values:

- \( x1 \): 1.0
- \( x2 \): 3.0

### Explanation of Output

- The optimal value of the objective function \( Z = 3x1 + 5x2 \) is 13.0.
- The optimal values of the variables are \( x1 = 1.0 \) and \( x2 = 3.0 \), meaning this combination maximizes the objective function under the given constraints.

Here is the complete process:

1. The **objective function** is defined as \( 3x1 + 5x2 \).
2. The **constraints** are \( 2x1 + 3x2 <= 12 \) and \( 4x1 + x2 <= 8 \).
3. By solving this Linear Programming Problem using the PuLP library, the optimal solution is found to be \( x1 = 1.0 \) and \( x2 = 3.0 \).
4. Substituting these values into the objective function gives \( Z = 3(1) + 5(3) = 3 + 15 = 18 \).

When you run the Streamlit app with these inputs, it will output the optimal solution and the maximum value of the objective function as described.
