with source as (
    select * from {{ source('raw', 'YOUTUBE_VIDEO_DATA') }}
)

select
    upper(trim(title)) as title,
    try_cast(published_date as date) as published_date,
    try_cast(views as integer) as views,
    try_cast(likes as integer) as likes,
    try_cast(comments as integer) as comments,
    initcap(trim(channel_name)) as channel_name
from source
