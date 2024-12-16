import os
import random
from pathlib import Path

def process_user_data(data_dict, key, index_list):
    try:
        # Attempt to retrieve a value by key from the dictionary
        value = data_dict[key]
        # Convert the retrieved value to a float
        float_value = float(value)
        # Use the float (after converting it to int) as an index for another list
        result = index_list[int(float_value)]
        print(f"Processed result: {result}")
    except KeyError as e:
        print(f"KeyError: The key '{e.args[0]}' was not found in the dictionary.")
    except ValueError as e:
        print("tisk:", e)
        print(f"ValueError: Unable to convert '{value}' to a float. Details: {e}")
    except IndexError as e:
        print(f"IndexError: The index derived from '{float_value}' is out of range. Details: {e}")
# Example usage
data = {'a': '10', 'b': '3.5', 'c': 'not_a_number'}
list_data = [100, 200, 300, 400, 500]
process_user_data(data, 'a', list_data)   # out of range
process_user_data(data, 'b', list_data)   # Should trigger IndexError
process_user_data(data, 'c', list_data)   # Should trigger ValueError
process_user_data(data, 'd', list_data)   # Should trigger KeyError