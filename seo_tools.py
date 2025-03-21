import re

def calculate_keyword_density(text, keywords):
    word_count = len(text.split())
    keyword_count = sum(text.lower().count(kw.lower()) for kw in keywords)
    return round((keyword_count / word_count) * 100, 2)

def generate_url_slug(title):
    return re.sub(r'[^a-z0-9]+', '-', title.lower()).strip('-')
