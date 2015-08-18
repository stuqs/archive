from os import listdir, path
from zipfile import ZipFile


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

    arc_name = dir_out + "archive-" + year + "-" + month + ".rar"
    arc_list = []
    for name in original_list[:]:
        if str(original_list[0]).split("-")[1] == year and str(original_list[0]).split("-")[2] == month:
            arc_list.append(name)
            original_list.remove(name)
    return original_list, arc_list, arc_name


def create_archieve(arc_list, arc_name):
    """
    Create zip archive with name arc_name and files in arc_list
    :param arc_list: list of files to archive
    :param arc_name: name of archive
    :return: true if successful, else false
    """
    # Make absolute path
    for i in range(len(arc_list) - 1):
        arc_list[i] = path.abspath(arc_list[i])
    # Make Zip archive
    try:
        print(arc_name)
        with ZipFile(arc_name, 'a') as zip_archive:
            for name in arc_list:
                zip_archive.write(name)
            zip_archive.close()
    except IOError:
        return False
    return True


# Input dir
dir = r"D:\\ARH"
# Output dir
dir_out = r"D:\\ARH\\WEEKLY\\"

# Receive list of file from dir
files = listdir(dir)

# Filter list for txt files
pathes = list(filter(lambda x: x.endswith('.txt'), files))

# Remove last(active) element
if len(pathes) > 1:
    pathes = pathes[0:-1]

print(pathes)
print("-"*20)

while len(pathes) > 0:

    pathes, arc_list, arc_name = get_files_of_a_month(pathes)

    if create_archieve(arc_list, arc_name):
        # TODO delete arc_list
        pass
    else:
        # TODO create log
        pass


    print(pathes)
    print(arc_list)
    print(arc_name)
    print("-"*20)







