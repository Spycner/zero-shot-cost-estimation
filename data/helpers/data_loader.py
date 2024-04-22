import json
import os
from types import SimpleNamespace


def load_json(path, namespace=True):
    """
    Loads a JSON file from the specified path and returns the parsed JSON object.

    Args:
        path (str): The path to the JSON file to load.
        namespace (bool, optional): If True, the JSON object is loaded into a SimpleNamespace object. Otherwise, a regular dictionary is returned. Defaults to True.

    Returns:
        Union[SimpleNamespace, dict]: The parsed JSON object.
    """
    with open(path) as json_file:
        if namespace:
            json_obj = json.load(json_file, object_hook=lambda d: SimpleNamespace(**d))
        else:
            json_obj = json.load(json_file)
    return json_obj


def load_schema_json(dataset):
    """
    Loads the schema JSON file for the specified dataset.

    Args:
        dataset (str): The name of the dataset.

    Returns:
        SimpleNamespace: The parsed schema JSON object.
    """
    schema_path = os.path.join("data/datasets/", dataset, "schema.json")

    if not os.path.exists(schema_path):
        raise ValueError(f"Could not find schema.json ({schema_path})")

    return load_json(schema_path)
