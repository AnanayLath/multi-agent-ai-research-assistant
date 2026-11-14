
from agents.research_agent import ResearchAgent
from agents.summary_agent import SummaryAgent
from agents.comparison_agent import ComparisonAgent


def main():

    print("\n===== AI RESEARCH ASSISTANT =====")

    topic = input("\nEnter research topic: ")

    research_agent = ResearchAgent(max_results=5)

    print("\nSearching research papers...")
    papers = research_agent.search_papers(topic)

    if not papers:
        print("No research papers found.")
        return

    print("\nResearch Papers Found:\n")

    for i, paper in enumerate(papers, start=1):
        print(f"{i}. {paper['title']}")

    print("\nChoose an operation:")
    print("1. Summarize a single research paper")
    print("2. Compare five research papers")

    choice = input("\nEnter your choice (1 or 2): ")

    summary_agent = SummaryAgent()

    if choice == "1":

        paper_choice = int(input("\nSelect paper number: "))

        if paper_choice < 1 or paper_choice > len(papers):
            print("Invalid paper selection.")
            return

        selected_paper = papers[paper_choice - 1]

        print("\nGenerating paper summary...")

        summary = summary_agent.generate_summary(selected_paper)

        print("\n===== RESEARCH PAPER SUMMARY =====")
        print("Title:", selected_paper["title"])
        print(summary)

    elif choice == "2":

        if len(papers) < 5:
            print("Five papers are required for comparison.")
            return

        print("\nGenerating summaries of five papers...")

        summaries = summary_agent.generate_summaries(papers)

        comparison_agent = ComparisonAgent()

        print("\nComparing research papers...")

        report = comparison_agent.compare_papers(summaries)

        print("\n===== FIVE PAPER COMPARISON =====")
        print(report)

    else:
        print("Invalid choice. Please select 1 or 2.")


if __name__ == "__main__":
    main()
