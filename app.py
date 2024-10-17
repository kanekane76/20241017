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
        hp INTEGER,
        catch_rate INTEGER,
        image_url TEXT
    )
    """
    )

    sample_data = [
        (1, "ピカチュウ", "でんき", None, 35, 190, "https://example.com/pikachu.png"),
        (2, "リザードン", "ほのお", "ひこう", 78, 45, "https://example.com/lizardon.png"),
        (3, "カビゴン", "ノーマル", None, 160, 25, "https://example.com/kabigon.png"),
    ]
    c.executemany("INSERT OR IGNORE INTO pokemon VALUES (?, ?, ?, ?, ?, ?, ?)", sample_data)

    conn.commit()
    conn.close()


def get_pokemon(name):
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()

    c.execute("SELECT * FROM pokemon WHERE name=?", (name,))
    pokemon = c.fetchone()

    if pokemon:
        print(f"名前: {pokemon[1]}, タイプ1: {pokemon[2]}, タイプ2: {pokemon[3]}, HP: {pokemon[4]}")
        print(f"画像: {pokemon[6]}")
    else:
        print("ポケモンが見つかりませんでした。")

    conn.close()


def get_pokemon_by_type(type1, type2=None):
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()

    if type2:
        c.execute("SELECT * FROM pokemon WHERE type1=? AND type2=? AND hp >= 50", (type1, type2))
    else:
        c.execute("SELECT * FROM pokemon WHERE type1=? AND hp >= 50", (type1,))

    pokemon = c.fetchone()

    if pokemon:
        print(f"名前: {pokemon[1]}, タイプ1: {pokemon[2]}, タイプ2: {pokemon[3]}, HP: {pokemon[4]}")
    else:
        print("該当するポケモンはありません。")

    conn.close()


def display_catch_rate_ranking(order="asc"):
    conn = sqlite3.connect("pokemon.db")
    c = conn.cursor()

    if order == "asc":
        c.execute("SELECT * FROM pokemon ORDER BY catch_rate ASC")
    else:
        c.execute("SELECT * FROM pokemon ORDER BY catch_rate DESC")

    rankings = c.fetchall()

    for rank in rankings:
        print(f"名前: {rank[1]}, 捕まえやすさ: {rank[5]}")

    conn.close()


def main():
    create_database()

    name = input("ポケモンの名前を入力してください: ")
    get_pokemon(name)

    type1 = input("タイプ1を入力してください: ")
    type2 = input("タイプ2を入力してください（省略可）: ") or None
    get_pokemon_by_type(type1, type2)

    print("捕まえやすさランキング（昇順）:")
    display_catch_rate_ranking("asc")

    print("捕まえやすさランキング（降順）:")
    display_catch_rate_ranking("desc")


if __name__ == "__main__":
    main()
