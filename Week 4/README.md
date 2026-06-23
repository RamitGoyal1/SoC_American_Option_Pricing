# Week 4: American Option Pricing Baseline

A clean, verified implementation of the Cox-Ross-Rubinstein (CRR) binomial tree model used to price European and American put options. This framework acts as the baseline target engine for subsequent machine learning models.

## Dependencies

- Python 3
- NumPy
- Matplotlib
- pytest (Optional, for running tests)

## Repository Layout

- `american_put.py`: Core mathematical function pricer with explicit parameter error checks.
- `test_american_put.py`: Financial sanity checks (monotonicity, vega limits, premium floors).
- `week4_report.py`: Script to print the metrics table and generate analytical figures.

## How to Run

Execute the main reporting routine via the terminal to get prices, numbers, and saved figures:
```bash
python week4_report.py
