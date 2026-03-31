import subprocess
from context import detect_breeze_context

def run_command(cmd):
    print(f"\nRunning: {cmd}")
    result = subprocess.run(cmd, shell=True)
    return result.returncode == 0


def run_prek(max_retries=2):
    for attempt in range(max_retries + 1):
        success = run_command("echo 'Simulating prek checks...'")
        if success:
            print("prek passed")
            return True
        print(f"prek failed (attempt {attempt+1})")
    return False


def run_pytest():
    print("\nRunning pytest (simulated or empty suite)...")
    result = subprocess.run("pytest", shell=True)

    # Treat "no tests ran" as success for PoC
    if result.returncode == 5:
        print("No tests found — treating as success for PoC")
        return True

    return result.returncode == 0


def main():
    context = detect_breeze_context()
    print("Detected context:", context)

    # Step 1: run prek
    if not run_prek():
        print("Stopping: prek failed")
        return

    # Step 2: run pytest
    if context == "host":
        print("NOTE: In real system, would enter Breeze container")

    success = run_pytest()

    if success:
        print("Workflow SUCCESS")
    else:
        print("Workflow FAILED")


if __name__ == "__main__":
    main()