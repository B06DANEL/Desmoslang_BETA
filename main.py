varN = ["out", "x", "y"]
varC = ["0", "x", "y"]
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
    if "=" in text:
        var1=text.split("=")[0].strip()
        var2=replaceVars(text.split("=")[1].strip())
        set(var1,var2)
execLine("a=10")
execLine("b=a*5")
print(replaceVars("out=x+b"))
