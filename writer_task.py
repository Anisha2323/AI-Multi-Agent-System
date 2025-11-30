from crewai import Task

def create_writer_task(agent):
    """Create and return the Writer Task."""
    
    writer_task = Task(
        description="""Create a comprehensive final report based on the research findings and analysis.
        
        Your task is to:
        1. Read both 'research_findings.md' and 'analysis_report.md'
        2. Review all the gathered information and analysis
        3. Create a well-structured, comprehensive report
        
        The final report must include:
        - Executive Summary: A concise overview of the topic and key findings
        - Introduction: Context and background information about the topic
        - Main Findings: Detailed presentation of the research findings organized logically
        - Analysis and Insights: Key insights, patterns, and conclusions from the analysis
        - Sources and References: Complete list of all reliable sources used in the research
        
        Save the final report to 'final_report.md' with proper formatting, clear sections, 
        and professional presentation suitable for stakeholders or decision-makers.
        """,
        agent=agent,
        expected_output="A comprehensive, well-structured final report saved to 'final_report.md' containing executive summary, introduction, main findings, analysis, and reliable sources."
    )
    
    return writer_task

