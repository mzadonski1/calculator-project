# CLI kasutajaliides kalkulaatorile
from __future__ import annotations

import sys
from typing import Callable, Dict, Tuple

from calculator import operations as op

# Menüü kirjeldus: klahv -> (sildi tekst, vastav funktsioon)
MenuMap = Dict[str, Tuple[str, Callable[[float, float], float]]]

MENU: MenuMap = {
    "1": ("Addition (a + b)", op.add),
    "2": ("Subtraction (a - b)", op.subtract),
    "3": ("Multiplication (a * b)", op.multiply),
    "4": ("Division (a / b)", op.divide),
    "5": ("Exponent (a ** b)", op.exponent),
    "6": ("Modulus (a % b)", op.modulus),
}


def read_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip().replace(",", ".")
        try:
            return float(raw)
        except ValueError:
            print("Please enter a valid number (e.g., 3.14).")


def main() -> int:
    print("=== Python CLI Calculator ===")
    while True:
        print("\nChoose operation:")
        for key, (label, _) in sorted(MENU.items(), key=lambda x: x[0]):
            print(f"{key}) {label}")
        print("q) Quit")
        choice = input("> ").strip().lower()

        if choice in ("q", "quit", "exit"):
            print("Goodbye!")
            return 0

        if choice not in MENU:
            print("Unknown option. Try again.")
            continue

        a = read_number("Enter a: ")
        b = read_number("Enter b: ")

        label, func = MENU[choice]
        try:
            result = func(a, b)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue

        print(f"Result ({label}): {result}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

