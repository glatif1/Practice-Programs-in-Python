def equal_file(file1, file2, length_of_file):
    for i in range(length_of_file):
        if file1[i] != file2[i]:
            print('Mismatch at character %d %s != %s' % ((i), (file1[i]), (file2[i])))

def compare_files():
    file_name1 = input("Enter File Name: ").strip()
    file_name2 = input("Enter Second File Name: ").strip()

    file1=""
    file2=""

    with open(file_name1) as myfile:
        while True:
            read_file = myfile.read()
            if not read_file:
                break
            file1 += read_file

    with open(file_name2) as myfile:
        while True:
            read_file = myfile.read()
            if not read_file:
                break
            file2 += read_file

    length_of_file = min(len(file1),len(file2))

    equal_file(file1, file2, length_of_file)

    character = length_of_file
    while character<len(file1):
        print('No matching character for character %d (%s) found in %s.' % ((character), (file1[character]), (file_name1)))
        character += 1

    while character<len(file2):
        print('No matching character for character %d (%s) found in %s.' % ((character), (file1[character]), (file_name2)))
        character += 1

    return

compare_files()