import urllib

ramin = urllib.urlopen('http://api.ipify.org/')

ip = ramin.read()
print("ip public you : " + ip)
