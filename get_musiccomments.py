import requests
import json
def get_comments(song_id, page):
    url = f"https://music.163.com/api/v1/resource/comments/R_SO_4_{song_id}?limit=20&offset={(page-1)*20}"
    headers = {
        "Referer": "https://music.163.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    comments = []
    for comment in data['comments']:
        content = comment['content']
        comments.append(content)
    return comments
def main():
    song_id = input("请输入音乐 ID：")
    page = int(input("请输入评论页数："))
    comments = get_comments(song_id, page)
    for i, comment in enumerate(comments):
        print(f"{i+1}. {comment}")
if __name__ == "__main__":
    main()