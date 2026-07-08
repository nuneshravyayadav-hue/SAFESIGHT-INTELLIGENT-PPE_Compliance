# PPE Compliance Monitoring System

## About

This repository contains my individual contributions to an AI-based Personal Protective Equipment (PPE) Compliance Monitoring System for construction sites. My work focuses on dataset preparation and validation, which are essential steps before training an object detection model. The repository includes scripts for cleaning annotation labels, validating the dataset structure, and managing the project dependencies.

## Project Objective

The objective of this project is to prepare a high-quality dataset for PPE detection by ensuring that the annotations are clean, consistent, and compatible with YOLO-based object detection models. Proper dataset preprocessing helps improve the accuracy and reliability of the model during training.

## Dataset

The dataset used for this project consists of annotated construction site images containing workers and Personal Protective Equipment (PPE). During preprocessing, the annotation labels were cleaned and remapped to maintain consistency and prepare the dataset for object detection tasks.

## My Contributions

As part of this repository, I have:

- Added the dataset configuration file (`data.yaml`).
- Developed `clean_labels.py` to clean and remap annotation labels.
- Developed `check_dataset.py` to verify the dataset structure and identify missing annotation files.
- Added `train.py` to define the YOLOv8 model training workflow using the project dataset configuration.
- Added `requirements.txt` to manage the required project dependencies.

## Repository Structure

```
.
├── clean_labels.py
├── check_dataset.py
├── train.py
├── data.yaml
├── requirements.txt
└── README.md
```

## Installation

Install the required Python packages using:

```bash
pip install -r requirements.txt
```

## Running the Scripts

Run the dataset preprocessing script:

```bash
python clean_labels.py
```

Run the dataset validation script:

```bash
python check_dataset.py
```
Run the YOLOv8 training script:

```bash
python train.py
```

## Technologies used

Python
