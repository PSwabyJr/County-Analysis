#filemanager.py
import abc
import json

class FileSaver(abc.ABC):
    @abc.abstractmethod
    def save_data(self, data):
        pass

class FileManager(abc.ABC):
    @abc.abstractmethod
    def get_data(self, file_name):
        pass

class JSONFileManager(FileManager):

    def get_data(self, file_name):
        try:
            with open(file_name, 'r') as json_file:
                json_data = json.load(json_file)
                return json_data
        except FileNotFoundError:
            print("File not found. Please check the file name and try again.")
        except json.decoder.JSONDecodeError:
            print("File is not a json file. Please check the file type and try again.")

class CSVFileSaver(FileSaver):

    def save_data(self, file_name:str, data:list):
        with open(file_name, 'w') as csv_file:
            csv_file.writelines(data)
        csv_file.close()