import sys

print('<html>\n<head>\n<style>\ntable, th, td {\n border: 1px solid black;\n}\n</style>\n</head>\n<body>\n<table style="width:100%">')

for line in sys.stdin:

    if line == "":
        continue
    line = line.split(";")
    print("<tr>")
    for i in line:
        print('<th>', i, '</th>')
    print("</tr>")

print('</table>\n</body>\n</html>')

#Převede csv soubor do html tabulky
