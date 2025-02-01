import requests
from server import PromptServer
import re

class URLFetcherNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "urls": ("STRING", {"multiline": True, "placeholder": "Enter URLs separated by spaces or newlines"}),
            },
        }

    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("output",)
    CATEGORY = "example"
    FUNCTION = "fetch_urls"

    def fetch_urls(self, urls):
        # Split the input text into individual URLs
        url_list = re.split(r'\s+', urls.strip())
        results = []

        for url in url_list:
            if not url.startswith("http"):
                url = "https://" + url  # Assume HTTPS if protocol is missing

            try:
                # Fetch the webpage
                response = requests.get(url)
                response.raise_for_status()

                # Extract the title using regex
                title_match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
                title = title_match.group(1).strip() if title_match else "No Title"

                # Remove everything between <script> and <style> tags
                cleaned_content = re.sub(r'<script.*?</script>', '', response.text, flags=re.DOTALL)
                cleaned_content = re.sub(r'<style.*?</style>', '', cleaned_content, flags=re.DOTALL)

                # Remove all remaining HTML tags
                cleaned_content = re.sub(r'<[^>]+>', ' ', cleaned_content)

                # Normalize whitespace
                cleaned_content = re.sub(r'\s+', ' ', cleaned_content).strip()

                # Format the result
                result = f"{title}: {cleaned_content}"
                results.append(result)
            except Exception as e:
                results.append(f"Error fetching {url}: {str(e)}")

        # Combine all results into a single string
        output = "KAKIKAKIKAKI\n".join(results)

        # Send a message to the front-end (optional)
        PromptServer.instance.send_sync("url_fetcher.message", {"message": "Finished fetching URLs"})

        return (output,)