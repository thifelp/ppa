import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('/home/thi/Dev/ppa/repository/ppe_un.csv')
data.dropna(inplace= True, axis= 0)
data.info()

taxa_retencao = []
taxa_evasao = []
taxa_reprovacao = []
taxa_matricula = []
taxa_efetividade = []
taxa_permanencia_exito = []
taxa_saida_com_exito = []
percentual = []
def tb(data):
    for tb in data.values:
        if tb[2] == "Taxa de Reten??o":
            taxa_retencao.append(tb[2])
            percentual.append(tb[3])
        elif tb[2] == "Taxa de Evas?o":
            taxa_evasao.append(tb[2])
            percentual.append(tb[3])
        elif tb[2] == "Taxa de Reprova??o":
            taxa_reprovacao.append(tb[2])
            percentual.append(tb[3])
        elif tb[2] == "Taxa de Matr?cula Continuada Regular":
            taxa_matricula.append(tb[2])
            percentual.append(tb[3])
        elif tb[2] == "Taxa de Efetividade Acad?mica":
            taxa_efetividade.append(tb[2])
            percentual.append(tb[3])
        elif tb[2] == "Taxa de Perman?ncia e ?xito":
            taxa_permanencia_exito.append(tb[2])
            percentual.append(tb[3])
        elif tb[2] == "Taxa de Sa?da com ?xito":
            taxa_saida_com_exito.append(tb[2])
            percentual.append(tb[3])

tb(data)

sns.boxplot(x = percentual)

plt.title('Indicadores')
plt.ylabel('Percentual das taxas')
plt.show()

