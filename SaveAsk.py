import Strings
import numpy

def show(data_):
    path = input(Strings.save_csv)
    print(numpy.savetxt(path, data_, delimiter=","))

def show_model_save(data_):
    path = input(Strings.save_csv)
    print(numpy.savetxt(path, data_, delimiter=","))
