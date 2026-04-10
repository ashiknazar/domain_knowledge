# Finance Domain

Overview of the domain.

> The finance domain deals with money flow, risk, investments, and transactions.

-  It includes areas like:
  - Banking
  - Payments (UPI, cards)
  - Stock markets
  - Loans & credit
  - Insurance

___

- Core Idea
  - Finance = movement and management of money over time
  - just like
    - E-commerce → user actions
    - Finance → money-related events
___

- Event-driven thinking (same concept as e-commerce)

___

##### Example: Banking System
- A user uses a banking app:
  - Logs in
    - Event: login
  - Checks balance
    - Event: balance_view
  - Transfers money
    - Event: transaction
  - Pays bill
    - Event: bill_payment
     
___

#### Types of Finance Domains
-  Banking
   - Accounts, transactions, balances
   - Example: SBI, HDFC
- Payments
   - UPI, wallets, card payments
   - Example: Google Pay, PhonePe
- Stock Market / Trading
   - Buying/selling stocks
   - Price movements
- Lending / Credit
   - Loans, EMIs, credit scores
- Insurance
   - Premiums, claims, risk analysis

___
#### What Data Analysts / Data Scientists do here

- Fraud Detection (very important use case)
   - Detect suspicious transactions
     - Sudden ₹1,00,000 transfer at midnight
     - Foreign transaction after local usage
- Credit Scoring
   - Decide if a user can get a loan
     - Income
     - Spending patterns
     - Repayment history
- Customer Segmentation
   - Classify users:
     - High-value customers
     - Risky users
     - Low spenders
- Risk Analysis
   - Predict:
     - Will this user default?(Default = failure to repay a loan)
     - Will this investment lose money?
- Transaction Analytics
   - Metrics like:
     - Daily transaction volume
     - Average transaction value
     - Cash flow trends