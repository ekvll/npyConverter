import os

from load_data import NumpyFileLoader
from logger_setup import logger
from utils import (
    filenames_in_dir,
    validate_file_type,
    save_data_as_mat,
    delete_file,
    save_npy_as_csv,
    load_csv_as_df,
    extract_values_from_df,
)


def process(values: dict) -> None:

    output_fileformat = _fetch_file_type(values)
    valid_file_type = ".npy"
    
    logger.info(f"Input file format {valid_file_type}")
    logger.info(f"Output file format {output_fileformat}")

    path_input = values.get("-NPY_DIR-")
    path_output = values.get("-MAT_DIR-")

    filenames = filenames_in_dir(path_input)

    logger.info("Iterating over files...")
    for idx, filename in enumerate(filenames):
        logger.info("-" * 50)
        logger.info(f"Processing file {idx + 1}/{len(filenames)}: {filename}")

        if validate_file_type(filename, valid_file_type):

            npy_filepath, mat_filepath, csv_filepath = _gen_filepaths(
                path_input, filename, path_output
            )

            npy_data = NumpyFileLoader(npy_filepath).load_file()

            # If output format is .mat
            if "mat" in output_fileformat:
                tmp_csv_filepath = os.path.join(path_output, "tmp_a3b2c1_.csv")
                save_npy_as_csv(npy_data, tmp_csv_filepath)

                df = load_csv_as_df(csv_filepath)
                data_dict = extract_values_from_df(df)

                save_data_as_mat(data_dict, mat_filepath)
                delete_file(tmp_csv_filepath)

            # If output format is .csv
            if "csv" in output_fileformat:
                save_npy_as_csv(npy_data, csv_filepath)

    logger.info("-" * 50)

    _outro(path_output)


def _fetch_file_type(values: dict):
    if values.get("-MAT-"):
        return ".mat"
    elif values.get("-CSV-"):
        return ".csv"
    else:
        return None


def _gen_filepaths(npy_dir, npy_filename, mat_dir):
    npy_filepath = os.path.join(npy_dir, npy_filename)
    mat_filename = os.path.splitext(npy_filename)[0] + ".mat"
    csv_filename = os.path.splitext(npy_filename)[0] + ".csv"
    mat_filepath = os.path.join(mat_dir, mat_filename)
    csv_filepath = os.path.join(mat_dir, csv_filename)
    return npy_filepath, mat_filepath, csv_filepath


def _outro(path_output: str) -> None:
    logger.info("All files processed!")
    logger.info(f"Files saved to: {path_output}")
    logger.info("Feel free to close the application")
    logger.info("=" * 50)
