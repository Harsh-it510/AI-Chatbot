from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# Enhanced template for better conversational flow
template = """
You are a helpful and intelligent AI assistant. 
Respond clearly, concisely, and politely to the user's questions.

Here is the chat history:
{context}

{question}
AI:"""

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

chat_history = ""

def get_bot_response(user_input):
    global chat_history
    result = chain.invoke({"question": user_input, "context": chat_history})
    chat_history += f"👨🏼: {user_input}\n🤖: {result}\n"

    return result
