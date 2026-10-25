# Sign Language Recognition

A Python computer vision project for recognizing English alphabet hand gestures using OpenCV, MediaPipe Hands, and geometric landmark analysis.

## Project Overview

Version 1 uses hand landmark detection, geometric feature extraction, and rule-based gesture recognition.

## Features

- Hand detection and tracking using MediaPipe
- Analysis of 21 hand landmarks
- Geometric feature extraction
- Rule-based alphabet recognition (A-Z)
- Gesture recognition and word-building modules

## Technologies

- Python
- OpenCV
- MediaPipe
- NumPy

## Project Structure

```text
Project-01-SignLanguage/
├── camera/
├── docs/
├── output/
├── vision/
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/KrishnaKoushik2006/Project-01-SignLanguage.git
cd Project-01-SignLanguage
```

### 2. Create and activate a virtual environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

### 4. Run the application

```powershell
python main.py
```

A working camera is required for execution modes that use live video input.

## Current Approach

The current version uses hand landmarks and geometric rules to classify alphabet gestures. Recognition may be affected by lighting, hand orientation, camera angle, and similarities between gestures.

## Future Improvements

- Develop and integrate a custom machine-learning classifier
- Improve recognition of visually similar gestures
- Improve support for dynamic and two-handed signs
- Expand testing across different users and environments

These are planned improvements, not claims of completed functionality.

## Project Status

**Version 1 — Rule-based alphabet recognition**

This project is a learning and development effort in computer vision and sign-language-related gesture recognition.

## Author

Krishna Koushik