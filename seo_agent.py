from textstat import textstat
import re

class SEOAgent:
    def optimize_content(self, content, keywords):
        optimized = content
        
        for kw in keywords[:3]:
            optimized = re.sub(
                fr'\b({kw})\b', 
                r'<b>\1</b>', 
                optimized, 
                flags=re.IGNORECASE, 
                count=2
            )
        
        if textstat.flesch_reading_ease(optimized) < 60:
            optimized = self._simplify_language(optimized)
        
        return optimized
    
    def generate_meta(self, content, keywords):
        return f"""
        <meta name="description" content="{content[:155]}...">
        <meta name="keywords" content="{', '.join(keywords)}">
        """

    def _simplify_language(self, text):
        # Simplification logic can be added here if needed.
        return text  

