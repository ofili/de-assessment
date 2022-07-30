import json
import os




# get data_dir
def get_data_dir():
    """
    Get the data directory
    """
    data_dir = os.path.abspath(__file__ + '../../data')
    
    print(f'Data directory: {data_dir}')
    return data_dir
    

if __name__ == '__main__':
    get_data_dir()
    
    # path to continents.json
    continents_json = os.path.join(get_data_dir(), 'continents.json')

    # path to languages.json
    languages_json = os.path.join(get_data_dir(), 'languages.json')

    # path to countries.json
    countries_json = os.path.join(get_data_dir(), 'countries.json')
