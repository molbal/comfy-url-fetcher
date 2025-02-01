from .url_fetcher_node import URLFetcherNode

NODE_CLASS_MAPPINGS = {
    "URL Fetcher": URLFetcherNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "URL Fetcher": "URL Fetcher",
}
WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]