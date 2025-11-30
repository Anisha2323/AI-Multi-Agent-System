from crewai import Task

def create_research_task(agent):
    """Create and return the Research Task."""
    
    research_task = Task(
        description="""Conduct comprehensive research on the topic: {topic}
        
        Your task is to:
        1. Search for the most current and relevant information about the topic
        2. Gather information from multiple authoritative sources
        3. Identify key facts, statistics, and important data points
        4. Document all sources and references
        5. Ensure the information is accurate and up-to-date
        
        Save your findings to a markdown file named 'research_findings.md' with:
        - A clear title and topic overview
        - Key facts and statistics
        - Important information organized by subtopics
        - All sources and references properly cited
        """,
        agent=agent,
        expected_output="A comprehensive markdown file (research_findings.md) containing all research findings, key facts, statistics, and properly cited sources about the topic."
    )
    
    return research_task

