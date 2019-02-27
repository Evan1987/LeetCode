# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 09:51:32 2019

@author: Cigar
"""
import os
import sys
import time

existing = []

def generate(path, file_name):
    number_, name, _ = file_name.split(".")

    if number_ in existing:  # 如果已经有相应md文件就不再写了
        return number_, False

    number = number_ if len(number_) >= 4 else "0" * (4 - len(number_)) + number_
    write_name = number + " " + name + ".md"
    write_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    title = "LeetCode" + " " + number + name
    tags = "leetcode"

    with open(path + "/" + file_name, "r", encoding="utf-8") as f_r, open(path + "/" + write_name, "w", encoding="utf-8") as f_w:
        f_w.write("---\n")
        f_w.write("title: %s\n" % title)
        f_w.write("date: %s\n" % write_time)
        f_w.write("tags: %s\n" % tags)
        f_w.write("---\n\n")

        content = f_r.readlines()
        start = False
        for line in content:
            if not start:
                if "[%s]" % number_ in line:
                    start = True
                    f_w.write(line)  # 起始行
            else:
                if line[0] == "#":
                    f_w.write(line[1::])
        f_w.write("## Solutions:\n\n")

    return write_name, True


if __name__ == "__main__":
    args = sys.argv
    path = os.getcwd()
    files = os.listdir(path)

    targets = []
    for file in files:
        suffix = file.split(".")[-1]
        if suffix == "py" and file != args[0]:
            targets.append(file)
        elif suffix == "md":
            try:
                number = str(int(file.split(" ")[0]))
                existing.append(number)
            except ValueError:
                pass

    count = 0
    omitted = 0
    for file_name in targets:
        r, is_done = generate(path, file_name)
        if is_done:
            print("%s finished!" % r)
            count += 1
        else:
            print("%s omitted!" % r)
            omitted += 1

    print("-" * 20)
    print("%d Files finished, %d Files omitted!" % (count, omitted))



