# Concerts Project

## Overview

The **Concerts Project** is a Python application designed to manage concerts, bands, and venues using SQLAlchemy and SQLite. This project helps users handle data related to bands, venues, and concerts, providing functionalities to query and analyze concert-related information.

## Project Structure

The project is organized into the following folders and files:

- **`app/`**: Contains the main application code, including models, database setup, and methods.
  - **`__init__.py`**: Initializes the `app` package.
  - **`models.py`**: Defines the SQLAlchemy models for `Band`, `Venue`, and `Concert`.
  - **`database.py`**: Sets up the database connection and session management.
  - **`migrations/`**: Contains Alembic migration files for managing database schema changes.
  - **`main.py`**: Entry point for initializing the database.
  - **`methods.py`**: Contains business logic and methods for interacting with the database.
- **`tests/`**: Contains test cases for models and methods.
  - **`test_models.py`**: Tests for the `Band`, `Venue`, and `Concert` models.
  - **`test_methods.py`**: Tests for the methods defined in `methods.py`.
- **`.gitignore`**: Specifies files and directories to be ignored by Git.
- **`README.md`**: This file, providing project documentation.
- **`requirements.txt`**: Lists the Python packages required to run the project.

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the Repository**

   ```bash
   # Clone the repository to your local machine
   git clone https://github.com/yourusername/concerts_project.git
   cd concerts_project
