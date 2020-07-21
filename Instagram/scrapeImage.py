from subprocess import call

USERNAME="stooleysbargrill" # add the insta username to scrape here
INCLUDE_IMAGE = True
INCLUDE_VIDEO = False

if (INCLUDE_IMAGE and INCLUDE_VIDEO) or (not(INCLUDE_IMAGE) and not(INCLUDE_VIDEO)):
    media_types = ""   
elif INCLUDE_IMAGE:
    media_types = "--media-types=image"
elif INCLUDE_VIDEO:
    media_types = "--media-types=video"

call(["instagram-scraper", USERNAME, "--profile-metadata", "--media-metadata", media_types])