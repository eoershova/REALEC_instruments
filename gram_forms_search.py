import os
import re
import csv


def file_scanner(file, file_address):
    file_address = file_address + '/' + file
    # print(file)
    with open(file_address, encoding='utf-8') as file:
        raw_data = file.read()
        our_tag = re.compile('T\d+\sPRON\s(\d+)\s\d+\s(.*)\n.*\nT\d+\sPRON\s\d+\s\d+\s(.*)\n.*\nT\d+\sVERB\s\d+\s(\d+)\s(.*)\n.*\n')
        our_tags = re.findall(our_tag, raw_data)

        #print(our_tags)
        if len(our_tags) >= 1:
            for i in our_tags:
                print(i[1])
                if i[1] == 'him' or i[1] == 'her':
                    print(i)
                    file = file_address
                    tags = our_tags
                    ann_txt_match(file, tags)


def csv_table_creator():
    with open('gram_form_search2.csv', mode='a+', encoding="utf-8") as csv_file:
        fieldnames = ['example', 'sentence', 'essay']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()


def csv_table_writer(tag, sentence, essay):
    sentence = sentence
    essay = essay
    tag = tag
    with open('gram_form_search2.csv', mode='a+', encoding="utf-8") as csv_file:
        fieldnames = ['example', 'sentence', 'essay']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames, delimiter=';')
        writer.writerow({'example': tag, 'sentence': sentence, 'essay': essay})


def ann_txt_match(file, tags):
    file_address = re.sub('\.ann', '.txt', file)
    with open(file_address, encoding='utf-8') as file:
        raw_data = file.read()
        sentences = raw_data.split('.')
        for tag in tags:
            print(tag[0], tag[3])
            tag_start = int(tag[0])
            tag_end = int(tag[3])

            len_text = 0
            for sentence in sentences:
                len_text += len(sentence)
                if len_text >= tag_start and len_text <= tag_end:
                    essay = re.findall('([A-Za-z]+_\d+_\d+\.txt)', file_address)[0]
                    tag = tag[1] + ' ' + tag[2] + ' ' + tag[4]
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
    #'exam2014', 'exam2015', 'exam2016',
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