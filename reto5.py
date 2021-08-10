from data_filtering_db import DATA

def print_all_python_devs():
    all_python_devs=list(filter(lambda worker:worker["language"]=="python",DATA))
    all_python_devs=list(map(lambda worker:worker["name"],all_python_devs))

    print("Los trabajadores que manejan python son: ")
    for worker in all_python_devs:
        print(worker)
    print("\n")

def print_all_Platzi_workers():
    all_Platzi_workers=list(filter(lambda worker:worker["organization"]=="Platzi",DATA))
    all_Platzi_workers=list(map(lambda worker:worker["name"],all_Platzi_workers))

    print("Los trabajadores que están vinculados a Platzi son: ")
    for worker in all_Platzi_workers:
        print(worker)
    print("\n")

def print_adults():
    adults=[workers["name"] for workers in DATA if workers["age"]>18]

    print("Los trabajadores adultos son: ")
    for worker in adults:
        print(worker)
    print("\n")

def print_old_people():
    old_people=[worker | {"old":worker["age"]>70} for worker in DATA]

    print("Los trabajadores mayores de 70 años son: ")
    for worker in old_people:
        print(worker)
    print("\n")




def run():
    print_all_python_devs()
    print_all_Platzi_workers()
    print_adults()
    print_old_people()


if __name__=='__main__':
    run()