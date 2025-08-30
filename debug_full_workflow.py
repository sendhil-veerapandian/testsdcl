"""
Debug script to test the full workflow from get_user_requirements
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.sdlc.graph.graph_builder import GraphBuilder
from src.sdlc.graph.graph_executor import GraphExecutor
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import uuid

load_dotenv()

def test_full_workflow():
    """Test the full workflow including analysis"""
    
    print("🚀 Testing full workflow...")
    
    # Initialize the LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.1
    )
    
    # Create graph
    graph_builder = GraphBuilder(llm)
    graph = graph_builder.setup_graph()
    graph_executor = GraphExecutor(graph)
    
    print("✅ Graph initialized")
    
    # Start workflow
    start_response = graph_executor.start_workflow("E-Commerce Platform")
    task_id = start_response["task_id"]
    
    print(f"✅ Workflow started with task_id: {task_id}")
    print(f"Initial state: {start_response['state']}")
    
    # Generate user stories (this should now call analyze_project_universally)
    requirements = [
        "Users can browse the products",
        "Users should be able to add the product in the cart", 
        "Users should be able to do the payment",
        "Users should be able to see their order history"
    ]
    
    print(f"\n🔍 Generating user stories with requirements: {requirements}")
    
    try:
        stories_response = graph_executor.generate_stories(task_id, requirements)
        
        print("✅ User stories generated successfully!")
        final_state = stories_response["state"]
        
        # Check if project_analysis was created
        if final_state.get("project_analysis"):
            analysis = final_state["project_analysis"]
            print(f"\n📊 Project Analysis Created:")
            print(f"Domain: {analysis.domain}")
            print(f"Project Type: {analysis.project_type}")
            print(f"Complexity: {analysis.complexity}")
            print(f"Stakeholders: {analysis.stakeholders}")
            print(f"Timeline: {analysis.estimated_timeline}")
        else:
            print("❌ project_analysis is still None!")
            return False
            
        # Check user stories
        if final_state.get("user_stories") and final_state["user_stories"].get("user_stories"):
            stories = final_state["user_stories"]["user_stories"]
            print(f"\n📝 Generated {len(stories)} user stories:")
            for i, story in enumerate(stories[:2], 1):  # Show first 2 stories
                print(f"  {i}. {story.id}: {story.title}")
                print(f"     Epic: {story.epic}")
                print(f"     Story Points: {story.story_points}")
                print(f"     User Persona: {story.user_persona}")
                if hasattr(story, 'assignee') and story.assignee:
                    print(f"     ❌ ERROR: Assignee should be empty but got: {story.assignee}")
                else:
                    print(f"     ✅ Assignee: None (correct)")
        else:
            print("❌ No user stories generated!")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error during workflow: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_full_workflow()
    print(f"\n🎯 Full Workflow Test {'PASSED' if success else 'FAILED'}")
