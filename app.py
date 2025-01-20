#from langchain_ollama.llms import OllamaLLM
#llm = OllamaLLM(model="llama3.2") # Using latest llama 3.2 3B-param model
#print(llm.invoke("Tell me a joke"))
#Output: Shows in Terminal or Console

from langchain_ollama.llms import OllamaLLM
import streamlit as st

#
#   LANGCHAIN OLLAMA WRAPPER
#

llm = OllamaLLM(model="llama3.2") # Using latest llama 3.2 3B

#
#   STREAMLIT APP
#

st.title("Dinesh GPT")

# User query input
query = st.text_input(label="Enter your Question??")

# Submit button
if st.button(label="Ask DineshGPT", type="primary"):

    with st.container(border=True):
        with st.spinner(text="Generating response"):
            # Get response from llm
            response = llm.invoke(query)

        # Display it
        st.write(response)