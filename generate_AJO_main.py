import os

#Read possible filter cathegories
with open("support_files/filter_cathegories.txt", "r") as f:
    filter_cathegories = [line.strip() for line in f.readlines()]

html_filters = ""

#Loop over filter cathegories
for filter_cathegory in filter_cathegories:
    file_path = f"support_files/options_{filter_cathegory}.txt"

    #Read filter option for the considered cathegory
    with open(file_path, "r", encoding="utf-8") as f:
        options = f.readlines()

    # Remove underscores and capitalize the first letter for filter title
    filter_cathegory_title = filter_cathegory.replace("_", " ").capitalize()

    html_filters += f"\t\t<!-- {filter_cathegory} Group -->\n"
    html_filters += f"\t\t<div class=\"toggleContainer\" onclick=\"toggleOptions('{filter_cathegory}List', '{filter_cathegory}Arrow')\">\n"
    html_filters += f"\t\t\t<div class=\"toggleElementContainer\">\n"
    html_filters += f"\t\t\t<img class=\"toggleElement\" src=\"Images/RightArrowShort.svg\" alt=\">\" id=\"{filter_cathegory}Arrow\">\n"
    html_filters += f"\t\t\t<div class=\"optionsText\">{filter_cathegory_title}</div>\n\t\t\t</div>\n\t\t</div>\n\n"
    
    # List all options in the html
    html_filters += f"\t\t<ul class=\"optionsList {filter_cathegory}List\">\n"
    for option in options:
        html_filters += f"\t\t\t<li> <input type=\"checkbox\" class=\"optionCheckbox\" id=\"{option.strip()}\"> <label for=\"{option.strip()}\">{option.strip()}</label> </li>\n"
    html_filters += f"\t\t</ul>\n\n"

# Read the HTML file with placeholders
with open("AJO_main_placeholders.html", "r") as f:
    html_placeholders = f.read()

#Replace the placeholder with the HTML string with options
html = html_placeholders.replace("<placeholder_filters>", html_filters)

# Write the modified HTML to a new file
with open("AJO_main.html", "w") as f:
    f.write(html)