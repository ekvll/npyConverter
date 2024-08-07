import os
from typing import Union, List

import numpy as np
import pandas as pd
from scipy.io import savemat

from logger_setup import logger


def validate_file_type(filename: str, target_type: str) -> bool:
    if filename.endswith(target_type):
        logger.info(f"Valid file type")
        return True
    else:
        logger.error(f"Invalid file type. Jumping to next file...")
        return False


def filenames_in_dir(path: str) -> List[str]:
    logger.info(f"Reading files from: {path}")
    try:
        filenames = [
            f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))
        ]

        logger.info(f"Found {len(filenames)} file(s)")
        return filenames

    except Exception as e:
        logger.error(f"Error reading directory: {e}. Returning empty list")
        return []


def save_data_as_mat(data_dict: dict, filepath: str) -> None:
    try:
        logger.info(f"Saving file as .mat file")
        savemat(filepath, data_dict)
        logger.info(f"Saved successfully")

    except Exception as e:
        logger.error(f"Error when saving as .mat file: {e}")


def delete_file(path: str) -> None:
    if os.path.exists(path):
        os.remove(path)
    else:
        logger.error(f"The file does not exist: {path}")


def save_npy_as_csv(npy_data, csv_filepath: str) -> None:
    try:
        np.savetxt(csv_filepath, npy_data, delimiter=",")
    except Exception as e:
        logger.error(f"Error when saving as .csv file: {e}")


def load_csv_as_df(csv_filepath: str) -> Union[pd.DataFrame, None]:
    try:
        df = pd.read_csv(csv_filepath, header=None)
        return df
    except Exception as e:
        logger.error(f"Error when loading .csv file: {e}. Returning None")
        return None


def extract_values_from_df(df: pd.DataFrame) -> dict:
    data_dict = {"data": df.values}
    return data_dict


def extract_dirpath(filepath: str):
    if os.path.isdir(filepath):
        return filepath
    else:
        return os.path.dirname(filepath)
