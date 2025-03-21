from openai import OpenAI

class ContentPlanner:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    
    def create_outline(self, trends, keywords):
        prompt = f"""
        Create a blog outline about HR trends in 2025. 
        Main topics: {', '.join(trends)}
        Target keywords: {', '.join(keywords[:3])}
        Structure:
        1. Introduction (150 words)
        2. 5 Main Sections with 3 subsections each
        3. Conclusion (200 words)
        Format: Markdown with ## and ### headings
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
