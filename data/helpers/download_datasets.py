import logging
import os
import shutil

from data.helpers.data_loader import load_schema_json


logger = logging.getLogger(__name__)


def is_download_successful(table):
    """
    Checks if the download of the specified table was successful.

    Args:
        table (str): The name of the table that was downloaded.

    Returns:
        bool: True if the download was successful, False otherwise.
    """
    if not os.path.exists(f"{table}.csv"):
        return False

    filesize = os.path.getsize(f"{table}.csv")
    return filesize > 0


def download_dataset(rel_fit_dataset_name, dataset_name, data_dir="data/datasets"):
    """
    Downloads the specified dataset from the relational.fit.cvut.cz MySQL database.

    Args:
        rel_fit_dataset_name (str): The name of the dataset in the relational.fit.cvut.cz database.
        dataset_name (str): The name of the dataset to be used as the directory name for storing the downloaded data.
        data_dir (str, optional): The directory where the dataset will be stored. Defaults to "data/datasets".

    Raises:
        ValueError: If a table could not be downloaded after 3 retries.
    """
    schema = load_schema_json(dataset_name)

    dataset_dir = os.path.join(data_dir, dataset_name)
    os.makedirs(dataset_dir, exist_ok=True)

    for table in schema.tables:
        retries = 0
        target_table_file = os.path.join(dataset_dir, f"{table}.csv")

        if not os.path.exists(target_table_file):
            while not is_download_successful(table) and retries < 3:
                #! Note: relational.fit.cvut.cz doesn't seem reachable anymore
                logger.warning(
                    "relational.fit.cvut.cz doesn't seem reachable anymore, this may not work. Please refer to the README.md"
                )

                retries += 1
                download_cmd = f'echo "select * from `{table}`;" | mysql --host=relational.fit.cvut.cz --user=guest --password=relational {rel_fit_dataset_name} > {table}.csv'
                logger.info(download_cmd)
                os.system(download_cmd)

            if not is_download_successful(table):
                raise ValueError(f"Could not download table {table}")

            shutil.move(f"{table}.csv", target_table_file)

        elif is_download_successful(table):
            logger.info(f"Skipping download for {table}, already downloaded")
        else:
            logger.warning(f"Download failed for table: {table}")
