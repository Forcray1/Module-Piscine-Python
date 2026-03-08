def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt\n")
    try:
        with open("ancient_fragment.txt", "r", encoding="utf-8") as f:
            output = f.read()
        print("RECOVERED DATA:")
        print(f"{output}")
        print("\nData recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")


if __name__ == "__main__":
    main()
