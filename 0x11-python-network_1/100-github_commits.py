#!/usr/bin/python3
""" A Python script that lists the 10 most recent commits on a given GitHub repository """

if __name__ == "__main__":
    from requests import get, auth
    import sys
    repository = sys.argv[1]
    owner = sys.argv[2]
    url = f"https://api.github.com/repos/{owner}/{repository}/commits"
    response = get(url)
    try:
        js = response.json()
        for j in js[:10]:
            author, name = None, None
            # date = None
            sha = j.get('sha')
            commit = j.get('commit')
            if commit:
                author = commit.get('author')
                # message = commit.get('message')
            if author:
                name = author.get('name')
                # date = author.get('date')
            print("{}: {}".format(sha, name))
    except ValueError:
        print("Not a valid JSON")
