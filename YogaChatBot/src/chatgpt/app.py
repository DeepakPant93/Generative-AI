# Copyright (c) 2024 AwesomeHelpersInc. All rights reserved.
# This file is part of the YogaGPT project.

import os

import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
## Langmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
# os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

ERROR_MSG = 'You exceeded your current quota, please check your plan and billing details. For more information contact to the system administrator.'


def start_chat():
    ## Prompt Template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system",
             "You are a yoga assistant. Please response to the user queries based on there Yoga related questions. You're only eligible to take questions related to Yoga only, like what is yoga, pranayam and how to cure with yoga."),
            ("user", "Question:{question}")
        ]
    )
    ## streamlit framework
    st.title('Your Personal Yoga Assistant')
    input_text = st.text_input("Search anything related to Yoga...")
    # openAI LLm
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    if input_text:
        output = ERROR_MSG
        try:
                output = chain.invoke({'question': input_text})
        except Exception as e:
            print('Error::', str(e))
            pass
        st.write(output)
