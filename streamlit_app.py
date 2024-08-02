import streamlit as st

st.title("Wiktionary entry code autogeneration")

body = """
==Thai==

===Pronunciation===
{{th-pron}}

===Etymology 1===
{{der+|th|nan-hbl|幣|tr=pī|gloss=[[currency]]; [[money]]}}.<ref>{{cite-thesis
|year=1983
|first=Pranee
|last=Gyansurut
|title=Chinese Loanwords in Modern Thai
|publisher=Chulalongkorn University
|url=https://cuir.car.chula.ac.th/handle/123456789/37061
|page=182
|language=th
}}</ref>

====Noun====
{{th-noun}}

# one round of a gambling game

===Adverb===
{{th-adv}}

# [[fast]]; [[quickly]]; [[rapidly]].

====Synonyms====
{{col3|th
|title=quickly
|ไว
|รวดเร็ว
|ว่องไว
}}
"""

st.code(body, language="wiki", line_numbers=True)