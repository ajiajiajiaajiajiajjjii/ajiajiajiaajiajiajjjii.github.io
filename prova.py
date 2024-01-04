import os

num_options_display = 4

with open(os.path.join("support_files", "options_regions.txt"), "r") as f:
    regions = [line.strip() for line in f.readlines()]

html = "<!DOCTYPE html>\n<html>\n<head>\n\t<title>Italian Regions</title>\n\t<style>\n\t\t.hidden {\n\t\t\tdisplay: none;\n\t\t}\n\t</style>\n</head>\n<body>\n\t<h1>Italian Regions</h1>\n\t<ul>\n"
for i in range(num_options_display):
    html += f"\t\t<li>{regions[i]}</li>\n"
for i in range(num_options_display, len(regions)):
    html += f"\t\t<li class=\"hidden\">{regions[i]}</li>\n"
html += f"\t</ul>\n\t<a href=\"#\" onclick=\"showMore()\">Show more ({len(regions)})</a>\n\t<a href=\"#\" onclick=\"showLess()\" class=\"hidden\">Show less ({num_options_display})</a>\n\t<script>\n\t\tfunction showMore() {{\n\t\t\tvar hiddenRegions = document.querySelectorAll(\".hidden\");\n\t\t\tfor (var i = 0; i < hiddenRegions.length; i++) {{\n\t\t\t\thiddenRegions[i].style.display = \"list-item\";\n\t\t\t}}\n\t\t\tdocument.querySelector(\"a\").style.display = \"none\";\n\t\t\tdocument.querySelector(\"a.hidden\").style.display = \"inline\";\n\t\t}}\n\t\tfunction showLess() {{\n\t\t\tvar hiddenRegions = document.querySelectorAll(\".hidden\");\n\t\t\tfor (var i = 0; i < hiddenRegions.length; i++) {{\n\t\t\t\thiddenRegions[i].style.display = \"none\";\n\t\t\t}}\n\t\t\tdocument.querySelector(\"a.hidden\").style.display = \"none\";\n\t\t\tdocument.querySelector(\"a\").style.display = \"inline\";\n\t\t}}\n\t</script>\n</body>\n</html>"

if not os.path.exists("support_files"):
    os.makedirs("support_files")

with open(os.path.join("support_files", "prova.html"), "w") as f:
    f.write(html)
