import os

#Read options for Aree Settoriali
with open("support_files/options_aree_settoriali.txt", "r") as f:
    options_areesettoriali = f.readlines()

#Read options for Institutes
with open("support_files/options_institutes.txt", "r", encoding="utf-8") as f:
    options_institutes = f.readlines()

#Read options for Regions
with open("support_files/options_regions.txt", "r", encoding="utf-8") as f:
    options_regions = f.readlines()

#Open html and header
html = "<!DOCTYPE html>\n<html>\n<head>\n\t<title>Filtri</title>\n\t<style>\n\t\t.filter {\n\t\t\tdisplay: block;\n\t\t\tmargin-bottom: -3px;\n\t\t}\n\t\t.listings {\n\t\t\tdisplay: inline-block;\n\t\t\tmargin-left: 20px;\n\t\t\tvertical-align: top;\n\t\t}\n\t</style>\n</head>\n<body>\n\t<h1>Filters</h1>\n"

#Filters Aree Settoriali
html += "\t<div class=\"filter-container\">\n\t\t<div class=\"filter-category\">\n\t\t\t<h2>Area Settoriale</h2>\n\t\t\t<form>\n"

for option in options_areesettoriali:
    html += f"\t\t\t\t<label class=\"filter\"><input type=\"checkbox\" name=\"area-settoriale\" value=\"{option.strip()}\"> {option.strip()}</label>\n"

html += "\t\t\t</form>\n\t\t</div>\n\t</div>\n"

#Filters Regions
html += "\t<div class=\"filter-container\">\n\t\t<div class=\"filter-category\">\n\t\t\t<h2>Regione</h2>\n\t\t\t<form>\n"

for option in options_regions:
    html += f"\t\t\t\t<label class=\"filter\"><input type=\"checkbox\" name=\"region\" value=\"{option.strip()}\"> {option.strip()}</label>\n"

html += "\t\t\t</form>\n\t\t</div>\n\t</div>\n"

#Filters Institutes
html += "\t<div class=\"filter-container\">\n\t\t<div class=\"filter-category\">\n\t\t\t<h2>Istituto</h2>\n\t\t\t<form>\n"

for option in options_institutes:
    html += f"\t\t\t\t<label class=\"filter\"><input type=\"checkbox\" name=\"institute\" value=\"{option.strip()}\"> {option.strip()}</label>\n"

html += "\t\t\t</form>\n\t\t</div>\n\t</div>\n"

#Close html
html += "</body>\n</html>"

if not os.path.exists("support_files"):
    os.makedirs("support_files")

with open("support_files/AJO_filter_page.html", "w") as f:
    f.write(html)