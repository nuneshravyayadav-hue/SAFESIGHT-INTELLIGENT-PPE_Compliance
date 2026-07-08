import os

# Dataset folders
image_folders = [
    r"D:\shravya\data\images\train",
    r"D:\shravya\data\images\val",
    r"D:\shravya\data\images\test"
]

label_folders = [
    r"D:\shravya\data\labels\train",
    r"D:\shravya\data\labels\val",
    r"D:\shravya\data\labels\test"
]

for images_folder, labels_folder in zip(image_folders, label_folders):

    image_files = [f for f in os.listdir(images_folder)
                   if f.endswith((".jpg", ".jpeg", ".png"))]

    label_files = [f for f in os.listdir(labels_folder)
                   if f.endswith(".txt")]

    print("=" * 50)
    print("Images Folder :", images_folder)
    print("Labels Folder :", labels_folder)

    print("Total Images :", len(image_files))
    print("Total Labels :", len(label_files))

    missing_labels = []

    for image in image_files:
        label_name = os.path.splitext(image)[0] + ".txt"

        if label_name not in label_files:
            missing_labels.append(label_name)

    if missing_labels:
        print("\nMissing Labels:")
        for label in missing_labels:
            print(label)
    else:
        print("\nNo missing labels found.")

print("\nDataset check completed successfully.")
