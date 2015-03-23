#!/bin/python

import re

ouf = open("harjoitukset.tex", "w")
ouf.write("\\input{preamble}\n")
ouf.write("\\begin{document}\n")

hbegin = re.compile(r"^\s*\\begin{harj}$")
hend = re.compile(r"^\s*\\end{harj}$")
inharj = False

for kerta in [1,2,3,4]:
    ouf.write("\\section{" + str(kerta) + ". kerta}\n")
    inf = open(str(kerta) + "kerta.tex", "r")
    for line in inf.readlines():
        if not inharj:
            if hbegin.match(line):
                inharj = True
                ouf.write("\\begin{fframe}\n")
                ouf.write(line)
        else:
            ouf.write(line)
            if hend.match(line):
                inharj = False
                ouf.write("\\end{fframe}\n")
    inf.close()

ouf.write("\\end{document}\n")

