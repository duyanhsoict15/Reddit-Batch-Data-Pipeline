from etls.reddit_etl import connect_reddit, extract_posts, load_data_to_csv, transform_data
from utils.constants import CLIENT_ID, OUTPUT_PATH, SECRET
import pandas as pd

def reddit_pipeline(file_name: str, subreddit: str, time_filter = 'day', limit=None):
    #ket noi toi reddit instance
    instance = connect_reddit(CLIENT_ID, SECRET, 'MyRedditApp/1.0 by karmeme1508@gmail.com')
    #extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)
    #transformation
    post_df = transform_data(post_df)
    #loading to csv
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(post_df, file_path)
    return file_path