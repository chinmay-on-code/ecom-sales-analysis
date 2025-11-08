from pathlib import Path
import pandas as pd

class Olist:
    def __init__(self):
        pass
    """
    The Olist class provides methods to interact with Olist's e-commerce data.

    Methods:
        get_data():
            Loads and returns a dictionary where keys are dataset names (e.g., 'sellers', 'orders')
            and values are pandas DataFrames loaded from corresponding CSV files.
    """
    def get_data(self):
        """
        This function returns a Python dict.
        Its keys should be 'sellers', 'orders', 'order_items' etc...
        Its values should be pandas.DataFrames loaded from csv files
        """

        csv_path = Path("/Users/chinmaybhosale/code/01-Data-Analysis/csv").expanduser()

        file_paths = list(csv_path.iterdir())

        file_names =[]
        for file in file_paths:
            file_names.append(file.name)

        key_names_for_data_dict = []
        for file in file_names:
            key_name = file.replace(".csv", " ").replace("_dataset", " ").replace("olist_", " ").strip()
            key_names_for_data_dict.append(key_name)

        data = {}

        for (key, value) in zip(key_names_for_data_dict, file_paths):
            data[key] = pd.read_csv(value)

        return data
