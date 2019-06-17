import requests

headers ={}
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYwNTAxMTY0LCJqdGkiOiJiMmM3NjE5ODUxNDI0MmRjYjEwMmRkMTU1ZThiYjE3YiIsInVzZXJfaWQiOjF9.OFAbdssOCxn6hBNKzQMSLnJ_F78VieN8nLSPZpIPHoU'

r = requests.get('http://127.0.0.1:8000/blogs/rest_posts/Post/', headers=headers)
print(r.text)