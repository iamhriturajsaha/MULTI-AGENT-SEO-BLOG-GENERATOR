from agents.research_agent import ResearchAgent
from agents.planning_agent import ContentPlanner
from agents.generation_agent import ContentGenerator
from agents.seo_agent import SEOAgent
from agents.review_agent import ReviewAgent

import markdown
import pdfkit

class BlogGenerator:
    def __init__(self):
        self.researcher = ResearchAgent()
        self.planner = ContentPlanner()
        self.writer = ContentGenerator()
        self.seo = SEOAgent()
        self.reviewer = ReviewAgent()
    
    def generate_blog(self):
        # Research Phase
        trends = self.researcher.get_trends()
        
        keywords = sorted(trends, key=lambda x: self.researcher.get_keyword_volume(x), reverse=True)[:5]
        
        # Planning Phase
        outline = self.planner.create_outline(trends, keywords)
        
        # Content Generation Phase
        sections = [self.writer.expand_section(section) for section in outline.split('##')[1:]]
        
        draft = "\n".join(sections)
        
         # SEO Optimization Phase 
         optimized_content= self.seo.optimize_content(draft, keywords)
         meta_tags= self.seo.generate_meta(optimized_content, keywords)
         
         # Review Phase 
         final_content= self.reviewer.proofread(optimized_content)
         seo_report= self.reviewer.validate_seo(final_content)

         # Formatting Phase 
         html_output= f"""
         <!DOCTYPE html>
         <html>
         <head>{meta_tags}</head>
         <body>{markdown.markdown(final_content)}</body>
         </html>
         """
         
         return {
             "markdown": final_content,
             "html": html_output,
             "seo_report": seo_report,
             "trends": trends,
             "keywords": keywords,
             "outline": outline,
         }

if __name__ == "__main__":
     generator= BlogGenerator()
     blog= generator.generate_blog()
     
     with open("outputs/blogs/hr_trends_2025.md", "w") as f:
          f.write(blog['markdown'])
     
     pdfkit.from_string(blog['html'], "outputs/blogs/hr_trends_2025.pdf")
     print("Blog generated successfully!")

