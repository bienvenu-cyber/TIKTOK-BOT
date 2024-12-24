import requests
import time
import random

# Remplacer par vos propres clés et jetons d'API TikTok
API_KEY = "votre_cle_api"
ACCESS_TOKEN = "votre_token_acces"

# Fonction pour obtenir des utilisateurs par hashtag
def get_users_by_hashtag(hashtag):
    url = f"https://api.tiktok.com/v1/hashtag/{hashtag}/users"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json().get('users', [])
    return []

# Fonction pour suivre un utilisateur
def follow_user(user_id):
    url = f"https://api.tiktok.com/v1/user/{user_id}/follow"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.post(url, headers=headers)
    return response.status_code == 200

# Fonction pour liker un post
def like_post(post_id):
    url = f"https://api.tiktok.com/v1/post/{post_id}/like"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    response = requests.post(url, headers=headers)
    return response.status_code == 200

# Fonction pour commenter un post
def comment_on_post(post_id, comment):
    url = f"https://api.tiktok.com/v1/post/{post_id}/comment"
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
    }
    data = {
        "text": comment
    }
    response = requests.post(url, headers=headers, json=data)
    return response.status_code == 200

# Exemple d'utilisation
hashtags = ["coding", "programming", "developer"]

for hashtag in hashtags:
    users = get_users_by_hashtag(hashtag)
    for user in users:
        follow_user(user['id'])
        time.sleep(random.randint(30, 90))  # Attendre entre 30 et 90 secondes entre les suivis
        for post in user['posts'][:5]:  # Liker et commenter les 5 premiers posts
            like_post(post['id'])
            time.sleep(random.randint(10, 30))  # Attendre entre 10 et 30 secondes entre les likes
            comment_on_post(post['id'], "Super post !")
            time.sleep(random.randint(20, 60))  # Attendre entre 20 et 60 secondes entre les commentaires
