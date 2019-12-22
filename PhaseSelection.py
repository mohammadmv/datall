import Strings

def show():
    selection=input("""
Select in which Phase you want manipulate your data:
0- pre-process
1- process
2- visualize
other- return
which one? """)

    if selection==0:
        tool_selection = input(Strings.pre_menu)
