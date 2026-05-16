import ollama

class Generation:
    def callOpensourceModel(context,question):
         print("Calling Open Source Model",context,question)
         response=ollama.chat(
              model="mistral",
              messages=[
                   {
                        "role": "system",
                        "content": f"You are strict assistant.ANswer ONLY using context below.If the answer is not in context say don't know:\n{context}"
                   },
                   {
                        "role": "user",
                        "content": question
                   }
              ]
         )
         return response.message.content
