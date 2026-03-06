# Template needs to count number of cats and split into groups of three (can adjust later)
# Fill out cat name with coloured hearts either side, picture, then info on name, gender, age, breed and a link to click.
# User click through to page with full picture of cat and other details

from jinja2 import Environment, FileSystemLoader
import openpyxl as xl
import pandas as pd

image_location = 'images/'
import_file = 'cat database.xlsx'

cat_database = pd.ExcelFile(import_file)
cat_sheet = cat_database.parse(cat_database.sheet_names[0])
cats_dict = cat_sheet.T.to_dict()
cats_list = list(cats_dict.values())

print(cats_list)

# cat_database = xl.load_workbook('cat database.xlsx')
# cat_sheet = cat_database['Sheet1']


# data = cat_sheet.values
# # Get first line in file as header line
# columns = next(data)[0:]
#
# df = pd.DataFrame(data, columns=columns)
#
# print(df.head(2))