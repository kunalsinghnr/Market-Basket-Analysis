# Market-Basket-Analysis

Market Basket Analysis using Apriori Algorithm
This Python script performs market basket analysis on retail transaction data using the Apriori algorithm. The dataset used is from online retail transactions, and the analysis is conducted separately for two countries: France and Germany.

Overview of the Code:
Data Loading and Cleaning:

Libraries are imported, and the dataset is loaded from an Excel file.
Initial data exploration includes handling missing values, cleaning up spaces in the 'Description' column, and managing null values in the 'Customer ID' column.
Data Preparation for Apriori Algorithm:

Canceled invoices are excluded from the dataset.
For each country (France and Germany), a basket is created, where each row represents a unique invoice, and each column represents a product (Description). Values in the table indicate the quantity of each product in the respective invoice.
Binary encoding is applied to represent whether a product was bought (1) or not (0).
Apriori Algorithm and Association Rules:

The Apriori algorithm is applied separately to the France and Germany baskets to identify frequent itemsets (products frequently bought together).
Association rules are generated based on these frequent itemsets, considering metrics like support, confidence, and lift.
Rules are filtered to find strong associations with a lift greater than or equal to 6 and confidence greater than or equal to 0.8.
Summary of Results:

The final lists of associated items for both France and Germany are displayed.
End Goal:
The objective of this code is to uncover patterns of association between products in retail transactions for different countries. The Apriori algorithm is utilized to reveal relationships between items frequently purchased together, providing actionable insights for marketing, inventory management, and other business strategies.
