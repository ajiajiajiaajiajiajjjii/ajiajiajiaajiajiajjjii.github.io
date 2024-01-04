import os
from datetime import datetime

import pandas as pd
import wget


def modify_all_accents(string):
    """
    Modifies all accents in a string
    :param string: the string to modify
    :return: the modified string
    """
    string = string.replace("&agrave;", "à")
    string = string.replace("&eacute;", "é")
    string = string.replace("&egrave;", "è")
    string = string.replace("&igrave;", "ì")
    string = string.replace("&ograve;", "ò")
    string = string.replace("&ugrave;", "ù")
    # capital letters
    string = string.replace("&Agrave;", "À")
    string = string.replace("&Eacute;", "É")
    string = string.replace("&Egrave;", "È")
    string = string.replace("&Igrave;", "Ì")
    string = string.replace("&Ograve;", "Ò")
    string = string.replace("&Ugrave;", "Ù")

    return string


def wget_with_retry(url, output_directory, allow_overwrite, max_trials=3):
    """
    Downloads a file with wget, retrying if it fails
    :param url: the url of the file to download
    :param output_directory: the output directory
    :param allow_overwrite: whether to overwrite the file if it already exists
    :param max_trials: the maximum number of trials
    :return: None
    """
    # check whether the file exists:
    filename = output_directory + "/" + url.split("/")[-1].split("?")[0] + ".html"
    # print(filename)
    if os.path.exists(filename):
        if allow_overwrite:
            # remove that file
            os.remove(filename)
        else:
            print(f"File {filename} already exists and allow_overwrite is False")
            return filename

    for i in range(max_trials):
        try:
            filename = wget.download(url, out=filename)
            print(f"Successfully downloaded {url}")
            return filename
        except:  # todo specify the exception
            print(f"Failed to download {url} on trial {i + 1} out of {max_trials}")
            continue
    else:
        print(f"Failed to download {url} after {max_trials} trials")


def download_pages(fellowship_numbers, output_directory, type):
    """
    Downloads the fellowship pages
    :param fellowship_numbers: a list of fellowship numbers
    :return: None
    """
    # loop over all entries in the list and download the corresponding page
    for fellowship_number in fellowship_numbers:
        url = f"https://bandi.miur.it/bandi.php/public/{type}/id_fellow/" + fellowship_number
        # extension html
        filename = wget_with_retry(url, output_directory + f"/{type}s", allow_overwrite=False)


def extract_fellowship_numbers(filename):
    """
    Extracts the fellowship numbers from a file
    :param filename: the name of the file
    :return: a list of fellowship numbers
    """
    fellowship_numbers = []
    with open(filename, "r") as f:
        for line in f:
            if "/bandi.php/public/fellowship/id_fellow/" in line:
                fellowship_numbers.append(line.split("/")[5].split("\"")[0])
    return fellowship_numbers


def save_list_to_file(list_to_save, filename):
    """
    Saves a list to a file
    :param list_to_save: a list to save
    :param filename: the name of the file
    :return: None
    """
    with open(filename, "w") as f:
        for item in list_to_save:
            f.write("%s\n" % item)


def read_list_from_file(filename):
    """
    Reads a list from a file
    :param filename: the name of the file
    :return: the list
    """
    with open(filename, "r") as f:
        read_list = f.read().splitlines()
    return read_list


output_directory = "downloaded_pages"

urls = [
    "https://bandi.miur.it/bandi.php/public/cercaFellowship?jf_comp_status_id=2-3&bb_type_code=%25&idarea=%25&azione=cerca"]
types = ["fellowship"]
# todo add urls for the other types

for url, opening_type in zip(urls, types):
    # write webpage https://bandi.miur.it/bandi.php/public/cercaFellowship?jf_comp_status_id=2-3&bb_type_code=%25&idarea=%25&azione=cerca
    # to a file
    filename = wget_with_retry(url, output_directory, allow_overwrite=False)  # todo this should be set to True, used for debug

    # find all lines which include /bandi.php/public/fellowship/id_fellow/252922 and store the number
    # of the fellowship in a list

    fellowship_numbers_new = extract_fellowship_numbers(filename)

    # print(len(fellowship_numbers_new))
    # print(fellowship_numbers_new[0:10])

    # read the list from "downloaded_pages/fellowship_numbers_current.txt"
    # and compare it with the new list
    # if there are differences, download the html pages of the new fellowships
    fellowship_numbers_old = read_list_from_file(output_directory + f"/{opening_type}_numbers_current.txt")

    # save the new list in f"{output_directory}/fellowship_numbers_current.txt"
    save_list_to_file(fellowship_numbers_new, output_directory + f"/{opening_type}_numbers_current.txt")

    # find the difference
    fellowship_numbers_diff = list(set(fellowship_numbers_new) - set(fellowship_numbers_old))

    print(fellowship_numbers_diff)

    # download the pages that have been added now. Notice this does not re-download the previous ones so we do not know
    # if things have changed
    download_pages(fellowship_numbers_diff, output_directory=output_directory, type=opening_type)

    # read the files "downloaded_pages/fellowships/<fellowship_number>" and extract all fields between <th> and </th> and the corresponding
    # values between <td> and </td> in a dictionary
    fellowship_dict_list = []

    for index in fellowship_numbers_diff:
        print(index)
        # read the file "downloaded_pages/fellowships/{index}"
        filename = f"{output_directory}/{opening_type}s/{index}.html"

        with open(filename, "r") as f:
            keys_list = []
            values_list = []
            for line in f:
                if "<th>" in line or "<th >" in line:

                    # store the key
                    key = line.split(">")[1].split("<\th")[0][:-4].strip()

                    # clean up the key
                    # remove <span style... from key if present
                    if "<span style" in key:
                        key = key.split("<span")[0].strip()
                    # replace "&ograve" with "ò" and "&agrave" with "à"
                    key = key.replace("&ograve;", "ò")
                    key = key.replace("&agrave;", "à")

                    keys_list.append(key)
                    # read the following lines until </td> and store the value
                    value = ""
                    while "</td>" not in line:
                        line = next(f)
                        value += line.strip()

                    # clean up value
                    # only keep things between "<td.*> and </td>
                    value = value.split("<td")[1].split("</td>")[0][1:].strip()
                    # remove <br /> from value
                    value = value.replace("<br />", "")
                    # remove "class=justify livelink"> from value, if it starts with that:
                    if value.startswith("class="):
                        # keep only things after ">"
                        value = value.split(">")[1]
                    # value = value.replace("class=justify livelink\">", "")
                    # if href, only keep things between > and </a>
                    if "<a href" in value:
                        value = value.split(">")[1].split("</a>")[0][:-3].strip()
                    # accents
                    value = modify_all_accents(value)

                    values_list.append(value)

                if "<strong>" in line:
                    # this is the University
                    value = line.split("<strong>")[1].split("</strong>")[0].strip()

                    # clean up value
                    # only keep things between "<strong> and </strong>
                    value = modify_all_accents(value)

                    key = "university"

                    keys_list.append(key)
                    values_list.append(value)

            keys_list.append("index")
            values_list.append(index)

        # print(len(keys_list))
        # create dict
        fellowship_dict = dict(zip(keys_list, values_list))
        fellowship_dict_list.append(fellowship_dict)

    # convert to a pandas dataframe
    df_diff = pd.DataFrame(fellowship_dict_list)
    print(df_diff.shape)
    df_diff["type"] = opening_type  # add the type of opening

    # now I load the old dataframe and merge it with df_diff
    df_old = pd.read_json(f"{opening_type}s.json", orient="records")

    # discard those for which deadline is passed:
    df_old = df_old[df_old['Data di scadenza del bando'] > datetime.now()]
    # todo also need to delete the old files (or move to a different folder for archiving)

    # merge
    df = pd.concat([df_old, df_diff])

    # save back to json
    df.to_json(f"{opening_type}s.json", orient="records")
