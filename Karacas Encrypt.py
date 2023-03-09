dic = {
    "a" : "0",
    "e": "1",
    "i" : "2",
    "o" : "3",
    "u ": "4"
}
deDic= {
    "0" : "a",
    "1": "e",
    "2" : "i",
    "3" : "o",
    "4 ": "u"
}

def encrypt(string):
    tempString = ""
    resulte = ""
    for z in string:
        tempString = z + tempString
    for z in tempString:
        if z in dic:
            resulte += dic[z] 
        else:
            resulte += z
    resulte += "aca"
    return resulte



def decrypt(string):
    decList = string.split("aca")
    decString = decList[0]
    tempString =""
    resulte = ""
    for z in decString:
        tempString = z + tempString
    for z in tempString:
        if z in deDic:
            resulte += deDic[z] 
        else:
            resulte += z
    return resulte



print(decrypt(" "))
