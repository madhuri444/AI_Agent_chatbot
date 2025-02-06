This AI agent utilizes Tavily Search to fetch real-time web search results, processes the data using LangGraph, and provides intelligent responses via FastAPI. The agent leverages LLMs to generate insightful answers, making it an effective tool for information retrieval and decision-making.

Features

Real-time web search using Tavily Search API

Graph-based state management with LangGraph

Fast API responses with FastAPI & Uvicorn

LLM-powered reasoning for enhanced query understanding

Scalable & modular architecture

Tech Stack

LangGraph: For agent state management

FastAPI: API framework for serving the AI agent

Uvicorn: ASGI server for FastAPI

Tavily Search API: For retrieving up-to-date web information

LLMs: For processing and generating intelligent responses

Installation


# Create a virtual environment
conda create -p venv python==3.12
conda avtivate venv # To activate the environment
# Install dependencies
pip install -r requirements.txt

Configuration

Get an API key from Tavily Search

Set up environment variables in .env file:

TAVILY_API_KEY=your_api_key
LLM_PROVIDER=your_llm_provider

