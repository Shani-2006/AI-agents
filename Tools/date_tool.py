from openai import OpenAI
from pydantic import BaseModel,Field
from datetime import date
import json

class JsonReAct(BaseModel):
    Thought: str =Field(description="why you chose the action")
    Action: str =Field(description="'Function' if you need to act the function or 'Finatl Answer'")
    Output: str=Field(description="empty for Function, or the final answer text for Final Answer")

def get_current_date():
    return date.today().strftime("%y-%m-%d")

def add_numbers(a,b):
    return str(a+b)


client = OpenAI()

tools = [
 {
    "type": "function",
    "function": {
        "name": "get_current_date",
        "description": "Returns the current date in YY-MM-DD format",
        "strict": True, 
        "parameters": {
            "type": "object",
            "properties": {},
            "additionalProperties": False,
            "required": [] 
        }
    }
},
{
    "type": "function",
    "function": {
        "name": "add_numbers",
        "description": "Adds two integers and returns the result",
        "strict": True, 
        "parameters": {
            "type": "object",
            "properties": {
                    "a": {
                        "type": "integer",
                        "description": "The first number to add"
                    },
                    "b": {
                        "type": "integer",
                        "description": "The second number to add"
                    }
                },
            "additionalProperties": False, 
            "required": ["a","b"] 
        }
    }
}

]

system ="If you need today's date/day to answer, set Action='get_current_date' " \
"If you can answer without it, set Acion='FinalAnswer' and put the full answer in Output."
messages=[{"role":"system","content": system}]
#messages=[]
def chat_with_tool(messages):
    
    response = client.chat.completions.parse(
        model="gpt-4.1-mini",
        messages=messages,
        tools=tools,
        response_format= JsonReAct
)
    assistant_message = response.choices[0].message
    stepObj=response.choices[0].message.parsed

    if(assistant_message.tool_calls):
        messages.append(assistant_message)
        for tool_call in assistant_message.tool_calls:
            function_name = tool_call.function.name
            #function_to_call = function_name
            function_to_call = globals().get(function_name)
            function_args = json.loads(tool_call.function.arguments)
            result = function_to_call(**function_args)
            print(stepObj.Thought)
            messages.append({"tool_call_id": tool_call.id, "role":"tool","name":function_name,"content":result})
        return chat_with_tool(messages)
    return stepObj.Output

# הפעלה
messages.append({"role": "user","content":"and Joseph has 4 apples and 5 oranges, how many fruits does Joseph have?"})
result = chat_with_tool(messages)
print(result)