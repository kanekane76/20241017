# # import os
# # import sqlite3
# # from datetime import datetime


# # date_str = datetime.now().strftime("%Y-%m-%d")
# # folder_path = os.path.join(os.path.expanduser("~"), "Desktop", date_str)
# # os.makedirs(folder_path, exist_ok=True)


# # def create_database():
# #     conn = sqlite3.connect("pokemon.db")
# #     c = conn.cursor()

# #     c.execute(
# #         """
# #     CREATE TABLE IF NOT EXISTS pokemon (
# #         id INTEGER PRIMARY KEY,
# #         name TEXT,
# #         type1 TEXT,
# #         type2 TEXT,
# #         height REAL,
# #         weight REAL,
# #         generation INTEGER,
# #         total_stats INTEGER,
# #         hp INTEGER,
# #         attack INTEGER,
# #         defense INTEGER,
# #         special_attack INTEGER,
# #         special_defense INTEGER,
# #         speed INTEGER,
# #         catch_rate INTEGER,
# #         is_baby BOOLEAN,
# #         is_legendary BOOLEAN,
# #         evolves_from INTEGER,
# #         image_url TEXT
# #     )
# #     """
# # )

# #     # sample_data = [
# #     #     (1, "ピカチュウ", "でんき", None, 35, 190, "https://example.com/pikachu.png"),
# #     #     (2, "リザードン", "ほのお", "ひこう", 78, 45, "https://example.com/lizardon.png"),
# #     #     (3, "カビゴン", "ノーマル", None, 160, 25, "https://example.com/kabigon.png"),
# #     # ]
# #     # c.executemany("INSERT OR IGNORE INTO pokemon VALUES (?, ?, ?, ?, ?, ?, ?)", sample_data)

# # # データベースに接続（または存在しない場合は作成）
# # ｌ
# import requests
# from PIL import Image
# from io import BytesIO


# def get_pokemon_data(pokemon_name):
#     # APIのURLを設定
#     url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
#     response = requests.get(url)

#     if response.status_code != 200:
#         print("ポケモンが見つかりませんでした。正しい名前を入力してください。あほ")
#         return

#     data = response.json()
#     name = data["name"].capitalize()
#     types = [t["type"]["name"].capitalize() for t in data["types"]]
#     hp = data["stats"][0]["base_stat"]
#     image_url = data["sprites"]["front_default"]

#     # データを表示
#     print(f"ポケモンの名前: {name}")
#     print(f"タイプ1: {types[0]}")
#     if len(types) > 1:
#         print(f"タイプ2: {types[1]}")
#     else:
#         print("タイプ2: なし")
#     print(f"HP: {hp}")

#     # 画像を表示
#     display_image(image_url)


# def display_image(url):
#     # 画像をダウンロードして表示
#     response = requests.get(url)
#     image = Image.open(BytesIO(response.content))
#     image.show()


# if __name__ == "__main__":
#     pokemon_name = input("ポケモンの名前を入力してください: ")
#     get_pokemon_data(pokemon_name)


import sqlite3
import tkinter as tk
from tkinter import Label
from PIL import Image, ImageTk
import requests
from io import BytesIO


# データベースに接続
conn = sqlite3.connect("pokemon.db")
c = conn.cursor()
# ユーザーにポケモンの名前をターミナルで入力させる
name = input("検索したいポケモンの名前を入力してください: ")
# SQLクエリを実行して、特定のデータを1つだけ取得
c.execute("SELECT type1, type2, hp, image_url FROM pokemon WHERE name = ?", (name,))
# 取得したデータをフェッチ
row = c.fetchone()
# データベース接続を閉じる
conn.close()


# GUIの初期設定
root = tk.Tk()
root.title("ポケモン情報表示")
if row:
    type1, type2, hp, image_url = row

    # タイプ1、タイプ2、HPを表示
    Label(root, text=f"名前: {name}", font=("Arial", 20)).pack(padx=20, pady=10)
    Label(root, text=f"タイプ1: {type1}", font=("Arial", 16)).pack(padx=20, pady=5)

    if type2:  # タイプ2がある場合のみ表示
        Label(root, text=f"タイプ2: {type2}", font=("Arial", 16)).pack(padx=20, pady=5)

    Label(root, text=f"HP: {hp}", font=("Arial", 16)).pack(padx=20, pady=5)

    # 画像を取得して表示
    response = requests.get(image_url)
    img_data = BytesIO(response.content)
    img = Image.open(img_data)
    img = img.resize((200, 200), Image.LANCZOS)  # 画像のサイズを調整
    photo = ImageTk.PhotoImage(img)
    Label(root, image=photo).pack(padx=20, pady=10)

else:
    Label(root, text=f"ポケモン '{name}' は見つかりませんでした。", font=("Arial", 16)).pack(padx=20, pady=20)


# ウィンドウの表示
root.mainloop()
