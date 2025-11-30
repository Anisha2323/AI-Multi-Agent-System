"""
Streamlit web application for the AI Research Assistant.
"""
import streamlit as st
import os
from dotenv import load_dotenv
from crew import create_research_crew

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🔍",
    layout="wide"
)

# Title and description
st.title("🔍 AI Research Assistant")
st.markdown("""
    Welcome to your personal AI Research Assistant powered by CrewAI!
    
    This application uses a multi-agent system to:
    1. **Research** - Gather comprehensive information from multiple sources
    2. **Analyze** - Extract key insights and patterns
    3. **Write** - Create a well-structured final report
""")

# Check API keys configuration
groq_key = os.getenv("GROQ_API_KEY")
serper_key = os.getenv("SERPER_API_KEY")

if not groq_key or groq_key == "your_groq_api_key_here":
    st.error("⚠️ GROQ_API_KEY is not configured. Please set it in your .env file.")
    st.stop()

if not serper_key or serper_key == "your_serper_api_key_here":
    st.error("⚠️ SERPER_API_KEY is not configured. Please set it in your .env file.")
    st.stop()

# Sidebar for information
with st.sidebar:
    st.header("📋 Instructions")
    st.markdown("""
    1. Enter your research topic in the text box below
    2. Click "Start Research" to begin the process
    3. Wait for the agents to complete their work
    4. Download the final report when ready
    """)
    
    st.header("⚙️ Configuration")
    st.info(f"**LLM Model:** {os.getenv('RESEARCH_AGENT_LLM', 'llama-3.1-70b-versatile')}")
    st.info("**Status:** ✅ Ready")

# Main content area
st.header("📝 Research Topic")

# Input for research topic
topic = st.text_input(
    "Enter your research topic:",
    placeholder="e.g., Climate Change Impact on Agriculture",
    key="research_topic"
)

# Initialize session state
if "research_completed" not in st.session_state:
    st.session_state.research_completed = False
if "status_message" not in st.session_state:
    st.session_state.status_message = "Ready to start research"

# Status display
st.subheader("📊 Status")
status_placeholder = st.empty()

# Start Research button
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    start_button = st.button("🚀 Start Research", type="primary", use_container_width=True)

if start_button:
    if not topic or topic.strip() == "":
        st.warning("⚠️ Please enter a research topic before starting.")
    else:
        # Update status
        status_placeholder.info("🔄 Research in progress... Please wait.")
        
        try:
            # Create crew
            with st.spinner("Initializing research crew..."):
                crew = create_research_crew()
            
            # Update status
            status_placeholder.info("🔍 Research Specialist: Gathering information from multiple sources...")
            
            # Execute the crew
            with st.spinner("Processing your research request..."):
                result = crew.kickoff(inputs={"topic": topic})
            
            # Update status
            status_placeholder.info("📊 Content Analyst: Analyzing data and extracting insights...")
            
            # Final status
            status_placeholder.success("✅ Research completed! Analysis finished. Final report generated.")
            
            st.session_state.research_completed = True
            st.session_state.status_message = "Research completed successfully!"
            st.session_state.result = result
            
            st.success("🎉 Your research has been completed successfully!")
            
        except Exception as e:
            status_placeholder.error(f"❌ Error occurred: {str(e)}")
            st.error(f"An error occurred during research: {str(e)}")
            st.session_state.research_completed = False

# Display current status if not processing
if not start_button and not st.session_state.research_completed:
    status_placeholder.info(f"💡 {st.session_state.status_message}")

# Download section
if st.session_state.research_completed:
    st.header("📥 Download Report")
    
    # Check if final_report.md exists
    if os.path.exists("final_report.md"):
        with open("final_report.md", "r", encoding="utf-8") as f:
            report_content = f.read()
        
        st.download_button(
            label="📄 Download Final Report",
            data=report_content,
            file_name="final_report.md",
            mime="text/markdown",
            use_container_width=True
        )
        
        # Preview section
        with st.expander("📖 Preview Final Report"):
            st.markdown(report_content)
    else:
        st.warning("⚠️ Final report not found. Please check if the research process completed successfully.")
    
    # Also show other generated files
    st.subheader("📁 Generated Files")
    
    col1, col2, col3 = st.columns(3)
    
    if os.path.exists("research_findings.md"):
        with open("research_findings.md", "r", encoding="utf-8") as f:
            research_content = f.read()
        with col1:
            st.download_button(
                label="📄 Research Findings",
                data=research_content,
                file_name="research_findings.md",
                mime="text/markdown"
            )
    
    if os.path.exists("analysis_report.md"):
        with open("analysis_report.md", "r", encoding="utf-8") as f:
            analysis_content = f.read()
        with col2:
            st.download_button(
                label="📄 Analysis Report",
                data=analysis_content,
                file_name="analysis_report.md",
                mime="text/markdown"
            )
    
    if os.path.exists("final_report.md"):
        with open("final_report.md", "r", encoding="utf-8") as f:
            final_content = f.read()
        with col3:
            st.download_button(
                label="📄 Final Report",
                data=final_content,
                file_name="final_report.md",
                mime="text/markdown"
            )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: gray;'>
        <p>Powered by CrewAI | Built with Streamlit</p>
    </div>
""", unsafe_allow_html=True)

