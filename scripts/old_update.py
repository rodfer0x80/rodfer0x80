#!/usr/bin/python3
import os
import sys
import subprocess


def updateAdd(lsu):
    with open("index.html", 'r') as rh:
        _html = rh.read()
    _html = _html.splitlines()    
    html = list()
    updated = False
    for line in _html:
        if not updated and "<li><a" in line:
            updated = True
            for l in lsu:
                html.append(f"{' '*8}<li><a href=" + "'posts/" + f"{''.join(l.split(' '))}" + f".txt'>{l}</a></li>")
        html.append(line)
    with open("index.html", 'w') as ah:
        ah.write(''.join(f"{line}\n" for line in html))
    return 0

def updateDel(lsu):
    with open("index.html", 'r') as rh:
            _html = rh.read()
    _html = _html.splitlines()
    html = list()
    for line in _html:
        add = True
        for lu in lsu:
            if str(lu) in line:
                add = False
        if add:
            html.append(line)
    with open("index.html", 'w') as ah:
        ah.write(''.join(f"{line}\n" for line in html))
    return 0

def main():
    os.chdir("docs/")
    _ls = os.listdir("posts/")
    ls = list()
    for l in _ls:
        ls.append(l.split(".")[0].strip())
    
    with open("index.html", 'r') as hr:
        _lsi = hr.readlines()
    lsi = list()
    for l in _lsi:
        if "<li>" in l:
            a = l.split("posts/")[1].split(".txt")[0].strip()
            if a[-1] == "'":
                lsi.append(a[0:-1])
            else:
                lsi.append(a)
    update = False
    lsu = list()
    update_add = False
    update_del = False

    for l in ls:
        if l not in lsi:
            update_add = True
            lsu.append(l.strip())

    if update_add:
        updateAdd(lsu)
        sys.stdout.write("[*] Successfully added new entries to index.html\n")
        return 0

    for l in lsi:
        if l not in ls:
            update_del = True
            lsu.append(l)
    if update_del:
        updateDel(lsu)
        sys.stdout.write("[*] Successfully deleted incorrect entries in index.html\n")
        return 0

    sys.stdout.write("[*] Nothing else to update\n")
    return 0


if __name__ == '__main__':
    sys.exit(main())