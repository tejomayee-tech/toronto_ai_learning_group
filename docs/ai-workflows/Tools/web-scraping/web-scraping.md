
# 🌐 What *Is* Web Scraping?

Web scraping is the process of writing a program that **downloads a web page** and **extracts specific information** from it — like titles, prices, headlines, names, etc.

It’s commonly used for things like:

* Collecting product data
* Getting news headlines
* Monitoring prices
* Extracting tables or lists
* Learning how websites structure their content

**Always scrape respectfully:**
Check the website’s rules (`robots.txt`) and never try to bypass logins or security.

---

# Simple Web Scraping Example

Let’s scrape the **titles of articles** from a basic HTML page.

### Requirements

```bash
pip install requests beautifulsoup4
```

---

# **BEGINNER-FRIENDLY PYTHON CODE**

```python
import requests
from bs4 import BeautifulSoup

# 1. Download the page
url = "https://example.com"
response = requests.get(url)

# 2. Parse the HTML text
soup = BeautifulSoup(response.text, "html.parser")

# 3. Find something simple — like <h1> or <h2> tags
titles = soup.find_all("h2")

# 4. Print the results
for t in titles:
    print(t.get_text())
```

---

# What This Does

* Connects to `example.com`
* Reads the webpage’s HTML
* Collects **all `<h2>` elements** (super common for section headings)
* Prints them out cleanly

---

# 🪄 Even Simpler Version (1-liner extraction)

```python
from bs4 import BeautifulSoup
import requests

print([h2.text for h2 in BeautifulSoup(requests.get("https://example.com").text, "html.parser").find_all("h2")])
```

---