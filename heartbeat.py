import requests
from bs4 import BeautifulSoup
import datetime

def get_github_trends():
    """Path 1: The Trend Hunter"""
    try:
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
        res = requests.get(url).json()
        repo = res['items'][0]
        return f"🔥 TREND: {repo['full_name']} | {repo['html_url']}\n"
    except Exception as e:
        return f"🔥 TREND: Error fetching trends ({e})\n"

def get_arxiv_research():
    """Path 2: The Research Sentinel"""
    try:
        url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=1&sortBy=submittedDate&sortOrder=descending"
        res = requests.get(url)
        soup = BeautifulSoup(res.content, "xml") 
        # ArXiv XML usually has the main title first, then entry titles. 
        # We skip the first one to get the actual paper.
        entries = soup.find_all("entry")
        if entries:
            title = entries[0].find("title").text
            link = entries[0].find("id").text
            return f"🧠 RESEARCH: {title.strip()} | {link}\n"
        return "🧠 RESEARCH: No new papers found.\n"
    except Exception as e:
        return f"🧠 RESEARCH: Error fetching ArXiv ({e})\n"

def get_directory_leads():
    """Path 3: The Lead Generator"""
    return "💼 LEAD: Check YC 'Newly Launched' for today's batch.\n"

# --- Main Execution ---
if __name__ == "__main__":
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    content = f"--- Pulse {now} ---\n"
    content += get_github_trends()
    content += get_arxiv_research()
    content += get_directory_leads() + "\n"

    with open("pulse.txt", "a") as f:
        f.write(content)

    print("Intelligence Engine executed successfully.")
