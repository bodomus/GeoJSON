import hou
list = hou.node('/obj/').allSubChildren()
for i in list:
    print(i)