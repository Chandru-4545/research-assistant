from google import genai
import chromadb

# Paste your Gemini API key here
client = genai.Client(api_key="AIzaSyD6Gp6_ITw97J9tZjC42NFP5bO2URJDtTY")

def ask_question(question):
    if not question.strip():
        return "⚠️ Please enter a question."

    try:
        db = chromadb.PersistentClient(path="./chroma_db")
        collection = db.get_collection("research_docs")
        results = collection.query(query_texts=[question], n_results=3)
        context = "\n\n".join(results["documents"][0])

        prompt = f"""You are a helpful assistant. Answer the question using ONLY the context below.
If the answer is not found in the context, say "I couldn't find that in the document."

Context:
{context}

Question: {question}

Answer:"""

        response = client.models.generate_content(
          model="gemini-2.5-flash",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"❌ Error: {str(e)}"