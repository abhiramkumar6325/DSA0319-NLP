words=['cat','dog','man','bus']
for i in words:
    if i.endswith('t') or i.endswith('g'):
        print(i+'s')
    elif(i=='man'):
        print("men")
    else:
        print(i+'es')
