# wap to extract all email address from a given text
import re
text="""contact us at support @mkd221524@gmail.com or 0241ece134@niet.co.in.
you can also reach out to saurabh@123gmail.com"""
email_pattern=r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails=re.findall(email_pattern,text)
print(emails)