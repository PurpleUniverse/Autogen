import autogen

from pathlib import Path
from autogen.agentchat.contrib.text_analyzer_agent import system_message
from autogen.coding import LocalCommandLineCodeExecutor
from mistral_agent.config import llm_config

# Setting up the code executor
workdir = Path("../coding")
workdir.mkdir(exist_ok=True)
code_executor = LocalCommandLineCodeExecutor(work_dir=workdir)

# Setting up the Mistral agent
assistant = autogen.AssistantAgent(
    name="Assistant",
    system_message=system_message,
    llm_config=llm_config
)

# Setting up the User agent
user_proxy = autogen.UserProxyAgent(
    name="User",
    is_termination_msg=lambda msg: "FINISH" in msg.get("content"),
    code_execution_config={"executor": code_executor},
    llm_config=llm_config,
    system_message="""You are a helpful AI assistant who writes code and the user executes it.
Solve tasks using your coding and language skills.
In the following cases, suggest python code (in a python coding block) for the user to execute.
Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.
IMPORTANT: Wait for the user to execute your code and then you can reply with the word "FINISH". DO NOT OUTPUT "FINISH" after your code block."""

)

# User agent task
task = """
Write a Python function that takes a list of numbers and returns the average of the numbers.
"""

# Initialize
user_proxy.initiate_chat(
    assistant,
    message=task,
)