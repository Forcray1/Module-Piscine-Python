import sys


if __name__ == "__main__":
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print("Input Stream active. Enter archivist ID: ")
    ID = input()
    print("Input Stream active. Enter status report: ")
    status = input()
    print(f"\n[STANDARD] Archive status from {ID} : {status}", file=sys.stdout)
    print("[ALERT] System diagnostic: Communication channels verified",
          file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print("\nThree-channel communication test successful.")
