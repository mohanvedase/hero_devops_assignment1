# Write a program for performing regular backups of important files 

import os
import shutil
import datetime


def backup_files_with_timestamp(source_folder, destination_folder):
    for file_name in os.listdir(source_folder):
        source = os.path.join(source_folder, file_name)
        destination = os.path.join(destination_folder, file_name)

        if os.path.isfile(destination):
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
            new_destination = os.path.join(destination_folder, timestamp + " - " + file_name)
            shutil.copy(source, new_destination)
        else:
            shutil.copy(source, destination)


if __name__ == "__main__":
    source_folder = r"C:\Users\hi\Desktop\Master file\\"
    destination_folder = r"F:\krishna\IT\Backup_file\\"

    backup_files_with_timestamp(source_folder, destination_folder)