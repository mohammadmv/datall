import Strings
import MissingValue
import SavaAsk

def show(data_):
    selection=input("""
Select in which Phase you want manipulate your data:
0- pre-process
1- process
2- visualize
other- return
which one? """)
    print(selection)
    if selection=='0':
        tool_selection = input(Strings.pre_menu)

    if tool_selection=='00':
        command = input(Strings.imputers)

    print(tool_selection + command)
    if tool_selection+command=='000':
        data_new=MissingValue.KNN_Imputer(data_)
        SavaAsk.show(data_new)
    if tool_selection+command=='001':
        data_new=MissingValue.Mean_Imputer(data_)
        SavaAsk.show(data_new)
    if tool_selection+command=='002':
        data_new=MissingValue.Most_Frequent(data_)
        SavaAsk.show(data_new)


