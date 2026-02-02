"""
University of South Asia
Experiment 6: Advanced Debugging Techniques
Objective: Identify and resolve multiple bug types (Syntax, Runtime, Logic)
"""

import logging

# Configure logging to track debugging steps (Professional alternative to print)
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s: %(message)s')

class DataProcessor:
    def __init__(self, data):
        self.data = data

    def calculate_results(self):
        """
        This function contains several 'bugs' to be debugged.
        1. Potential Runtime Error: Division by Zero.
        2. Logic Error: Incorrect formula for calculating percentage.
        """
        results = []
        
        logging.debug(f"Starting calculation with data: {self.data}")

        # --- BUG 1: RUNTIME ERROR (Empty list check) ---
        if not self.data:
            logging.error("Empty list provided! Returning 0 to avoid crash.")
            return 0

        total_sum = sum(self.data)
        
        # --- BUG 2: LOGIC ERROR ---
        # Messy version would use: average = total_sum / (len(self.data) - 1)
        # Clean/Debugged version:
        average = total_sum / len(self.data)
        
        for value in self.data:
            # --- BUG 3: LOGIC ERROR ---
            # Scenario: We need to see how much each value contributes to the total.
            # Incorrect logic: percentage = (value / average) 
            # Correct logic:
            percentage = (value / total_sum) * 100
            results.append(round(percentage, 2))
            
        logging.info(f"Calculations successful. Results: {results}")
        return results

def debug_test_environment():
    """
    Simulating a debugging environment with different test cases.
    """
    print("--- DEBUGGING SESSION START ---")
    
    # CASE 1: Valid Data
    print("\n[Case 1: Valid Data]")
    processor1 = DataProcessor([10, 20, 30, 40])
    print(f"Outcome: {processor1.calculate_results()}")

    # CASE 2: Edge Case (Runtime Error prevention)
    print("\n[Case 2: Empty Data (Potential Runtime Error)]")
    processor2 = DataProcessor([])
    print(f"Outcome: {processor2.calculate_results()}")

    # CASE 3: Logic Verification
    print("\n[Case 3: Single Item (Logic Check)]")
    processor3 = DataProcessor([100])
    print(f"Outcome: {processor3.calculate_results()}") # Should be [100.0]

if __name__ == "__main__":
    debug_test_environment()