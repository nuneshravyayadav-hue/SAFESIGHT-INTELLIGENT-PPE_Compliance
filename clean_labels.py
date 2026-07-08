import os

# Folder containing YOLO label files
folders = [
    r"D:\shravya\data\labels\train",
                r"D:\shravya\data\labels\val",
                r"D:\shravya\data\labels\test"
    ]
for labels_folder in folders:
    class_mapping = {
        0: 0,
        1: 1,
        2: 2,
        3: 3,
        4: 4,
        5: 5
}

for filename in os.listdir(labels_folder):
    if filename.endswith(".txt"):
        filepath = os.path.join(labels_folder, filename)

        new_labels = []

        with open(filepath, "r") as f:
            lines = f.readlines()

        for line in lines:
            data = line.strip().split()
            class_id = int(data[0])

            # Keep only required classes
            if class_id in class_mapping:
                data[0] = str(class_mapping[class_id])
                new_labels.append(" ".join(data))

        with open(filepath, "w") as f:
            f.write("\n".join(new_labels))

print("Dataset preprocessing completed successfully.")
