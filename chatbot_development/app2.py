from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
from langserve import add_routes
import uvicorn

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"


app=FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)


add_routes(
    app,
    ChatOpenAI(),
    path="/openai"
)

model=ChatOpenAI()
llm=Ollama(model="llama3.2:1b")

prompt1=ChatPromptTemplate.from_template("Write me an essay about {topic}")
prompt2=ChatPromptTemplate.from_template("Write me a poem about {topic}")

add_routes(
    app,
    prompt1|model,
    path="/essay"
)

add_routes(
    app,
    prompt2|model,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)