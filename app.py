import os
import sqlite3
from datetime import datetime


date_str = datetime.now().strftime("%Y-%m-%d")
folder_path = os.path.join(os.path.expanduser("~"), "Desktop", date_str)
os.makedirs(folder_path, exist_ok=True)


def create_database():
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()

    c.execute(
        """
    CREATE TABLE IF NOT EXISTS pokemon (
        id INTEGER PRIMARY KEY,
        name TEXT,
        type1 TEXT,
        type2 TEXT,
        height REAL,
        weight REAL,
        generation INTEGER,
        total_stats INTEGER,
        hp INTEGER,
        attack INTEGER,
        defense INTEGER,
        special_attack INTEGER,
        special_defense INTEGER,
        speed INTEGER,
        catch_rate INTEGER,
        is_baby BOOLEAN,
        is_legendary BOOLEAN,
        evolves_from INTEGER,
        image_url TEXT
    )
    """
    )

    # sample_data = [
    #     (1, "ピカチュウ", "でんき", None, 35, 190, "https://example.com/pikachu.png"),
    #     (2, "リザードン", "ほのお", "ひこう", 78, 45, "https://example.com/lizardon.png"),
    #     (3, "カビゴン", "ノーマル", None, 160, 25, "https://example.com/kabigon.png"),
    # ]
    # c.executemany("INSERT OR IGNORE INTO pokemon VALUES (?, ?, ?, ?, ?, ?, ?)", sample_data)

# データベースに接続（または存在しない場合は作成）
conn = sqlite3.connect('pokemon.db')
c = conn.cursor()

# ユーザーにtype1の値を入力させる
type1_input = input("検索したいタイプ1を入力してください: ")

# SQLクエリを実行して、特定のデータを取得
c.execute("SELECT name, hp FROM pokemon WHERE type1 = ?", (type1_input,))

# 取得したデータをフェッチして表示
rows = c.fetchall()
if rows:
    for row in rows:
        print(f"名前: {row[0]}, HP: {row[1]} ")
else:
    print(f"タイプ1が '{type1_input}' のポケモンは見つかりませんでした。")

# データベース接続を閉じる


conn.close()

