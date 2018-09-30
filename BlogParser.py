from bs4 import BeautifulSoup
import urllib.request as req
import re

class BlogPostParser():

  def __init__(self,site):
    self.url = site
    self.loadBlogPost(site)

  def loadBlogPost(self, site):
    f = req.urlopen(site)
    html = f.read()
    soup = BeautifulSoup(html, features="html.parser")
    self.post_title = soup.find('h2', attrs = {'class': 'entry-title'}).text
    print(self.post_title)
    date = soup.find('p', attrs = {'class': 'date'}).text
    self.post_date = date.split('§')[0]
    entry = soup.find('div', attrs = {'class': 'entry'})
    #pdf.multi_cell(200,10, str(title.replace('\u201d', '"').replace('\u201c', '"').replace('\u2018', "'").replace('\u2019', "'")), 0,1,'C')

    i = 0
    for child in entry.children:
      try:
        c = child.get('id')
        if c[0] == 'jp-post-flair':
          break
        else:
          i = i+1 
      except:
        i = i+1

    entry_list = list(entry.children)[0:i]
    s = ""
    for e in entry_list:
      s = s + str(e)

    self.post_entry = self.htmlCleanUp(s)

    #self.comments_title = entry.find('h3', {'id':'comments'}).text

    self.comments = []
    #print(entry)
    
    comments = entry.find('ul', {'class':'commentlist'})
    try:
      comment_list = comments.find_all('li')
    except:
      print("Skipped comments")
      return
    for c in comment_list:
      comment_author = c.find("div", {"class":"comment-author vcard"}).text.strip()
      comment_time = c.find('div', {'class':'comment-meta commentmetadata'}).text.strip()
      comment_time = comment_time.replace('\n', '').replace('\t','')
      comment_children = list(list(c.children)[1].children)
      comment_reduced = [str(x) for x in comment_children if not r"<img" in str(x) and not r"comment-meta" in str(x) and "comment-author vcard" not in str(x)]
      comment = "".join(comment_reduced).strip()
      comment = self.htmlCleanUp(comment)
      #print(comment_author)
      #print(comment_time)
      #print(comment + "\n")
      comm = BlogComment(comment_author, comment_time, comment)
      self.comments.append(comm)

  def htmlCleanUp(self, s):
    s = s.replace(r'<p>', '')
    s = s.replace(r'</p>', '')
    s = s.replace(r'<br/>','')
    s = s.replace(r'&amp;', r'&')
    links = re.findall("(<a href=.*?</a>)", s)
    for l in links:
      hyperL = re.search('>(.*?)<', l).group(1)
      linkName = re.search('href="(.*?)"', l).group(1)
      new = hyperL + " (" + linkName + ")"
      s = s.replace(l, new)
    return s

class BlogComment():
  def __init__(self, author, time, comment):
    self.author = author
    self.time = time
    self.comment = comment
