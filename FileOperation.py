import os


appData=os.getenv('APPDATA')
profile=appData+"\\Mozilla\\Firefox\\Profiles\\"
current=os.listdir(profile)
fireFoxProfile=profile+current[0]
print fireFoxProfile
