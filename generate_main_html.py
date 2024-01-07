import os

# Read the HTML file with placeholders
with open("AJO_main_with_placeholder.html", "r") as f:
    html = f.read()

#Read possible options for Aree Settoriali, Institutes, and Regions
with open("support_files/options_aree_settoriali.txt", "r") as f:
    options_areesettoriali = f.readlines()

with open("support_files/options_institutes.txt", "r", encoding="utf-8") as f:
    options_institutes = f.readlines()

with open("support_files/options_regions.txt", "r", encoding="utf-8") as f:
    options_regions = f.readlines()

# Generate the HTML string with options
options_areesettoriali_html = ""
for option in options_areesettoriali:
    options_areesettoriali_html += f"\t\t\t\t<label class=\"filter\"><input type=\"checkbox\" name=\"area-settoriale\" value=\"{option.strip()}\"> {option.strip()}</label>\n"

options_regions_html = ""
for option in options_regions:
    options_regions_html += f"\t\t\t\t<label class=\"filter\"><input type=\"checkbox\" name=\"region\" value=\"{option.strip()}\"> {option.strip()}</label>\n"

options_institutes_html = ""
for option in options_institutes:
    options_institutes_html += f"\t\t\t\t<label class=\"filter\"><input type=\"checkbox\" name=\"institute\" value=\"{option.strip()}\"> {option.strip()}</label>\n"

#Replace the placeholder with the HTML string with options
html = html.replace("<placeholder_filters_regions>", options_regions_html)
html = html.replace("<placeholder_filters_area_settoriale>", options_areesettoriali_html)
html = html.replace("<placeholder_filters_institutes>", options_institutes_html)

# Write the modified HTML to a new file
with open("AJO_main.html", "w") as f:
    f.write(html)