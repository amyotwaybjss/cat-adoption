# Template needs to count number of cats and split into groups of three (can adjust later)
# Fill out cat name with coloured hearts either side, picture, then info on name, gender, age, breed and a link to click.
# User click through to page with full picture of cat and other details

from jinja2 import Environment, FileSystemLoader
import openpyxl as xl
import pandas as pd

image_location = '../images/'
import_file = 'cat_database.xlsx'
output_file_location = 'output/'

cat_colour = {
    "orange" : "🧡",
    "black" : "🖤",
    "grey" : "🩶",
    "white" : "🤍"
}

cat_database = pd.ExcelFile(import_file)
cat_sheet = cat_database.parse(cat_database.sheet_names[0])
cats_dict = cat_sheet.T.to_dict()
cats_list = list(cats_dict.values())

environment = Environment(loader=FileSystemLoader('templates/'))
template = environment.get_template('cat_page.html')

for cat in cats_list:
    filename = f'page_{cat['Name']}.html'
    output_file = output_file_location + filename
    content = template.render(
        cat,
        image_location=image_location,
        colour_emoji = cat_colour[cat['Colour'].lower()],
    )
    with open(output_file, mode='w') as page:
        page.write(content)
        print(f'Written to {output_file}')