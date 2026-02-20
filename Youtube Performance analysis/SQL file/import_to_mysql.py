import pandas as pd
import mysql.connector

# ---- CHANGE THESE ----
host = "localhost"
user = "root"
password = "Suraj@1234"
database = "youtube_canada"
# ----------------------

# Connect to MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

cursor = conn.cursor()

# Read CSV safely
df = pd.read_csv("CAvideos.csv", encoding="latin1")

# Drop description column (causes problems)
if "description" in df.columns:
    df = df.drop(columns=["description"])

# Insert row by row
for _, row in df.iterrows():
    sql = """
    INSERT INTO cavideos_clean
    (video_id, trending_date, title, channel_title, category_id,
     publish_time, tags, views, likes, dislikes,
     comment_count, thumbnail_link,
     comments_disabled, ratings_disabled, video_error_or_removed)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = tuple(row)
    cursor.execute(sql, values)

conn.commit()
print("Import completed successfully!")
