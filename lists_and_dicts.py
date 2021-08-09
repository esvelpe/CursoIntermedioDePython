def run():
    my_list=[1,"Hello",True,4.5]
    my_dict={"firstname":"Facundo","lastname":"García"}

    super_list=[
        {"firstname":"Facundo","lastname":"García"},
        {"firstname":"Miguel","lastname":"Torres"},
        {"firstname":"Pepe","lastname":"Rodelo"},
        {"firstname":"Susana","lastname":"Martínez"},
        {"firstname":"José","lastname":"García"}
    ]

    #print(super_list[0]['firstname'])

    super_dict={
        "natural_nums":[1,2,3,4,5],
        "integer_nums":[-1,-2,0,1,2],
        "floating_nums":[1.1,4.5,6.43]
    }

    def printSuper_dict(super_dict):
        for key, value in super_dict.items():
            print(key,"-",value)

    def printSuper_list(super_list):
        for dict in super_list:
            print("El nombre es: " + dict['firstname'] + " y el apellido es: " + dict['lastname'])


    printSuper_list(super_list)


if __name__=='__main__':
    run()