'''@filename: run.py
@content: to generate a map from scripts to topics
---------------------------------------------------
@author: Tianyi Wang
@modified time: Oct 25 2019
'''


import os
import re


def check_update(folder, dir_):
    new = []
    info = []
    dir_ = {}
    for root, folders, files in os.walk(folder):
        for file_ in files:
            new.append(os.path.join(root, file_))
            with open(os.path.join(root, file_)) as fi:
                data = fi.readline()
                dir_[file_] = data.split(':')[1][1:]
    return dir_


def add(file_path, new):
    with open(file_path, "a+") as fil:
        for i in new:
            with open(i) as file_:
                data = file_.readline()
                fil.write(i.split('/')[-1] + ' --- ' + data.split(':')[1][1:])


def create_dir(file_path):
    dir_ = {}
    with open(file_path) as file_:
        data = file_.read()

        info = re.findall('[a-z_0-9]+.py' + ' --- ' + "[^\n]+", data)
        for i in info:
            buff = i.split(' --- ')
            dir_[buff[0]] = buff[1]
        return dir_


if __name__ == '__main__':
    import argparse
    from os import path

    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--update', action='store_true')
    parser.add_argument('-f', '--folder', type=str)
    parser.add_argument('-l', '--log', type=str)
    parser.add_argument('-s', '--search', type=str)
    args = parser.parse_args()

    dir_ = {}
    if path.isfile(args.log):
        dir_ = create_dir(args.log)
    if args.update:
        dir_ = check_update(args.folder, dir_)
        with open(args.log, "w") as f:
            for d in list(dir_.keys()):
                f.write(d + ' --- ' + dir_[d])
    else:
        try:
            print(f'topic is {dir_[args.search]}')
        except KeyError:
            print(f'No such file {args.search}')
