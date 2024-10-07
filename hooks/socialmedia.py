from textwrap import dedent
import urllib.parse
import re

x_intent = "https://x.com/intent/tweet"
fb_sharer = "https://www.facebook.com/sharer/sharer.php"
li_sharer = "https://www.linkedin.com/sharing/share-offsite/"
include = re.compile(r"blog/[1-9].*")

def on_page_markdown(markdown, **kwargs):
    page = kwargs['page']
    config = kwargs['config']
    if not include.match(page.url):
        return markdown

    page_url = config.site_url+page.url
    page_title = urllib.parse.quote(page.title+'\n')

    return markdown + dedent(f"""
    <div class="centered" markdown>
    [:simple-x:]({x_intent}?text={page_title}&url={page_url}){{ .share-social }}
    [:simple-facebook:]({fb_sharer}?u={page_url}){{ .share-social }}
    [:simple-linkedin:]({li_sharer}?url={page_url}){{ .share-social }}
    </div>

    --8<-- "includes/gen/brandmark.md"
    """)