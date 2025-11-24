import os
from dotenv import load_dotenv
from chromadb import PersistentClient
from chromadb.config import Settings


memory_history = []

def update_history(role, content):
    memory_history.append({"role": role, "content": content})

def get_history():
    return memory_history
