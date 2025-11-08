import streamlit as st
import math

# -------------------------------
# 🎨 Page Configuration
# -------------------------------
st.set_page_config(page_title="Scientific Calculator", page_icon="🧮", layout="centered")

# -------------------------------
# 💬 App Title and Description
# -------------------------------
st.title("🧮 Scientific Calculator")
st.markdown("A powerful and user-friendly **Scientific Calculator** built with Streamlit.")

# -------------------------------
# 🔢 Input Section
# -------------------------------
st.header("Enter Numbers")
num1 = st.number_input("Enter first number", value=0.0, step=1.0)
num2 = st.number_input("Enter second number (if required)", value=0.0, step=1.0)

# -------------------------------
# ⚙️ Operation Selection
# -------------------------------
st.header("Select Operation")

operation = st.selectbox(
    "Choose an operation",
    (
        "Addition",
        "Subtraction",
        "Multiplication",
        "Division",
        "Power (x^y)",
        "Square Root",
        "Logarithm (log base 10)",
        "Exponential (e^x)",
        "Sine (sin x)",
        "Cosine (cos x)",
        "Tangent (tan x)",
        "Factorial"
    )
)

# -------------------------------
# 🧮 Perform Calculation
# -------------------------------
result = None

if st.button("Calculate"):
    try:
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
        elif operation == "Power (x^y)":
            result = math.pow(num1, num2)
        elif operation == "Square Root":
            if num1 >= 0:
                result = math.sqrt(num1)
            else:
                st.error("❌ Square root of negative number is not defined.")
        elif operation == "Logarithm (log base 10)":
            if num1 > 0:
                result = math.log10(num1)
            else:
                st.error("❌ Logarithm only defined for positive numbers.")
        elif operation == "Exponential (e^x)":
            result = math.exp(num1)
        elif operation == "Sine (sin x)":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine (cos x)":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent (tan x)":
            result = math.tan(math.radians(num1))
        elif operation == "Factorial":
            if num1 >= 0 and float(num1).is_integer():
                result = math.factorial(int(num1))
            else:
                st.error("❌ Factorial only defined for non-negative integers.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# -------------------------------
# 📊 Display Result
# -------------------------------
if result is not None:
    st.success(f"✅ Result of {operation}: **{result}**")

# -------------------------------
# 👇 Footer
# -------------------------------
st.markdown("---")
st.caption("Developed with ❤️ using Streamlit | Scientific Calculator")
