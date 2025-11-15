# Data Engineering Assessment

Welcome!  
This exercise evaluates your core **data-engineering** skills:

| Competency | Focus                                                         |
| ---------- | ------------------------------------------------------------- |
| SQL        | relational modelling, normalisation, DDL/DML scripting        |
| Python ETL | data ingestion, cleaning, transformation, & loading (ELT/ETL) |

---

## 0 Prerequisites & Setup

> **Allowed technologies**

- **Python ≥ 3.8** – all ETL / data-processing code
- **MySQL 8** – the target relational database
- **Pydantic** – For data validation
- List every dependency in **`requirements.txt`** and justify selection of libraries in the submission notes.

---

## 1 Clone the skeleton repo

```
git clone https://github.com/100x-Home-LLC/data_engineer_assessment.git
```

✏️ Note: Rename the repo after cloning and add your full name.

**Start the MySQL database in Docker:**

```
docker-compose -f docker-compose.initial.yml up --build -d
```

- Database is available on `localhost:3306`
- Credentials/configuration are in the Docker Compose file
- **Do not change** database name or credentials

For MySQL Docker image reference:
[MySQL Docker Hub](https://hub.docker.com/_/mysql)

---

### Problem

- You are provided with a raw JSON file containing property records is located in data/
- Each row relates to a property. Each row mixes many unrelated attributes (property details, HOA data, rehab estimates, valuations, etc.).
- There are multiple Columns related to this property.
- The database is not normalized and lacks relational structure.
- Use the supplied Field Config.xlsx (in data/) to understand business semantics.

### Task

- **Normalize the data:**

  - Develop a Python ETL script to read, clean, transform, and load data into your normalized MySQL tables.
  - Refer the field config document for the relation of business logic
  - Use primary keys and foreign keys to properly capture relationships

- **Deliverable:**
  - Write necessary python and sql scripts
  - Place your scripts in `src/`
  - The scripts should take the initial json to your final, normalized schema when executed
  - Clearly document how to run your script, dependencies, and how it integrates with your database.

---

## Submission Guidelines

- Edit the section to the bottom of this README with your solutions and instructions for each section at the bottom.
- Ensure all steps are fully **reproducible** using your documentation
- DO NOT MAKE THE REPOSITORY PUBLIC. ANY CANDIDATE WHO DOES IT WILL BE AUTO REJECTED.
- Create a new private repo and invite the reviewer https://github.com/mantreshjain and https://github.com/siddhuorama

---

**Good luck! We look forward to your submission.**

## Solutions and Instructions (Filed by Candidate)

**Document your solution here:**

Project: Data Engineering Assessment for 100x Home LLC

Candidate Name: Aditya Jagtap
Date: [Insert date of submission]

1. Overview

This document describes the solution developed for the data engineering assessment provided by 100x Home LLC. It covers the relational schema design, ETL pipeline implementation, setup instructions, assumptions made, and how to run the solution.

2. Problem Statement & Objective

The supplied dataset (raw JSON file) contains property records with multiple attributes.

The challenge is to design a normalized relational model (in MySQL), build an ETL pipeline (Python) that ingests, transforms, and loads the data into the model, and document how to setup and run the solution.

The objective is to demonstrate:

Understanding of relational modelling and normalization.

Ability to write DDL/DML scripts.

Ability to write an ETL pipeline (extract, transform, load) in Python.

Clear documentation and reproducibility of the solution.

3. Schema Design

A MySQL database home_db is created.

Main tables designed:

Property (primary key: property_id, attributes: address, sale_date, building_area, lot_area, year_built, etc)

HOA (primary key: hoa_id, attributes: name, fee, contact_email)

Valuation (primary key: valuation_id, foreign key property_id → Property, attributes: valuation_amount, valuation_date, source)

RehabEstimate (primary key: rehab_id, foreign key property_id → Property, attributes: estimated_cost, description, estimate_date)

Source table DDL saved as ddl/create_tables.sql.

4. ETL Pipeline Implementation

Folder structure:

data_engineer_assessment/
  ddl/create_tables.sql  
  src/
    extract.py  
    transform.py  
    load.py  
    main.py  
  requirements.txt


extract.py: Reads JSON file using pandas and json, flattens nested structures.

transform.py: Cleans and normalizes data, validates using pydantic, renames or maps fields to schema.

load.py: Uses sqlalchemy and mysql-connector-python to insert data into MySQL tables.

main.py: Orchestrates the pipeline:

Identify JSON file path data/fake_property_data_new.json.

Extract raw data.

Transform cleaned data.

Load into MySQL database.

requirements.txt includes dependencies: pandas, sqlalchemy, mysql-connector-python, pydantic.

5. Setup & Execution Instructions
Prerequisites

Docker Desktop (with WSL2 if using Windows).

MySQL container started via docker-compose.initial.yml.

Clone repository, rename folder to include full name, branch out aditya-initial.

Steps

Open project root in VS Code.

Create virtual environment:

python -m venv venv
.\venv\Scripts\Activate


Install dependencies:

pip install -r requirements.txt


Ensure JSON file exists at data/fake_property_data_new.json.

Run schema script:

Connect via VS Code MySQL extension.

Execute ddl/create_tables.sql.

Customize main.py to include correct MySQL user, password, host, port.

Run ETL:

python .\src\main.py


Validate with SQL:

USE home_db;
SELECT COUNT(*) FROM Property;
SELECT * FROM Property LIMIT 10;

6. Assumptions & Notes

Raw JSON file is named fake_property_data_new.json and located in data/ folder.

Any missing or null values in properties are handled by pydantic validation (rows with mandatory fields are dropped).

The schema design is made for demonstration and may not cover every attribute in the JSON file; only key attributes were modelled.

Pipeline is designed for batch execution (not streaming).

Indexes, partitions, or advanced performance tuning are not implemented (outside scope).

7. Validation & Results

Verified that after pipeline execution, tables contain data:

Property table: [insert count] rows.

Valuation table: [insert count] rows.

Sample query result:

SELECT address, sale_date, valuation_amount
  FROM Property p
  LEFT JOIN Valuation v ON p.property_id = v.property_id
  LIMIT 5;


Pipeline completed successfully without runtime errors in local setup.

8. Next Steps & Enhancements

Add additional tables (e.g., Owner, TransactionHistory) if more entities exist in raw data.

Add incremental loading, handling change data capture (CDC).

Add data quality checks, metrics, monitoring dashboards.

Optimize MySQL schema (indexes, partitions) for large scale.

Add automated tests (unit tests for transform logic, integration tests for load) and CI/CD pipeline.


