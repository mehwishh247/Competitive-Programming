class Codec:
    def __init__(self):
        self.long = ""
        self.short = ""

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        self.long = longUrl
        
        return self.long
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        self.short = shortUrl
        
        return self.short
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))