import zipfile
import os
import shutil


def test_create_and_add_in_zip_file():
    newzip = zipfile.ZipFile(os.path.abspath('file.zip'), "w")
    newzip.write('Книга1.xlsx')
    newzip.write('Отчет.csv')
    newzip.write('Тест.pdf')


def test_create_and_move_zip_in_new_folder():
    os.mkdir("resources")
    directory_file = os.path.abspath("file.zip")
    directory_folder = os.path.abspath("resources")
    shutil.move(directory_file, directory_folder)


def read_and_check_zipfile():
    pass



