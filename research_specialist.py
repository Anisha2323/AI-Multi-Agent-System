from crewai import Agent
from crewai_tools import SerperDevTool, FileWriteTool
import os
from langchain_groq import ChatGroq

def create_research_specialist():
    """Create and return the Research Specialist Agent."""
    
    # Initialize the tools
    search_tool = SerperDevTool()
    file_write_tool = FileWriteTool()
    
    # Get LLM configuration from environment
    model = os.getenv("RESEARCH_AGENT_LLM", "llama-3.1-70b-versatile")
    temperature = float(os.getenv("RESEARCH_AGENT_TEMPERATURE", "0.7"))
    
    # Initialize Groq LLM
    llm = ChatGroq(
        model=model,
        temperature=temperature,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Create the agent
    research_agent = Agent(
        role="Research Specialist",
        goal="Gather comprehensive and accurate information on a given topic from multiple sources",
        backstory="""You are an expert researcher with a keen eye for detail and a passion for 
        finding the most current and reliable information. You excel at searching through multiple 
        sources and identifying key facts, statistics, and authoritative references.""",
        tools=[search_tool, file_write_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    return research_agent

