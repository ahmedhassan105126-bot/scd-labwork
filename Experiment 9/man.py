import subprocess
import sys
import os
import logging
from datetime import datetime
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Ellipse, Rectangle

# =============================================================================
# PHASE 1: EXPERIMENT 7 - BUILD TOOLS & DEPENDENCY MANAGEMENT
# =============================================================================
def setup_build_environment():
    print("=" * 70)
    print("🛠️  PHASE 1: BUILD TOOLS & AUTOMATION")
    print("=" * 70)

    # 1. Create requirements.txt (Dependency Management)
    requirements_content = """# Project Dependencies
numpy==1.24.3
pandas==2.0.2
matplotlib==3.7.1
"""
    with open('requirements.txt', 'w') as f:
        f.write(requirements_content)
    print("✅ requirements.txt created")

    # 2. Create setup.py (Project Configuration)
    setup_content = """from setuptools import setup
setup(
    name="library-management-system",
    version="1.0.0",
    author="University Student",
    description="LMS with automated build and UML design",
    install_requires=["numpy", "pandas", "matplotlib"],
    python_requires=">=3.8",
)"""
    with open('setup.py', 'w') as f:
        f.write(setup_content)
    print("✅ setup.py created")

    # 3. Install Dependencies (Environment Consistency)
    packages = ['numpy', 'pandas', 'matplotlib']
    for package in packages:
        try:
            __import__(package)
            print(f"✅ {package} - Already installed")
        except ImportError:
            print(f"⏳ Installing {package}...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", package, "--quiet"])
    print("✅ Environment consistent across machines\n")

# =============================================================================
# PHASE 2: EXPERIMENT 9 - UML DIAGRAM GENERATOR (LMS)
# =============================================================================
def generate_uml_diagrams():
    print("=" * 70)
    print("🎨 PHASE 2: UML DIAGRAM DESIGN")
    print("=" * 70)

    output_dir = "uml_diagrams"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # --- 1. CLASS DIAGRAM ---
    fig1, ax1 = plt.subplots(figsize=(10, 8))
    ax1.set_xlim(0, 12)
    ax1.set_ylim(0, 10)
    ax1.axis('off')

    # Library Class
    ax1.add_patch(Rectangle((1, 5.5), 3.5, 3.5, fill=True, color='#fff9c4', ec='black'))
    plt.text(2.75, 8.6, "Library", weight='bold', ha='center')
    plt.text(1.2, 7.5, "- books: List\n- members: List", fontsize=9)
    plt.text(1.2, 6.0, "+ add_book()\n+ issue_book()\n+ return_book()", fontsize=9)

    # Book Class
    ax1.add_patch(Rectangle((7, 6), 3.5, 3, fill=True, color='#e1f5fe', ec='black'))
    plt.text(8.75, 8.6, "Book", weight='bold', ha='center')
    plt.text(7.2, 7.5, "- isbn: String\n- title: String\n- status: bool", fontsize=9)
    plt.text(7.2, 6.5, "+ get_info()", fontsize=9)

    # Association Relationship
    ax1.add_patch(FancyArrowPatch((4.5, 7.5), (7, 7.5), arrowstyle='<->', mutation_scale=20))
    plt.text(5.75, 7.7, "1..* contains", ha='center', fontsize=8)

    plt.title("LMS Class Diagram")
    plt.savefig(f"{output_dir}/class_diagram.png")
    print("✅ Class Diagram generated")

    # --- 2. SEQUENCE DIAGRAM (Issue Book) ---
    fig2, ax2 = plt.subplots(figsize=(10, 8))
    ax2.set_xlim(0, 10)
    ax2.set_ylim(0, 10)
    ax2.axis('off')

    # Lifelines
    lifelines = [("Member", 2), ("Librarian", 5), ("Database", 8)]
    for name, x in lifelines:
        ax2.plot([x, x], [2, 8], 'k--', lw=1)
        ax2.add_patch(Rectangle((x-0.75, 8), 1.5, 0.8, color='lightgrey', ec='black'))
        plt.text(x, 8.4, name, ha='center', weight='bold')

    # Interaction Arrows (The Sequence)
    # 1. Member -> Librarian: Request Book
    ax2.annotate('', xy=(5, 7.5), xytext=(2, 7.5), arrowprops=dict(arrowstyle='->'))
    plt.text(3.5, 7.6, "1: Request Book", ha='center', fontsize=8)

    # 2. Librarian -> Database: Check Availability
    ax2.annotate('', xy=(8, 6.5), xytext=(5, 6.5), arrowprops=dict(arrowstyle='->'))
    plt.text(6.5, 6.6, "2: Check ISBN", ha='center', fontsize=8)

    # 3. Database -> Librarian: Confirm
    ax2.annotate('', xy=(5, 5.5), xytext=(8, 5.5), arrowprops=dict(arrowstyle='->', ls='--'))
    plt.text(6.5, 5.6, "3: Available", ha='center', fontsize=8)

    plt.title("LMS Sequence Diagram: Issue Book")
    plt.savefig(f"{output_dir}/sequence_diagram.png")
    print("✅ Sequence Diagram generated")
    plt.show()

# =============================================================================
# MAIN EXECUTION
# =============================================================================
if __name__ == "__main__":
    setup_build_environment()
    generate_uml_diagrams()
    print("\n" + "=" * 70)
    print("✅ ALL EXPERIMENTS SUCCESSFULLY COMPLETED")
    print("=" * 70)