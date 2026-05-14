from llm_client import get_ai_response_stream
import streamlit as st

content = st.text_input("Enter the topic: ")
is_submitted = st.button("Submit")
if is_submitted:
    response_stream = get_ai_response_stream(
        contents=[
            {
                "role":"user",
                "parts":[
                    {
                        "text":"""
    Your Task:
    1. Read the user's input carefully, interpret user's wished topic and understand user's intent.
    2. Search the web related to user's topic according to user's intent.
    3. Carefully extract the passages to write the perfect blog of the user wished for.
    Ex. Format:- 
    [Title](In Bold and big Letters)
    [Divider]
    [Introduction]

    [Main Body]

    [Conclusion]
    """
                    },
                    {
                        "text":f"""
    User's Input:
    {content}
    """
                    }
                ]
                
            }
        ],
                config={
                        "system_instruction": "You are a professional blog creator.",
                        "temperature": 0.5
                }
    )

    try:
        st.write_stream(chunk.text for chunk in response_stream if chunk.text)
    except Exception as e:
        st.write("An unexpected error occured: ", e)