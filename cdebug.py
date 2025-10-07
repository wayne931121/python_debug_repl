import os, time
while 1:
    try:
        cd = input("$cdebug" + time.strftime("%Y%m%d-%H%M%S", time.localtime()) + ": " )
        if cd=="exit":
             break
        cd = cd.replace("\\br","\n")
        if len(cd) and cd[0:1]=="!":
            os.system(cd[1:])
        else:
            exec(cd, globals())
    except Exception as e:
        print(e)
