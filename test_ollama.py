
import ollama

response = ollama.chat(
    model="qwen2.5:3b",
    messages=[
        {
            "role": "user",
            "content": "Explain what a research paper is in simple words."
        }
    ]
)

print(response["message"]["content"])
