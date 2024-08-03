import streamlit as st
import pandas as pd
import re

st.title("Acehnese")
st.header("Term")

term = st.text_input(
    label="Term",
    label_visibility="collapsed",
    placeholder="Term"
)

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

ace_ortho = {"a":"a", "é":"e", "è":"ɛ", "e":"ə", "ë":"ə̯", "i":"i", "ô":"o", "o":"ɔ", "ö":"ʌ", "u":"u", "b":"b", "c":"c", "d":"d", "g":"g", "h":"h", "j":"ɟ", "k":"k", "l":"l", "m":"m", "n":"n", "p":"p", "r":"r", "s":"s", "t":"t", "w":"w", "y":"j"}


def IPAgen(term):
    term = str(term)
    subterm = re.sub(
        pattern=r"([aeiouèéëôö])k", 
        repl=r"\1ʔ",
        string=term
        )
    subterm = re.sub(
        pattern=r"ng",
        repl=r"ŋ",
        string=subterm
        )
    subterm = re.sub(
        pattern=r"ny",
        repl=r"ɲ",
        string=subterm
        )
    subterm = re.sub(
        pattern=r"eu",
        repl=r"ɯ",
        string=subterm
        )
    
    final = ""

    for x in subterm:
        try:
            final += ace_ortho[x]
        except:
            final += x

    #nasalization

    final = re.sub(
        pattern=r"’(.)",
        repl=r"\1̃",
        string=final
    )

    #removing '-'

    final = re.sub(
        pattern=r'-',
        repl=r'.',
        string=final
    )

    return final




termpropipa = IPAgen(term)
st.header("Pronunciation")

st.caption("IPA from spelling")
st.code(termpropipa)
IPA = st.text_input(
    label="IPA", 
    placeholder="IPA",
    value=termpropipa
)



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
add += "{{head|ace|" + f"{posbox_res}" + "}\n\n"
st.code(add, language="wiki")
body += add

st.header("Senses")
df = pd.DataFrame(
    [
       {"Sense": "None", "Reference": "Other", "Page": "1"},
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
                                       "Bakar 1985 Seri 2",
                                       "Other"
                                   ]
                               ),
                               "Page":st.column_config.TextColumn(width="small")
                           },
                           hide_index=True,
                           )

ref_dict={"Bakar 1985 Seri 1":"R:ace:Bakar 1985 Seri 1", "Bakar 1985 Seri 2":"R:ace:Bakar 1985 Seri 2", "Other":"Other"}

add = ""
for x in edited_df.to_numpy():
    sense = x[0]
    reference = x[1]
    page = x[2]

    add += "# [["
    add += sense
    add += "]]<ref>{{"
    add += ref_dict[reference]
    add += "|"
    add += str(page)
    add += "}}</ref>\n"


st.code(add, language="wiki")
body += add

body += "\n===References===\n<references/>"

st.header("Final code")

st.code(body, language="wiki", line_numbers=True)

st.button("Reset", type="primary")