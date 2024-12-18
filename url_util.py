from urllib.parse import urlparse, urlunparse, parse_qs, urlencode
import re

URL_GET = "https://docs.google.com/forms/d/1PS5LMEs-C0T2EkJmoEHbv-zhNhGwZO4RenWu7CXJGoA/viewform"


def url_update(url, token):
    parsed_url = urlparse(url)
    path = parsed_url.path.replace("viewform", "formResponse")
    query = parse_qs(parsed_url.query)
    query['edit2'] = token
    query_string = urlencode(query, doseq=True)
    modified_url = urlunparse(parsed_url._replace(path=path, query=query_string))
    return modified_url


def extract_token(html):
    pattern = r'href="[^"]*?edit2=([^"&]+)'
    match = re.search(pattern, html)
    if match:
        return match.group(1)
    return None
