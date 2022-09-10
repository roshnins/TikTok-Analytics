def process_results(data):
    nested_values = ['video', 'author', 'music', 'stats', 'authorStats',
                     'challenges', 'duetInfo', 'textExtra', 'stickersOnItem']
    skip_values = ['challenges', 'duetInfo', 'textExtra', 'stickersOnItem']

    # Create blank dictionary
    flattened_data = {}
    # Loop through each video
    for idx, value in enumerate(data):
        flattened_data[idx] = {}
        # Loop through each property in each video
        for property_id, property_value in value.items():
            # Check if nested
            if property_id in nested_values:
                if property_id in skip_values:
                    pass
                else:
                    # Loop through each nested property
                    for nested_idx, nested_value in property_value.items():
                        flattened_data[idx][property_id +
                                            '_'+nested_idx] = nested_value
            # If it's not nested, add it back to the flattened dictionary
            else:
                flattened_data[idx][property_id] = property_value

    return flattened_data
