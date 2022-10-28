#!/usr/bin/python3


import os
import sys
import subprocess


class Updater:
    def __init__(self):
        self.docs_local = "docs/"
        self.posts_local = "posts/"
        self.index_local = "index.html"
        self.html_tab = " "*6
        self.html_tab2 = " "*8
        try:
            os.chdir(self.docs_local)
        except:
            sys.stderr.write(f"[x] Error changing to working directory {self.docs_local}\n")
        
        self.ls = list()
        self._html = ""
        self.html = ""

        return None
    
    def generatePosts(self):
        _ls = os.listdir("posts/")
        for l in _ls:
            self.ls.append(l.split(".txt")[0])
        return 0

    def buildHtml(self):
        posts = ""
        i = len(self.ls)
        ii = 0
        for l in self.ls:
            posts = posts + f"<li><a href='posts/{str(l)}.txt'>{str(l).replace('_', ' ')}</a></li>"
            ii += 1
            if i != ii:
                posts = posts + "<br>"
                posts = posts + "\n" + self.html_tab2
        self.html = self._html.split("<li><a")[0]+ posts + f"\n{self.html_tab}</ul>" + self._html.split("</ul>")[1]
        return 0

    def runme(self):
        self.generatePosts()

        try:
            with open(self.index_local, 'r') as rh:
                self._html = rh.read()
        except:
            sys.stderr.write(f"[x] Error reading to {self.index_local}\n") 

        self.buildHtml()

        try:
            with open(self.index_local, 'w') as wh:
                wh.write(self.html)
        except:
            sys.stderr.write(f"[x] Error writting to {self.index_local}\n") 
       
        sys.stdout.write("[*] Successfully updated posts\n")
        return 0


def main():
    updater = Updater()
    updater.runme()
    return 0

if __name__ == '__main__':
    sys.exit(main())