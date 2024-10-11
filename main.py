import asyncio
import sys
import time

import pandas as pd
from pyexpat import model
from PyQt6 import QtCore, QtGui, QtWidgets

import Algorithms as algo
import RunTimeScrapping
import scrapper
import ui as project_ui


class SortWorker(QtCore.QThread):
    progress = QtCore.pyqtSignal(int)
    finished = QtCore.pyqtSignal(pd.DataFrame, float)
    error = QtCore.pyqtSignal(str, str)

    def __init__(self, df, algorithm, columns, ascending):
        super().__init__()
        self.df = df
        self.algorithm = algorithm
        self.columns = columns
        self.ascending = ascending

    def run(self):
        start_time = time.perf_counter()
        sorted_df = self.df.copy()
        total_time = 0

        for column, asc in zip(reversed(self.columns), reversed(self.ascending)):
            column_data = sorted_df.iloc[:, column].tolist()
            start_time = time.perf_counter()
            try:
                sorted_column_data = self.algorithm(
                    column_data, reverse=not asc, callback=self.emit_progress
                )
            except RecursionError:
                self.emit_error(
                    "Recursion Error",
                    "The selected algorithm cannot handle the size of the data.",
                )
                return
            except Exception as e:
                self.emit_error(
                    "Error", f"An error occurred while sorting the data: {e}"
                )
                return
            end_time = time.perf_counter()
            total_time += end_time - start_time

            indexed_column_data = list(enumerate(column_data))
            indexed_column_data.sort(key=lambda x: sorted_column_data.index(x[1]))

            sorted_indices = [index for index, value in indexed_column_data]

            sorted_df = sorted_df.iloc[sorted_indices].reset_index(drop=True)

        end_time = time.perf_counter()
        run_time = end_time - start_time

        self.finished.emit(sorted_df, run_time)  

    def emit_progress(self, progress):
        self.progress.emit(progress)

    def emit_error(self, title, message):
        self.error.emit(title, message)  
        
    @QtCore.pyqtSlot(str, str)
    def show_error_message(self, title, message):
        QtWidgets.QMessageBox.warning(None, title, message)


class MyApp(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = project_ui.Ui_Window()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.sort_data)
        self.ui.btn_scrap.clicked.connect(self.scrap_data)
        self.ui.btn_search.clicked.connect(self.search)
        self.ui.btn_pause.clicked.connect(self.pause_scraping)
        self.ui.btn_Resume.clicked.connect(self.resume_scraping)
        self.ui.btn_stop.clicked.connect(self.stop_scraping)
        self.ui.btn_start.clicked.connect(self.start_scraping)
        self.df = pd.DataFrame()
        self.load_data()
        self.algorithms = {
            "Bubble Sort": algo.BubbleSort,
            "Insertion Sort": algo.InsertionSort,
            "Merge Sort": algo.MergeSort,
            "Quick Sort": algo.QuickSort,
            "Selection Sort": algo.SelectionSort,
            "Count Sort": algo.CountingSort,
            "Hybrid Merge Sort": algo.HybridMergeSort,
            "Bucket Sort": algo.BucketSort,
            "Radix Sort": algo.RadixSort,
            "Heap Sort": algo.HeapSort,
            "Shell Sort": algo.ShellSort,
        }

    def pause_scraping(self):
        scrapper.pause_scraping()

    def resume_scraping(self):
        scrapper.resume_scraping()

    def stop_scraping(self):
        scrapper.stop_scraping()

    def start_scraping(self):
        scrapper.start_scraping()
        scrapper.scraper.progress.connect(
            self.update_scraping_progress
        )  # Connect progress signal

    def load_data(self):
        if self.df.empty:
            self.df = pd.read_csv("data.csv")
        self.df = self.df.dropna()
        self.df = self.df.applymap(lambda x: x.lower() if isinstance(x, str) else x)

        # Ensure integer columns are not displayed as floats
        for col in self.df.select_dtypes(include=['int', 'float']).columns:
            if all(self.df[col] == self.df[col].astype(int)):
                self.df[col] = self.df[col].astype(int)

        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(self.df.columns.tolist())

        for row in self.df.values.tolist():
            items = [QtGui.QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        self.ui.data_view.setModel(model)

    def search(self):
        search_term = self.ui.txt_search.text().lower()
        filter_type = self.ui.txt_searching_base.currentText()

        # Reset the table if no search term is provided
        if not search_term:
            self.load_data()
            QtWidgets.QMessageBox.warning(
                None, "Error", "Enter something to search. All data loaded."
            )
            return

        # Check if a valid filter type is selected
        if not filter_type:
            QtWidgets.QMessageBox.warning(
                None, "Error", "Select a search type (contains, starts with, ends with)."
            )
            return

        # Copy the original DataFrame to filter
        filtered_df = self.df.copy()

        # Apply the selected filter type
        if filter_type == "Contains":
            filtered_df = filtered_df[
                filtered_df.apply(
                    lambda row: row.astype(str).str.contains(search_term, case=False).any(),
                    axis=1,
                )
            ]
        elif filter_type == "Start with":
            filtered_df = filtered_df[
                filtered_df.apply(
                    lambda row: row.astype(str).str.lower().str.startswith(search_term).any(),
                    axis=1,
                )
            ]
        elif filter_type == "Ends with":
            filtered_df = filtered_df[
                filtered_df.apply(
                    lambda row: row.astype(str).str.lower().str.endswith(search_term).any(),
                    axis=1,
                )
            ]

        # Check if the filtered DataFrame is empty
        if filtered_df.empty:
            QtWidgets.QMessageBox.information(
                None, "No Results", "No matching results found."
            )
            return

        # Clear the existing model
        model = QtGui.QStandardItemModel()
        model.setHorizontalHeaderLabels(filtered_df.columns.tolist())

        # Populate the model with filtered data
        for row in filtered_df.values.tolist():
            items = [QtGui.QStandardItem(str(field)) for field in row]
            model.appendRow(items)

        # Set the model in the data view
        self.ui.data_view.setModel(model)
        self.ui.data_view.update()  # Ensure the view is updated

    def validate_sorting(self, algorithm_name, column_data):
        if algorithm_name == "Radix Sort":
            if any(
                isinstance(num, str)
                or isinstance(num, float)
                and num != int(num)
                or num < 0
                for num in column_data
            ):
                QtWidgets.QMessageBox.warning(
                    None,
                    "Error",
                    "Radix Sort does not support strings, negative, or floating-point values.",
                )
                return False
        elif algorithm_name == "Counting Sort":
            if any(
                isinstance(num, str) or isinstance(num, float) or num < 0
                for num in column_data
            ):
                QtWidgets.QMessageBox.warning(
                    None,
                    "Error",
                    "Counting Sort does not support strings, negative, or floating-point values.",
                )
                return False
        elif algorithm_name == "Bucket Sort":
            if any(isinstance(num, str) or num < 0 for num in column_data):
                QtWidgets.QMessageBox.warning(
                    None,
                    "Error",
                    "Bucket Sort does not support strings or negative values.",
                )
                return False
        return True

    def sort_data(self):
        self.update_progress(0)
        algorithm_name = self.ui.txt_algorithm.currentText()
        sorting_base = self.ui.txt_sorting_base.currentText().strip()
        selected_columns = self.ui.data_view.selectionModel().selectedColumns()

        if not selected_columns:
            QtWidgets.QMessageBox.warning(
                None, "Error", "No columns selected for sorting."
            )
            return

        algorithm = self.algorithms.get(algorithm_name)
        if not algorithm:
            QtWidgets.QMessageBox.warning(
                None, "Error", f"Algorithm '{algorithm_name}' not found."
            )
            return

        columns = [col.column() for col in selected_columns]
        ascending = [sorting_base == "Ascending"] * len(columns)

        for column in columns:
            column_data = self.df.iloc[:, column].tolist()
            if isinstance(column_data[0], str):
                column_data = [str(val) for val in column_data]
                for i, val in enumerate(column_data):
                    if not isinstance(val, str):
                        print(
                            f"Column {column} contains non-string value {val} at index {i}"
                        )
            if not self.validate_sorting(algorithm_name, column_data):
                return

        self.worker = SortWorker(self.df, algorithm, columns, ascending)
        self.worker.progress.connect(self.update_progress)
        self.worker.finished.connect(self.on_sort_finished)
        self.worker.error.connect(self.on_sort_error)
        self.worker.start()
        self.worker.finished.connect(lambda: self.update_progress(0))

    def update_progress(self, value):
        self.ui.progressBar.setValue(value)

    def update_scraping_progress(self, value):
        self.ui.scarpping_bar.setValue(value)

    def on_sort_finished(self, sorted_df, run_time):
        self.df = sorted_df
        self.load_data()
        self.ui.progressBar.setValue(100)
        self.ui.label_5.setText(f"Runtime: {run_time:.3f} seconds")

    def on_sort_error(self, title, message):
        QtWidgets.QMessageBox.warning(None, title, message)

    def scrap_data(self):
        url = self.ui.txt_url.text()  
        if not url.startswith("https://"):
            QtWidgets.QMessageBox.warning(None, "Error", "URL must start with 'https://'")
            return

        try:
            asyncio.run(RunTimeScrapping.scrape_and_save(url))
        except Exception as e:
            QtWidgets.QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")


if __name__ == "__main__":
    try:
        app = QtWidgets.QApplication(sys.argv)
        window = MyApp()
        window.show()
        sys.exit(app.exec())
    except Exception as e:
        QtWidgets.QMessageBox.warning(None, "Error", f"An error occurred: {str(e)}")