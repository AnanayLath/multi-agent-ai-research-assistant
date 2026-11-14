
from agents.research_agent import ResearchAgent
from agents.summary_agent import SummaryAgent
from agents.comparison_agent import ComparisonAgent

# Step 1: Search five research papers
research_agent = ResearchAgent(max_results=5)

topic = input("Enter research topic: ")
papers = research_agent.search_papers(topic)

if len(papers) < 5:
    print("We need five papers for comparison.")
    exit()

# Step 2: Generate summaries
summary_agent = SummaryAgent()

summaries = summary_agent.generate_summaries(papers)

# Step 3: Compare all five papers
comparison_agent = ComparisonAgent()

print("\nComparing five research papers...")

report = comparison_agent.compare_papers(summaries)

# Step 4: Display final report
print("\n========== FIVE PAPER COMPARISON ==========\n")
print(report)
