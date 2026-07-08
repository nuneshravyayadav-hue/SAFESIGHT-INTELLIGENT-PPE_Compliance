from ultralytics import YOLO

def train_model():
    # Load a pretrained YOLOv8 model
    model = YOLO("yolov8s.pt")

    # Train the model
    model.train(
        data=r"D:\shravya\data\data.yaml",
        epochs=50,
        imgsz=640,
        batch=16,
        project="runs",
        name="train_ppe"
    )

if __name__ == "__main__":
    train_model()
