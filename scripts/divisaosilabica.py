abc = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r",
"s","t","u","v","w","x","y","z"]

from BeautifulSoup import BeautifulSoup
import urllib

file = open('../data/divisaosilabica.csv','w')
file.write("palavra,tipo,divisao_silabica\n")

for letra in abc:
    r = urllib.urlopen('http://www.portaldalinguaportuguesa.org/index.php?action=syllables&act=list&letter='+letra)
    data = r.read()
    soup = BeautifulSoup(data)
    rows = soup.find(id="rollovertable").findAll("tr")
    for row in rows:
        cells = row.findAll("td")
        if cells:
            palavra = cells[0].find('b').find('a').getText()
            file.write(palavra.encode('utf-8'))
            file.write(',')
            tipo = cells[0].getText().split("(")[1].split(")")[0]
            file.write(tipo.encode('utf-8'))
            file.write(',')
            divisaosilabica = cells[1].getText()
            file.write(divisaosilabica.encode('utf-8').replace("&middot;","."))
            file.write("\n")
