from dotenv import load_dotenv
from pydantic import BaseModel
#from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import search_tool, wiki_tool, save_tool

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary:set
    sources: list[str]
    tools_used: list[str]

#llm = ChatOllama (model="gemma3:latest")
llm = ChatOpenAI (model = "gpt-3.5-turbo")
#response = llm.invoke("should i eat butter naan or roomali roti?")
#print(response.content)
parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
[
    (
        "system",
        """
        You are a research assitant that will help generate a reasearch paper.
        Answer the user query and use necessary tools. 
        Wrap the output in this format and provide no other text \n{format_instructions}
        """,
    ),
    ("placeholder","{chat_history}"),
    ("human", "{query}"),
    ("placeholder","{agent_scratchpad}"),
]
).partial(format_instructions=parser.get_format_instructions())

tools =[search_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools=tools
)

agent_executor=AgentExecutor(agent=agent, tools=tools, verbose=True)
query = input ("What can I help you research? ")
raw_response = agent_executor.invoke({"query": query})
print(raw_response)

try:
    structured_response = parser.parse(raw_response.get("output"))
    print(structured_response)
except Exception as e:
    print("Error parsing response",e,"Raw response - ", raw_response)