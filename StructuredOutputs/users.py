from openai import OpenAI
import httpx 

client = OpenAI(
    api_key="(client key)",
    http_client=httpx.Client(verify=False)
)

schema = {
 "type": "object",
 "properties": {
     "name": {"type": "string"},
     "age": {"type": "integer"}
    },
    "required": ["name", "age"]
}


def get_user(user_prompt):
    response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[{"role": "user", "content":user_prompt }],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "user_schema",
            "schema": schema
    }
     }
    )   
    return(response.choices[0].message.content)
n=input("enter sen ")
print(get_user(n))

    