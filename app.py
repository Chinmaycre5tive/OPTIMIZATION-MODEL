import streamlit as st
from pulp import LpMaximize, LpProblem, LpVariable, value, LpStatus

st.title("Product Mix Optimizer")

labor = st.number_input("Enter available labor hours", value=100.0)
material = st.number_input("Enter available raw materials", value=40.0)

if st.button("Solve"):
    model = LpProblem("product-mix", LpMaximize)
    x = LpVariable("Product_A", lowBound=0)
    y = LpVariable("Product_B", lowBound=0)

    model += 20 * x + 30 * y
    model += 2 * x + 3 * y <= labor
    model += x + y <= material

    model.solve()

    st.success(f"Status: {LpStatus[model.status]}")
    st.write(f"Product A: {x.value()}")
    st.write(f"Product B: {y.value()}")
    st.write(f"Maximum Profit: ${value(model.objective)}")
