from database import init_db, insert_customer_record
from Schemas import raw_data_cleanup
from pydantic import ValidationError

init_db()

raw_churn_payload = [
    # Source A: Clean inputs, string IDs
    {
        "user_id": "1001",
        "tenure_months": 12,
        "monthly_charges": "65.50",
        "total_support_tickets": 2,
        "is_churned": 0
    },
    # Source B: Alternative keys ('account_id', 'months_active'), string floats
    {
        "account_id": "1002",
        "months_active": " 24 ",
        "monthly_charges": 89.99,
        "total_support_tickets": "0",
        "is_churned": "0"
    },
    # Source A: Negative monthly charges (Dirty)
    {
        "user_id": 1003,
        "tenure_months": 3,
        "monthly_charges": -15.00,
        "total_support_tickets": 5,
        "is_churned": 1
    },
    # Source B: Invalid numeric string for charges (Dirty)
    {
        "account_id": "1004",
        "months_active": 6,
        "monthly_charges": "N/A",
        "total_support_tickets": 1,
        "is_churned": 1
    }
]

print("Starting data processing pipeline...\n")

valid_records = []
invalid_records = []

for index, raw_record in enumerate(raw_churn_payload, start=1):
    try:
        record = raw_data_cleanup(**raw_record)
        clean_data = record.model_dump()
        insert_customer_record(clean_data)
        valid_records.append(record)
        print(f"index: {index} sucessfully valided and saved into DB")
    except ValidationError as e:
        print(f"REJECTED INDEX {index}, {e.errors()[0]['msg']}") 
        invalid_records.append(raw_record)

