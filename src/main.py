import os
import sys
import json
from importlib.resources import files

from groq import Groq
from dotenv import load_dotenv
from functions.run_functions import run_tool_calls
from prompts import controllerPrompt,toolCallerSystemPrompt
from models import currentModel


def main():
    if len(sys.argv) < 2:
        print("Please enter a prompt")
        sys.exit(1)

    UserPrompt = str(sys.argv[1])

    load_dotenv("../Ai-agent/.env")
    load_dotenv()
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    with files("functions").joinpath("functionsSchema.json").open(encoding="utf-8") as f:
        toolSchema = json.load(f)

    """ # MessageContextArr should store the context of the conversation.
    messageContextArr = []
    messageContextArr.append(
        {
        "role" : "user",
        "content" : UserPrompt
        }
    ) """

    # Step 1: Controller breaks down the user request into steps
    controllerChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": controllerPrompt
            },
            {
                "role": "user",
                "content": UserPrompt
            }
        ],
        model=currentModel,
    )
    controllerMessage = controllerChatCompletion.choices[0].message
    controllerSteps = controllerMessage.content

    print("Controller Steps:")
    print(controllerSteps)
    print("\n" + "="*50 + "\n")

    # Step 2: Tool caller takes the steps and makes tool calls
    toolCallerChatCompletion = client.chat.completions.create(
        messages=[
            {
                "role": "system",
                "content": toolCallerSystemPrompt
            },
            {
                "role": "user",
                "content": f"Execute the following steps:\n{controllerSteps}"
            }
        ],
        tools=toolSchema,
        tool_choice="auto",
        model=currentModel,
    )

    tool_calls = toolCallerChatCompletion.choices[0].message.tool_calls

    if tool_calls:
        results = run_tool_calls(tool_calls)
        print("Tool Call Results:")
        
        
        for t in tool_calls : 
            print(t)
            print("\n") 

if __name__ == "__main__":
    main()