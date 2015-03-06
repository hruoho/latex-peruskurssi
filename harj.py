import re

n = '2'
inf = open('slides_part' + n + '.tex', 'r')
ouf = open('slides_part' + n + '.uusi.tex', 'w')
lif = open('slides_part' + n + '.harj.tex', 'w')

lines = inf.readlines()

justout = True
count = 1

for line in lines:
    if justout:
        if re.search('\\\\begin\\{harj\\}', line):
            indentation = re.match('\s*', line).group(0)
            justout = False
            houf = open('harj' + n + '_' + str(count) + '.tex', 'w')
            ouf.write(indentation + '\\input{harj' + n + '_' + str(count) + '}\n')
            lif.write('\\input{harj' + n + '_' + str(count) + '}\n')
            houf.write(line)
            count += 1
        else:
            ouf.write(line)
    else:
        houf.write(line)
        if re.search('\\\\end\\{harj\\}', line):
            justout = True
            houf.close()

