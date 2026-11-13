# Household Spending Analyzer

## What it does
This tool sorts bank transactions into categories, looks for recurring payments, and will compare spending to budgets. Currently it has the ID generator, categorization rules, and the day-gap helper.

## Setup
1. Clone the repo
2. Create a virtual environment: python -m venv venv
3. Activate it: .\venv\Scripts\Activate.ps1
4. Install packages: pip install -r requirements.txt

## How to run
python src/categorize.py
python src/ids.py
python src/recurring.py

## What works
- User ID generator
- Keyword categorization
- Day gap helper
Recurring check: tells whether a series of dates is monthly (28 to 31 days between payments) 

## What doesn't work yet
- Budget comparison
- Full 500,000-row dataset

## Assumptions
Monthly means 28 to 31 days between payments.

## Decisions
The first keyword that matches decides the category, based on dictionary order. A description with two keywords gets the first category. I plan to add an explicit priority field later.

## How I used AI
I used Claude to plan the project, explain concepts, and check my understanding. I typed the ID generator, the categorization function, and the day-gap helper myself, testing each one as I went. I asked for the full code once, then wrote it myself with step-by-step guidance. I also used it to draft the prompt history and this README, which I reviewed and edited.