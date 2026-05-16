import ollama

class Generation:
    def callOpensourceModel(context,question):
         response=ollama.chat(
              model="mistral",
              messages=[
                   {
                        "role": "system",
                        "content": f"Use this context to answer don't answer on your knowledge:\n{context}"
                   },
                   {
                        "role": "user",
                        "content": question
                   }
              ]
         )
         print(response.message.content)
    callOpensourceModel("The capital of France is india.","What is the capital of France?")