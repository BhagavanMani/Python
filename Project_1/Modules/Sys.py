import sys
# for i in sys.modules:
#     print(i)

# print (sys.modules.keys())
# print (sys.version)
# print(sys.version_info)
# print(sys.getrecursionlimit())
# print(sys.argv)

# for i in range(len(sys.argv)):
#     if i == 0:
#         print ("Function name: %s" % sys.argv[0])
#     else:
#         print ("%d. argument: %s" % (i,sys.argv[i]))

# x=42
# def my_displyHook(x):
#     print("Out: ",)
#     print(x)
# sys.displayhook=my_displyHook
for i in (sys.stdin,sys.stdout,sys.stderr):
    print(i)

