import urllib.request, urllib.parse, urllib.error

inp=input('Enter the URL:')
fhand=urllib.request.urlopen(inp)

for line in fhand:
    print(line.decode().strip())
    