from bs4 import BeautifulSoup

# Read the HTML file
with open("downloaded_html/cercaFellowship.html", "r", encoding="utf-8") as f:
    html = f.read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# Extract all the options from the HTML file
options = []
for select in soup.find_all("select"):
    options.extend([option.text for option in select.find_all("option")])

# Remove leading and trailing whitespace characters and newline characters
options = [option.strip().replace("\n", "") for option in options]

# Remove the first 4 elements of the list (referring to Aperti, Scaduti, etc)
options = options[4:]

# Find the index of the first occurrence of "Tutti", to separate the institutes from the Aree Disciplinari
index = options.index("Tutti")

institutes = options[:index]  # List with Institutes
areedisciplinari = options[index + 1:]  # List with Aree Disciplinari

# Write the options to text files
with open("support_files/options_institutes.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(institutes))

with open("support_files/options_aree_settoriali.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(areedisciplinari))
