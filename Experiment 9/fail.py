import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import Rectangle, FancyArrowPatch, Circle, Ellipse
import os

# =============================================================================
# EXPERIMENT 9: UML DIAGRAMS - COMPLETE DEMONSTRATION
# Creates Class, Use Case, and Sequence diagrams with export functionality
# =============================================================================

def setup_output():
    output_dir = "uml_diagrams"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    return output_dir

# --- 1. CLASS DIAGRAM ---
def create_class_diagram(output_dir):
    print("🎨 Generating Class Diagram...")
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Class: Library (Controller)
    ax.add_patch(Rectangle((1, 5), 3.5, 4, color='#fff9c4', ec='black', lw=2))
    plt.text(2.75, 8.6, "Library", weight='bold', ha='center', fontsize=12)
    plt.text(1.2, 7.2, "- books: List\n- members: List", fontsize=10)
    plt.text(1.2, 5.5, "+ add_book()\n+ register_member()\n+ issue_book()\n+ return_book()", fontsize=10)

    # Class: Book (Entity)
    ax.add_patch(Rectangle((7, 6), 3.5, 3, color='#e1f5fe', ec='black', lw=2))
    plt.text(8.75, 8.6, "Book", weight='bold', ha='center', fontsize=12)
    plt.text(7.2, 7.5, "- isbn: String\n- title: String\n- is_available: bool", fontsize=10)
    plt.text(7.2, 6.5, "+ get_details()", fontsize=10)

    # Relationship: Association
    ax.add_patch(FancyArrowPatch((4.5, 7), (7, 7), arrowstyle='<->', mutation_scale=20, color='black'))
    plt.text(5.75, 7.2, "1..* contains", ha='center', fontsize=9)

    plt.title("UML Class Diagram: Library Management System", pad=20, fontsize=14)
    plt.savefig(f"{output_dir}/1_class_diagram.png", dpi=300, bbox_inches='tight')
    plt.show()

# --- 2. USE CASE DIAGRAM ---
def create_use_case_diagram(output_dir):
    print("🎨 Generating Use Case Diagram...")
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # System Boundary
    ax.add_patch(Rectangle((3, 1), 4, 8, fill=None, ec='black', ls='--'))
    plt.text(5, 8.6, "Library System", ha='center', weight='bold')

    # Use Cases (Ellipses)
    use_cases = ["Search Books", "Issue Book", "Return Book", "Manage Members"]
    y_pos = [7, 5, 3, 1.5]
    for i, text in enumerate(use_cases):
        ax.add_patch(Ellipse((5, y_pos[i]), 2.5, 0.8, color='white', ec='black'))
        plt.text(5, y_pos[i], text, ha='center', va='center', fontsize=9)

    # Actor: Librarian
    plt.text(1.5, 5.5, "웃", fontsize=40, ha='center')
    plt.text(1.5, 4.5, "Librarian", ha='center', weight='bold')

    # Connect Actor to Use Cases
    for y in y_pos:
        ax.annotate('', xy=(3.8, y), xytext=(1.8, 5), arrowprops=dict(arrowstyle='-', lw=1))

    plt.title("UML Use Case Diagram: Library Management System", pad=20, fontsize=14)
    plt.savefig(f"{output_dir}/2_use_case_diagram.png", dpi=300, bbox_inches='tight')
    plt.show()

# --- 3. SEQUENCE DIAGRAM ---
def create_sequence_diagram(output_dir):
    print("🎨 Generating Sequence Diagram...")
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    # Lifelines
    entities = [("Member", 2), ("Librarian", 5), ("Database", 8)]
    for name, x in entities:
        ax.plot([x, x], [1.5, 8], 'k--', lw=1) # Vertical line
        ax.add_patch(Rectangle((x-0.8, 8), 1.6, 0.7, color='lightgrey', ec='black'))
        plt.text(x, 8.35, name, ha='center', weight='bold')

    # Interaction Arrows (The Logic Flow)
    # 1. Member -> Librarian: Request
    ax.annotate('', xy=(5, 7), xytext=(2, 7), arrowprops=dict(arrowstyle='->', lw=1.5))
    plt.text(3.5, 7.2, "1: Request(ISBN)", ha='center', fontsize=9)

    # 2. Librarian -> Database: Check
    ax.annotate('', xy=(8, 6), xytext=(5, 6), arrowprops=dict(arrowstyle='->', lw=1.5))
    plt.text(6.5, 6.2, "2: CheckAvailability()", ha='center', fontsize=9)

    # 3. Database -> Librarian: Response
    ax.annotate('', xy=(5, 5), xytext=(8, 5), arrowprops=dict(arrowstyle='->', ls='--', lw=1))
    plt.text(6.5, 5.2, "3: StatusAvailable", ha='center', fontsize=9)

    # 4. Librarian -> Member: Confirm
    ax.annotate('', xy=(2, 4), xytext=(5, 4), arrowprops=dict(arrowstyle='->', lw=1.5))
    plt.text(3.5, 4.2, "4: IssueBook()", ha='center', fontsize=9)

    plt.title("UML Sequence Diagram: Issue Book Process", pad=20, fontsize=14)
    plt.savefig(f"{output_dir}/3_sequence_diagram.png", dpi=300, bbox_inches='tight')
    plt.show()

# =============================================================================
# EXECUTION
# =============================================================================
if __name__ == "__main__":
    path = setup_output()
    create_class_diagram(path)
    create_use_case_diagram(path)
    create_sequence_diagram(path)
    print(f"\n✅ Experiment 9 Complete. Diagrams saved in '{path}/'")