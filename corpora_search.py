import os
import re
import csv


def file_reader(file, file_address):
    file_address = file_address + '/' + file
    #print(file)
    with open(file_address, encoding='utf-8') as file:
        our_text1 = 'also'
        our_text2 = 'Also'
        raw_data = file.read()
        sentences = raw_data.split('.')
        texts = []
        for sentence in sentences:
            if our_text1 in sentence or our_text2 in sentence:
                texts.append(sentence)
                print(texts)

#Here's a way to find all interrogative sentences:                
        #not_our_text = re.compile("[A-Z].*[^.]\.")
        #clear_data = re.sub(not_our_text, '', raw_data)
        #our_text = re.compile("([A-Z][A-Za-z\s,:;%'\n]*\?)")
        #our_texts = re.findall(our_text, clear_data)

    return texts


# finds all the files in the given directory, for convenience sake create a folder named REALEC and put the folders you
# want to work with there
def file_finder():
    folders = ['exam2014', 'exam2015', 'exam2016', 'exam2017']
    for where in folders:
        file_address = '/REALEC/' + where
        print(where)
        files = os.listdir(file_address)
        print(files)
        tag_counter(files, file_address)


def csv_table_writer(text, file):
    sentence = text
    essay = file
    with open('text_search_also.csv', mode='a+', encoding="utf-8") as csv_file:
        fieldnames = ['sentence', 'essay']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writerow({'sentence': sentence, 'essay': essay})


def csv_table_creator():
    with open('text_search_also.csv', mode='a+', encoding="utf-8") as csv_file:
        fieldnames = ['sentence', 'essay']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()


# determines the type of file you are after, there are 3 - .txt, .json and .ann and also subtypes like _1.ann for
# annotation files for graph description essays
def tag_counter(files, file_address):
    csv_table_creator()
    ann_files = []
    tags = 0
    for i in files:
        if i.endswith('.txt'):
            ann_files.append(i)

    for file in ann_files:
        texts = file_reader(file, file_address)
        for text in texts:
            csv_table_writer(text, file)

    print(ann_files)
    print(tags)


def main():
    file_finder()


if __name__ == '__main__':
    main()
