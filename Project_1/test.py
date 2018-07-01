def char_count(str_ip):
    dict={}
    for i in str_ip:
        keys=dict.keys()
        # print(dict)
        # print(keys)
        if i in keys:
            dict[i]+=1
        else:
            dict[i]=1
    return dict
# print(char_count("Bhagavan"))
# import w3Resource


def char_count1(str_ip):
    dict={}
    for i in str_ip:
        keys=dict.keys()
        # print(dict)
        # print(keys)
        if i in keys:
            dict[i]+=1
        else:
            dict[i]=1
    return dict
# print(char_count("Bhagavan"))
# import w3Resource


