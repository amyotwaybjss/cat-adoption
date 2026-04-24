from jinja2 import Environment, FileSystemLoader
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
cats_count = len(cats_list)

environment = Environment(loader=FileSystemLoader('templates/'))
template_homepage = environment.get_template('index_template.html')
template_individual = environment.get_template('cat_page.html')

for cat in cats_list:
    clean_name = cat['Name'].lower().replace(' ', '_')
    filename = f'page_{clean_name}.html'
    output_file = output_file_location + filename
    cat["Url"] = filename
    content = template_individual.render(
        cat,
        image_location = image_location,
        colour_emoji = cat_colour[cat['Colour'].lower()],
    )
    with open(output_file, mode='w') as page:
        page.write(content)
        print(f'Written to {output_file}')

index_output = output_file_location + 'index.html'
table_width = 0.8
col_width = table_width/cats_count

context = {
    "table_width": table_width,
    "col_width": col_width,
    "cats_list": cats_list,
    "image_location": image_location,
}
with open(index_output, mode='w') as index:
    index.write(template_homepage.render(context))
    print(f'Written to {index_output}')
