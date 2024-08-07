import logging
from typing import Union, Tuple, List

import PySimpleGUI as sg

from logger_setup import logger
from processing import process


class NpyConverter:
    def __init__(self):
        self.layout = self.create_layout()
        self.window = sg.Window("npyConverter", self.layout, finalize=True)

    def create_layout(self) -> List[List[sg.Element]]:
        return [
            [sg.Text("Input directory .npy files:")],
            [sg.Input(key="-NPY_DIR-"), sg.FolderBrowse()],
            [sg.Text("Output directory:")],
            [sg.Input(key="-MAT_DIR-"), sg.FolderBrowse()],
            [
                sg.Text("Output file format:"),
                sg.Radio(".mat", "FILE_FORMAT", key="-MAT-", default=True),
                sg.Radio(".csv", "FILE_FORMAT", key="-CSV-"),
            ],
            [sg.Button("Convert"), sg.Button("Contact Info"), sg.Button("Cancel")],
        ]
    
    def run(self) -> None:
        logger.info("Starting application...")

        while True:
            event, values = self.window.read()

            if event in (sg.WIN_CLOSED, "Cancel"):
                logger.info("Application closed by user")
                break

            if event == "Convert":
                process(values)

            if event == "Contact Info":
                sg.popup(
                    "Contact Information",
                    "Creator: Erik Lindvall\nEmail: erik.lindvall@ri.se",
                    keep_on_top=True,
                )

        self.window.close()


if __name__ == "__main__":
    NpyConverter().run()
