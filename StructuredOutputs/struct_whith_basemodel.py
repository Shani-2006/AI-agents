from openai import OpenAI
from pydantic import BaseModel

class user_schema(BaseModel):
    name: str
    age: int



def get_user(user_prompt):
    client = OpenAI()
    response = client.chat.completions.parse(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content":user_prompt }],
    response_format=user_schema
    )   
    return(response.choices[0].message.parsed)

print(get_user( "Hi, How are you today?"))

    