# MySQL Database Files

This folder contains SQL scripts, database schema, and queries used in the Customer Churn Prediction project.

## Contents

- **schema.sql** - Database schema creation and table definitions
- **queries.sql** - Analysis and aggregate queries
- **data_import.sql** - Scripts to import and prepare data

## Usage

To set up the database:

```bash
mysql -u your_username -p your_database < schema.sql
mysql -u your_username -p your_database < data_import.sql
```

## Notes

- Replace `your_username` and `your_database` with your actual MySQL credentials
- Ensure MySQL server is running before executing scripts



