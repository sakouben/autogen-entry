import streamlit as st
import pandas as pd

st.title("Acehnese")

body = """
==Acehnese==

===Alternative forms===
* [[aleue]] (''nonstandard'')

===Pronunciation===
{{IPA|ace|/alɯə/}}

===Noun===
{{head|ace|noun}}

# [[floor]]<ref>{{R:ace:Bakar 1985 Seri 1|18|entry=aleue}}</ref>

===References===
<references/>
"""

body = "==Acehnese==\n\n"

df_altf = pd.DataFrame(
    [
       {"Alternative forms": None},
   ]
)

st.header("Alternative forms")
edited_df_altf = st.data_editor(
    df_altf,
    num_rows = "dynamic",
    use_container_width = True,
    column_config = {
        "Alternative forms": st.column_config.TextColumn()
    },
    hide_index = True
)

add = "===Alternative forms===" + "\n"
for x in edited_df_altf.iterrows():
    add += "[[" + str(x[1]["Alternative forms"]) + "]]\n"

add += "\n"

st.code(add, language="wiki")
body += add


st.header("Pronunciation")
IPA = st.text_input("IPA")

add = "===Pronunciation===" + "\n"
add += "{{" + f"IPA|ace|/{IPA}/" + "}}\n\n"
st.code(add, language="wiki")
body += add


st.header("Part of Speech")
poslookupdict = {
    "adjective":"a",
    "adverb":"adv",
    "article":"art",
    "cardinal number":"cnum",
    "conjunction":"conj",
    "converb":"conv",
    "determiner":"det",
    "interjection":"int",
    "noun":"n",
    "numeral":"num",
    "ordinal number":"onum",
    "participle":"part",
    "particle":"pcl",
    "phrase":"phr",
    "proper noun":"pn",
    "postposition":"postp",
    "preposition":"pre",
    "pronoun":"pro",
    "proper noun":"prop",
    "verb":"v",
    "intransitive verb":"vi",
    "transitive verb":"vt",
    "transitive and intransitive verb":"vti"
    }
posbox = st.selectbox(
    label = "Part of Speech",
    options=[
    "Adjective",
    "Adverb",
    "Conjunction",
    "Noun",
    "Pronoun",
    "Verb",
    ]
)
posbox_res = str(poslookupdict[posbox.lower()])
add = f"==={posbox}===" + "\n"
add += "{{head|ace|" + f"{posbox_res}" + "}}"
st.code(add, language="wiki")
body += add

df = pd.DataFrame(
    [
       {"Sense": None, "Reference": None},
   ]
)

edited_df = st.data_editor(df,
                           num_rows="dynamic", 
                           use_container_width=True, 
                           column_config={
                               "Sense":st.column_config.TextColumn(),
                               "Reference":st.column_config.SelectboxColumn(
                                   options=[
                                       "Bakar 1985 Seri 1",
                                       "Bakar 1985 Seri 2"
                                   ]
                               )
                           },
                           hide_index=True
                           )









st.code(body, language="wiki", line_numbers=True)

st.button("Reset", type="primary")