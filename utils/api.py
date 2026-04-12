import requests
import pandas as pd

def get_repos(language="python", pages=2):
    repos = []

    for page in range(1, pages + 1):
        url = "https://api.github.com/search/repositories"

        params = {
            "q": f"language:{language}",
            "sort": "stars",
            "order": "desc",
            "page": page,
            "per_page": 30
        }

        response = requests.get(url, params=params)

        if response.status_code != 200:
            return pd.DataFrame()

        data = response.json()

        for item in data.get("items", []):
            repos.append({
                "name": item["name"],
                "stars": item["stargazers_count"],
                "language": item["language"],
                "url": item["html_url"],
                "description": item["description"]
            })

    return pd.DataFrame(repos)