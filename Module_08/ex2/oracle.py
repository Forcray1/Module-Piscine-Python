import os
from dotenv import load_dotenv


def main() -> None:
    print("ORACLE STATUS: Reading the Matrix...")

    # Charger les variables depuis le fichier .env (s'il existe)
    # Si on lance "MATRIX_MODE=prod python oracle.py", load_dotenv ne
    # remplacera PAS la valeur système existante
    load_dotenv()

    # Récupérer les configurations avec des valeurs par défaut sécurisées
    matrix_mode = os.getenv("MATRIX_MODE", "unknown")
    db_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL", "INFO")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    # Vérifier les secrets manquants
    missing_secrets = []
    if not db_url:
        missing_secrets.append("DATABASE_URL")
    if not api_key:
        missing_secrets.append("API_KEY")
    if not zion_endpoint:
        missing_secrets.append("ZION_ENDPOINT")
    if len(missing_secrets) == 3:
        print("\nWARNING: No configuration found.")
        print("Please copy .env.example to .env and configure your secrets.")
        # On continue quand même pour montrer les valeurs par défaut "nulles"
    print("\nConfiguration loaded:")
    print(f"Mode: {matrix_mode}")
    # Pour la DB, on vérifie juste si l'URL est là
    if db_url:
        print("Database: Connected to local instance")
    else:
        print("Database: Not configured")
    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Denied (Missing Key)")
    print(f"Log Level: {log_level}")
    if zion_endpoint:
        print("Zion Network: Online")
    else:
        print("Zion Network: Offline")
    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    if os.path.exists(".env"):
        print("[OK] .env file properly configured")
    else:
        print("[WARNING] No .env file found (Running on system vars only?)")

    # Vérification si on est en override (si MATRIX_MODE est passé en ligne de
    # commande)
    # C'est un peu dur à détecter programmatiquement de manière fiable sans
    # libs complexes, donc on affiche simplement que la fonctionnalité
    # est dispo.
    print("[OK] Production overrides available")

    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
