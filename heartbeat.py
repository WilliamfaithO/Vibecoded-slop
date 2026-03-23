import requests
import feedparser
import datetime
import os
import random

def get_github_trends():
    """Path 1: The Trend Hunter (Secured & Randomized)"""
    token = os.getenv("GH_TOKEN")
    headers = {
        "Authorization": f"token {token}" if token else "",
        "User-Agent": "Vibecoded-Slop-Engine/1.0"
    }
    try:
        page = random.randint(1, 3)
        url = f"https://api.github.com/search/repositories?q=language:python&sort=stars&order=desc&page={page}"
        res = requests.get(url, headers=headers).json()
        repo = res['items'][0]
        return f"| 🔥 **Trend** | **{repo['full_name']}**: {repo['description'][:100]}... | [View Repo]({repo['html_url']}) |\n"
    except Exception as e:
        return f"| 🔥 **Trend** | API Error / Rate Limit | N/A |\n"

def get_arxiv_research():
    """Path 2: The Research Sentinel (Deep Abstract via Feedparser)"""
    try:
        url = "http://export.arxiv.org/api/query?search_query=cat:cs.AI&max_results=1&sortBy=submittedDate&sortOrder=descending"
        feed = feedparser.parse(url)
        if feed.entries:
            entry = feed.entries[0]
            title = entry.title.replace('\n', ' ')
            # Pulls a solid paragraph for actual reading
            summary = entry.summary.replace('\n', ' ')[:450]
            link = entry.link
            return f"| 🧠 **Research** | **{title}**: {summary}... | [Read Paper]({link}) |\n"
    except:
        return "| 🧠 **Research** | Sentinel Node Offline | N/A |\n"

def get_directory_leads():
    """Path 3: The Lead Generator (Live YC API)"""
    try:
        url = "https://yc-oss.github.io/api/companies/all.json"
        res = requests.get(url).json()
        latest = res[-1] 
        name = latest.get('name', 'Stealth Startup')
        desc = latest.get('description', 'No description provided.')
        site = latest.get('website', '#')
        return f"| 💼 **Lead** | **{name}**: {desc} | [Visit Site]({site}) |\n"
    except:
        return "| 💼 **Lead** | YC Feed Timeout | N/A |\n"

if __name__ == "__main__":
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # 1. Build THIS Run's Pulse Content
    header = f"\n### ⚡ Pulse Log: {now} UTC\n"
    table_head = "| Category | Insight & Intelligence | Action |\n| :--- | :--- | :--- |\n"
    current_pulse = header + table_head + get_github_trends() + get_arxiv_research() + get_directory_leads() + "\n"
    
    # 2. Append to the permanent historical log (pulse.txt)
    with open("pulse.txt", "a", encoding="utf-8") as f:
        f.write(current_pulse)
    
    # 3. Read the log, grab the last 7, and flip them (Newest first)
    try:
        with open("pulse.txt", "r", encoding="utf-8") as f:
            all_logs = f.read()
        
        # Split the text file by the header to separate each run into a list item
        blocks = [b for b in all_logs.split("### ⚡ Pulse Log:") if b.strip()]
        
        # Take the last 7 blocks, and reverse the list so the newest is at the top
        last_7 = blocks[-7:]
        last_7.reverse()
        
        # Rebuild the string for the README
        readme_table_content = "\n".join([f"### ⚡ Pulse Log:{block}" for block in last_7])
        
        # 4. Inject into README.md
        with open("README.md", "r", encoding="utf-8") as f:
            readme = f.read()
            
        start_marker = ""
        end_marker = ""
        
        if start_marker in readme and end_marker in readme:
            # Sandwich the rolling dashboard between the markers
            before = readme.split(start_marker)[0]
            after = readme.split(end_marker)[1]
            new_readme = f"{before}{start_marker}\n\n{readme_table_content.strip()}\n\n{end_marker}{after}"
            
            with open("README.md", "w", encoding="utf-8") as f:
                f.write(new_readme)
            print("README storefront successfully updated with the latest 7 pulses.")
        else:
            print("Could not find PULSE_START or PULSE_END markers in README.md")
            
    except Exception as e:
        print(f"README injection failed: {e}")

    print(f"High-octane pulse recorded at {now}")
