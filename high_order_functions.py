my_list=[1,2,3,4,5]

def challenge(list):
    new_list=[i**2 for i in list]
    print(new_list)

def mapFunction(list1):
    new_list=list(map(lambda x: x**2,list1))
    print(new_list)


def run():
    challenge(my_list)
    mapFunction(my_list)

        






if __name__=='__main__':
    run()