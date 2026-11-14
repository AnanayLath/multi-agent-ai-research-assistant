
import ollama


class SummaryAgent:

    def __init__(self, model="qwen2.5:3b"):
        self.model = model

    def generate_summary(self, paper):

        prompt = f"""
        You are an AI research paper summarization assistant.

        Summarize the following research paper.

        Include:
        1. Research Objective
        2. Problem Addressed
        3. Methodology
        4. Key Findings
        5. Conclusion

        Paper Title:
        {paper['title']}

        Abstract:
        {paper['abstract']}

        Explain in simple language.
        Do not invent information.
        If something is not mentioned, say it is not available
        in the abstract.
        """

        response = ollama.chat(
            model=self.model,
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        return response["message"]["content"].strip()

    def generate_summaries(self, papers):

        summaries = []

        for i, paper in enumerate(papers, start=1):

            print(f"\nGenerating summary for Paper {i}...")

            summary = self.generate_summary(paper)

            summaries.append({
                "title": paper["title"],
                "summary": summary
            })

        return summaries
