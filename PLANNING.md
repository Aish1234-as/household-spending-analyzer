# Planning Notes

## What I'm building
A tool that sorts transactions into categories, finds recurring payments like rent and subscriptions, and compares spending against monthly budgets.

## Still to work out
- How I'll generate the data, and which seed I'll use
- The category list and the rules for assigning each transaction
- How I'll tell refunds and transfers apart from spending
- How I'll detect recurring payments

## Plan
1. Set up the project and data model
2. Generate a small starter dataset
3. Add categorization rules
4. Add recurring payment detection
5. Add budget comparison
6. Add validation checks
7. Scale up and write the README

## Entities
- UserProfile: user_id (USR-000001), name, city
- Account: account_id (ACC-<user-id>-01), user_id, account_type
- Merchant: merchant_id, name, aliases
- Category: category_id, name, parent_category
- CategoryRule: rule_id, merchant_pattern, category_id, priority
- Transaction: transaction_id (TXN-2026-00000001), account_id, merchant_id, date, amount (negative = spending), description, category_id, is_transfer, is_refund
- Budget: budget_id (BUD-<user-id>-2026-01-<category-code>), user_id, category_id, month, amount
- RecurringSeries: series_id (REC-000001), user_id, merchant_id, frequency, expected_amount
- Insight: insight_id, user_id, month, category_id, total_spent, budget_amount
## Decisions
- Categorization uses the first keyword that matches, based on dictionary order. A description containing two keywords (e.g. "SWIGGY NETFLIX") gets the first category. I plan to replace this with an explicit priority field later.