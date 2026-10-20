from pathlib import Path

from functions import get_files_content

CALCULATOR_DIR = str(Path(__file__).resolve().parents[1] / "calculator")


def main():
    print(get_files_content(CALCULATOR_DIR, "main.py"))
    print(get_files_content(CALCULATOR_DIR, "pkg/calculator.py"))
    print(get_files_content(CALCULATOR_DIR, "bin"))
    print(get_files_content(CALCULATOR_DIR, "pkg/does_not_exist.py"))


if __name__ == "__main__":
    main()
