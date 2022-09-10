# Importing the tiktok Python SDK
from TikTokApi import TikTokApi as tiktok

# Import JSON for export of data
import json
# Import data processing helper
from helper import process_results

# Get cookie data from TikTok and set into verify variable
verifyFp = "verify_kx2ee558_BH6fvQVi_cXHF_4lfK_Bimg_hH0lYMCV6Vm6"
api = tiktok.get_instance(custom_verifyFp=verifyFp, use_test_endpoints=True)

# Get data by hashtag 'singaporefoodfestival'
trending = api.by_hashtag('singaporefoodfestival')
# print(trending)

# Process data
flattened_data = process_results(trending)

# Export data to json
with open('export.json', 'w') as f:
    json.dump(flattened_data, f)
