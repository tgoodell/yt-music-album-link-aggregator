from bs4 import BeautifulSoup
import sys

def main():
    if len(sys.argv) < 2:
        print(f"usage: {sys.argv[0]} HTML_FILE_TO_SCRAPE", file=sys.stderr)
        sys.exit(-1)

    fileName = sys.argv[1]

    with open(fileName) as fp:
        soup = BeautifulSoup(fp, "html.parser")
        
        relevantATags = soup.find_all("a", class_="yt-simple-endpoint image-wrapper style-scope ytmusic-two-row-item-renderer")
        
        for tag in relevantATags:
            if tag["href"][0] == 'b':
                print("https://music.youtube.com/" + tag["href"])
            else: 
                print(tag["href"])

if __name__ == '__main__':
    main()