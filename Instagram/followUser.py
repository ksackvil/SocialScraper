""" Quickstart script for InstaPy usage """
# imports
from instapy import InstaPy
from instapy import smart_run

# login credentials
insta_username = 'TheDevinJJones'  # <- enter username here
insta_password = '6Ac8EY99QC9yKv5'  # <- enter password here

# get an InstaPy session!
# set headless_browser=True to run InstaPy in the background
session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False)

with smart_run(session):
    """ Activity flow """
    # ~~~~~ GENERAL SETTINGS ~~~~~ #
    # allow actions on private accounts
    session.set_skip_users(skip_private=False)
    # session.set_skip_users(skip_private=True,
    #                     private_percentage=100,
    #                     skip_no_profile_pic=False,
    #                     no_profile_pic_percentage=100,
    #                     skip_business=False,
    #                     skip_non_business=False,
    #                     business_percentage=100,
    #                     skip_business_categories=[],
    #                     dont_skip_business_categories=[])

    # ~~~~~ ACTIONS ~~~~~ # 
    # follows a list of users, will only follow 'times' amount
    # there is a limit, daily limit is 200 a day. 10 follows and unfollows per hour 
    session.follow_by_list(followlist=['sara_van_b', 'teaandbujo'], times=1, sleep_delay=600, interact=False)
