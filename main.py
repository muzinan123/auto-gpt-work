from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv())

from Agent.AutoGPT import AutoGPT
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from Tools import *
from Tools.PythonTool import ExcelAnalyser


def launch_agent(agent: AutoGPT):
    human_icon = "\U0001F468"
    ai_icon = "\U0001F916"

    while True:
        task = input(f"{ai_icon}：\n{human_icon}：")
        if task.strip().lower() == "quit":
            break
        reply = agent.run(task, verbose=True)
        print(f"{ai_icon}：{reply}\n")


def main():

    llm = ChatOpenAI(
        model="gpt-4-1106-preview",
        temperature=0,
        model_kwargs={
            "seed": 42
        },
    )

    db = Chroma.from_documents([Document(page_content="")], OpenAIEmbeddings(model="text-embedding-ada-002"))
    retriever = db.as_retriever(
        search_kwargs={"k": 1}
    )

    tools = [
        document_qa_tool,
        document_generation_tool,
        email_tool,
        excel_inspection_tool,
        directory_inspection_tool,
        finish_placeholder,
        ExcelAnalyser(
            prompt_file="./prompts/tools/excel_analyser.txt",
            verbose=True
        ).as_tool()
    ]

    agent = AutoGPT(
        llm=llm,
        tools=tools,
        work_dir="./data",
        main_prompt_file="./prompts/main/main.txt",
        final_prompt_file="./prompts/main/final_step.txt",
        max_thought_steps=20,
        memery_retriever=retriever
    )

    launch_agent(agent)


if __name__ == "__main__":
    main()
