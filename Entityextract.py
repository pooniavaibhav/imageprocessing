import re
from nltk.tag import pos_tag
# doc = ['MTA', '‘SO', 'GOVERNMENTORDIONE——', 'Rew', 'faarea', 'eee', 'Riteish', 'Vilasrao', 'Deshmukh', 'wea', 'aYYOB:1977', 'RT', 'Male', '_2173', '1296', '4875']
# doc = ['ANA', 'ata', 'Government', 'of', 'India', 'faster', 'as', 'Nirmla', 'Bai', 'eH', 'FAA', '/', 'DOB', ':', '05/07/1990', 'Afeat', '/', 'Female', 'i']
doc = ['FT', 'FHS', 'TCS', 'E', 'Chandrasekar', 'Umis', 'sror', '|', 'DOB:', 'es', 'er', '|', 'MALE', '2007', '8686', '4767']
r = re.compile(r"[A-Z][a-z]*")

tagged_sent = pos_tag(doc)
propernouns = [word for word,pos in tagged_sent if pos == 'NNP']


for i in propernouns:
    i.title()
    if r.match(i):
        print(i)
    else:
        pass
