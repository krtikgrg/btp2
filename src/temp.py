dic = {
    'a':5,
    'd':7,
    'c':3
}
dic = list(sorted(dic,key=lambda k:dic[k]))
dic.reverse()
print(dic)