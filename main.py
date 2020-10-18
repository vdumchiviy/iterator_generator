from country import Countries
from filestrmd5 import file_str_md5


def country_wiki(file_name):
    file_countries = Countries(file_name)
    for item in file_countries:
        print(item)


def file_md5(file_name):
    for item in file_str_md5(file_name):
        print(item)


country_wiki('countries.json')
file_md5('countrywiki.json')
