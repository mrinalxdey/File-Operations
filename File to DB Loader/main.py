from loader import load_files_to_db
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

if __name__ == '__main__':
    load_files_to_db(BASE_DIR / 'Data')