import sqlite3

DB_NAME = "econnmer_pipeline.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS churn_records (
            user_id INTEGER PRIMARY KEY,
            tenure_months INTEGER CHECK(tenure_months >= 0),
            monthly_charges REAL CHECK(monthly_charges > 0.0),
            total_support_tix INTEGER CHECK(total_support_tix >= 0),
            is_churned INTEGER CHECK(is_churned IN (0,1))
        )
        """
    )
    conn.commit()
    conn.close()


    
def insert_customer_record(record: dict):

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT OR REPLACE INTO churn_records
        (user_id, tenure_months, monthly_charges, total_support_tix, is_churned)
        VALUES (?, ?, ?, ?, ?)
    """,
        (
            record["user_id"],
            record["tenure_months"],
            record["monthly_charges"],
            record["total_support_tix"],
            record["is_churned"],
        ),
    )
    conn.commit()
    conn.close()


