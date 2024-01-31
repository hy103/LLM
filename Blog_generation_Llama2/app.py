import streamlit as st 
from langchain.prompts import PromptTemplate
from langchain.llms import CTransformers
from ctransformers import AutoModelForCausalLM

##To get response from Llama-2 model
def get_llama_response(input_text, no_words, blog_style):
    ##Llama-2 model

    llm = AutoModelForCausalLM.from_pretrained("TheBloke/Llama-2-7B-Chat-GGML", model_file="llama-2-7b-chat.ggmlv3.q8_0.bin")

                        

    ## prompt Template 
    template = """
            Write a blog for {blog_style} jpb profile for a topic {input_text}
            within {no_words} words."""


    prompt =PromptTemplate(input_variables= ["blog_style", "input_text", "no_words"],
                           template = template)
    
    #Generate the response from llama 2 model
    response = llm(prompt.format(blog_style = blog_style, input_text = input_text, no_words = no_words))
    print(response)

    return response



st.set_page_config(page_title = "Blog Generation", page_icon = ':bar_chart:',
layout = 'centered',
initial_sidebar_state = 'collapsed')

st.header("Blog Generation")

input_text = st.text_input("Enter the topic for blog")


##Create columns for fields 
col1, col2 = st.columns([5,5])

with col1:
    no_words = st.text_input("No of words")

with col2:
    blog_style = st.selectbox("Writing the blog for", ("Researchers", "Data Scientist", "Literature"), index=0)

submit = st.button("Generate")

if submit:
    st.write(get_llama_response(input_text, no_words, blog_style))