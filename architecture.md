# Lab 5 architecture

```text
[JSONPlaceholder /todos]
          |
          | HTTPS (HTTP over TLS), TCP 443, JSON response
          v
[Python client: api_client.py]
          |
          | Writes frontend_feed.json (JSON file)
          v
[Local Python HTTP server: localhost:8080]
          |
          | HTTP, TCP 8080, JSON response to GET /frontend_feed.json
          v
[Frontend client]
```
