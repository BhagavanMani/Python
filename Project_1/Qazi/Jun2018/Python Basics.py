#
# str='Bhagavan | CenduitServices | Sr Software Engineer'
# print(str)
# # print(str.split('|'))
# st=0;en=str.stex('|')
# print(st,en)
# Employee=str[st:en]
# st=en+1;en=str.stex('|',st)
# Employer=str[st:en]
# st=en+1;en=len(str)+1
# Desg=str[st:en]
# print(Employee,Employer,Desg)
# # lst=[].append(str.fst('|',st,en))
# # print(lst)

# entrada = "MegaDrive | 250€ | Retro"
# producto = entrada[0:entrada.stex("|")-1]
# precio_tipo = entrada[entrada.stex("|")+1:]
# precio = precio_tipo[1:precio_tipo.stex("|")-1]
# tipo = precio_tipo[precio_tipo.stex("|")+2:]
#
# print(producto)
# print(precio)
# print(tipo)

#
str='Bhagavan | CenduitServices | Sr Software Engineer'
st=0;En=0;count=0
en=str.index('|')
while count<3:
    # print(st,en)
    name=str[st:en]
    count=count+1
    str=str[en+1:].strip()
    # print(str)
    if en>=16:
        pass
    else:
        en=str.index('|')
    # print(en)
    print(name.strip(),count)


# str.rjust('')
