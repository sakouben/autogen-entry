st.header("References")


def display_input_row(index):
    left, right = st.columns(2)
    left.selectbox(
        label="Reference template",
        options=["Bakar 1985 Seri 1",
                 "Bakar 1985 Seri 2"],
        key=f'ref_temp_{index}',
        help="You must select a valid pre-existing reference template."
    )
    right.number_input(
        label="Page number",
        min_value=1,
        max_value=999, #change to auto later
        step=1,
        key=f'page_{index}',
        help="Input the page number of your reference."
    )

if 'references' not in st.session_state:
    st.session_state['references'] = 0

def increase_references():
    st.session_state['references'] += 1

st.button('Add', on_click=increase_references)

for i in range(st.session_state['references']):
    display_input_row(i)

# Show the results
st.subheader('Test')
for i in range(st.session_state['references']):
    st.write(
        f'Person {i+1}:',
        st.session_state[f'ref_temp_{i}'],
        st.session_state[f'page_{i}']
    )