import json

def update_classification(json_data):
    for entry in json_data:
        if "Classification" not in entry:
            print("Tokenized Tweet:", entry["Tweet"])
            classification = input("Enter the classification (0 or 1, or 'q' to quit): ")

            if classification.lower() == 'q':
                break

            while classification not in ['0', '1']:
                print("Invalid input. Please enter 0 or 1.")
                classification = input("Enter the classification (0 or 1, or 'q' to quit): ")

            entry["Classification"] = int(classification)

            with open(json_file_path, 'w') as f:
                json.dump(existing_data, f, indent=6)

    return json_data

json_file_path = './Tweet_Datasets/Tokenized_Tweets/Tokenized_Tweets.json'
with open(json_file_path, 'r') as f:
    existing_data = json.load(f)

tweets_without_classification = [entry for entry in existing_data if "Classification" not in entry]
updated_data = update_classification(tweets_without_classification)

print("Classification updated successfully.")


