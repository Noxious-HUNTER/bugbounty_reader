def classify_writeups(writeups):
    topics = {
        "xss": ["cross-site scripting", "xss", "javascript"],
        "ssrf": ["server-side request forgery", "ssrf"],
        "idor": ["insecure direct object reference", "idor"],
        "mfa": ["mfa bypass", "2fa", "authentication"],
        "sql": ["sql injection", "sqlmap"],
        # Add more topics here
    }

    for writeup in writeups:
        writeup["tags"] = []
        for tag, keywords in topics.items():
            if any(keyword.lower() in writeup["title"].lower() or keyword.lower() in writeup["description"].lower() for keyword in keywords):
                writeup["tags"].append(tag)

    return writeups
