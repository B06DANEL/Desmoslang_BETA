# V0.11
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
set("a","10")
print(replaceVars("out=x+a"))
