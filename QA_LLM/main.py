from langchain_helper import get_few_shot_db_chain

import streamlit as st 

st.title("Tshirts Database Q&A")

question = st.text_input("Ask a question :")

if question:
    chain = get_few_shot_db_chain()
    answer = chain.run(question)
    #print(answer)

    st.header("Answer :")
    st.write(answer)