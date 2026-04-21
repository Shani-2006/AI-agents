from openai import OpenAI

client = OpenAI()

def start_chat():
    history=[{"role": "system", "content": "You are a bad assistance."}]
    while(True):
        user_input = input(">>")
        if(user_input=="."):
            break
        history.append({"role": "user", "content": user_input})
        try:
            response = client.chat.completions.create(
            model="gpt-4.1-mini",  
            messages=history,
            max_tokens=100
            temperature=2
            )
            ai_message = response.choices[0].message.content
            print(f"AI: {ai_message}")
            history.append({"role": "assistant", "content": ai_message})
        except Exception as e:
            print(f"ERROR: {e}")
             
start_chat()
