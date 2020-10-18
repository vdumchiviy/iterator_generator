import hashlib
import os


def file_str_md5(file_name):
    file_size = os.path.getsize(file_name)
    f = open(file_name, "rt", encoding="utf-8")
    while f.tell() < file_size:
        read_line = f.readline()
        yield hashlib.md5(read_line.encode("utf-8")).hexdigest()
    f.close()


if __name__ == "__main__":
    for item in file_str_md5('countrywiki.json'):
        print(item)
