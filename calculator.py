import streamlit as st

# -------------------------------
# 🎨 Page Configuration
# -------------------------------
st.set_page_config(page_title="Simple Calculator", page_icon="🧮", layout="centered")

# -------------------------------
# 💬 App Title and Description
# -------------------------------
st.title("🧮 Simple Streamlit Calculator")
st.markdown("A basic calculator built with **Streamlit** for addition, subtraction, multiplication, and division.")

# -------------------------------
# 🔢 User Inputs
# -------------------------------
st.header("Enter Numbers")
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number", value=0.0, step=1.0)

# -------------------------------
# ⚙️ Operation Selection
# -------------------------------
operation = st.radio(
    "Select Operation",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# -------------------------------
# 🧠 Calculation Logic
# -------------------------------
result = None

if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("❌ Cannot divide by zero!")

# -------------------------------
# 📊 Display Result
# -------------------------------
if result is not None:
    st.success(f"✅ The result of {operation.lower()} is: **{result}**")

# -------------------------------
# 👇 Footer
# -------------------------------
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit")
