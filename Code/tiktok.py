# Importing the tiktok Python SDK
from TikTokApi import TikTokApi as tiktok

# Import JSON for export of data
import json

# Import pandas to create dataframes
import pandas as pd

# Import data processing helper
from helper import process_results

# Import sys dependency to extract command line arguments
import sys

# Import subprocess to run tiktok script from command line
from subprocess import call


def get_data(hashtag):
    # Get cookie data from TikTok and set into verify variable
    verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"
    api = tiktok.get_instance(
        custom_verifyFp=verifyFp, use_test_endpoints=True)

    # Get data by hashtag 'singaporefoodfestival'
    trending = api.by_hashtag(hashtag)


    # Process data
    flattened_data = process_results(trending)


    # Convert the preprocessed data to a dataframe
    df = pd.DataFrame.from_dict(flattened_data, orient='index')
    df.to_csv('tiktokdata_clean.csv', index=False)



if __name__ == '__main__':
    get_data(sys.argv[1])
