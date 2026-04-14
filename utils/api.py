import requests
import streamlit as st
@st.cache_data(ttl=600)
def get_repos(language="python", pages=2):
    repos = []
    token = st.secrets.get("GITHUB_TOKEN", None)
    headers = {
        "Accept": "application/vnd.github+json"
    }
    
    if token:
        headers["Authorization"] = f"Bearer {token}"
    for page in range(1, pages + 1):
        url = "https://api.github.com/search/repositories"
        params = {
            "q": f"language:{language}",
            "sort": "stars",
            "order": "desc",
            "page": page,
            "per_page": 30
        }
        response = requests.get(url, params=params, headers=headers)
        if response.status_code != 200:
            return {
                "error": True,
                "status_code": response.status_code,
                "message": response.json()
            }
        data = response.json()
        for item in data.get("items", []):
            repos.append({
                "name": item.get("name"),
                "stars": item.get("stargazers_count", 0),
                "forks": item.get("forks_count", 0),
                "language": item.get("language"),
                "url": item.get("html_url"),
                "description": item.get("description")
            })
    return repos