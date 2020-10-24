from country import Countries
from filestrmd5 import file_str_md5
from debug import decorator_for_logging


@decorator_for_logging('somelog.log')
def country_wiki(file_name):
    file_countries = Countries(file_name)
    for item in file_countries:
        print(item)


@decorator_for_logging('somelog2.log')
def file_md5(file_name):
    for item in file_str_md5(file_name):
        print(item)


country_wiki(file_name='countries2.json')
file_md5('countrywiki.json')
