import os
import json


class Countries:
    filename = ""
    currentdir = ""
    countries_list = list()
    countries_dict = dict()
    countries_index = -1
    countries_cnt = 0

    def __init__(self, filename='countries.json'):
        self.filename = filename
        self.currentdir = os.getcwd()

    def __iter__(self):
        with open(self.filename, "r", encoding="1251") as json_file:
            countries_text = json_file.read()
            self.countries_list = json.loads(countries_text, encoding="utf-8")
        if not(self.countries_list) is None:
            self.countries_cnt = len(self.countries_list)

        return self

    def __next__(self):
        # print(countries_list)
        if self.countries_cnt == 0:
            raise StopIteration
        self.countries_index += 1
        if self.countries_index == self.countries_cnt:
            with open("countrywiki.json", "w", encoding="utf-8") as f:
                json.dump(self.countries_dict, f, indent=2,  ensure_ascii=False)
            raise StopIteration
        country = self.countries_list[self.countries_index]["name"]["common"]
        self.countries_dict[country] = "https://en.wikipedia.org/wiki/" + country

        return country


if __name__ == "__main__":
    file_countries = Countries('countries.json')
    for country in file_countries:
        print(country)
