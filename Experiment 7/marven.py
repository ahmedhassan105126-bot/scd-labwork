import subprocess
import sys
import os

print("=" * 70)
print("🧪 EXPERIMENT 7: BUILD TOOLS - COMPLETE DEMONSTRATION")
print("=" * 70)

# ==============================================================
# STEP 1: CREATE requirements.txt
# ==============================================================
print("\n" + "=" * 70)
print("📝 STEP 1: Creating requirements.txt")
print("=" * 70)

requirements_content = """# requirements.txt
# Project Dependencies

numpy==1.24.3
pandas==2.0.2
matplotlib==3.7.1
"""

with open('requirements.txt', 'w') as f:
    f.write(requirements_content)

print("✅ requirements.txt created")
print("\n📄 Content:")
print(requirements_content)

# ==============================================================
# STEP 2: CREATE setup.py
# ==============================================================
print("\n" + "=" * 70)
print("⚙️ STEP 2: Creating setup.py")
print("=" * 70)

setup_content = """from setuptools import setup

setup(
    name="calculator-project",
    version="1.0.0",
    author="Your Name",
    description="Calculator with build automation",
    install_requires=["numpy", "pandas", "matplotlib"],
    python_requires=">=3.8",
)
"""

with open('setup.py', 'w') as f:
    f.write(setup_content)

print("✅ setup.py created")
print("\n📋 Configuration:")
print("   Package: calculator-project v1.0.0")
print("   Dependencies: numpy, pandas, matplotlib")
print("   Python: >=3.8")

# ==============================================================
# STEP 3: INSTALL DEPENDENCIES
# ==============================================================
print("\n" + "=" * 70)
print("📦 STEP 3: Installing Dependencies")
print("=" * 70)

packages = ['numpy', 'pandas', 'matplotlib']
for package in packages:
    try:
        __import__(package)
        print(f"✅ {package} - Already installed")
    except ImportError:
        print(f"⏳ Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
        print(f"✅ {package} - Installed successfully")

# ==============================================================
# STEP 4: CALCULATOR APPLICATION
# ==============================================================
print("\n" + "=" * 70)
print("🔢 STEP 4: Calculator Application")
print("=" * 70)

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

class Calculator:
    """Professional Calculator with Dependencies"""
    
    def __init__(self):
        self.version = "1.0.0"
        self.history = []
        print(f"Calculator v{self.version} initialized")

    def add(self, a, b):
        result = a + b
        self.history.append({'operation': 'add', 'result': result})
        return result

    def subtract(self, a, b):
        result = a - b
        self.history.append({'operation': 'subtract', 'result': result})
        return result

    def multiply(self, a, b):
        result = a * b
        self.history.append({'operation': 'multiply', 'result': result})
        return result

    def divide(self, a, b):
        if b == 0: return "Error"
        result = a / b
        self.history.append({'operation': 'divide', 'result': result})
        return result

    def calculate_mean(self, data):
        return np.mean(data)

    def calculate_std(self, data):
        return np.std(data)

    def get_history_df(self):
        return pd.DataFrame(self.history)

    def plot_results(self):
        """Using Matplotlib dependency"""
        df = self.get_history_df()
        plt.figure(figsize=(10, 4))
        plt.plot(df.index, df['result'], marker='o', linewidth=2)
        plt.xlabel('Operation')
        plt.ylabel('Result')
        plt.title('Calculator Results')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        plt.show()

# ==============================================================
# STEP 5: TEST CALCULATOR
# ==============================================================
print("\n" + "=" * 70)
print("🧪 STEP 5: Testing Calculator")
print("=" * 70)

calc = Calculator()

print("\n📊 Basic Operations:")
print(f"➕ 10 + 5 = {calc.add(10, 5)}")
print(f"➖ 20 - 8 = {calc.subtract(20, 8)}")
print(f"✖️ 6 * 7 = {calc.multiply(6, 7)}")
print(f"➗ 100 / 4 = {calc.divide(100, 4)}")

print("\n📈 Advanced Operations (Using NumPy):")
numbers = [10, 20, 30, 40, 50]
print(f"Numbers: {numbers}")
print(f"Mean: {calc.calculate_mean(numbers):.2f}")
print(f"Std Dev: {calc.calculate_std(numbers):.2f}")

print("\n📅 History (Using Pandas):")
print(calc.get_history_df())

print("\n📈 Visualization (Using matplotlib):")
calc.plot_results()

# ==============================================================
# STEP 6: BUILD COMMANDS INFO
# ==============================================================
print("\n" + "=" * 70)
print("🛠️ STEP 6: Build Commands")
print("=" * 70)

print("\n📁 Files Created:")
for file in ['requirements.txt', 'setup.py']:
    if os.path.exists(file):
        print(f"   ✅ {file}")

print("\n🔨 Common Build Commands:")
print("   1. pip install -r requirements.txt  -> Install dependencies")
print("   2. pip install -e .                 -> Install in dev mode")
print("   3. python setup.py sdist            -> Create distribution")
print("   4. pip install .                    -> Install package")

print("\n" + "=" * 70)
print("✅ EXPERIMENT COMPLETE - SUMMARY")
print("=" * 70)