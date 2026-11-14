
from agents.research_agent import ResearchAgent
from agents.summary_agent import SummaryAgent

# Search for research papers
research_agent = ResearchAgent(max_results=5)

topic = input("Enter research topic: ")
papers = research_agent.search_papers(topic)

if not papers:
    print("No papers found.")
    exit()

# Display available papers
print("\nAvailable Research Papers:\n")

for i, paper in enumerate(papers, start=1):
    print(f"{i}. {paper['title']}")

# Select one paper
choice = int(input("\nSelect a paper (1-5): "))

if choice < 1 or choice > len(papers):
    print("Invalid selection.")
    exit()

selected_paper = papers[choice - 1]

# Generate summary
summary_agent = SummaryAgent()

print("\nGenerating summary...")
summary = summary_agent.generate_summary(selected_paper)

print("\n========== RESEARCH PAPER SUMMARY ==========")
print("Title:", selected_paper["title"])
print(summary)
