from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain import hub
from langchain.agents import create_react_agent, AgentExecutor
from tools.system_time_tool import check_system_time
from tools.system_performance_tool import check_system_performance


load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo")

query = "give me current cpu usage percent?"

prompt_template = hub.pull("hwchase17/react")

tools = [check_system_performance]
agent = create_react_agent(
    llm,
    tools,
    prompt_template
)

agent_executor = AgentExecutor(agent=agent,tools=tools,verbose=True)

agent_executor.invoke({"input": query})



