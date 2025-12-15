"""
Multi-Agent Agentic AI System for Data Science
Main execution script for the CrewAI-based analysis system.
"""

# Windows compatibility patch for signal module
import signal
import sys

# Add missing Unix signals for Windows compatibility
if sys.platform == "win32":
    if not hasattr(signal, 'SIGHUP'):
        signal.SIGHUP = 1
    if not hasattr(signal, 'SIGQUIT'):
        signal.SIGQUIT = 3
    if not hasattr(signal, 'SIGUSR1'):
        signal.SIGUSR1 = 10
    if not hasattr(signal, 'SIGUSR2'):
        signal.SIGUSR2 = 12
    if not hasattr(signal, 'SIGTSTP'):
        signal.SIGTSTP = 18
    if not hasattr(signal, 'SIGCONT'):
        signal.SIGCONT = 19
    if not hasattr(signal, 'SIGTTIN'):
        signal.SIGTTIN = 21
    if not hasattr(signal, 'SIGTTOU'):
        signal.SIGTTOU = 22

import argparse
import os
from dotenv import load_dotenv
from crewai import Crew, Process

from agents import (
    create_planner_agent,
    create_data_analyst_agent,
    create_modeling_agent,
    create_report_writer_agent
)
from tasks import create_tasks


def main():
    """Main execution function."""
    # Load environment variables
    load_dotenv()
    
    # Check for LLM configuration
    use_ollama = os.getenv("USE_OLLAMA", "false").lower() == "true"
    use_gemini = os.getenv("USE_GEMINI", "false").lower() == "true"
    has_openai = os.getenv("OPENAI_API_KEY")
    
    if not use_ollama and not use_gemini and not has_openai:
        print("=" * 80)
        print("⚠️  NO LLM CONFIGURED")
        print("=" * 80)
        print("\nYou need to configure an LLM to use this system.")
        print("\n📖 FREE OPTIONS AVAILABLE! See: docs/FREE_LLM_SETUP.md")
        print("\n🆓 Recommended: Ollama (100% Free, Local)")
        print("   1. Install: https://ollama.ai")
        print("   2. Pull model: ollama pull llama2")
        print("   3. Create .env file:")
        print("      USE_OLLAMA=true")
        print("      OLLAMA_MODEL=llama2")
        print("\n💳 Or use OpenAI ($5 free trial):")
        print("   1. Sign up: https://platform.openai.com/signup")
        print("   2. Get API key")
        print("   3. Create .env file:")
        print("      OPENAI_API_KEY=sk-your-key-here")
        print("\n" + "=" * 80)
        sys.exit(1)
    
    # Configure LLM
    llm = None
    if use_ollama:
        from crewai import LLM
        ollama_model = os.getenv("OLLAMA_MODEL", "llama2")
        ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
        
        # Ensure model has ollama/ prefix for LiteLLM
        if not ollama_model.startswith("ollama/"):
            ollama_model = f"ollama/{ollama_model}"
            
        print(f"🦙 Using Ollama with model: {ollama_model}")
        print(f"   Base URL: {ollama_base_url}")
        
        llm = LLM(
            model=ollama_model, 
            base_url=ollama_base_url
        )
    elif use_gemini:
        print("🔷 Using Google Gemini API")
        # Gemini setup would go here
    else:
        print(f"🤖 Using OpenAI API")
        # OpenAI is default, no custom LLM needed
    
    
    # Parse command line arguments
    parser = argparse.ArgumentParser(
        description="Multi-Agent Data Science Analysis System"
    )
    parser.add_argument(
        "--topic",
        type=str,
        required=True,
        help="Business description or analysis objective"
    )
    parser.add_argument(
        "--csv",
        type=str,
        required=True,
        help="Path to the CSV dataset file"
    )
    parser.add_argument(
        "--output",
        type=str,
        default="report_final.md",
        help="Output filename for the final report (default: report_final.md)"
    )
    
    args = parser.parse_args()
    
    # Validate inputs
    if not os.path.exists(args.csv):
        print(f"ERROR: CSV file not found: {args.csv}")
        sys.exit(1)
    
    # Convert to absolute path
    csv_path = os.path.abspath(args.csv)
    
    print("=" * 80)
    print("MULTI-AGENT DATA SCIENCE ANALYSIS SYSTEM")
    print("=" * 80)
    print(f"\n📊 Business Objective: {args.topic}")
    print(f"📁 Dataset: {csv_path}")
    print(f"📝 Output Report: {args.output}")
    print("\n" + "=" * 80)
    print("INITIALIZING AGENTS")
    print("=" * 80)
    
    # Create agents
    print("\n✓ Creating Project Planner Agent...")
    planner = create_planner_agent(llm=llm)
    
    print("✓ Creating Data Analyst Agent (with CSV & Stats tools)...")
    analyst = create_data_analyst_agent(llm=llm)
    
    print("✓ Creating Modeling Agent...")
    modeler = create_modeling_agent(llm=llm)
    
    print("✓ Creating Report Writer Agent...")
    writer = create_report_writer_agent(llm=llm)
    
    
    print("\n" + "=" * 80)
    print("DEFINING TASKS")
    print("=" * 80)
    
    # Create tasks
    tasks = create_tasks(
        planner=planner,
        analyst=analyst,
        modeler=modeler,
        writer=writer,
        topic=args.topic,
        csv_path=csv_path
    )
    
    print(f"\n✓ Created {len(tasks)} tasks:")
    print("  1. Planning Task → Project Planner")
    print("  2. EDA Task → Data Analyst")
    print("  3. Modeling Task → ML Engineer")
    print("  4. Report Writing Task → Technical Writer")
    
    print("\n" + "=" * 80)
    print("ASSEMBLING CREW")
    print("=" * 80)
    
    # Create crew
    crew = Crew(
        agents=[planner, analyst, modeler, writer],
        tasks=tasks,
        process=Process.sequential,
        verbose=True
    )
    
    print("\n✓ Crew assembled with sequential process")
    
    print("\n" + "=" * 80)
    print("STARTING ANALYSIS")
    print("=" * 80)
    print("\nThis may take several minutes. The agents will work sequentially:")
    print("Planning → EDA → Modeling → Report Writing\n")
    
    # Execute the crew
    try:
        result = crew.kickoff(inputs={
            "topic": args.topic,
            "csv_path": csv_path
        })
        
        print("\n" + "=" * 80)
        print("ANALYSIS COMPLETE")
        print("=" * 80)
        
        # Save the final report
        with open(args.output, 'w', encoding='utf-8') as f:
            f.write(str(result))
        
        print(f"\n✓ Final report saved to: {args.output}")
        print(f"✓ File size: {os.path.getsize(args.output):,} bytes")
        
        print("\n" + "=" * 80)
        print("SUCCESS")
        print("=" * 80)
        print(f"\nYour technical report is ready: {args.output}")
        print("Thank you for using the Multi-Agent Data Science Analysis System!")
        
    except Exception as e:
        print("\n" + "=" * 80)
        print("ERROR DURING EXECUTION")
        print("=" * 80)
        print(f"\nAn error occurred: {str(e)}")
        print("\nPlease check:")
        print("  - Your OpenAI API key is valid")
        print("  - The CSV file is properly formatted")
        print("  - You have sufficient API credits")
        sys.exit(1)


if __name__ == "__main__":
    main()
