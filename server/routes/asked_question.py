import os
from typing import List

from fastapi import APIRouter, Form
from fastapi.responses import JSONResponse

from logger import logger
from modules.llm import get_llm_chain
from modules.query_handle import query_chain

from pinecone import Pinecone
from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
from langchain_google_genai import GoogleGenerativeAIEmbeddings


router = APIRouter()


class SimpleRetriever(BaseRetriever):
    docs: List[Document]

    def _get_relevant_documents(self, query: str) -> List[Document]:
        return self.docs

    async def _aget_relevant_documents(self, query: str) -> List[Document]:
        return self.docs


@router.post("/ask/")
async def ask_question(question: str = Form(...)):
    try:
        logger.info(f"User query: {question}")

        # Pinecone
        pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
        index = pc.Index(os.environ["PINECONE_INDEX_NAME"])

        # Gemini Embedding
        embed_model = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            output_dimensionality=768,
        )

        embedded_query = embed_model.embed_query(question)

        # Search Pinecone
        response = index.query(
            vector=embedded_query,
            top_k=3,
            include_metadata=True,
        )

        docs = []

        for match in response["matches"]:
            docs.append(
                Document(
                    page_content=match["metadata"].get("text", ""),
                    metadata=match["metadata"],
                )
            )

        if len(docs) == 0:
            return {"answer": "No relevant information found."}

        retriever = SimpleRetriever(docs=docs)

        chain = get_llm_chain(retriever)

        result = query_chain(chain, question)

        logger.info("Query successful")

        return result

    except Exception as e:
        logger.exception(e)
        return JSONResponse(
            status_code=500,
            content={"error": str(e)},
        )