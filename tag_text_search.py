import os
import re
import csv


def file_scanner(file, file_address):
    file_address = file_address + '/' + file
    # print(file)
    with open(file_address, encoding='utf-8') as file:
        raw_data = file.read()
        our_tag = re.compile('T\d+\s(Attr_participial\s\d+\s\d+)\s(.*)\n#\d+\sAnnotatorNotes\sT\d+\s(.*)\n')
        our_tags = re.findall(our_tag, raw_data)
        print(our_tags)
        if len(our_tags) >= 1:
            file = file_address
            tags = our_tags
            ann_txt_match(file, tags)


def csv_table_creator():
    with open('tag_text_Attr_participial3.csv', mode='a+', encoding="utf-8") as csv_file:
        fieldnames = ['tag', 'sentence', 'correction', 'essay']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()


def csv_table_writer(tag, sentence, essay):
    sentence = sentence
    essay = essay
    correction = tag[2]
    print(tag, correction)
    tag = tag[0], tag[1]


    #print(correction, tag)
    with open('tag_text_Attr_participial3.csv', mode='a+', encoding="utf-8") as csv_file:
        fieldnames = ['tag', 'sentence', 'correction', 'essay']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writerow({'tag': tag, 'correction': correction, 'sentence': sentence, 'essay': essay})


def ann_txt_match(file, tags):
    file_address = re.sub('\.ann', '.txt', file)
    with open(file_address, encoding='utf-8') as file:
        raw_data = file.read()
        sentences = raw_data.split('.')
        for tag in tags:
            print(tag[1])
            for sentence in sentences:
                if tag[1] in sentence:
                    print(sentence)
                    essay = re.findall('([A-Za-z]+_\d+_\d+\.txt)', file_address)[0]
                    print(tag)
                    csv_table_writer(tag, sentence, essay)



        #print(file_address)
        #print(raw_data)



def file_finder():
    #print("Insert the folder's name")
    # where = input()
    # file_address = '/Users/elizavetaersova/PycharmProjects/approximation/REALEC/' + where
    #file_address = '/Users/elizavetaersova/PycharmProjects/approximation/REALEC/exam2017'
    #folders = ['exam2014', 'exam2015', 'exam2016', 'exam2017']
    #for where in folders:
    #file_address = '/Users/elizavetaersova/PycharmProjects/approximation/REALEC/' + where
    #print(where)
    #files = os.listdir(file_address)
    #print(files)
    #tag_counter(files, file_address)
    #, 'exam2015', 'exam2016', 'exam2017'
    folders = ['exam2014', 'exam2015', 'exam2016', 'exam2017']
    for where in folders:
        file_address = '/Users/elizavetaersova/PycharmProjects/approximation/REALEC/' + where
        csv_table_creator()
        print(where)
        files = os.listdir(file_address)
        #print(files)
        tag_counter(files, file_address)


def tag_counter(files, file_address):
    ann_files = []
    tags = 0
    for i in files:
        if i.endswith('.ann'):
            ann_files.append(i)
    for file in ann_files:
        texts = file_scanner(file, file_address)





def main():
    file_finder()


if __name__ == '__main__':
    main()
