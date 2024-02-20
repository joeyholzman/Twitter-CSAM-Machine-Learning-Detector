import json

def update_classification(json_data):
    for entry in json_data:
        if "Classification" not in entry:
            print("Tokenized Tweet:", entry["TweetText"])
            classification = input("Enter the classification (0 or 1, or 'q' to quit): ")

            if classification.lower() == 'q':
                break

            while classification not in ['0', '1']:
                print("Invalid input. Please enter 0 or 1.")
                classification = input("Enter the classification (0 or 1, or 'q' to quit): ")

            entry["Classification"] = int(classification)

    return json_data

# Read existing JSON file
json_file_path = './Tweet_Datasets/Tokenized_Tweets/Tokenized_Tweets.json'
with open(json_file_path, 'r') as f:
    existing_data = json.load(f)

# Update the classification for each tokenized tweet
updated_data = update_classification(existing_data)

# Write the updated data back to the JSON file
with open(json_file_path, 'w') as f:
    json.dump(updated_data, f, indent=6)

print("Classification updated successfully.")


