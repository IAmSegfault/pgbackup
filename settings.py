from pathlib import Path
BIN_DIR = str(Path('C:/iCRco/postgresql-9.0.15/bin'))
BACKUP_BIN = str(Path('C:/iCRco/postgresql-9.0.15/bin/pg_dump.exe'))
BACKUP_DIR = Path('C:/iCRco/sql_backups')
DATABASE_USER = 'postgres'
DATABASES = ['arrdb', 'pacsdb', 'postgres']
DAYS_TO_RETAIN = 365

BACKUP_TEMPLATES = []

for database in DATABASES:
    BACKUP_TEMPLATES.append(str(BACKUP_DIR) + str(Path("/" + database)))
