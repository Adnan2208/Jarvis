from pathlib import Path

from functions import write_files_content

CALCULATOR_DIR = str(Path(__file__).resolve().parents[1] / "calculator")


def main():
    print(write_files_content(CALCULATOR_DIR, "asdf.py", "print(hello world)"))
    print(write_files_content(CALCULATOR_DIR, "../hello", "should not type"))


if __name__ == "__main__":
    main()
