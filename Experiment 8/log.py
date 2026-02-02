import logging
import sys
import datetime

def run_detailed_experiment():
    # --- STEP 1: SETTING UP LOGGING HANDLERS ---
    print("="*70)
    print("🛠️  PHASE 1: SYSTEM INITIALIZATION")
    print("="*70)
    
    # 8.3.3 Best Practice: Log errors with timestamp and details
    logger = logging.getLogger('RobustApp')
    logger.setLevel(logging.INFO)

    # Creating handlers for dual-output (File + Console)
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler('experiment8_detailed.log', mode='w')
    
    # Setting the format for systematic debugging
    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    # Adding handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)
    
    print("✅ Step 1: Logging handlers created and attached.")
    print("✅ Step 2: error_log.txt initialized for persistent storage.\n")

    # --- STEP 2: ROBUST EXECUTION ENGINE ---
    print("="*70)
    print("🧪 PHASE 2: EXECUTING EXCEPTION-HANDLING LOGIC")
    print("="*70)

    # Define various scenarios to trigger specific Exception Types
    scenarios = [
        {"desc": "Valid Input", "num1": "50", "num2": "5", "op": "/"},
        {"desc": "Invalid Type (ValueError)", "num1": "abc", "num2": "5", "op": "+"},
        {"desc": "Zero Division (ZeroDivisionError)", "num1": "10", "num2": "0", "op": "/"},
        {"desc": "Invalid Key (KeyError)", "num1": "10", "num2": "5", "op": "%"}
    ]

    for item in scenarios:
        print(f"\n▶️ TASK: {item['desc']}")
        
        # 8.3.2 Try: Code that might cause error
        try:
            # 8.3.3 Validate inputs before processing
            a = float(item['num1']) # Potential ValueError
            b = float(item['num2'])
            op = item['op']

            if op == '+':
                result = a + b
            elif op == '/':
                # 8.2.1 ZeroDivisionError: Division by zero
                if b == 0:
                    raise ZeroDivisionError("Math error: Division by zero is not allowed.")
                result = a / b
            else:
                # 8.2.1 KeyError: Dictionary key or operator not found
                raise KeyError(f"The operator '{op}' is not supported in this build.")

        # 8.3.2 Except: Handle specific exceptions systematically
        except ValueError as e:
            logger.error(f"ValueError Detected: {e}")
        
        except ZeroDivisionError as e:
            logger.error(f"ZeroDivisionError Detected: {e}")

        except KeyError as e:
            logger.warning(f"KeyError Detected: {e}")

        except Exception as e:
            # Catch-all for unexpected runtime errors to prevent crashes
            logger.critical(f"Unexpected Error: {e}")

        # 8.3.2 Else: Runs only if no error occurs
        else:
            print(f"✅ Output: {result}")
            logger.info(f"Successful Operation: {item['num1']} {item['op']} {item['num2']} = {result}")

        # 8.3.2 Finally: Always executes for cleanup
        finally:
            print(f"🔄 Cleanup: Task '{item['desc']}' attempt finished.")

    print("\n" + "="*70)
    print("✅ EXPERIMENT 8 COMPLETE: ALL LOGS SAVED")
    print("=" * 70)

if __name__ == "__main__":
    run_detailed_experiment()