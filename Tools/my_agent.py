from smolagents import CodeAgent, DuckDuckGoSearchTool,OpenAIModel,ToolCallingAgent,FinalAnswerTool,tool
from datetime import date

@tool
def get_current_date() -> date:
    """A tool that return current date"""
    return date.today()

# 1. הגדרת המודל (LLM) - כאן אנחנו משתמשים במודל של Hugging Face
model = OpenAIModel(model_id="gpt-4.1-mini")

# 2. בחירת הכלים שהסוכן יוכל להשתמש בהם
# במקרה הזה, כלי לחיפוש מידע באינטרנט
search_tool = DuckDuckGoSearchTool()
final_answer=FinalAnswerTool()
# 3. יצירת הסוכן
# אנחנו נותנים לו רשימת כלים ואת המודל שבחרנו
agent = CodeAgent(tools=[search_tool,final_answer,get_current_date], model=model)#,max_steps=5)

# 4. הפעלה: נבקש מהסוכן לבצע משימה שדורשת מחקר וחישוב
a= agent.run("Who is the current CEO of Nvidia, and what is the result of his age multiplied by 2?")
print(a)