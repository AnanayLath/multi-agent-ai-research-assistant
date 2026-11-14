
import arxiv


class ResearchAgent:

    def __init__(self, max_results=5):
        self.max_results = max_results
        self.client = arxiv.Client()

    def search_papers(self, topic):

        search = arxiv.Search(
            query=topic,
            max_results=self.max_results,
            sort_by=arxiv.SortCriterion.Relevance
        )

        papers = []

        for result in self.client.results(search):
            paper = {
                "title": result.title,
                "authors": [author.name for author in result.authors],
                "abstract": result.summary,
                "pdf_url": result.pdf_url,
                "published": str(result.published.date())
            }

            papers.append(paper)

        return papers


if __name__ == "__main__":

    agent = ResearchAgent(max_results=5)

    topic = input("Enter your research topic or paper title: ")

    results = agent.search_papers(topic)

    if results:
        print("\nResearch Papers Found:\n")

        for i, paper in enumerate(results, start=1):
            print(f"\nPaper {i}:")
            print("Title:", paper["title"])
            print("Authors:", ", ".join(paper["authors"]))
            print("Published:", paper["published"])
            print("Abstract:", paper["abstract"])
            print("PDF:", paper["pdf_url"])
            print("-" * 70)

    else:
        print("No research papers found.")
