# Dataset

This project uses the **Surface Crack Detection Dataset**, a collection of industrial surface images used for binary image classification.

## Dataset Overview

The dataset contains two classes:

| Class    | Description                      |
| -------- | -------------------------------- |
| Positive | Images containing surface cracks |
| Negative | Images without surface cracks    |

### Total Images

| Category        | Count  |
| --------------- | ------ |
| Crack Images    | 20,000 |
| No Crack Images | 20,000 |
| Total Images    | 40,000 |

---

## Download Dataset

The dataset is not included in this repository due to its size.

Download it from Kaggle:

https://www.kaggle.com/datasets/arunrk7/surface-crack-detection

---

## Directory Structure

After downloading, place the dataset in the following structure:

```text
Dataset/
└── CrackDataset/
    ├── Positive/
    │   ├── image1.jpg
    │   ├── image2.jpg
    │   └── ...
    │
    └── Negative/
        ├── image1.jpg
        ├── image2.jpg
        └── ...
```

---

## Dataset Split

When the project is executed, the dataset is automatically divided into:

| Split      | Percentage |
| ---------- | ---------- |
| Training   | 70%        |
| Validation | 15%        |
| Testing    | 15%        |

The processed dataset is stored in:

```text
Processed_CrackDataset/
├── train/
├── validation/
└── test/
```

---

## Citation

If you use this dataset in your own work, please cite the original dataset source from Kaggle.

Dataset Source:
https://www.kaggle.com/datasets/arunrk7/surface-crack-detection
