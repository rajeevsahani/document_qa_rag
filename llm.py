#Implement Ollama-based LLM Wrapper (llm.py)
import ollama

class LLMModel:
    def __init__(self, model_name="llama2:7b"):
        self.model_name = model_name

    def generate_answer(self, query: str, context: str):
        response = ollama.chat(
            model=self.model_name,
            messages=[
                {"role": "system", "content": "You are an AI assistant answering document-based questions."},
                {"role": "user", "content": f"Context: {context}\n\nQuestion: {query}"}
            ]
        )
        return response["message"]["content"]
# Run the model manually
if __name__ == "__main__":
    # Instantiate the LLM model
    llm = LLMModel()

    # Example inputs
    example_query = "What is the purpose of embeddings in NLP?"
    example_context = """
    Embeddings in NLP are vector representations of words or phrases. 
    They capture semantic meanings and are used in machine learning models for better text understanding.
    """

    # Generate and print the response
    answer = llm.generate_answer(example_query, example_context)
    print("\n📝 Generated Answer:\n", answer)


