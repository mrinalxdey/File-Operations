import pandas as pd
import os
import configparser
from pathlib import Path
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

load_dotenv()
BASE_DIR = Path(__file__).resolve().parent

def get_engine():
    config = configparser.ConfigParser()
    config.read(BASE_DIR / 'config' / 'config.ini')
    creds = config['mysql']
    url = f"mysql+pymysql://{os.getenv('MYSQL_USER')}:{os.getenv('MYSQL_PASSWORD')}@{creds['host']}:{creds['port']}/{creds['database']}"
    return create_engine(url)

def load_files_to_db(data_dir):
    engine = get_engine()
    for file in os.listdir(data_dir):
        if file.endswith('.csv'):
            table_name = os.path.splitext(file)[0]
            print(f"Loading {file} into table {table_name}")
            df = pd.read_csv(os.path.join(data_dir, file))
            df.to_sql(table_name, con=engine, if_exists='replace', index=False)
            print(f"Loading complete for {file}")
