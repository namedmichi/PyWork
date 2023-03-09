def disarium(nummber):
    counter = 1
    temp = 0
    for z in str(nummber):
        temp += pow(int(z), counter)
        counter += 1
    if temp == nummber:
        return True
    else: 
        return False



print(disarium(135))
