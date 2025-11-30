from crewai import Task

def create_analysis_task(agent):
    """Create and return the Analysis Task."""
    
    analysis_task = Task(
        description="""Analyze the research findings from the file 'research_findings.md'.
        
        Your task is to:
        1. Read and review the research findings from research_findings.md
        2. Extract key insights and patterns from the gathered information
        3. Identify relationships between different pieces of information
        4. Draw meaningful conclusions based on the data
        5. Highlight important trends, implications, or noteworthy observations
        
        Create a detailed analysis report and save it to 'analysis_report.md' with:
        - Executive summary of key insights
        - Pattern analysis and trends identified
        - Key conclusions and implications
        - Important observations and recommendations
        """,
        agent=agent,
        expected_output="A detailed analysis report saved to 'analysis_report.md' containing key insights, patterns, conclusions, and recommendations based on the research findings."
    )
    
    return analysis_task

