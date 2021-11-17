import settings
from subprocess import Popen
from datetime import date
import time
import os

def backup_db(db_id):
    now = date.today()
    file = settings.BACKUP_TEMPLATES[db_id] + "_" + now.strftime("%Y-%m-%d")
    cmd = settings.BACKUP_BIN + " -U " + settings.DATABASE_USER + " -Fp -b -v -f " + file + " " + settings.DATABASES[db_id]
    process = Popen(cmd, shell=False)
    process.wait()

def cleanup():
    seconds = time.time() - (settings.DAYS_TO_RETAIN * 24 * 60 * 60)
    for root, dirs, files in os.walk(settings.BACKUP_DIR, topdown=False):
        for f in files:
            file_path = os.path.join(root, f)
            stat = os.stat(file_path)

            if stat.st_mtime <= seconds:
                os.remove(file_path)

if __name__ == '__main__':
    for i in range(0, len(settings.DATABASES)):
        backup_db(i)
    cleanup()


