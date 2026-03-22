import requests
from bs4 import BeautifulSoup
import datetime

def get_github_trends():
    """Path 1: The Trend Hunter"""
        url = "https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc"
            res = requests.get(url).json()
                repo = res['items'][0]
                    return f"🔥 TREND: {repo['full_name']} | {repo['html_url']}\n"

                    def get_arxiv_research():
                        """Path 2: The Research Sentinel"""
                            url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=1&sortBy=submittedDate&sortOrder=descending"
                                res = requests.get(url)
                                    soup = BeautifulSoup(res.content, "xml") # Using the xml parser
                                        title = soup.find("title").text if soup.find("title") else "No title found"
                                            link = soup.find("id").text if soup.find("id") else ""
                                                return f"🧠 RESEARCH: {title.strip()} | {link}\n"

                                                def get_directory_leads():
                                                    """Path 3: The Lead Generator (Example: Y-Combinator Companies)"""
                                                        # This is a placeholder for a specific directory; scraping logic varies by site
                                                            return "💼 LEAD: Check YC 'Newly Launched' for today's batch.\n"

                                                            # Execute and save to pulse.txt
                                                            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
                                                            content = f"--- Pulse {now} ---\n"
                                                            content += get_github_trends()
                                                            content += get_arxiv_research()
                                                            content += get_directory_leads() + "\n"

                                                            with open("pulse.txt", "a") as f:
                                                                f.write(content)

                                                                print("Intelligence Engine executed successfully.")
                                                                