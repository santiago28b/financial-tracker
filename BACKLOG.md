# Backlog

Ideas that are not in the current phase. Writing it here is how you avoid
building it today.

- Bank CSV import
- Revisit DECISIONS 004 (no splits) at S9.9: a hand-entered 80 + 40 won't match an imported −120
- Budgets and per-category limits
- Net worth / account balance tracking
- Forecasting from recurring income and bills
- Multi-user / shared household finances
- Mobile layout
- OOP solo rep: classes, encapsulation, interfaces (ABCs / Protocols), polymorphism, inheritance vs composition, and when a class beats a function (after S4.10)
- Spend/Income toggle in the transaction form (Stage 5): the UI sets the sign so users never type a minus; domain keeps "negative = out" (S1.6)
- totals_summary when the total is ≤ 0 (S2.8): {+5, −5} raises decimal.DivisionByZero; {−10, +5} gives 200% / −100% and flips the sort. Decide: raise, return 0%, or base percentages on spending only
