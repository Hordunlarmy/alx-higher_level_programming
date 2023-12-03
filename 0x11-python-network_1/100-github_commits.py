#!/usr/bin/python3
"""
evaluates candidates applying for a back-end position, filtering by commits
"""
import requests
import sys

if __name__ == "__main__":
    r = requests.get(
        f"https://api.github.com/repos/{sys.argv[1]}/{sys.argv[2]}/commits")

    for i in range(1, 11):
        sha = r.json()[i].get("sha")
        commit = r.json()[i].get("commit").get("author").get("name")
        print(f"{sha}: {commit}")
