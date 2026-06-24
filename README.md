# 🚀 AI App Compiler

AI App Compiler is an AI-powered system that transforms natural language application requirements into structured software blueprints, database schemas, API specifications, authentication rules, and executable backend code.

Instead of manually designing software architecture, users can describe an application in plain English and the compiler automatically generates the core components required to build the system.

---

## ✨ Features

### 🧠 AI-Powered Requirement Analysis

* Converts natural language prompts into structured application requirements
* Identifies application type, features, and user roles
* Uses Gemini API for intelligent extraction

### 🔄 Intelligent Fallback Mechanism

* Automatically switches to rule-based extraction when AI quotas are exceeded
* Ensures uninterrupted execution of the pipeline

### 🏗️ System Design Generation

* Generates:

  * Business entities
  * Application pages
  * User roles
* Produces a structured software architecture blueprint

### 🎨 UI Schema Generation

Automatically generates UI page definitions:

Example:

* Login
* Dashboard
* Contacts
* Analytics

---

### 🌐 API Schema Generation

Generates complete CRUD APIs:

Example:

GET /api/user

POST /api/user

PUT /api/user/{id}

DELETE /api/user/{id}

---

### 🗄️ Database Schema Generation

Automatically creates database schemas with entity-specific columns.

Example:

User

* id
* name
* email

Contact

* id
* name
* email
* phone

Subscription

* id
* plan_name
* price
* status

---

### 🔐 Authentication Schema Generation

Automatically generates role definitions and access structures.

Example:

Admin

User

---

### ✅ Validation Engine

Validates generated schemas to ensure:

* Entity consistency
* API consistency
* Database consistency
* Authentication consistency

---

### 🛠️ SQLite Runtime Engine

Executes generated database schemas directly in SQLite.

Automatically:

* Creates tables
* Verifies creation
* Validates generated structures

---

### ⚡ FastAPI Backend Code Generation

Generates executable FastAPI route definitions.

Example:

```python
@app.get("/api/user")
def get_users():
    return {"message": "generated"}
```

The generated backend is saved automatically for further development.

---

## 🏛️ Architecture

```text
User Prompt
      │
      ▼
Intent Extractor
(Gemini + Fallback)
      │
      ▼
System Designer
(Gemini + Fallback)
      │
      ▼
Schema Generator
      │
      ├── UI Schema
      ├── API Schema
      ├── DB Schema
      └── Auth Schema
      │
      ▼
Validator
      │
      ▼
Repair Engine
      │
      ▼
SQLite Runtime
      │
      ▼
Backend Code Generator
      │
      ▼
Generated Application Blueprint
```

---

## 🛠️ Tech Stack

### Backend

* Python
* FastAPI
* SQLite
* Pydantic

### AI

* Google Gemini API

### Development Tools

* Git
* GitHub
* VS Code

---

## 📂 Project Structure

```text
backend/
│
├── pipeline/
│   ├── intent_extractor.py
│   ├── system_designer.py
│   ├── schema_generator.py
│   ├── validator.py
│   ├── repair_engine.py
│   ├── runtime.py
│   └── code_generator.py
│
├── schemas/
│
├── outputs/
│   └── generated_backend.py
│
├── main.py
│
└── generated_app.db
```

---
<img width="1220" height="546" alt="image" src="https://github.com/user-attachments/assets/cc98451d-9255-4749-8068-cf7a25787dfe" />


## 📌 Example

### Input

```text
Build a CRM with login, contacts, dashboard,
role-based access, premium plans with payments.
Admins can view analytics.
```

### Generated Output

#### Intent

```json
{
  "app_type": "CRM",
  "features": [
    "login",
    "dashboard",
    "contacts",
    "payments",
    "analytics"
  ],
  "roles": [
    "user",
    "admin"
  ]
}
```

#### Generated Entities

* User
* Contact
* Subscription

#### Generated Pages

* Login
* Dashboard
* Contacts
* Analytics

#### Generated APIs

* GET /api/user
* POST /api/user
* PUT /api/user/{id}
* DELETE /api/user/{id}

---

## 🎯 Future Improvements

* Frontend React code generation
* SQLAlchemy model generation
* OpenAPI documentation generation
* Multi-database support
* Docker deployment generation
* Full-stack application generation
* Agentic workflow orchestration

---

## 👨‍💻 Author

**Veekshitha Adharasani**

B.Tech CSE (AI & ML)

Passionate about:

* Generative AI
* Agentic AI Systems
* Software Engineering
* Full Stack Development
* AI-Powered Automation
