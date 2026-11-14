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
- Data generator: creates 500 users and one account each, saved to data/accounts.csv (small sample, not the full 500,000 rows)
- Validation checks: duplicate IDs and accounts that point to a real user (src/validate.py)
- Sample transactions: varied merchants per account (grocery, Netflix, Swiggy, electricity), with a fixed seed (data/transactions.csv)
- Ground-truth labels: expected category for each sample transaction (data/ground_truth.csv)
-  Categorization: keyword rules plus refund and transfer detection. Accuracy was 0.685 when Uber and Amazon were uncovered on the 500-account sample, and 1.0 after adding keyword rules for them (the sample uses six merchant types, so this is not a real-world accuracy test)
- Recurring check on generated accounts (runs on the sample; every account has one transaction, so all show False)
- Varied sample transactions (grocery, Netflix, Swiggy, electricity) with accuracy 1.0 on the sample
- Reproducibility: running the generator twice with the same seed produces identical output
- Data generator: creates 500 users and one account each, saved to data/accounts.csv (small sample, not the full 500,000 rows)
- Recurring detection at scale: monthly rent detected in 500 of 500 accounts across 12-month histories (src/history.py); the histories are generated, so this tests the logic, not real bank data
- Scale test: generated 12,000,000 history rows (500,000 accounts, 12 months each, 24 rows per account) in 6.79 seconds on this machine; this is row generation only, not a categorized or validated dataset
- Full-size categorized run: 12,000,000 rows across 500,000 accounts, all matched a rule; this measures rule coverage on eight known merchant names, not labeled accuracy (src/categorized_run.py)
- Data dictionary: column types, rules, and ID formats for each table (docs/DATA_DICTIONARY.md)
- Reconciliation: 500 accounts with totals, grand total -122,850, and 0 duplicate rows (src/reconcile.py)
- Timezone boundary check: a transaction at 18:45 UTC on Jan 15 is Jan 16 in IST; shown in src/timezone_check.py. The main dataset still stores plain dates, so this is a documented limitation, not yet handled in budgets
- Budget category check: flags budget categories that are not in the taxonomy (Groceries was flagged against Food, Entertainment, and the rest) (src/budget_check.py)
- Mid-size categorized run: 40,000 rows across 10,000 accounts, all matched a rule; this measures rule coverage on known merchants, not labeled accuracy (src/categorized_run.py)
- Labeled full-size accuracy: 1.0 across 12,000,000 rows with known merchant labels (src/labeled_full.py); this is accuracy on known merchants, not generalization to new ones
## What doesn't work yet
- Full 500,000-row, 12-month dataset (only a single 12-month test history exists)
- Refunds are handled by a rule, but the sample refund row is the only test case
- Transfers are handled by a rule, but the sample transfer row is the only test case
-- Generalization to unseen merchants: 0.6 on five fresh merchant descriptions (src/fresh_check.py), where brands without rules fail. Known brands with new wording scored 1.0 (src/fresh_check2.py), which measures wording variation, not new merchants
- Timezone-aware dates in budgets: transactions store plain dates and are not yet converted to local time before grouping


## Assumptions
Monthly means 28 to 31 days between payments.

## Decisions
The first keyword that matches decides the category, based on dictionary order. A description with two keywords gets the first category. I plan to add an explicit priority field later.

## How I used AI
I used Claude to plan the project, explain concepts, and check my understanding. I typed the ID generator, the categorization function, the day-gap helper, and the data generator myself, testing each one as I went. I asked for the full code once, then wrote it myself with step-by-step guidance. I also used it to draft the prompt history and this README, which I reviewed and edited.
