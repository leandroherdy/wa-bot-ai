# API Documentation - Chatbot Integration with Groq API

<p align="center">
    <a href="https://pre-commit.com/"><img src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white" alt="Pre-Commit"></a>
    <a href="https://github.com/leandroherdy/wa-bot-ai/actions"><img src="https://github.com/leandroherdy/wa-bot-ai/actions/workflows/code-quality.yaml/badge.svg" alt="CI/CD"></a>
</p>

## **Overview**

This API is designed to integrate a chatbot with the Groq API, enabling automated responses based on user input. The system processes incoming messages and responds using predefined instructions. It leverages FastAPI for high-performance HTTP handling and integrates the Groq AI model for instruction processing.

---

## **Features**

1. **Webhook Integration**:
   - Receives incoming messages via POST requests.
   - Processes messages using the Groq API and returns responses.
2. **Groq API Client**:
   - Loads instructions from a local file (`instruction.txt`).
   - Communicates with the Groq API to process user inputs and return AI-generated responses.
3. **Typing Simulation**:
   - Utilizes Waha service to simulate typing before sending responses.
4. **Session Handling**:
   - Supports session-based communication.

---

## **Request and Response Structure**

### **Request Format**
Incoming requests should follow this structure:

```json
{
  "chatId": "12132132130@c.us",
  "text": "Hi there!",
  "session": "default"
}
```

### **Response Format**
Successful responses follow this format:

```json
{
  "status": "success",
  "chat_id": "12132132130@c.us",
  "response": "Hello! How can I assist you?"
}
```

Error responses follow this format:

```json
{
  "status": "error",
  "detail": "An error occurred while processing the request."
}
```

---

## **Endpoints**

### **1. Webhook**

- **Method**: `POST`
- **URL**: `/api/chatbot/webhook`
- **Description**: Processes incoming user messages, applies instructions, and returns automated responses.

**Headers**:
- `Content-Type: application/json`

**Request Body**:
```json
{
  "chatId": "12132132130@c.us",
  "text": "Hi there!",
  "session": "default"
}
```

**Response**:
- **Success (201)**:
  ```json
  {
    "status": "success",
    "chat_id": "12132132130@c.us",
    "response": "Hello! How can I assist you?"
  }
  ```
- **Error (500)**:
  ```json
  {
    "status": "error",
    "detail": "An error occurred while processing the request."
  }
  ```

---

## **Configuration**

### **Environment Variables**
Set the following variables in your `.env` file:

- `GROQ_API_KEY`: API key for authenticating with the Groq API.

### **Project Structure**
```plaintext
.
├── app/
│   ├── endpoints/
│   │   └── waha.py
│   ├── schemas/
│   │   └── waha_schema.py
│   ├── services/
│       ├── groq_API_client.py
│       └── waha_service.py
├── instructions/
│   └── instruction.txt
├── .env
├── pyproject.toml
├── uv.lock
```

---

## **Execution**

### **Prerequisites**
- **Python**: `>=3.12`
- **FastAPI**: `>=0.95.0`
- **uvicorn**: `0.5.15`
- **Docker**: `>=4.36.0`
- **Kubernetes**: `>=1.22`

### **Steps to Run**

1. **Clone the repository**:
   ```bash
   git clone git@github.com:your-repo/chatbot-groq-api.git
   cd chatbot-groq-api
   ```

2. **Install dependencies**:
   ```bash
   uv install
   ```

3. **Deploy to Kubernetes**:
   - Create a Kubernetes deployment file (`deployment.yaml`) to define your service.
   - Apply the deployment:
     ```bash
     kubectl apply -f deployment.yaml
     ```

4. **Start the application locally**:
   ```bash
   uv run fastapi dev
   ```

5. **Test the API using Swagger at `/docs`.

---

## **Testing**

### **Run Tests**
Execute tests and generate coverage reports using:
```bash
uv test --cov
```

---

## **Final Notes**

This API integrates seamlessly with the Groq API to provide an intelligent chatbot experience. For enhancements or contributions, feel free to open a pull request or issue in the repository.
