from datetime import datetime
import instaloader

connect_lib = instaloader.Instaloader()
connect_lib.login('user', 'password')

# Posts do perfil escolhidos
posts = instaloader.Profile.from_username(connect_lib.context, "User").get_posts()

# Período dos posts para downloadings
since = datetime(2021, 1, 16)
until = datetime(2021, 1, 18)

for post in posts:
    if post.date >= since and post.date <= until:
        print(post.date)
        connect_lib.download_post(post, "Insta_downloads") # Path onde será salvo os arquivos