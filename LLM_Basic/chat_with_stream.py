from openai import OpenAI

client = OpenAI()

def start_chat():
    history=[{"role": "system", "content": "You are a bad assistant."}]
    while(True):
        user_input = input(">>")
        if(user_input=="."):
            break
        history.append({"role": "user", "content": user_input})
        try:
            response = client.chat.completions.create(
            model="gpt-4.1-mini",  
            messages=history,
            stream=True
            )
            reply=""
            print("AI: ",end="")
            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    print(content,end="",flush=True)
                    reply+=content
            print()
            history.append({"role": "assistant", "content": reply})
        except Exception as e:
            print(f"ERROR: {e}")
             
  
start_chat()
