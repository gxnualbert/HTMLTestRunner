import os


myappdata=os.getenv('APPDATA')

firefoxprofil=myappdata+"\\Mozilla\\Firefox\\Profiles\\"

l=os.listdir(firefoxprofil)
lastfil=l[0]

st=firefoxprofil+lastfil
print st
