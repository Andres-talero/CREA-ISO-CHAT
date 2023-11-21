import streamlit as st
from streamlit_chat import message
from src.utils.chainData_ import get_response


st.set_page_config(page_title="Creasistemas", page_icon=":robot:")
st.header("Creasistemas - ISO Chat")

if "generated" not in st.session_state:
    st.session_state["generated"] = []

if "past" not in st.session_state:
    st.session_state["past"] = []


def get_text():
    input_text = st.text_input("You: ", "", key="input")
    return input_text


user_input = get_text()

if user_input:
    output = get_response(user_input)

    st.session_state.past.append(user_input)
    st.session_state.generated.append(output.get('text', ''))

if st.session_state["generated"]:
    for i in range(len(st.session_state["generated"]) - 1, -1, -1):
        message(st.session_state["generated"][i], key=str(i))
        message(st.session_state["past"][i],
                is_user=True, key=str(i) + "_user")
