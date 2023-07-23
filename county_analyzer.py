# couny_analyzer.py
from growth_counties import CountyWithGrowth, CountyWithGrowthJSON
from parse_arguments import ParseArugmentWithJSON
from filemanager import JSONFileManager, FileSaver, CSVFileSaver


class CountyAnalyzer:

    def __init__(self, file_name:str, output_file:str, growing_counties:CountyWithGrowth, file_saver:FileSaver):
        self._file_name = file_name
        self._output_file = output_file
        self._growing_counties = growing_counties
        self._file_saver = file_saver
    
    def _save_data(self, data:list):
        self._file_saver.save_data(f'results/{self._output_file}', data)
    
    def get_counties_with_positive_growth(self):
            output_data = self._growing_counties.identify_growing_counties(self._file_name)
            self._save_data(output_data)

def main():
    parser = ParseArugmentWithJSON()
    args = parser.get_arguments()
    output_file = args.output
    file_name = f'raw_files/{args.file_name}'
    analyzer = CountyAnalyzer(file_name, output_file, CountyWithGrowthJSON(JSONFileManager()), CSVFileSaver())
    analyzer.get_counties_with_positive_growth()


if __name__ == "__main__":
    main()