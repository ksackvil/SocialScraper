# SocialScraper

This repo contains utilities used for web scraping various social media sites.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

You will need the following to run this project:
- [python 3](https://www.python.org/downloads/)
- pip resources installed (see below)

### Installing

A step by step series of examples that tell you how to get a development env running

1. Install python requirements.

```
pip install -r requirements.txt
```

### Running scrapeImage.py

1. Open the file scrapeImage.py in your favorite text editor, and on line 3 add the Instagram username of the account you want to scrape from.

`USERNAME="<insta-username>"`

2. Open terminal and go to the folder '<pathToDir>/SocialScraper/Instagram', then run the command:

`python scrapeImage.py`

A new folder containing the scraped images should appear in the directory '<pathToDir>/SocialScraper/Instagram'.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
