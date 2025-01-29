from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate

from .prompts import diarization_prompt, notes_prompts, notes_formatting


class Chain:
    def __init__(self):
        self.llm_diarization = ChatOpenAI(model="gpt-4o", temperature="0")
        self.llm_notes = ChatOpenAI(model="gpt-4o", temperature="0.7")

    def diarization(self, transcript):
        prompt = ChatPromptTemplate.from_messages(
            [
                (SystemMessagePromptTemplate.from_template(diarization_prompt)),
                ("human", "{input}"),
            ]
        )

        chain = {"input": RunnablePassthrough()} | prompt | self.llm_diarization

        response = chain.invoke(transcript)

        return response.content
    
    def notes(self, transcript):
        prompt = ChatPromptTemplate.from_messages(
            [
                (SystemMessagePromptTemplate.from_template(notes_prompts)),
                ("human", "{input}"),
                (SystemMessagePromptTemplate.from_template(notes_formatting)),
            ]
        )

        chain = {"input": RunnablePassthrough()} | prompt | self.llm_notes

        response = chain.invoke(transcript)

        return response.content