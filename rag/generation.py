import ollama
from rag.retrieval import Retrieval

class Generation:
    def callOpensourceModel(question):
         obj=Retrieval()
         context=obj.retrieve(question)
         context_str="\n".join(context) if context else "No relevant context found."
         
         print("Context",context)
         response=ollama.chat(
              model="mistral",
              messages=[
                   {
                        "role": "system",
                        "content": (
                        "You are a strict assistant. You must answer ONLY from the context provided below. "
                        "Do NOT use any outside knowledge. "
                        "If the context does not contain the answer, respond with exactly: "
                        "'Not enough context to answer this question.'\n\n"
                        f"Context:\n{context}"
                    )
                   },
                   {
                        "role": "user",
                        "content": question
                   }
              ]
         )
         return response.message.content
