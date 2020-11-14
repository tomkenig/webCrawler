'''
DONE: funGetUrlData
DONE: funGetUrlDataWithSession
TODO: funGetLinks
TODO: funGetMeta
DONE: funfunGetArticleText
DONE: funFibonacci
TODO: funGetArticleFibonacciTeaser

IDEAS:
find first H1/H2/H3 and crawl down

https://kaijento.github.io/2017/03/30/beautifulsoup-removing-tags/ ------------howto scrap table
NEED:
pip install bs4
pip install Django
'''

# libs
import requests
from bs4 import BeautifulSoup #https://beautiful-soup-4.readthedocs.io/en/latest/ i https://www.crummy.com/software/BeautifulSoup/bs4/doc/#modifying-string

# defs # defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs
# defs # defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs
# defs # defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs
# defs # defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs
# defs # defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs# defs

# tomekenig: Fibonacci function
def funFibonacci(numberElements_in):
    fib_list = [0, 1]
    if numberElements_in == 1:
        return fib_list[-2]
    if numberElements_in == 2:
        return fib_list[-1]
    for i in range(numberElements_in-2):
        fib_list.append(fib_list[-2] + fib_list[-1])
    return fib_list

# tomekenig: Get html code from url address
def funGetUrlData(urlString_in):
    return requests.get(urlString_in).text

# tomekenig: Get html code from url address. Function creates session
def funGetUrlDataWithSession(urlString_in):
    return requests.Session().get(urlString_in).text

# tomkenig: get all normal text without comments # function also remove html tags from text. Remove double space and \n
def funGetArticleText(urlDataString_in):
    soup = BeautifulSoup(urlDataString_in, 'html.parser')
    article_only_out = str(soup.find("article").find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "li"]))
    soup2 = BeautifulSoup(str(article_only_out), 'html.parser')
    article_only_out2 = str(soup2.get_text()).replace('  ','').replace('\n','').replace('[','').replace(']','').replace('\xa0','').strip()
    return article_only_out2

# tomkenig: get all normal text without comments # function also remove html tags from text. Remove double space and \n
def funGetArticleTeaser(urlDataString_in):
    soup = BeautifulSoup(urlDataString_in, 'html.parser')
    article_only_out = soup.find("article").find_all(["p", "h1", "h2", "h3", "h4", "h5", "h6", "ul", "li"])
    return article_only_out

#in - string of sentences
#out - List of sentences
#mods:
# transform string to a list delimited by '.'
# delete very short sentences
# take sentences indexed like fibonacci values - remember, that number 1 you can find twice, so delete second
def funGetArticleFibonacciTeaser(urlString_in):
    # clear strings
    articleText = funGetArticleText(funGetUrlData(urlString_in))
    lstArticleText = articleText.split(".")
    lstArticleText = filter(None, lstArticleText)
    lstArticleText = filter(bool, lstArticleText)
    lstArticleText = filter(len, lstArticleText)
    lstArticleTextMod = []
    for i in lstArticleText:
        if len(i) > 15:
            lstArticleTextMod.append(i)
    # return sentences based on fibonacci. Delete second 1 in fibonacci also
    lstArticleTextNew = []
    for i in funFibonacci(100):
        try:
            lstArticleTextNew.append(lstArticleTextMod[i])
        except:
            if len(lstArticleTextNew) >=2:
                del(lstArticleTextNew[2])
                return lstArticleTextNew
            else:
                return lstArticleTextNew
    return ['Publication is to large']


# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests
# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests
# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests
# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests
# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests# tests

url = 'https://www.komputerswiat.pl/aktualnosci/sprzet/nvidia-geforce-rtx-3080-ti-zadebiutuje-na-poczatku-2021-roku-znamy-cene-karty/b4mrd6y' #'https://tomaszkenig.pl/kurs-excel-vba/petla-while-wend-w-excel-vba/' #'https://tomaszkenig.pl/kurs-excel-vba/' #
#'https://tomaszkenig.pl/kurs-excel-vba/petla-while-wend-w-excel-vba/' #

url1 = 'https://www.komputerswiat.pl/recenzje/sprzet/inne/playstation-5-test-wydajnosci-w-grach-sprawdzamy-4k-60-fps-i-ray-tracing/z118ygn'
url2 = 'https://www.komputerswiat.pl/gamezilla/aktualnosci/cyberpunk-2077-zobaczcie-nowy-teledysk-gry-raperskiej-grupy-run-the-jewels/dvz1vfv'
url3 = 'https://www.auto-swiat.pl/wiadomosci/aktualnosci/krotszy-egzamin-na-prawo-jazdy-ministerstwo-szuka-pieniedzy/7rbxmp3'
url4 = 'https://www.auto-swiat.pl/uzywane/co-warto-kupic/kia-rio-mazda-2-i-skoda-fabia-ktore-auto-miejskie-jest-najlepsze-za-20-30-tys-zl/9h92mye'
url5 = 'https://tomaszkenig.pl/kurs-sql-server/operacje-dml-w-transact-sql/'
url6 = 'https://tomaszkenig.pl/kurs-excel-vba/'
url7 = 'https://officeinside.org/excel-vba-functions/sin-vba-function-how-to-calculate-the-sinus/'

print(funGetArticleFibonacciTeaser(url))

print(funGetArticleFibonacciTeaser(url1))
print(funGetArticleFibonacciTeaser(url2))
print(funGetArticleFibonacciTeaser(url3))
print(funGetArticleFibonacciTeaser(url4))
print(funGetArticleFibonacciTeaser(url5))
print(funGetArticleFibonacciTeaser(url6))
print(funGetArticleFibonacciTeaser(url7))