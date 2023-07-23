# growth_counties.py
import abc
from constants import CountyParams
from filemanager import FileManager


class CountyWithGrowth(abc.ABC):
    @abc.abstractmethod
    def identify_growing_counties(self, file_name:str):
        pass


class CountyWithGrowthJSON(CountyWithGrowth):
    def __init__(self, file_manager:FileManager) -> None:
        self._file_manager = file_manager
    
    def _get_data(self, file_name:str)->dict:
        data = self._file_manager.get_data(file_name)
        return data
    
    def _start_searching_through_data(self, data:dict)->dict:
        counties_with_positive_growth = []
        counties_with_positive_growth.append('County,Population,Growth Rate\n')
        for county in data:
            if county[CountyParams.GROWTH.value] > 0:
                data_entry = f"{county[CountyParams.COUNTY.value]},{county[CountyParams.POPULATION.value]},{county[CountyParams.GROWTH.value]}\n"
                counties_with_positive_growth.append(data_entry)
        return counties_with_positive_growth
 
    def identify_growing_counties(self, file_name:str)->dict:
        try:
            data = self._file_manager.get_data(file_name)
            output_data = self._start_searching_through_data(data)
        except FileNotFoundError as error:
            output_data = f'{error} File Not Found'
        except TypeError as error:
            output_data = 'Probably put down the wrong file name'
        return output_data