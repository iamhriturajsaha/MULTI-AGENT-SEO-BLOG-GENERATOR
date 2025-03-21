from openai import OpenAI
import re

class ContentGenerator:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def expand_section(self, outline):
        prompt = f"""
        Write a detailed 300-word section for this blog outline.
        Maintain SEO-friendly structure with <h2> and <h3> tags.
        Use active voice and include statistics.
        Outline Section: {outline}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.5
        )
        return self._clean_html(response.choices[0].message.content.strip())
    
    def _clean_html(self, text):
        return re.sub(r'<(/?(h2|h3|b))>', lambda m: f'<{m.group(1)}>' if '/' in m.group(0) else f'<{m.group(1)}>', text)
