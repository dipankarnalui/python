import urllib.request

URL="https://www.transfermarkt.com/stoke-city/startseite/verein/512/saison_id/2018"
request = urllib.request.Request(URL)
result = urllib.request.urlopen(request)
resulttext = result.read()