from pathlib import Path

from functions import get_files_info

CALCULATOR_DIR = str(Path(__file__).resolve().parents[1] / "calculator")


def main():
    print(get_files_info(CALCULATOR_DIR, "."))
    print(get_files_info(CALCULATOR_DIR, "pkg"))
    print(get_files_info(CALCULATOR_DIR, "../"))
    print(get_files_info(CALCULATOR_DIR, "bin"))
    print(get_files_info(CALCULATOR_DIR))


if __name__ == "__main__":
    main()
