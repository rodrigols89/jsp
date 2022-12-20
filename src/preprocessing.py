from __future__ import annotations

import platform
from datetime import datetime

import pandas as pd
import py7zr


class Preprocessing:
    def extract_7z_data(self, path):

        start_time = datetime.now()

        # For Windows users.
        if platform.system() == "Windows":
            try:

                with py7zr.SevenZipFile(path, mode="r") as archive:
                    archive.extractall(path=r"C:\Windows\Temp")
            except FileNotFoundError:
                print("File or path not found!")
            else:
                print("File extracted!")
        # For Linux users.
        elif platform.system() == "Linux":
            try:
                with py7zr.SevenZipFile(path, mode="r") as archive:
                    archive.extractall(path="/tmp")
            except FileNotFoundError:
                print("File or path not found!")
            else:
                print("File extracted!")
        else:
            print("This method only works with Windows and Linux O.S.")

        # Time used to extract the file.
        end_time = datetime.now()
        print(f"Method runtime: {end_time - start_time}")

    def get_training_data(self):

        start_time = datetime.now()

        # For Windows users.
        if platform.system() == "Windows":
            try:
                df_training = pd.read_csv(r"C:\Windows\Temp\Train_rev1.csv")
            except FileNotFoundError:
                print("File or path not found!")
            else:
                print("Training data is ready!")
                # Time used to get the file.
                end_time = datetime.now()
                print(f"Method runtime: {end_time - start_time}")
                return df_training
        # For Linux users.
        elif platform.system() == "Linux":
            try:
                df_training = pd.read_csv("/tmp/Train_rev1.csv")
            except FileNotFoundError:
                print("File or path not found!")
            else:
                print("Training data is ready!")
                # Time used to get the file.
                end_time = datetime.now()
                print(f"Method runtime: {end_time - start_time}")
                return df_training

    def get_testing_data(self):

        start_time = datetime.now()

        # For Windows users.
        if platform.system() == "Windows":
            try:
                df_testing = pd.read_csv(r"C:\Windows\Temp\Test_rev1.csv")
            except FileNotFoundError:
                print("File or path not found!")
            else:
                print("Testing data ready!")
                # Time used to get the file.
                end_time = datetime.now()
                print(f"Method runtime: {end_time - start_time}")
                return df_testing
        # For Linux users.
        elif platform.system() == "Linux":
            try:
                df_testing = pd.read_csv("/tmp/Test_rev1.7z")
            except FileNotFoundError:
                print("File or path not found!")
            else:
                print("Testing data ready!")
                # Time used to get the file.
                end_time = datetime.now()
                print(f"Method runtime: {end_time - start_time}")
                return df_testing
