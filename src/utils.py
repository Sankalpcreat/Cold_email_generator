import requests
from bs4 import BeautifulSoup
from datetime import datetime
import html2text
import re

def clean_text(text) -> str:
    """Clean extracted text by removing extra whitespace and empty lines"""
    text = re.sub(r'\n\s*\n', '\n\n', text.strip())
    return text

def scrape_website(url, selector=None) -> str:
    
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, 'html.parser')
        
        
        for element in soup.select('script, style, nav, footer, header'):
            element.decompose()
        
        
        h = html2text.HTML2Text()
        h.ignore_links = False
        h.ignore_images = False
        h.body_width = 0  
        
        if selector:
            elements = soup.select(selector)
            content = '\n\n'.join(h.handle(str(element)) for element in elements)
        else:
            content = h.handle(str(soup.body))
        
        
        content = clean_text(content)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        
        with open(f'scraped_content_{timestamp}.md', 'w', encoding='utf-8') as file:
            file.write(content)
            
        return content
        
    except Exception as e:
        print(f"Error: {e}")
        return ""
