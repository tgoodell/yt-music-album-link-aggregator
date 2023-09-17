# YT Music Album Link Aggregator

This is a very simple Python script that takes in a file of html (from the list of albums or singles of a particular artist on Youtube music) and prints out the extracted URLs to each album/single. 

The intended usage of this script is:

`python3 "input.txt" > output.txt`

This list of URLs can then be directed to [youtube-dl](https://github.com/ytdl-org/youtube-dl) or [yt-dlp](https://github.com/yt-dlp/yt-dlp) to be scraped. 