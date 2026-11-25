"""Unsent: The Micro-Confession Sprint — entry for make.fun.

Writes two lines to /output/entry.txt. The first line names who the message was meant for, the second is the unsent message itself.
"""
import os

TEXT = """To: my old best friend
I still keep the birthday gift you gave me in 2019, wrapped, on the top shelf, because throwing it away would mean admitting we are done."""

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")

if __name__ == "__main__":
    main()
