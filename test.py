from bs4 import BeautifulSoup
import urllib.request as req
import re
import fpdf
from fpdf import FPDF, HTMLMixin
import BlogParser

class MyFPDF(FPDF, HTMLMixin):
    pass

pdf = MyFPDF(format = 'letter')
#pdf = fpdf.FPDF(format='letter')
pdf.add_page()
pdf.set_font("Times", size=12)

def rmQuotes(txt):
  return txt.replace('\u201d', '"').replace('\u201c', '"').replace('\u2018', "'").replace('\u2019', "'").replace('\u2013', '-').replace('\u2014', '-').replace('\u2026', '...').replace('\u2122', '(TM)').replace('\U0001f642', ':)')

main_site = r"https://zippycatholic.wordpress.com/"
for page in range(1,200):
  print(page)
#site = r"https://zippycatholic.wordpress.com/2018/08/10/a-future-conservative-catholic-blog-post/"
  site = main_site + r"page/" + str(page)
  f = req.urlopen(site)
  soup = BeautifulSoup(f.read())
  entries = soup.find_all('h2', attrs = {"class":"entry-title"})
  for e in entries:
    post_site = e.find('a').get('href')
    
    post = BlogParser.BlogPostParser(post_site) 
  #print(post.post_title)
    print(post.post_title)
    pdf.multi_cell(200, 5, rmQuotes(post.post_title) +"\n"+rmQuotes(post.post_date), 0,1,'C')
    #pdf.multi_cell(200, 10, rmQuotes(post.post_date), 0,1,'C')
    #pdf.multi_cell(200, 10, rmQuotes(post.post_entry), 0,1,'C')
    #pdf.write_html(r"<font face = Arial size = 12><i>" + rmQuotes(post.post_entry) +"</i></font>")

pdf.output('blog.pdf')
