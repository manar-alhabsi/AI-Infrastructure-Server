# AI Infrastructure Server

An AI-powered Infrastructure Management Server that combines Large Language Models (LLMs) with enterprise infrastructure services.

The goal of this project is to provide a natural language interface for IT administrators. Instead of using multiple management tools or writing scripts manually, administrators can interact with an AI assistant that understands requests and performs infrastructure operations.

---

## Project Overview

The server consists of three main components:

- **Ollama** – Runs local Large Language Models.
- **Open WebUI** – Provides a web-based chat interface.
- **FastAPI Backend** – Handles API requests and communicates with Ollama.

The backend exposes REST APIs that can later be extended to integrate with:

- Active Directory
- VMware vSphere
- Hyper-V
- Microsoft Intune
- ServiceNow / SMAX
- PowerShell automation
- Monitoring systems

---

## Current Features

- Local AI using Ollama
- Gemma 3 language model
- FastAPI REST API
- Docker Compose deployment
- OpenAPI (Swagger) documentation
- Open WebUI integration
- Containerized architecture
- Git version control

---

## Project Structure

```
AI-Infrastructure-Server/
│
├── backend/
│   ├── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── docs/
├── diagrams/
├── scripts/
├── screenshots/
│
├── docker-compose.yml
├── README.md
└── LICENSE
```

---

## Architecture

```
                User
                  │
                  ▼
          FastAPI Backend
                  │
                  ▼
             Ollama Server
                  │
                  ▼
            Gemma 3 Model
                  │
                  ▼
          AI Generated Reply
```

---

## Technologies Used

- Python 3.12
- FastAPI
- Docker
- Docker Compose
- Ollama
- Open WebUI
- Git
- GitHub

---

## Installation

Clone the repository:

```bash
git clone https://github.com/manar-alhabsi/AI-Infrastructure-Server.git

cd AI-Infrastructure-Server
```

Start the containers:

```bash
docker compose up -d
```

---

## API Documentation

After starting the project:

Swagger UI

```
http://SERVER-IP:8001/docs
```

Example:

```
http://192.168.xxx.xxx:8001/docs
```

---

## Example Request

POST

```
/chat
```

Request:

```json
{
    "message": "Hello"
}
```

Response:

```json
{
    "reply": "Hello! How can I help you today?"
}
```

---

## Future Roadmap

Planned features include:

- Active Directory management
- User provisioning
- Password reset
- Account lock/unlock
- VMware management
- Hyper-V management
- Intune integration
- ServiceNow integration
- Infrastructure monitoring
- Role-Based Access Control (RBAC)
- Audit logging
- AI function calling
- Multi-model support
- Dashboard and analytics

---

## Project Goal

This project demonstrates how Artificial Intelligence can simplify enterprise infrastructure management by allowing administrators to use natural language instead of manual administration or scripting.

The long-term vision is to build an AI Infrastructure Assistant capable of securely managing enterprise environments through conversational commands.

---

## Author

**Manar Al Habsi**

Computer Science Student

Specialization:
Intelligent Systems & Data Science

Sultan Qaboos University

---

## License

This project is licensed under the MIT License.
