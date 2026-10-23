# Modular Data Validation & Pipeline

Learning to build a professional Python data pipeline. It intakes raw records, enforces valiadtion using Pydantic and pushes clean data into SQLite. 


## Project Structure
Schemas.py: defines data models, cleaning logic, and field validators using Pydantic.
database.py: Handles SQLite 
Pipeline.py: batch data ingestion, error tracking and database insertion 

- `schemas.py`: Defines data models, cleaning logic, and field validators using Pydantic.
- `database.py`: Handles SQLite database initialization and explicit resource management.
- `pipeline.py`: Orchestrates batch data ingestion, error logging, and database insertion.

## Getting Started

### 1. Clone the repository
```bash
git clone <https://github.com/rzhang539/modular-data-pipeline.git>

### 2. Set up a virtual environment
Bash
python -m venv .venv
.\.venv\Scripts\Activate  

### 3. Install dependencies
Bash
pip install -r requirements.txt

### 4. Run the pipeline
Bash
python pipeline.py