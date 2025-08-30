# SDLC Automation Platform

## _Automate your entire software development lifecycle from idea to release_

## Overview
SDLC Automation Platform is an end-to-end solution designed to automate your entire software development lifecycle. This project leverages a modular, graph-based architecture to transform user requirements into a fully deployed solution. It handles everything from collecting user requirements and generating user stories to creating design documents, code generation, security and test reviews, and deployment. In addition, Markdown artifacts for each phase are automatically generated and made available for download.

SDLC Automation Platform uses a state-driven graph (powered by [LangGraph](https://www.langchain.com/langgraph)) with conditional routing to manage the process. The project also integrates with Redis (optionally hosted externally) for caching and state persistence, and provides a visual workflow diagram of the entire process.

## Features
- **End-to-End SDLC Automation:** Automates every stage of the software development lifecycle—from project initialization to deployment.
- **Graph-Based Orchestration:** Uses a state-driven graph with conditional routing to manage SDLC tasks.
- **Artifact Generation:** Automatically generates Markdown documentation for:
  - Project Requirements
  - User Stories
  - Design Documents (Functional & Technical)
  - Generated Code
  - Security Recommendations
  - Test Cases
  - QA Testing Comments
  - Deployment Feedback
- **Interactive Review & Feedback:** Dynamic review cycles at multiple stages with options to approve or provide feedback with Humman-in-the-Loop.

## Project Structure
```plaintext
SDLC/
├── artifacts/              # Generated Markdown artifact files
├── src/
│   └── sdlc/
│       ├── cache/          # Redis cache and state persistence
│       ├── api/            # Fast API integration logic
│       ├── graph/          # Graph builder and related logic
│       ├── LLMS/           # LLM integrations (Gemini, Groq, OpenAI, etc.)
│       ├── nodes/          # Individual nodes handling each SDLC phase (requirements, coding, etc.)
│       ├── state/          # SDLC state definitions and data models
│       ├── api/             # FastAPI endpoints and application
│       ├── utils/          # Utility functions or classes (formatting, helpers, etc.)
├── app_api.py              # FastAPI backend entry script
├── LICENSE
├── README.md
├── requirements.txt        # Python dependencies
├── workflow_graph.png      
├── .env                    # Environment variables (API keys, etc.)
└── .gitignore
```

## 🚀 Complete Setup Guide

### Prerequisites
- Python 3.11+ 
- Docker Desktop
- At least one LLM API key (Gemini, Groq, or OpenAI)

### Step-by-Step Installation

#### 1. Clone and Setup Environment
```bash
# Clone the repository
git clone <repository-url>
cd SDLC  # or whatever folder name you used

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### 2. Configure Environment Variables
Create a `.env` file in the project root:
```env
# LLM API Keys (you need at least one)
GEMINI_API_KEY=your_gemini_api_key_here
GROQ_API_KEY=your_groq_api_key_here
OPENAI_API_KEY=your_openai_api_key_here

# Redis Configuration (for local Docker)
# No additional config needed for local Docker Redis
```

**Get API Keys:**
- **Gemini (Free)**: https://ai.google.dev/gemini-api/docs/api-key
- **Groq (Free)**: https://console.groq.com/keys  
- **OpenAI (Paid)**: https://platform.openai.com/api-keys

#### 3. Start Redis (State Management)

**What is Redis?** Redis is a temporary storage system that remembers your project progress as you move through different SDLC stages. Think of it as the application's memory.

**Why do we need it?** When you create projects, generate user stories, and progress through development stages, Redis stores this information so you can continue where you left off.

```bash
# Start Docker Desktop first, then:
docker pull redis
docker run -d -p 6379:6379 --name sdlc-redis redis
```

**Redis Management Commands:**
```bash
# Check if Redis is running
docker ps

# Start Redis (after computer restart)
docker start sdlc-redis

# Stop Redis (when done working)
docker stop sdlc-redis

# Auto-start Redis on computer boot (optional)
docker update --restart unless-stopped sdlc-redis
```

**Important Notes:**
- Redis runs in the **background** - you don't need a separate terminal
- After computer restart, run: `docker start sdlc-redis`
- If you see `sdlc-redis` in `docker ps`, it's running ✅

### 🖥️ Running the Application

#### Option 1: FastAPI Backend (API Access)
```bash
# Production mode
python app_api.py

# Development mode (with auto-reload)
uvicorn src.sdlc.api.fastapi_app:app --host 0.0.0.0 --port 8000 --reload
```
- **Server**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Interactive API**: http://localhost:8000/redoc

#### Option 2: Next.js Frontend (Modern Web UI)
```bash
cd frontend
npm run dev
```
- **Web UI**: http://localhost:3000 (opens automatically)
- **Note**: Modern React-based frontend with enterprise-grade UI

### 🔧 Alternative Redis Setup (Cloud)
If you prefer cloud Redis instead of Docker:

1. **Sign up for Upstash Redis** (free tier available)
2. **Update** `src/sdlc/cache/redis_cache.py`:
   ```python
   # Comment out Docker Redis
   # redis_client = redis.Redis(...)
   
   # Uncomment Upstash Redis
   REDIS_URL = os.getenv("REDIS_URL")
   REDIS_TOKEN = os.getenv("REDIS_TOKEN")
   redis_client = Redis(url=REDIS_URL, token=REDIS_TOKEN)
   ```
3. **Add to .env**:
   ```env
   REDIS_URL=your_upstash_redis_url
   REDIS_TOKEN=your_upstash_redis_token
   ```

## FastAPI Endpoints

### 1. Start SDLC Process

Start the SDLC process by providing the project name. This endpoint initializes the SDLC process and returns a task ID.

**Request:**
```http
POST /api/v1/sdlc/start
Content-Type: application/json

{
    "project_name": "Ecommerce Platform"
}
``` 

**Response:**
```json
{
    "status": "success",
    "message": "SDLC process started successfully",
    "task_id": "sdlc-session-f0b4d555",
    "state": {
        "project_name": "Ecommerce Platform"
    },
    "error": null
}
```

### 2. Generate User Stories

Generate user stories based on the provided project name and requirements. Return the generated user stories and the next node to proceed to.

**Request:**
```http
POST /api/v1/sdlc/user_stories
Content-Type: application/json

{
    "project_name": "Ecommerce Platform",
    "requirements": [
        "Users can browser the products",
        "Users should be able to add the product in the cart",
        "Users should be able to do the payment",
        "Users should be able to see their order history"
    ],
    "task_id": "sdlc-session-f0b4d555" // Unique task_id for a particular SDLC process
}
```

**Response:**
```json
{
    "status": "success",
    "message": "User Stories generated successfully",
    "task_id": "sdlc-session-f0b4d555",
    "state": {
        "next_node": "review_user_stories",
        "project_name": "Ecommerce Platform",
        "requirements": [
            "Users can browser the products",
            "Users should be able to add the product in the cart",
            "Users should be able to do the payment",
            "Users should be able to see their order history"
        ],
        "user_stories": {
            "user_stories": [
                {
                    "id": 1,
                    "title": "Browse Products",
                    "description": "As a guest user, I want to browse the products so that I can explore available items.",
                    "priority": 2,
                    "acceptance_criteria": "Verify that products are displayed with relevant details such as name, price, and image.\nVerify that users can filter products based on categories.\nVerify that users can sort products based on price, popularity, and rating."
                },
                {
                    "id": 2,
                    "title": "Add Product to Cart",
                    "description": "As a registered user, I want to add products to the cart so that I can purchase them later.",
                    "priority": 1,
                    "acceptance_criteria": "Verify that users can add products to the cart from the product details page.\nVerify that the cart updates in real-time when a product is added.\nVerify that users can view the cart with the selected products and quantities."
                },
                {
                    "id": 3,
                    "title": "Process Payment",
                    "description": "As a customer, I want to do the payment so that I can complete my purchase.",
                    "priority": 1,
                    "acceptance_criteria": "Verify that users can complete the payment process using valid credit/debit cards.\nVerify that the payment process is secure and compliant with industry standards.\nVerify that users receive an order confirmation upon successful payment."
                },
                {
                    "id": 4,
                    "title": "View Order History",
                    "description": "As a registered user, I want to see my order history so that I can track my past purchases.",
                    "priority": 3,
                    "acceptance_criteria": "Verify that users can view their order history with details such as order date, products, and status.\nVerify that users can filter their order history by date or order status.\nVerify that users can view the details of each order."
                }
            ]
        }
    },
    "error": null
}
```

### 3. Update Workflow Progress

Update the SDLC workflow progress (e.g., moving to the review phase) by providing the next node, status, and feedback. This endpoint updates the workflow state and returns the updated state along with the next node to proceed to. This contains the humman in the loop feedback.

**Request:**
```http
POST /api/v1/sdlc/progress_flow
Content-Type: application/json

{
    "project_name": "Ecommerce Platform",
    "task_id": "sdlc-session-f0b4d555",
    "next_node": "review_user_stories", // next node to proceed to, each iteration will return the next node to proceed to
    "status": "approved", // approved or feedback
    "feedback": "None" // if status is feedback then provide the input
}
```
**Response:**
```json
{
  "status": "success",
  "message": "Flow progressed successfully to next step",
  "task_id": "sdlc-session-9884697b",
  "state": {
    "next_node": "review_design_documents",
    "project_name": "Ecommerce Platform",
    "requirements": [
      "Users can browser the products",
      "Users should be able to add the product in the cart",
      "Users should be able to do the payment",
      "Users should be able to see their order history"
    ],
    "user_stories": {
      "user_stories": [
        {
          "id": 1,
          "title": "Browse Products",
          "description": "As a guest user, I want to browse the products so that I can explore available items.",
          "priority": 2,
          "acceptance_criteria": "Verify that products are displayed with relevant details such as name, price, and image.\nVerify that users can filter products based on categories.\nVerify that users can sort products based on price, popularity, and rating."
        },
        {
          "id": 2,
          "title": "Add Product to Cart",
          "description": "As a registered user, I want to add products to the cart so that I can purchase them later.",
          "priority": 1,
          "acceptance_criteria": "Verify that users can add products to the cart from the product details page.\nVerify that the cart updates in real-time when a product is added.\nVerify that users can view the cart with the selected products and quantities."
        },
        {
          "id": 3,
          "title": "Process Payment",
          "description": "As a customer, I want to do the payment so that I can complete my purchase.",
          "priority": 1,
          "acceptance_criteria": "Verify that users can complete the payment process using valid credit/debit cards.\nVerify that the payment process is secure and compliant with industry standards.\nVerify that users receive an order confirmation upon successful payment."
        },
        {
          "id": 4,
          "title": "View Order History",
          "description": "As a registered user, I want to see my order history so that I can track my past purchases.",
          "priority": 3,
          "acceptance_criteria": "Verify that users can view their order history with details such as order date, products, and status.\nVerify that users can filter their order history by date or order status.\nVerify that users can view the details of each order."
        }
      ]
    },
    "user_stories_feedback": "None",
    "user_stories_review_status": "approved",
    "design_documents": {
      "functional": "```markdown\n# Functional Design Document: Ecommerce Platform\n\n## 1. Introduction and Purpose\n\nThis document outlines the functional design of a new e-commerce platform. The purpose of this platform is to provide a user-friendly and efficient online shopping experience for customers, while also providing a robust and manageable backend for administrators to manage products, orders, and customer data. This document serves as a blueprint for the development team, ensuring a shared understanding of the platform's intended functionality.\n\n## 2. Project Scope\n\nThis project encompasses the development of a fully functional e-commerce platform, including:\n\n*   **Product Catalog:**  Displaying and managing product information.\n*   **Shopping Cart:**  Allowing users to add, modify, and review items before purchase.\n*   **Checkout Process:**  Handling shipping information, payment processing, and order confirmation.\n*   **User Account Management:**  Providing user registration, login, and profile management.\n*   **Order Management:**  Tracking order status and history.\n*   **Payment Gateway Integration:**  Securely processing online payments.\n\nThis project excludes:\n\n*```",
      "technical": "```markdown\n# Technical Design Document: Ecommerce Platform\n\n## 1. System Architecture\n\nThe Ecommerce Platform will adopt a microservices architecture. This approach promotes modularity, scalability, and independent deployments.\n\n**Components:**\n\n*   **Frontend Service:** User interface, handles user interactions (browsing, cart management, checkout).\n*   **Product Catalog Service:** Manages product information (name, description, price, inventory).\n*   **Cart Service:** Manages user shopping carts.\n*   **Order Service:** Processes orders, manages order history.\n*   **Payment Service:** Handles payment processing.\n*   **User Service:** Manages user accounts and authentication.\n*   **Notification Service:** Sends email and other notifications (order confirmation, shipping updates).\n*   ```"
    }
  },
  "error": null
}
```

### How to Use
- **Start the Process:**  
  Send the "start" request to initialize the SDLC process, which returns a task ID and state.
  
- **Generate User Stories:**  
  Use the task ID from the start process, along with the project requirements, to generate user stories.
  
- **Update Workflow Progress:**  
  With the task ID, update the workflow (for example, by approving or giving feedback on user stories). With each iteration pass the next node to proceed to and the status of the previous node. Status can be approved or feedback. Based on the status the next node will be determined. Once the workflow is completed it will return the end node, which indicates the completion of the SDLC process.

- **Added Postman collection for reference.**

## 🎯 Usage Guide

### Using the Next.js Web UI (Recommended)

1. **Start the application**:
   ```bash
   cd frontend
   npm run dev
   ```

2. **Configure LLM**:
   - Select your LLM provider (Gemini/Groq/OpenAI) from the sidebar
   - Enter your API key
   - Choose the model

3. **Create a Project**:
   - Enter project name
   - Click "🚀 Let's Start"
   - Add requirements (one per line)

4. **Follow the SDLC Workflow**:
   - **User Stories**: Review and approve/provide feedback
   - **Design Documents**: Review functional & technical designs
   - **Code Generation**: Review generated code and security recommendations
   - **Test Cases**: Review test cases
   - **QA Testing**: Review testing comments
   - **Deployment**: Get deployment feedback
   - **Download Artifacts**: Download all generated documentation

### Using the FastAPI (For Developers)

1. **Start SDLC Process**:
   ```bash
   POST /api/v1/sdlc/start
   {
     "project_name": "My Project"
   }
   ```

2. **Generate User Stories**:
   ```bash
   POST /api/v1/sdlc/user_stories
   {
     "project_name": "My Project",
     "requirements": ["Requirement 1", "Requirement 2"],
     "task_id": "returned_task_id"
   }
   ```

3. **Progress Workflow**:
   ```bash
   POST /api/v1/sdlc/progress_flow
   {
     "project_name": "My Project",
     "task_id": "task_id",
     "next_node": "review_user_stories",
     "status": "approved",
     "feedback": "None"
   }
   ```

## 🔧 Troubleshooting

### Common Issues

**1. Import Errors**
```bash
ModuleNotFoundError: No module named 'src.sdlc'
```
**Solution**: Make sure you're in the project root directory and virtual environment is activated.

**2. Redis Connection Error**
```bash
redis.exceptions.ConnectionError
```
**Solution**: 
- Start Docker Desktop
- Run: `docker run -d -p 6379:6379 --name sdlc-redis redis`

**3. Schema Validation Errors**
```bash
tool call validation failed: parameters for tool UserStoryList did not match schema
```
**Solution**: This usually happens when the AI model generates data that doesn't match our expected format. The error should be automatically resolved with the latest schema updates.

**4. Logs Appearing in Frontend Terminal**
```bash
Backend logs showing in Next.js terminal
```
**Explanation**: This is normal behavior. The Next.js app communicates with the FastAPI backend, so backend logs appear in the backend terminal while frontend logs appear in the frontend terminal.

**5. API Key Errors**
```bash
Missing required API keys
```
**Solution**: 
- Create `.env` file with valid API keys
- Ensure at least one LLM provider key is set

**4. Package Version Conflicts**
```bash
ImportError: cannot import name 'LangSmithParams'
```
**Solution**: 
```bash
pip install langchain-google-genai==2.1.8 --force-reinstall
```

**5. Config File Not Found**
```bash
AttributeError: 'NoneType' object has no attribute 'split'
```
**Solution**: Config file path issue - already fixed in latest version.

### Development Commands

```bash
# Start with auto-reload (Development)
uvicorn src.sdlc.api.fastapi_app:app --host 0.0.0.0 --port 8000 --reload

# Start without reload (Production)
python app_api.py

# Check Redis status
docker ps | grep redis

# View Redis logs
docker logs sdlc-redis

# Stop Redis
docker stop sdlc-redis

# Remove Redis container
docker rm sdlc-redis
```

## 📊 Workflow Graph
![](workflow_graph.png)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Ensure all prerequisites are installed
3. Verify your API keys are valid
4. Check that Redis is running

For additional help, please open an issue on GitHub.

