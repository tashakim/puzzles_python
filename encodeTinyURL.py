class Codec:
    """
    Purpose: Design a URL shortening service.
    """
    def __init__(self):
        self.visited = dict()
        

    def encode(self, longUrl: str) -> str:
        """
        Purpose: Encodes a URL to a shortened URL.
        """
        shortUrl = longUrl[:-1] # Place encoding algorithm here. 
        # Currently, there is no restriction on how the encode/decode algorithm should work.
        self.visited[shortUrl] = longUrl
        
        return shortUrl


    def decode(self, shortUrl: str) -> str:
        """
        Purpose: Decodes a shortened URL to its original URL.
        """
        return self.visited[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))