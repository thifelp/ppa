import pandas as pd

#Open Doc and convert to CSV
pd.read_excel(r'/home/thi/Dev/ppa/repository/Pasta.xlsx').to_csv('/home/thi/Dev/ppa/repository/Pasta.csv')

# Read file csv
data = pd.read_csv('/home/thi/Dev/ppa/repository/Pasta.csv')

total = int(data.values[3][7])

arg1 = int(data.values[3][3])
arg2 = int(data.values[2][7])
def mutually(arg1, arg2):
    # Regra da Adição
    #     184 + 164 = 348
    #     ---   ---   ---
    #     409   409   409
    return print("%.2f" % ((arg1 + arg2) / total))

def mutuallyExclusive(arg1, arg2, arg3):

    # Regra da Adição
    #     arg1 + arg2 - arg3 = soma
    #     ----   ----   ----   ----
    #     total  total  total  total
    return print("%.2f" % (((arg1 + arg2) - arg3) / total))


print("1 - Qual a probabilidade de que o doador tenha sangue do tipo O ou tipo A?")
mutually(arg1, arg2)
print("2 - Qual a probabilidade de que o doador tenha sangue tipo B ou que seja Rh negativo? ")
mutuallyExclusive(45, 65, 8)

