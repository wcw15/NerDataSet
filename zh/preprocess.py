# -*- coding: utf-8 -*-
#
# File: preprocess.py
# Author: SmileTM
# Site: s-tm.cn
# Github: https://github.com/SmileTM
# Time: 10.03.2022
#
import json


def preprocess_weibo(weibo_dir):
    for name in ["train","dev", "test"]:
        with open(f"{weibo_dir}/weiboNER_2nd_conll.{name}", "r",encoding="utf-8") as f, \
            open(f"{weibo_dir}/{name}.json", "w",encoding="utf-8") as fw:
            text = []
            label = []
            while ((line := f.readline())):
                line = line.strip()
                if len(line) == 0:
                    data = {"text": text, "label": label}
                    assert len(text) == len(label)
                    fw.write(json.dumps(data, ensure_ascii=False))
                    fw.write("\n")
                    text.clear()
                    label.clear()
                else:
                    t = line.split("	")
                    assert len(t) == 2
                    text.append(t[0])
                    label.append(t[1])
        print(f"{weibo_dir} {name} data preprocess successed!!!!")

if __name__ == '__main__':
    preprocess_weibo("./WeiboNER")
