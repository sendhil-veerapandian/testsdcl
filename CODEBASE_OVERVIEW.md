# 🏗️ **SDLC Codebase Complete Overview**

## 📁 **Project Structure**
```
src/sdlc/
├── api/                    # FastAPI backend endpoints
├── LLMS/                   # AI model integrations
├── graph/                  # LangGraph workflow engine
├── nodes/                  # Individual workflow nodes
├── state/                  # Data models and state management
├── cache/                  # Redis caching system
├── dto/                    # Data transfer objects
├── utils/                  # Utility functions and helpers
└── ui/                     # User interface components
```

---

## 🚀 **Core Architecture Components**

### **1. API Layer (`/api/`)**
**Purpose**: RESTful API endpoints for the SDLC platform

#### **`fastapi_app.py`** - Main API Server
- **Function**: FastAPI application with CORS, middleware, and endpoint definitions
- **Key Features**:
  - **Lifespan Management**: Initializes LLM models and graph components on startup
  - **API Endpoints**:
    - `POST /api/v1/sdlc/start` - Initialize new SDLC project
    - `POST /api/v1/sdlc/user_stories` - Generate user stories
    - `POST /api/v1/sdlc/progress_flow` - Move workflow to next stage
  - **Security**: API key validation for different LLM providers
  - **Error Handling**: Comprehensive error responses with proper HTTP status codes

**Usage**: Serves as the backend API for both Streamlit and future Next.js frontends

---

### **2. AI Models (`/LLMS/`)**
**Purpose**: Integration with different Large Language Model providers

#### **`groqllm.py`** - Groq Integration
- **Function**: Wrapper for Groq's free LLM models
- **Models**: llama-3.1-8b-instant, llama-3.3-70b-versatile, gpt-oss variants
- **Cost**: FREE (primary recommendation for cost-conscious users)

#### **`openai_llm.py`** - OpenAI Integration  
- **Function**: Wrapper for OpenAI GPT models
- **Models**: GPT-5, GPT-4o, GPT-3.5-turbo variants
- **Cost**: Paid (input: $0.03/1K tokens, output: $0.06/1K tokens)

#### **`geminillm.py`** - Google Gemini Integration
- **Function**: Wrapper for Google's Gemini models
- **Models**: gemini-2.0-flash, gemini-2.5-pro-exp
- **Cost**: Free tier available

**Usage**: Provides AI capabilities for all workflow stages (requirements, design, coding, testing)

---

### **3. Workflow Engine (`/graph/`)**
**Purpose**: LangGraph-based workflow orchestration

#### **`graph_builder.py`** - Workflow Definition
- **Function**: Defines the complete SDLC workflow as a directed graph
- **Workflow Stages**:
  1. **Project Initialization** → **Requirements Collection**
  2. **User Stories Generation** → **Review** → **Design Documents**
  3. **Code Generation** → **Code Review** → **Security Review**
  4. **Test Cases** → **QA Testing** → **Deployment** → **Artifacts**
- **Key Features**:
  - **Conditional Edges**: Routes based on review feedback (approved/feedback)
  - **Interruption Points**: Pauses workflow for human review at critical stages
  - **Memory Management**: Redis-based state persistence

#### **`graph_executor.py`** - Workflow Execution
- **Function**: Manages workflow execution and state transitions
- **Key Methods**:
  - `start_workflow()` - Initialize new project session
  - `generate_stories()` - Generate user stories from requirements
  - `graph_review_flow()` - Handle review feedback and progress
  - `update_and_resume_graph()` - Resume workflow from specific nodes

**Usage**: Orchestrates the entire SDLC process with AI assistance

---

### **4. Workflow Nodes (`/nodes/`)**
**Purpose**: Individual processing units for each SDLC stage

#### **`project_requirement_node.py`** - Requirements & User Stories
- **Function**: Handles project initialization and user story generation
- **Key Methods**:
  - `initialize_project()` - Set up project state
  - `generate_user_stories()` - AI-powered user story creation
  - `review_user_stories()` - Handle review process
  - `review_user_stories_router()` - Route based on approval status

#### **`design_document_node.py`** - Design Documentation
- **Function**: Creates functional and technical design documents
- **Features**: AI-generated design docs with review/feedback loop

#### **`coding_node.py`** - Code Generation & Review
- **Function**: Handles code generation, review, and security analysis
- **Stages**: Code generation → Review → Security analysis → Testing

#### **`markdown_node.py`** - Artifact Generation
- **Function**: Creates final project artifacts and documentation

**Usage**: Each node processes specific SDLC stages with AI assistance

---

### **5. State Management (`/state/`)**
**Purpose**: Data models and state persistence

#### **`sdlc_state.py`** - Core Data Models
- **Function**: Defines the structure of SDLC workflow state
- **Key Models**:
  - `SDLCState`: Main workflow state with all stage data
  - `UserStories`: Structured user story format
  - `DesignDocument`: Functional and technical design docs
- **Features**: Pydantic validation, JSON serialization support

**Usage**: Maintains consistent data structure across all workflow stages

---

### **6. Caching System (`/cache/`)**
**Purpose**: Redis-based state persistence and session management

#### **`redis_cache.py`** - Redis Operations
- **Function**: Manages workflow state persistence
- **Key Methods**:
  - `save_state_to_redis()` - Save current workflow state
  - `get_state_from_redis()` - Retrieve saved state
  - `flush_redis_cache()` - Clear all cached data
- **Features**: 24-hour TTL, JSON serialization, error handling

**Usage**: Enables workflow resumption and multi-user sessions

---

### **7. Data Transfer (`/dto/`)**
**Purpose**: API request/response models

#### **`sdlc_request.py`** - API Request Models
- **Function**: Defines structure for incoming API requests
- **Fields**: project_name, requirements, task_id, status, feedback
- **Validation**: Pydantic field validation with examples

#### **`sdlc_response.py`** - API Response Models
- **Function**: Standardized API response format
- **Fields**: status, message, task_id, state, error

**Usage**: Ensures consistent API contract between frontend and backend

---

### **8. Utilities (`/utils/`)**
**Purpose**: Helper functions and system configuration

#### **`token_tracker.py`** - Cost & Usage Tracking
- **Function**: Monitors AI model usage and costs
- **Features**:
  - **Token Counting**: Accurate token usage per request
  - **Cost Calculation**: Real-time cost estimation per model
  - **Session Tracking**: Usage summaries and cost analysis
  - **Model Pricing**: Up-to-date pricing for all providers

#### **`constants.py`** - System Constants
- **Function**: Centralized workflow stage definitions
- **Constants**: All SDLC stage names and review types

#### **`logging_config.py` - Logging Setup
- **Function**: Configures application logging
- **Features**: Console + file logging, rotation, compression

#### **`Utility.py`** - General Utilities
- **Function**: Common helper functions

**Usage**: Provides essential system utilities and monitoring

---

### **9. User Interface (`/ui/`)**
**Purpose**: Frontend interface components

#### **`uiconfigfile.py`** - UI Configuration
- **Function**: Manages UI configuration from INI files
- **Features**: LLM options, model selections, page titles

#### **`streamlit_ui/streamlit_app.py`** - Streamlit Frontend
- **Function**: Complete Streamlit-based user interface
- **Features**:
  - **Project Setup**: Initialize new SDLC projects
  - **Requirements Management**: Add/edit project requirements
  - **User Stories**: View and manage AI-generated stories
  - **Token Tracking**: Real-time usage and cost monitoring
  - **Workflow Progress**: Visual progress through SDLC stages

**Usage**: Current frontend interface (will be replaced by Next.js)

---

## 🔄 **Data Flow Architecture**

```
User Input → Streamlit UI → FastAPI → LangGraph → AI Models → Redis Cache
    ↓
Workflow State → Node Processing → State Updates → Cache Persistence
    ↓
Response → API → UI → User Feedback → Workflow Continuation
```

---

## 🎯 **Key Features & Capabilities**

### **1. AI-Powered Workflow**
- **Automated Stages**: Each SDLC stage uses AI for content generation
- **Human Review**: Critical decision points require human approval
- **Feedback Loops**: Continuous improvement through review cycles

### **2. Multi-LLM Support**
- **Provider Flexibility**: Switch between Groq (free), OpenAI, Gemini
- **Cost Optimization**: Choose models based on budget and quality needs
- **Fallback Support**: Multiple providers ensure reliability

### **3. State Persistence**
- **Session Management**: Resume workflows across browser sessions
- **Multi-User**: Support for concurrent project development
- **Data Integrity**: Redis-based state validation and recovery

### **4. Token & Cost Tracking**
- **Real-time Monitoring**: Live usage tracking per request
- **Cost Estimation**: Accurate cost prediction before execution
- **Budget Control**: Prevent unexpected costs with usage limits

---

## 🚀 **Usage Patterns**

### **1. Starting a New Project**
```python
# API Call
POST /api/v1/sdlc/start
{
  "project_name": "E-commerce Platform"
}

# Response
{
  "task_id": "sdlc-session-abc123",
  "state": {...}
}
```

### **2. Adding Requirements**
```python
# API Call  
POST /api/v1/sdlc/user_stories
{
  "task_id": "sdlc-session-abc123",
  "requirements": ["User authentication", "Product catalog"]
}
```

### **3. Review & Progress**
```python
# API Call
POST /api/v1/sdlc/progress_flow
{
  "task_id": "sdlc-session-abc123",
  "status": "approved",
  "feedback": "Great user stories!",
  "next_node": "review_design_documents"
}
```

---

## 🔧 **Configuration & Environment**

### **Required Environment Variables**
```bash
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key  
OPENAI_API_KEY=your_openai_key
REDIS_URL=your_redis_url
```

### **Redis Configuration**
- **Local Development**: localhost:6379
- **Production**: Upstash Redis with URL/token

---

## 💡 **Next.js Migration Benefits**

### **Current Limitations (Streamlit)**
- ❌ Limited UI customization
- ❌ Poor mobile experience  
- ❌ Performance bottlenecks
- ❌ Limited state management

### **Next.js Advantages**
- ✅ **Modern UI**: Unlimited design flexibility
- ✅ **Performance**: Faster loading, better caching
- ✅ **Mobile**: Perfect responsive experience
- ✅ **Scalability**: Handle multiple users efficiently
- ✅ **Real-time**: WebSocket integration possible

---

## 🎯 **Recommendation**

**The codebase is perfectly architected for Next.js migration!**

1. **Backend is Ready**: All APIs, workflows, and AI integrations work perfectly
2. **Clean Separation**: Frontend and backend are completely decoupled
3. **State Management**: Redis-based state works with any frontend
4. **API Contract**: Well-defined DTOs ensure consistent communication

**Migration Effort**: 8-14 days to replace Streamlit with modern Next.js UI
**Risk Level**: Very Low (only frontend changes needed)
**Business Value**: High (professional UI, better UX, mobile support)

The foundation is solid - you just need a better frontend! 🚀

