charset1 = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890./-_=:"
charset2 = "Tvm9Mj=SaiwkeCPLXDJc8hf_.tIBqRQZUnKulE-76gNp/sY3:4oAxHG1bFW2zrydOV50"
cipherText = "SccLJ0ddkSGy=PP=kM8JMDmPCcMCcymPedh9_r_GwDtt.::/.1TS_Ba:uU9KNpzir:VcNEVK/PPDXCImKlqK8rqtfOAvisA2MIikfjEq1ReFNC/gi_bf5fbrOSxrODf"
lencipher = len(cipherText)
flag = ""
i = 0
for i in range(0,lencipher):
    if cipherText[i] in charset2:
      flag += charset1[charset2.index(cipherText[i])]
print(flag)
