# AutoStream Conversational AI Agent

## How to Run the Project
1. Install dependencies:
2. Run the agent:
3. Interact via terminal. Type `exit` to stop.

## Architecture Explanation
This project implements a conversational AI agent for AutoStream using a modular architecture.  
Intent detection is handled in `intent.py`, classifying user input into greeting, pricing inquiry, or high-intent lead.  
RAG functionality is implemented in `rag.py`, where the agent retrieves accurate responses from a local JSON knowledge base instead of hardcoded answers.  
The core agent logic resides in `agent.py`, which maintains conversational memory for up to 5–6 turns and controls the conversation flow.  
Tool execution is isolated in `tools.py`, ensuring the lead capture function is triggered only after all required user details are collected.  
This separation of concerns improves clarity, scalability, and real-world deployability.

## WhatsApp Integration (Concept)
The agent can be integrated with WhatsApp using webhooks via the WhatsApp Business API. Incoming user messages would be forwarded to the agent’s response function, and generated replies would be sent back through the WhatsApp API. The same intent detection, RAG retrieval, and tool execution logic would remain unchanged.
## Demo video
https://youtu.be/eFwxLNQ6LI8