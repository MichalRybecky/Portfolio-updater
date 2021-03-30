"""
main python file
handles reading from and writing to calc spreadsheet
"""
import pyoo
from time import sleep
from subprocess import Popen
from crawler import get_prices
from options import sheet_number, start_position, file_path


def write_to_cell(row: int, column: int, value):
    sheet[row, column].value = value


def check_tickers_in_file() -> list:
    """
    looks into the file and returns ticker symbols that are there
    """
    row = start_position[0]
    column = start_position[1]
    tickers = []
    while True:
        current_value = sheet[row, column].value
        if current_value == "":
            break
        tickers.append({"ticker": current_value, "row": row})
        row += 1
    return tickers


if __name__ == "__main__":
    # run soffice script and detach it
    soffice = Popen(["sh", "soffice.sh"])
    # wait a little bit to make sure soffice is running properly before we do anything
    # bump it up if you have problems or slower hardware
    sleep(1)

    desktop = pyoo.Desktop("localhost", 2002)

    # open file path imported from options.py
    doc = desktop.open_spreadsheet(file_path)

    # select desired sheet
    sheet = doc.sheets[sheet_number]

    # get dictionary from crawler module and tickers from file
    tickers_in_file = check_tickers_in_file()
    stock_data = get_prices(tickers_in_file)

    for ticker in tickers_in_file:
        ticker, row = ticker["ticker"], ticker["row"]
        write_to_cell(row=row, column=start_position[1] + 1, value=stock_data[ticker])

    # save document
    doc.save()

