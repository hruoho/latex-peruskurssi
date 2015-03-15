#!/usr/bin/bash

HFILE=harjoitukset.tex
echo "\\input{preamble}" > $HFILE
echo "\\begin{document}" >> $HFILE

for SECTION in 1 2 3 4
do
    echo "" >> $HFILE
    echo "\\section{$SECTION. kerta}" >> $HFILE
    for FILE in $(ls -1v harj${SECTION}.*.tex)
    do
        echo "\\begin{fframe}" >> $HFILE
        echo "    \\begin{harjoitus}" >> $HFILE
        echo "        \\input{$FILE}" >> $HFILE
        echo "    \\end{harjoitus}" >> $HFILE
        echo "\\end{fframe}" >> $HFILE
    done
done

echo "\\end{document}" >> $HFILE

