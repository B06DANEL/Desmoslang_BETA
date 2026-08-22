varN = ["out", "x", "y"]
varC = ["0", "x", "y"]
flag = False
def replaceVars (text):
    i=0
    while i<len(varN):
        if varC[i].isdigit() or i<3:
            text=text.replace(varN[i],varC[i])
        else:
            text=text.replace(varN[i],"("+varC[i]+")")
        i+=1
    return text
def set (var, cont):
    if var not in varN:
        varN.append(var)
        varC.append("0")
    varC[varN.index(var)]=cont
def execLine (text):
    global flag
    valid=False
    if not text.startswith("#"):
        if not flag:
            if "#" in text:
                valid=True
                text=text.split("#")[0].strip()
            if "=" in text:
                valid=True
                var1=text.split("=")[0].strip()
                var2=replaceVars(text.split("=")[1].strip())
                set(var1,var2)
        if text.endswith("{") and not flag:
            valid=True
            print (text[:-1])
            flag = True
        elif text.endswith("}") and flag:
            valid=True
            print ("end")
            flag = False
        if not valid:
            print("Error:"+text)
execLine("{a}++{")
execLine("{a}={a}+1}")
execLine("a=1")
execLine("a++")
execLine("out=a")
print(replaceVars("out"))
