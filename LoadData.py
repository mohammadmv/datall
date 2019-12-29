from numpy import genfromtxt
import PhaseSelection

def new_data_file():
    file_name = input("Enter your file location:")
    data = genfromtxt(file_name, delimiter=',')
    print("\nyou have "+ str(data.shape[0]) + " rows , "+ str(data.shape[1])+" cols in your dataset.")
    PhaseSelection.show(data)
