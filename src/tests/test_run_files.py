from pathlib import Path

from functions import run_files

CALCULATOR_DIR = str(Path(__file__).resolve().parents[1] / "calculator")


def main():
    print(run_files(CALCULATOR_DIR, "main.py"))
    print(run_files(CALCULATOR_DIR, "test.py"))


if __name__ == "__main__":
    main()
