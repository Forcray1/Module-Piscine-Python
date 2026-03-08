if __name__ == "__main__":
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n")
    print("Initiating secure vault access...")
    try:
        with open("vault.txt", "r", encoding="utf-8") as f:
            print("Vault connection established with failsafe protocols\n")
            output = f.read()
            print("SECURE EXTRACTION:")
            print("[CLASSIFIED] Quantum encryption keys recovered")
            print("[CLASSIFIED] Archive integrity: 100%\n")
            with open("Save.txt", "w", encoding="utf-8") as f:
                print("SECURE PRESERVATION:\n")
                f.write(output)
                print("[CLASSIFIED] New security protocols archived")
                print("Vault automatically sealed upon completion\n")
                print("All vault operations completed with maximum security.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found.")
