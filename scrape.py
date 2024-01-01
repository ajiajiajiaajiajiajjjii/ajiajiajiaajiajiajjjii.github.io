import pandas as pd
import wget

# write webpage https://bandi.miur.it/bandi.php/public/cercaFellowship?jf_comp_status_id=2-3&bb_type_code=%25&idarea=%25&azione=cerca
# to a file

url = "https://bandi.miur.it/bandi.php/public/cercaFellowship?jf_comp_status_id=2-3&bb_type_code=%25&idarea=%25&azione=cerca"

output_directory = "downloaded_html"
# filename = wget.download(url, out=output_directory)  # todo this gives error if the file exists
filename = "cercaFellowship"

# find all lines which include /bandi.php/public/fellowship/id_fellow/252922 and store the number
# of the fellowship in a list

fellowship_numbers = []
with open(output_directory + "/" + filename, "r") as f:
    for line in f:
        if "/bandi.php/public/fellowship/id_fellow/" in line:
            fellowship_numbers.append(line.split("/")[5].split("\"")[0])

# print(len(fellowship_numbers))
# print(fellowship_numbers[0:10])

# save this list in "downloaded_html/fellowship_numbers_new.txt"
with open(output_directory + "/fellowship_numbers_new.txt", "w") as f:
    for item in fellowship_numbers:
        f.write("%s\n" % item)

# read the list from "downloaded_html/fellowship_numbers_old.txt"
# and compare it with the new list
# if there are differences, download the html pages of the new fellowships
with open(output_directory + "/fellowship_numbers_old.txt", "r") as f:
    fellowship_numbers_old = f.read().splitlines()

# find the difference
fellowship_numbers_new = list(set(fellowship_numbers) - set(fellowship_numbers_old))

print(fellowship_numbers_new)

# loop over all entries in the list and download the corresponding page
for fellowship_number in fellowship_numbers_new:
    url = "https://bandi.miur.it/bandi.php/public/fellowship/id_fellow/" + fellowship_number
    # extension html
    filename = wget.download(url, out=output_directory + "/fellowships")

# read the file "downloaded_html/fellowships/255205" and extract all fields between <th> and </th> and the corresponding
# values between <td> and </td> in a dictionary

fellowship_dict_list = []
# todo do this loop only on the new pages
for index in fellowship_numbers_new:
    # read the file "downloaded_html/fellowships/255205"
    filename = f"downloaded_html/fellowships/{index}"

    with open(filename, "r") as f:
        keys_list = []
        values_list = []
        for line in f:
            if "<th>" in line or "<th >" in line:
                key = line.split(">")[1].split("<\th")[0]
                keys_list.append(key)
                # read the following lines until </td> and store the value
                value = ""
                while "</td>" not in line:
                    line = next(f)
                    value += line.strip()
                values_list.append(value)
                # todo clean up all keys and values

    # create dict
    fellowship_dict = dict(zip(keys_list, values_list))
    fellowship_dict_list.append(fellowship_dict)

# convert to a pandas dataframe
df = pd.DataFrame(fellowship_dict_list)

# store to json
df.to_json("fellowships.json", orient="records")

# todo remove the ones for which deadline is passed

