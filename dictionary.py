d={1:{'name':'P1','age':22},2:{'name':'P2','age':27}}
for k,v in d.items():
    age=v['age']
    if age>22:
        print(v['name'])