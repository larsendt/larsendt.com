#!/usr/bin/env python

import subprocess
import os
import config

def make_folders():
    for folder in ["public_html", "cache"]:
        if not os.path.exists(folder):
            print "Making", folder
            os.makedirs(folder)

def markdown_to_html(in_fname, out_fname):
    cmd = ["pandoc", in_fname, "-o", out_fname]
    subprocess.call(cmd)

def template_process(title, in_fname, out_fname):
    with open("template.html", "r") as f:
        template = f.read()

    with open(in_fname, "r") as f:
        document = f.read()

    template = template.replace("{title}", title)
    template = template.replace("{body}", document)

    with open(out_fname, "w") as f:
        f.write(template)
    
def make_htmls():
    for obj in config.get()["markdown"]:
        fname = obj["file"]
        title = obj["title"]
        outfname = obj["out"]

        fpath = "./markdown/" + fname
        outfpath = "./cache/" + outfname
        pub_fpath = "./public_html/" + outfname

        markdown_to_html(fpath, outfpath)
        template_process(title, outfpath, pub_fpath)



def main():
    make_folders()
    make_htmls()


if __name__ == "__main__":
    main()
