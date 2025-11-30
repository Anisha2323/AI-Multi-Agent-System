"""
Main execution file for testing the Research Crew.
"""
from dotenv import load_dotenv
from crew import create_research_crew

# Load environment variables
load_dotenv()

def main():
    """Test the research crew with a hardcoded topic."""
    
    # Create the crew
    crew = create_research_crew()
    
    # Test with a hardcoded topic
    topic = "Artificial Intelligence in Healthcare"
    
    print(f"Starting research on: {topic}")
    print("=" * 50)
    
    # Execute the crew
    result = crew.kickoff(inputs={"topic": topic})
    
    print("\n" + "=" * 50)
    print("Research completed!")
    print(f"\nResult: {result}")

if __name__ == "__main__":
    main()

