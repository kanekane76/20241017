import sqlite3

# データベースに接続
conn = sqlite3.connect("pokemon.db")
c = conn.cursor()


# タイプ1でHPが50以上のポケモンを検索する関数
def search_by_type1(type1):
    c.execute("SELECT name, hp FROM pokemon WHERE type1 = ? AND hp >= 50", (type1,))
    result = c.fetchone()
    if result:
        print(f"該当するポケモン: {result[0]}, HP: {result[1]}")
    else:
        print("該当するポケモンはありません")


# タイプ1とタイプ2でHPが50以上のポケモンを検索する関数
def search_by_type1_and_type2(type1, type2):
    c.execute("SELECT name, hp FROM pokemon WHERE type1 = ? AND type2 = ? AND hp >= 50", (type1, type2))
    result = c.fetchone()
    if result:
        print(f"該当するポケモン: {result[0]}, HP: {result[1]}")
    else:
        print("該当するポケモンはありません")


# ターミナルからの入力
type1_input = input("検索したいタイプ1を入力してください: ")
search_by_type1(type1_input)

type1_input = input("検索したいタイプ1を入力してください: ")
type2_input = input("検索したいタイプ2を入力してください: ")
search_by_type1_and_type2(type1_input, type2_input)

# 接続を閉じる
conn.close()
