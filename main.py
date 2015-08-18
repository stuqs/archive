import os
import zipfile


def get_files_of_a_month(original_list):
    """
    Generates a list of files from one month and year, and remove them from the incoming list
    :param original_list: list of files to process
    :return:
    :original_list: incoming list without arc_list files
    :arc_list: files from one month and year
    :arc_name: string with name of future archive
    """
    year = (str(original_list[0]).split("-")[1])
    month = (str(original_list[0]).split("-")[2])

    arc_name = os.path.join(dir_out, "archive-" + year + "-" + month + ".rar")
    arc_list = []
    for name in original_list[:]:
        if str(original_list[0]).split("-")[1] == year and str(original_list[0]).split("-")[2] == month:
            # Make absolute path
            arc_list.append(os.path.join(dir_in, name))
            original_list.remove(name)
    return original_list, arc_list, arc_name


def create_archieve(arc_list, arc_name):
    """
    Create zip archive with name arc_name and files in arc_list
    :param arc_list: list of files to archive
    :param arc_name: name of archive
    :return: true if successful, else false
    """
    # Make Zip archive
    try:
        with zipfile.ZipFile(arc_name, 'a', compression=zipfile.ZIP_DEFLATED) as zip_archive:
            for name in arc_list:
                zip_archive.write(name, os.path.basename(name))
            zip_archive.close()
    except:
        return False
    return True


def remove_file_list(file_list):
    """
    Delete all files from the list
    :param file_list: list of deleted files
    """
    for file in file_list:
        os.remove(file)


# Input dir
dir_in = r"D:\ARH"
# Output dir
dir_out = r"D:\ARH\WEEKLY"

# Receive list of file from dir
files = os.listdir(dir_in)

# Filter list for txt files
pathes = list(filter(lambda x: x.endswith('.txt'), files))

# Remove last(active) element
if len(pathes) > 1:
    pathes = pathes[0:-1]

    while len(pathes) > 0:

        pathes, arc_list, arc_name = get_files_of_a_month(pathes)

        if create_archieve(arc_list, arc_name):
            remove_file_list(arc_list)
