from crewai import Agent
from crewai_tools import FileReadTool, FileWriteTool
import os
from langchain_groq import ChatGroq

def create_content_analyst():
    """Create and return the Content Analyst Agent."""
    
    # Initialize the tools
    file_read_tool = FileReadTool()
    file_write_tool = FileWriteTool()
    
    # Get LLM configuration from environment
    model = os.getenv("ANALYSIS_AGENT_LLM", "llama-3.1-70b-versatile")
    temperature = float(os.getenv("ANALYSIS_AGENT_TEMPERATURE", "0.5"))
    
    # Initialize Groq LLM
    llm = ChatGroq(
        model=model,
        temperature=temperature,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Create the agent
    analyst_agent = Agent(
        role="Content Analyst",
        goal="Analyze gathered information to extract key insights, patterns, and conclusions",
        backstory="""You are a skilled analyst with expertise in identifying patterns, 
        extracting meaningful insights, and drawing well-reasoned conclusions from complex 
        information. You excel at synthesizing data from multiple sources and presenting 
        clear, actionable analysis.""",
        tools=[file_read_tool, file_write_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    return analyst_agent

