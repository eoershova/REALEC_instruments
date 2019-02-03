import os
import re


tags = 0
words = 0


def file_finder():
    print("Insert the folder's name")
    where = input()
    file_address = '/REALEC/' + where
    #print(where)
    files = os.listdir(file_address)
    #print(files)
    text_n_tag_counter(files, file_address, words, tags)

#annotator nicknames consist of the first letter of their names and two first letters of their surnames,
#EEr would stand for Elizaveta Ershova
def text_n_tag_counter(files, file_address, words, tags):
    annotator_files_txt = []
    annotator_files_ann = []

    for i in files:
        if i.startswith('DOv'):
            if i.endswith('.txt'):
                annotator_files_txt.append(i)
            if i.endswith('.ann'):
                annotator_files_ann.append(i)
            else:
                continue

    for file in annotator_files_txt:
        words += word_count(file, file_address)
    for file in annotator_files_ann:
        tags += tag_count(file, file_address)
    print('WORDS total: ', words)
    print('TAGS total: ', tags)


def word_count(file, file_address):
    with open(file_address + '/' + file, encoding='utf-8') as file:
        text = file.read()
        file_word_count = len(text.split())
    return file_word_count


def tag_count(file, file_address):
    with open(file_address + '/' + file, encoding='utf-8') as file:
        raw_data = file.read()
        pos_tags = re.compile('T\s[A-Z]{2,}\s.*', flags=re.DOTALL)
        clear_data = re.sub(pos_tags, '', raw_data)
        ann_tag = re.compile('T\d+\s')
        ann_tags = re.findall(ann_tag, clear_data)
        cause_tag = re.compile('A\d+\s')
        cause_tags = re.findall(cause_tag, clear_data)
        file_tag_count = len(cause_tags) + len(ann_tags)
    return file_tag_count


def main():
    file_finder()


if __name__ == '__main__':
    main()
