# Data Engineering Utilities

A collection of lightweight Python utilities for common data engineering workflows, including file format conversion and automated database loading.

## Projects

### 📁 File Format Converter

A utility for converting datasets between different file formats.

**Features**

* Convert CSV files to other supported formats.
* Batch processing support.
* Simple and reusable Python implementation.

---

### 🗄️ File to DB Loader

A modular ETL utility that automatically loads CSV files into a MySQL database.

**Features**

* Automatic table creation based on file names.
* Bulk loading using Pandas and SQLAlchemy.
* Environment-based credential management.
* Configuration-driven setup using `.env` and `config.ini`.
* Easily extensible for larger data ingestion pipelines.

**Project Structure**

```text
File to DB Loader/
│
├── Data/
├── config/
│   ├── config.ini.example
│   └── config.ini
├── .env.example
├── loader.py
├── main.py
└── requirements.txt
```

## Installation

```bash
git clone https://github.com/mrinalxdey/File-Operations.git
cd <repository-name>

pip install -r requirements.txt
```

Create your local configuration files:

* Copy `.env.example` → `.env`
* Copy `config/config.ini.example` → `config/config.ini`

Fill in your database credentials and configuration values.

## Technologies

* Python
* Pandas
* SQLAlchemy
* PyMySQL
* python-dotenv
* configparser

## Future Improvements

* Chunked loading for very large datasets
* Command-line interface (CLI)
* Support for PostgreSQL and SQLite
* Logging and error reporting
* Docker support

---

This repository is intended as a collection of reusable data engineering utilities and learning projects.
