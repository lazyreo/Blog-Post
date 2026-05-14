import streamlit as st

if "create_new_blog" not in st.session_state:
    st.session_state.create_new_blog = False

if "done" not in st.session_state:
    st.session_state.done = False


def create_new_blog():
    st.session_state.create_new_blog = True


if st.session_state.create_new_blog:
    if not st.session_state.done:
        title_input = st.text_input("Title")
        intro = st.text_input("Introduction")
        main_body = st.text_input("Main Body")
        concl = st.text_input("Conclusion")
        if title_input and intro and main_body and concl:
            st.session_state.title = title_input
            st.session_state.intro = intro
            st.session_state.main_body = main_body
            st.session_state.concl = concl
            st.session_state.done = True
    elif st.session_state.done:
        st.title(st.session_state.title, width="content")
        st.divider()
        st.write(st.session_state.intro)
        st.write(st.session_state.main_body)
        st.write(st.session_state.concl)


create = st.button("+ Create", on_click=create_new_blog)
