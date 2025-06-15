with base as (
    select * from {{ ref('stg_youtube_videos') }}
)

select
    title,
    channel_name,
    views,
    likes,
    comments,
    published_date,
    round((likes + comments) / nullif(views, 0), 4) as engagement_rate
from base
