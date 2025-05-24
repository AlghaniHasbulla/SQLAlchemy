# Articles - without SQLAlchemy Challenge

This project is designed to model the relationships between Authors, Articles, and Magazines using SQLAlchemy and SQLite. The project includes a database schema, model classes, and tests to ensure everything works correctly.

## Project Structure

The project is organized as follows:
SQLAlchemy/
├── lib/
│   ├── init.py
│   ├── db/
│   │   ├── init.py
│   │   ├── connection.py
│   │   ├── schema.sql
│   │   └── seed.py
│   ├── models/
│   │   ├── init.py
│   │   ├── author.py
│   │   ├── article.py
│   │   └── magazine.py
├── scripts/
│   ├── setup_db.py
│   └── run_queries.py
├── tests/
│   ├── init.py
│   ├── test_author.py
│   ├── test_article.py
│   └── test_magazine.py
├── README.md
└── Pipfile

## Setup Instructions

### Prerequisites

- Python 3.10 or higher
- Pipenv (for managing dependencies)

### Steps to Set Up the Project

1. **Clone the Repository:**

   ```sh
   git clone https://github.com/yourusername/SQLAlchemy.git
   cd SQLAlchemy
## Install Dependencies
  pipenv install pytest sqlite3
## Create a Virtual Environment
  pipenv shell
## Setup the Database
  python scripts/setup_db.py
## Run the Tests
  pytest


**Contributing**
Feel free to contribute to this project by submitting pull requests or opening issues. Any feedback is welcome!

**License**
This project is licensed under the MIT License. See the LICENSE file for details.

### Summary

This `README.md` file provides a comprehensive guide on how to set up and run the project. It includes detailed instructions on the project structure, setup steps, database schema, model classes, and running tests. This should help anyone get started with the project quickly and efficiently.