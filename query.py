import requests
import base64

def get(ip):
    request = requests.get("https://api.mcsrvstat.us/2/" + ip).json()
    info = ""
    if request["online"]:
        icon = request["icon"][22:]
        # image_result = open('icon.png','wb')
        # image_result.write(base64.b64decode(icon)[1:])
        # image_result.close()
        try:
            print("Trying")
            info = info + request["hostname"] + "\n"
            print(info)
        except:
            pass
        print(info)
        info = info + str(request["ip"]) + "\n"
        print(info)
        info = info + str(request["motd"]["clean"][0]) + "\n"
        print(info)
        info = info + "version:" + str(request["version"])
        print(info)
    else:
        info = "This server is not online :("
    return info

def online(ip):
    info = requests.get("https://api.mcsrvstat.us/2/" + ip).json()
    return info["online"]

def players(ip):
    info = requests.get("https://api.mcsrvstat.us/2/" + ip).json()
    try:
        return info["players"]["list"]
    except:
        return []

# mooncat.apexmc.co
# CVGSOC.playat.ch
# CVGSOC2.playat.ch
# mc.cssbham.com