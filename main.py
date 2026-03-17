from typing import List
import csv

TARGETS: List[str] = [
    "voce_me_encontrou",
    "YOU FOUND ME"
]


def search_file(filename: str) -> int:
    total_found = 0

    with open(filename, newline="", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f, delimiter=";")

        for row_index, row in enumerate(reader, start=1):
            for col_index, cell in enumerate(row, start=1):

                cell_lower = cell.lower()

                for target in TARGETS:
                    if target.lower() in cell_lower:
                        print(
                            f'{filename} | linha {row_index} | coluna {col_index} | {target}'
                        )
                        total_found += 1

    return total_found


total = 0
total += search_file("amazonsale1.csv")
total += search_file("amazonsale2.csv")

print(f"\nTotal encontrado: {total}")
