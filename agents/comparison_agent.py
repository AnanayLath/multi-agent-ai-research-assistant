
import ollama


class ComparisonAgent:

    def __init__(self, model="qwen2.5:3b"):
        self.model = model

    def compare_papers(self, summaries):

        paper_details = ""

        for i, paper in enumerate(summaries, start=1):
            paper_details += f"""
            Paper {i}
            Title: {paper['title']}
            Summary: {paper['summary']}
            """

        prompt = f"""
        You are an AI Research Paper Comparison Agent.

        Compare the following five research papers.

        Analyze these points:

        1. Research objectives
        2. Problems addressed
        3. Methodologies
        4. Key findings
        5. Similarities
        6. Differences
        7. Strengths and limitations
        8. Overall conclusion

        Research Papers:
        {paper_details}

        Use simple and understandable language.
        Do not invent facts.
        If information is missing, mention it.
        """

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"].strip()
