from datetime import datetime
import instaloader

connect_lib = instaloader.Instaloader()
connect_lib.login('user', 'password')

# Dados de seguidores e seguindo do perfil informado
followers = instaloader.Profile.from_username(connect_lib, "user_profile").get_followers()
followees = instaloader.Profile.from_username(connect_lib, "user_profile").get_followees()

# Dados Encotrados
print(f"""
Followers - {str(followers._data['count'])}
Followers - {str(followers._data['count'])}
Seguidores:
{followers._data['edges']}
""")