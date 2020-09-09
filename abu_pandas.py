import pandas as pd
import lxml

dfs = pd.read_html(
    "http://www.c-jump.com/CIS77/reference/Instructions_by_Mnemonic.html"
)
df = dfs[0]
options = df.Mnemonic.unique()

pd.set_option("display.max_colwidth", None)

while True:
    question = input("Insert the Mnemonic Word: ")
    if question not in options:
        print("*** Choose a valid Mnemonic Word***")
        print(options)
    else:
        print(df.loc[df["Mnemonic"] == question])
