import language_tool_python
from textstat import textstat

class ReviewAgent:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')
    
    def proofread(self, content):
        matches = self.tool.check(content)
        
        for match in matches:
            content = content[:match.offset] + match.replacements[0] + content[match.offset+match.errorLength:]
        
        return content
    
    def validate_seo(self, content):
        return {
            'readability': textstat.flesch_reading_ease(content),
            'keyword_density': self.calculate_keyword_density(content),
            'passive_voice': len(re.findall(r'\b(am|is|are|was|were|be|being|been)\b', content))
        }

    def calculate_keyword_density(self, text):
       words = text.split()
       total_words = len(words)
       keyword_count = len(re.findall(r'\b(?:keyword1|keyword2|keyword3)\b', text)) # Replace with actual keywords.
       return (keyword_count / total_words) * 100 if total_words > 0 else 0
