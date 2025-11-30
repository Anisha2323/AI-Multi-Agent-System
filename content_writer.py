from crewai import Agent
from crewai_tools import FileReadTool, FileWriteTool
import os
from langchain_groq import ChatGroq

def create_content_writer():
    """Create and return the Content Writer Agent."""
    
    # Initialize tools
    file_read_tool = FileReadTool()
    file_write_tool = FileWriteTool()
    
    # Get LLM configuration from environment
    model = os.getenv("WRITER_AGENT_LLM", "llama-3.1-70b-versatile")
    temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE", "0.7"))
    
    # Initialize Groq LLM
    llm = ChatGroq(
        model=model,
        temperature=temperature,
        groq_api_key=os.getenv("GROQ_API_KEY")
    )
    
    # Create the agent
    writer_agent = Agent(
        role="Content Writer",
        goal="Create comprehensive, well-structured reports and summaries",
        backstory="""You are an experienced technical writer and content creator with a talent 
        for transforming complex information into clear, engaging, and well-organized reports. 
        You excel at creating executive summaries, structuring content logically, and ensuring 
        all sources are properly cited.""",
        tools=[file_read_tool, file_write_tool],
        llm=llm,
        verbose=True,
        allow_delegation=False
    )
    
    return writer_agent

