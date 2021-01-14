import pyoo
from time import sleep
from subprocess import Popen
from crawler import get_prices


def write_to_cell(column: str, row, value):
    location = column + str(row)
    cell = active_sheet.getCellRangeByName(location)
    cell.String = value


def write_to_spreadsheet(stock_info: dict):
    for i, stock in enumerate(stock_info):
        write_to_cell('A', i+1, stock['ticker'])
        write_to_cell('B', i+1, stock['price'])

soffice = Popen(['sh', 'soffice.sh'])
sleep(3)

desktop = pyoo.Desktop('localhost', 2002)
doc = desktop.open_spreadsheet("/home/michal/Cloud Sync/Finance.xlsx")
sheet = doc.sheets[5]

sheet[0,0].value = 1
# # Set cell formula and get value:
# sheet[0,2].formula = '=$A$1+$B$1'
print(sheet[0,0].value)
