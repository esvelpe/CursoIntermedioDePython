def run():
    dic={}

    for i in range(1,101):
        pow=i**3
        if i%3!=0:
            dic[i]=i**3


    print(dic)



if __name__=='__main__':
    run()