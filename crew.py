from crewai import Crew
from agents.research_specialist import create_research_specialist
from agents.content_analyst import create_content_analyst
from agents.content_writer import create_content_writer
from tasks.research_task import create_research_task
from tasks.analysis_task import create_analysis_task
from tasks.writer_task import create_writer_task

def create_research_crew():
    """Create and return the Research Crew with all agents and tasks."""
    
    # Create agents
    research_agent = create_research_specialist()
    analyst_agent = create_content_analyst()
    writer_agent = create_content_writer()
    
    # Create tasks
    research_task = create_research_task(research_agent)
    analysis_task = create_analysis_task(analyst_agent)
    writer_task = create_writer_task(writer_agent)
    
    # Set task dependencies (sequential workflow)
    analysis_task.context = [research_task]
    writer_task.context = [research_task, analysis_task]
    
    # Create the crew
    crew = Crew(
        agents=[research_agent, analyst_agent, writer_agent],
        tasks=[research_task, analysis_task, writer_task],
        verbose=True
    )
    
    return crew

