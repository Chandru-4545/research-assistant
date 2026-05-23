from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
import chromadb

def ingest_pdf(pdf_path):
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()

    # Split into chunks
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)

    # Store in ChromaDB (local vector database)
    client = chromadb.PersistentClient(path="./chroma_db")

    # Clear old data if re-uploading
    try:
        client.delete_collection("research_docs")
    except:
        pass

    collection = client.get_or_create_collection("research_docs")

    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk.page_content],
            ids=[f"chunk_{i}"]
        )

    return f"✅ Ingested {len(chunks)} chunks from {len(pages)} pages."