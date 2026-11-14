
import ollama


class CoordinatorAgent:
    def __init__(self, model="qwen2.5:3b"):
        self.model = model

    def plan_workflow(self, query):
        prompt = f"""
        You are the Coordinator Agent of an AI Research Assistant.

        Analyze the user's request and decide which agents are required.

        Available agents:
        - research: Find relevant research papers.
        - reading: Read and summarize papers.
        - comparison: Compare papers and their methods.
        - citation: Manage paper references and citations.
        - report: Generate a literature review or report.

        Return only the required agent names as a comma-separated list.
        Do not add explanations.

        User request: {query}
        """

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"].strip()


if __name__ == "__main__":
    coordinator = CoordinatorAgent()

    query = "Find research papers on RAG and compare their methods."

    result = coordinator.plan_workflow(query)

    print("User Query:", query)
    print("Selected Agents:", result)
