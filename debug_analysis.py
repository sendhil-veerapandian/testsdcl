"""
Debug script to test the analyze_project_universally method
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.sdlc.nodes.project_requirement_node import ProjectRequirementNode
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

def test_project_analysis():
    """Test the project analysis method"""
    
    # Initialize the LLM
    llm = ChatGroq(
        model="llama-3.1-8b-instant",
        temperature=0.1
    )
    
    # Initialize the node
    node = ProjectRequirementNode(llm)
    
    # Test state
    test_state = {
        "project_name": "E-Commerce Platform",
        "requirements": [
            "Users can browse the products",
            "Users should be able to add the product in the cart", 
            "Users should be able to do the payment",
            "Users should be able to see their order history"
        ],
        "next_node": "analyze_project_universally",
        "project_analysis": None
    }
    
    print("🔍 Testing analyze_project_universally method...")
    print(f"Input state: {test_state}")
    
    try:
        # Call the method
        result_state = node.analyze_project_universally(test_state)
        
        print("\n✅ Analysis completed successfully!")
        print(f"Project Analysis: {result_state.get('project_analysis')}")
        
        # Verify the analysis was set
        if result_state.get("project_analysis"):
            analysis = result_state["project_analysis"]
            print(f"\n📊 Analysis Results:")
            print(f"Domain: {analysis.domain}")
            print(f"Project Type: {analysis.project_type}")
            print(f"Complexity: {analysis.complexity}")
            print(f"Stakeholders: {analysis.stakeholders}")
            print(f"Timeline: {analysis.estimated_timeline}")
            return True
        else:
            print("❌ project_analysis is still None!")
            return False
            
    except Exception as e:
        print(f"❌ Error during analysis: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_project_analysis()
    print(f"\n🎯 Test {'PASSED' if success else 'FAILED'}")
