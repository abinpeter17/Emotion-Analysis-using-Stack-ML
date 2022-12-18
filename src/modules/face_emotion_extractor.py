from deepface import DeepFace

def detect_emotions(image_path):

    # Use the DeepFace library to detect the emotions in the image
    emotions = DeepFace.analyze(image_path, actions=['emotion'])

    # Extract the list of emotions from the results
    emotions_list = emotions['emotion']

    return emotions_list

path_ = "D:/Data/Documents/Images/Dp Compressed.jpg"
data = print(detect_emotions(path_))
# Apply Min-Max normalization
# min_val = min(data.values())
# max_val = max(data.values())
# normalized_data_min_max = {k: (v - min_val) / (max_val - min_val) for k, v in data.items()}
# print(normalized_data_min_max)

# Apply z-score normalization
# mean = np.mean(list(data.values()))
# std = np.std(list(data.values()))
# normalized_data_z_score = {k: (v - mean) / std for k, v in data.items()}
# print(normalized_data_z_score)

# Apply decimal scaling
# normalized_data_decimal_scaling = {k: v / 10 for k, v in data.items()}
# print(normalized_data_decimal_scaling)

# # Apply range normalization
# min_val = min(data)
# max_val = max(data)
# normalized_data_range = [(x - min_val) / (max_val - min_val) for x in data]
# print(normalized_data_range)

# # Apply unit norm
# normalized_data_unit_norm = [x / np.sqrt(sum([x**2 for x in data])) for x in data]
# print(normalized_data_unit_norm)