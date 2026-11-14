# Household Spending Analyzer

## What it does
This tool sorts bank transactions into categories, looks for recurring payments, and compares spending to budgets. Currently it has the ID generator, categorization rules, day-gap helper, recurring check, budget comparison, and a small data generator.

## Setup
1. Clone the repo
2. Create a virtual environment: python -m venv venv
3. Activate it: .\venv\Scripts\Activate.ps1
4. Install packages: pip install -r requirements.txt

## How to run
python src/categorize.py
python src/ids.py
python src/recurring.py
python src/budget.py
python src/generate_data.py

## What works
- User ID generator
- Keyword categorization
- Day gap helper
- Recurring check: tells whether a series of dates is monthly (28 to 31 days between payments)
- Budget comparison: flags categories where spending is over budget
- Data generator: creates 50 users and one account each, saved to data/accounts.csv (small sample, not the full 500,000 rows)
- Validation checks: duplicate IDs and accounts that point to a real user (src/validate.py)
- Sample transactions: varied merchants per account (grocery, Netflix, Swiggy, electricity), with a fixed seed (data/transactions.csv)
- Ground-truth labels: expected category for each sample transaction (data/ground_truth.csv)
- Categorization accuracy: compares the categorizer against ground-truth labels (100% on the uniform sample, which is not a real accuracy test)
- Recurring check on generated accounts (runs on the sample; every account has one transaction, so all show False)
- Varied sample transactions (grocery, Netflix, Swiggy, electricity) with accuracy 1.0 on the sample
## What doesn't work yet
- Full 500,000-row dataset


## Assumptions
Monthly means 28 to 31 days between payments.

## Decisions
The first keyword that matches decides the category, based on dictionary order. A description with two keywords gets the first category. I plan to add an explicit priority field later.

## How I used AI
I used Claude to plan the project, explain concepts, and check my understanding. I typed the ID generator, the categorization function, the day-gap helper, and the data generator myself, testing each one as I went. I asked for the full code once, then wrote it myself with step-by-step guidance. I also used it to draft the prompt history and this README, which I reviewed and edited.