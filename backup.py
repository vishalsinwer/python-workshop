import os
import datetime
import shutil

def backup_files(source,destination):
    today = datetime.date.today()
    backup_file_name = os.path.join(destination,f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file_name,'gztar',source)
source = "\Users\Dell\Documents\python workshop"
destination = "\Users\Dell\Documents\python workshop\backups"

backup_files(source,destination)