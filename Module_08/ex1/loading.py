import sys
import importlib.metadata


def check_dependency(package_name: str) -> bool:
    try:
        version = importlib.metadata.version(package_name)
        print(f"[OK] {package_name} ({version}) - Ready")
        return True
    except importlib.metadata.PackageNotFoundError:
        print(f"[MISSING] {package_name} is not installed.")
        return False


def main() -> None:
    print("LOADING STATUS: Loading programs...")

    required = ["pandas", "numpy", "matplotlib"]
    missing = []

    print("Checking dependencies:")
    for lib in required:
        if not check_dependency(lib):
            missing.append(lib)

    if missing:
        print("\nERROR: Missing dependencies.")
        print(f"Please install: {', '.join(missing)}")
        print("Use: 'pip install -r requirements.txt' or 'poetry install'")
        sys.exit(1)
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    print("\nAnalyzing Matrix data...")

    data = np.random.randn(1000, 2)
    df = pd.DataFrame(data, columns=['Neo', 'Morpheus'])

    print("Processing 1000 data points...")
    print("Generating visualization...")

    plt.figure(figsize=(10, 6))
    plt.scatter(df['Neo'], df['Morpheus'], alpha=0.5, c='green')
    plt.title("Matrix Anomaly Detection")
    output_filename = "matrix\\_analysis.png"
    plt.savefig(output_filename)
    print("Analysis complete!")
    print(f"Results saved to: {output_filename}")

    print("\nAnalysis complete!")
    print(f"Results saved to: {output_filename}")


if __name__ == "__main__":
    main()
