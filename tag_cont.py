import os
import re


# reads the file and clears it from garbage
def file_reader(file, file_address):
    file_address = file_address + '/' + file
    #print(file)
    tags = 0
    with open(file_address, encoding='utf-8') as file:
        raw_data = file.read()
        pos_ann = re.compile("T\d+\t[A-Z]{2,}.*\n#\d+.*'")
        pos = re.sub(pos_ann, '',  raw_data)
        correction = re.compile('#.*\n')
        corrections = re.sub(correction, '',  pos)
        #print(corrections)
        our_tag = re.compile('Category_confusion')
        our_tags = re.findall(our_tag, corrections)
        print(our_tags)
        tags = len(our_tags)
        print(tags)
        #print(lines)

    return tags


# finds all the files in the given directory, for convenience sake create a folder named REALEC and put the folders you
# want to work with there
def file_finder():
    print("Insert the folder's name")
    where = input()
    file_address = '/Users/elizavetaersova/PycharmProjects/approximation/REALEC/' + where
    files = os.listdir(file_address)
    print(files)
    return files, file_address


# determines the type of file you are after, there are 3 - .txt, .json and .ann and also subtypes like _1.ann for
# annotation files for graph description essays
def tag_counter(files, file_address):
    ann_files = []
    tags = 0
    for i in files:
        if i.endswith('.ann'):
            ann_files.append(i)

    for file in ann_files:
        tags += file_reader(file, file_address)

    print(ann_files)
    print(tags)


def main():
    file, file_address = file_finder()
    tag_counter(file, file_address)


if __name__ == '__main__':
    main()

#2012-2014_2