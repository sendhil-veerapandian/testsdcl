# 🏗️ SDLC Platform - Complete Project Structure

**Microservices Architecture with Separate Backend and Frontend Services**

---

## 📁 **Root Project Structure**

```
SDLC/                                    # Root project folder
├── backend/                             # Python FastAPI Backend Service
│   ├── src/sdlc/                       # Core SDLC application
│   ├── app_api.py                      # FastAPI entry point
│   ├── requirements.txt                # Python dependencies
│   ├── dockerfile                      # Docker configuration
│   └── README.md                       # Backend documentation
│
├── frontend/                            # Next.js Frontend Service (NEW!)
│   ├── src/                            # Source code
│   ├── package.json                    # Node.js dependencies
│   ├── next.config.js                  # Next.js configuration
│   ├── tailwind.config.js              # Tailwind CSS configuration
│   ├── tsconfig.json                   # TypeScript configuration
│   └── README.md                       # Frontend documentation
│
├── postman_collection/                  # API testing collections
├── workflow_graph.png                   # Workflow visualization
├── README.md                            # Main project documentation
├── IMPROVEMENT_ROADMAP.md              # Future development plans
├── NEXTJS_MIGRATION_GUIDE.md           # Migration documentation
└── PROJECT_STRUCTURE.md                # This file
```

---

## 🔧 **Backend Service (Python/FastAPI)**

### **Location**: `backend/`

### **Technology Stack**
- **Framework**: FastAPI (Python)
- **Workflow Engine**: LangGraph
- **LLM Integration**: Gemini, Groq, OpenAI
- **State Management**: Redis
- **API**: RESTful endpoints

### **Key Components**
```
backend/
├── src/sdlc/
│   ├── api/                            # FastAPI application & endpoints
│   │   └── fastapi_app.py             # Main API application
│   ├── cache/                          # Redis cache management
│   │   └── redis_cache.py             # Redis connection & operations
│   ├── dto/                            # Data Transfer Objects
│   │   ├── sdlc_request.py            # API request models
│   │   └── sdlc_response.py           # API response models
│   ├── graph/                          # LangGraph workflow engine
│   │   ├── graph_builder.py           # Workflow definition
│   │   └── graph_executor.py          # Workflow execution
│   ├── LLMS/                           # LLM provider integrations
│   │   ├── geminillm.py               # Google Gemini integration
│   │   ├── groqllm.py                 # Groq integration
│   │   └── openai_llm.py              # OpenAI integration
│   ├── nodes/                          # Workflow nodes
│   │   └── project_requirement_node.py # Project setup node
│   ├── state/                          # State management
│   │   └── sdlc_state.py              # Workflow state models
│   ├── api/                            # FastAPI application & endpoints
│   │   └── fastapi_app.py             # Main API application
│   └── utils/                          # Utility functions
│       ├── constants.py                # Application constants
│       ├── logging_config.py           # Logging configuration
│       └── token_tracker.py            # Token usage tracking
```

### **API Endpoints**
- `POST /api/v1/sdlc/start` - Initialize project
- `POST /api/v1/sdlc/user_stories` - Generate user stories
- `POST /api/v1/sdlc/progress_flow` - Progress workflow
- `GET /docs` - API documentation (Swagger UI)

---

## 🎨 **Frontend Service (Next.js)**

### **Location**: `frontend/`

### **Technology Stack**
- **Framework**: Next.js 14 (React)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **State Management**: Zustand + React Query
- **UI Components**: Custom enterprise design system

### **Key Components**
```
frontend/
├── src/
│   ├── app/                            # Next.js App Router
│   │   ├── layout.tsx                 # Root layout with providers
│   │   ├── page.tsx                   # Landing page
│   │   ├── globals.css                # Global styles & Tailwind
│   │   └── providers.tsx              # React providers (React Query)
│   ├── components/                     # Reusable UI components
│   │   ├── ui/                        # Base UI components
│   │   ├── forms/                     # Form components
│   │   ├── workflow/                  # Workflow-specific components
│   │   └── layout/                    # Layout components
│   ├── lib/                           # Utilities & configurations
│   │   └── api.ts                     # API client for backend
│   ├── types/                         # TypeScript type definitions
│   │   └── index.ts                   # All application types
│   ├── hooks/                         # Custom React hooks
│   └── utils/                         # Utility functions
├── public/                            # Static assets
├── package.json                       # Dependencies & scripts
├── next.config.js                     # Next.js configuration
├── tailwind.config.js                 # Tailwind CSS configuration
├── postcss.config.js                  # PostCSS configuration
├── tsconfig.json                      # TypeScript configuration
└── README.md                          # Frontend documentation
```

### **Design System**
- **Colors**: Professional blues, grays, status colors
- **Typography**: Inter font family
- **Components**: Enterprise-grade cards, buttons, forms, tables
- **Spacing**: 8px grid system
- **Responsive**: Mobile-first approach

---

## 🌐 **Service Communication**

### **Architecture Pattern**
```
┌─────────────────┐    HTTP/REST    ┌─────────────────┐
│   Frontend      │ ◄──────────────► │    Backend      │
│   (Next.js)     │                 │   (FastAPI)     │
│   Port: 3000    │                 │   Port: 8000    │
└─────────────────┘                 └─────────────────┘
         │                                    │
         │                                    │
         ▼                                    ▼
┌─────────────────┐                 ┌─────────────────┐
│   Browser       │                 │     Redis       │
│   (User)        │                 │   (State DB)    │
└─────────────────┘                 └─────────────────┘
```

### **API Communication**
- **Protocol**: HTTP/REST
- **Format**: JSON
- **Authentication**: API keys (environment variables)
- **CORS**: Configured for cross-origin requests

---

## 🚀 **Development Workflow**

### **1. Start Backend Service**
```bash
cd backend
# Activate virtual environment
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate     # Windows

# Install dependencies
pip install -r requirements.txt

# Start FastAPI server
uvicorn src.sdlc.api.fastapi_app:app --host 0.0.0.0 --port 8000 --reload
```

### **2. Start Redis (Required)**
```bash
# Using Docker
docker run -d -p 6379:6379 --name sdlc-redis redis

# Or start existing container
docker start sdlc-redis
```

### **3. Start Frontend Service**
```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm run dev
```

### **4. Access Services**
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs
- **Frontend**: http://localhost:3000

---

## 🔄 **Migration Status**

### **✅ Completed**
- [x] **Backend**: FastAPI with LangGraph workflow engine
- [x] **Backend**: LLM integrations (Gemini, Groq, OpenAI)
- [x] **Backend**: Redis state management
- [x] **Backend**: REST API endpoints
- [x] **Frontend**: Next.js project setup
- [x] **Frontend**: TypeScript configuration
- [x] **Frontend**: Tailwind CSS with enterprise design system
- [x] **Frontend**: Landing page
- [x] **Frontend**: API client for backend communication

### **🚧 In Progress**
- [ ] **Frontend**: Dashboard layout and navigation
- [ ] **Frontend**: Project setup forms
- [ ] **Frontend**: Workflow management components
- [ ] **Frontend**: Real-time updates and WebSocket integration

### **📋 Planned**
- [ ] **Frontend**: Advanced UI components
- [ ] **Frontend**: Role-based access control
- [ ] **Frontend**: Analytics and reporting
- [ ] **Frontend**: Testing suite
- [ ] **Frontend**: Performance optimization

---

## 🎯 **Benefits of This Architecture**

### **1. Separation of Concerns**
- **Backend**: Business logic, AI workflows, data management
- **Frontend**: User interface, user experience, state management

### **2. Scalability**
- **Independent scaling** of frontend and backend
- **Microservices** can be deployed separately
- **Load balancing** for each service

### **3. Technology Flexibility**
- **Backend**: Python ecosystem (AI/ML libraries)
- **Frontend**: Modern web technologies (React, TypeScript)
- **Easy to swap** individual services

### **4. Development Efficiency**
- **Parallel development** of frontend and backend
- **Independent deployment** cycles
- **Technology-specific tooling** for each service

### **5. Enterprise Ready**
- **Professional UI/UX** for IT teams
- **Modern development practices** (TypeScript, React)
- **Scalable architecture** for large organizations

---

## 🔧 **Configuration Files**

### **Backend Configuration**
- **Environment Variables**: `.env` file for API keys
- **Redis**: Local Docker container (configurable)
- **LLM Models**: Configurable in `uiconfigfile.ini`

### **Frontend Configuration**
- **Environment Variables**: `.env.local` for API URL
- **API Endpoints**: Configurable via `NEXT_PUBLIC_API_URL`
- **Design System**: Tailwind CSS with custom components

---

## 📚 **Documentation Structure**

### **Root Level**
- `README.md` - Main project overview
- `PROJECT_STRUCTURE.md` - This file
- `IMPROVEMENT_ROADMAP.md` - Future development plans
- `NEXTJS_MIGRATION_GUIDE.md` - Migration documentation

### **Service Level**
- `backend/README.md` - Backend service documentation
- `frontend/README.md` - Frontend service documentation

---

## 🚀 **Next Steps**

### **Immediate (Phase 2)**
1. **Complete Dashboard Layout** - Professional navigation and layout
2. **Project Setup Forms** - Enterprise-grade forms for project initialization
3. **Workflow Components** - Interactive workflow management
4. **API Integration** - Complete frontend-backend communication

### **Short Term (Phase 3)**
1. **Real-time Features** - WebSocket integration for live updates
2. **Advanced UI Components** - Professional data tables, charts, forms
3. **Performance Optimization** - Code splitting, caching, optimization

### **Long Term (Phase 4)**
1. **Role-based Access Control** - User management and permissions
2. **Analytics Dashboard** - Comprehensive reporting and metrics
3. **Mobile Application** - React Native or PWA
4. **Enterprise Features** - SSO, audit logging, compliance

---

## 💡 **Development Tips**

### **1. Backend Development**
- Use FastAPI's automatic documentation at `/docs`
- Test API endpoints with Postman collections
- Monitor Redis connections and state management

### **2. Frontend Development**
- Use TypeScript for type safety
- Follow the enterprise design system
- Implement responsive design patterns
- Use React Query for server state management

### **3. Integration Testing**
- Test API communication between services
- Verify data flow from backend to frontend
- Test error handling and edge cases

---

**This architecture provides a solid foundation for building a professional, scalable SDLC automation platform that IT teams will love! 🚀**
