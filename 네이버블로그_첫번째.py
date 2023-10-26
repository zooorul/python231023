import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = "https://search.naver.com/search.naver?where=view&sm=tab_jum&query=%EB%A7%A5%EB%B6%81"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the page content with BeautifulSoup
    soup = BeautifulSoup(response.text, "html.parser")

    # Find and extract the relevant information
    blog_entries = soup.find_all("li", class_="bx")

    for entry in blog_entries:
        blog_name = entry.find("a", class_="sub_text")
        blog_address = entry.find("a", class_="sub_thumb")
        post_title = entry.find("a", class_="sh_blog_title")
        date = entry.find("span", class_="sub_time")

        if blog_name and blog_address and post_title and date:
            print("Blog Name:", blog_name.get_text())
            print("Blog Address:", blog_address["href"])
            print("Post Title:", post_title["title"])
            print("Date:", date.get_text())
            print("\n")

else:
    print("Failed to retrieve the page. Status code:", response.status_code)
