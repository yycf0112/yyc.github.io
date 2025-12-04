import io
import datetime as dt
import pandas as pd
import boto3

from googleapiclient.discovery import build

from src.utils.config_loader import load_config
from src.utils.logger import get_logger


logger = get_logger(__name__)


def fetch_youtube_data(api_key: str, channel_id: str, max_results: int = 20) -> pd.DataFrame:
    youtube = build("youtube", "v3", developerKey=api_key)

    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        maxResults=max_results,
        order="date",
        type="video"
    )
    response = request.execute()
    items = response.get("items", [])

    if not items:
        logger.warning("No video data returned.")
        return pd.DataFrame()

    rows = []
    for item in items:
        snippet = item["snippet"]
        rows.append({
            "video_id": item["id"]["videoId"],
            "title": snippet.get("title"),
            "published_at": snippet.get("publishedAt"),
            "channel_title": snippet.get("channelTitle"),
        })

    df = pd.DataFrame(rows)
    logger.info(f"Fetched {len(df)} videos.")
    return df


def upload_to_s3(df: pd.DataFrame, bucket: str, prefix: str = "raw/youtube", region: str = "eu-west-1"):
    if df.empty:
        logger.warning("No data to upload.")
        return

    s3 = boto3.client("s3", region_name=region)

    date_str = dt.date.today().strftime("%Y-%m-%d")
    timestamp = dt.datetime.utcnow().strftime("%H%M%S")
    key = f"{prefix}/dt={date_str}/youtube_{timestamp}.parquet"

    buffer = io.BytesIO()
    df.to_parquet(buffer, index=False)
    buffer.seek(0)

    s3.upload_fileobj(buffer, bucket, key)
    logger.info(f"Uploaded to s3://{bucket}/{key}")


def main():
    config = load_config()

    df = fetch_youtube_data(
        api_key=config["youtube"]["api_key"],
        channel_id=config["youtube"]["channel_id"],
        max_results=config["youtube"]["max_results"],
    )

    upload_to_s3(
        df=df,
        bucket=config["aws"]["s3_bucket"],
        region=config["aws"]["region"]
    )


if __name__ == "__main__":
    main()