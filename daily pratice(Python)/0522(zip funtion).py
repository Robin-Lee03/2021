name = ["Robin","Kevin","Nick"]
data = ['3/20','5/8','9/1']
height = ('177','180','182')

user = zip(name,data,height)
for i in user:
    print(i)
print(user)



def divided(a,b):
    try:
        return a/b
    except:
        return "Zero division is meaningless"

print(divided(1,0))