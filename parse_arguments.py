import argparse
import abc

class ParseArguments(abc.ABC):
    @abc.abstractmethod    
    def get_arguments(self):
        pass

class ParseArugmentWithJSON(ParseArguments):
    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("file_name", help="the name of the json file to be parsed")
        self.parser.add_argument("-o", "--output", help="the name of the output file", default="results.csv")
        self.args = self.parser.parse_args()
        
    def get_arguments(self):
        return self.args