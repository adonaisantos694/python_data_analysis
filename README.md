CSV Pattern Finder

Original CSV files are extremely large and messy. This project demonstrates how to extract meaningful data even when files cannot be manually cleaned.

CSV Pattern Finder is a Python tool that scans large, messy CSV files for specific keywords or patterns, automatically identifying their exact location. It solves a common real-world problem: exported data often comes disorganized, with inconsistent separators, huge text fields, and hidden insights.

Features

Reads large CSV files line by line without loading everything into memory

Handles different separators and encodings

Detects keywords anywhere in a cell, even inside long text or descriptions

Reports file name, row, column, and matched keyword

Counts total occurrences for quick analysis

Clean, readable output for instant understanding

Use Cases

Searching for errors or patterns in sales reports

Auditing customer or product data

Scanning logs or massive datasets

Automating tedious manual data tasks

Example Usage
python main.py

Output example:

amazonsale1.csv | linha 20 | coluna 21 | YOU FOUND ME
amazonsale2.csv | linha 1313 | coluna 46 | voce_me_encontrou

Total found: 5

How It Works

The script reads CSVs line by line, normalizes text if needed, and checks each cell for matches with your list of target keywords. It’s optimized for large datasets and messy files, making it practical for real-world automation tasks.

Why This Project

Automating data searches like this saves hours of manual work, ensures accuracy, and demonstrates practical Python skills in data handling, text processing, and automation. It’s a simple tool, but the logic scales to real enterprise problems.
