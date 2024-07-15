# Creare un dataframe e stamparlo avendo come fonte l’XML utilizzato perl’esercizio sui libri:
# <libri>
# <libro>
# <titolo>Python Cookbook</titolo>
# <autore>David Beazley</autore>
# </libro>
# <libro>
# <titolo>Fluent Python</titolo>
# <autore>Luciano Ramalho</autore>
# </libro>
# </libri> espotalo in csv e html 

import pandas as pd
import xml.etree.ElementTree as ET

dati_xml = """<libri>
<libro>
<titolo>Python Cookbook</titolo>
<autore>David Beazley</autore>
</libro>
<libro>
<titolo>Fluent Python</titolo>
<autore>Luciano Ramalho</autore>
</libro>
</libri>"""

root = ET.fromstring(dati_xml)

df_cols = ["libro", "titolo", "autore"]
righe = []

for libro in root.findall('libro'):
    titolo = libro.find('titolo').text
    autore = libro.find('autore').text
    righe.append({'libro': '', 'titolo': titolo, 'autore': autore})  

df = pd.DataFrame(righe, columns=df_cols)

csv_path = 'libri.csv'
df.to_csv(csv_path, index=False)

html_path = 'libri.html'
df.to_html(html_path, index=False)  

print(df)


# import xml.etree.ElementTree as ET

# xml = """<data>
# <student name="John">
# <email>john@mail.com</email>
# <grade>A</grade>
# <age>16</age>
# </student>
# <student name="Alice">
# <email>alice@mail.com</email>
# <grade>B</grade>
# <age>17</age>
# </student>
# <student name="Bob">
# <email>bob@mail.com</email>
# <grade>C</grade>
# <age>16</age>
# </student>
# <student name="Hannah">
# <email>hannah@mail.com</email>
# <grade>A</grade>
# <age>17</age>
# </student>
# </data>
# """


# root = ET.fromstring(xml)

# df_col = ["nome", "email", "grado", "età"]

# righe = []

# for nodo in root:
#     nome = nodo.attrib["name"]
#     mail = nodo.find("email").text if nodo is not None else None
#     grado = nodo.find("grade").text if nodo is not None else None
#     età = nodo.find("age").text if nodo is not None else None

#     righe.append({"nome":nome, "email":mail, "grado":grado, "età":età})

# #print(righe)

# df = pd.DataFrame(righe, columns=df_col)

# print(df)