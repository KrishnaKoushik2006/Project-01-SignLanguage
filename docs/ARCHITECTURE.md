# ARCHITECTURE

---

# Project Architecture

**Project Name:** Project-01 - Sign Language Recognition

**Current Version:** v1.1 (Geometry Engine Architecture)

---

# Project Structure

```text
Project-01-SignLanguage/

│
├── camera/
│   └── camera.py
│
├── vision/
│   ├── geometry.py
│   ├── pose_utils.py
│   ├── hand_utils.py
│   ├── hand_detector.py
│   ├── finger_counter.py
│   ├── feature_extractor.py
│   ├── gesture_detector.py
│   ├── alphabet_rules.py
│   ├── alphabet_detector.py
│   ├── word_builder.py
│   └── config.py
│
├── app/
│
├── assets/
│
├── config/
│
├── datasets/
│
├── docs/
│
├── models/
│
├── output/
│
├── tests/
│
├── utils/
│
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

# System Architecture

```text
Camera
   │
   ▼
Camera Module
   │
   ▼
MediaPipe Hand Detector
   │
   ▼
Left / Right Hand Separation
   │
   ▼
Pose Wrapper (PoseUtils)
   │
   ▼
Geometry Engine
   │
   ▼
Feature Extractor
   │
   ├──────────────┐
   ▼              ▼
Gesture Detector  Alphabet Detector
                      │
                      ▼
                Word Builder
                      │
                      ▼
             Recognition Result
                      │
                      ▼
               Display Output
```

---

# Layered Architecture

```text
Presentation Layer
│
├── main.py
│
Recognition Layer
│
├── gesture_detector.py
├── alphabet_detector.py
├── alphabet_rules.py
├── word_builder.py
│
Feature Layer
│
├── feature_extractor.py
│
Geometry Layer
│
├── geometry.py
├── pose_utils.py
├── hand_utils.py
├── finger_counter.py
│
Vision Layer
│
├── hand_detector.py
│
Hardware Layer
│
└── camera.py
```

---

# Module Responsibilities

---

## main.py

Application Entry Point

Responsibilities

- Initialize all modules
- Capture webcam frames
- Execute recognition pipeline
- Display detected gestures
- Display alphabets
- Display recognized words
- Close application safely

---

## camera.py

Camera Engine

Responsibilities

- Open webcam
- Capture frames
- Return current frame
- Release webcam

---

## hand_detector.py

Vision Engine

Responsibilities

- Detect hands using MediaPipe
- Detect 21 landmarks
- Separate left and right hands
- Draw landmarks
- Return processed frame

---

## pose_utils.py

Landmark Wrapper

Responsibilities

- Store landmark references
- Provide easy access to landmarks

Example

```
thumb_tip

index_tip

middle_tip

ring_tip

little_tip
```

No calculations are performed inside this module.

---

## geometry.py

Geometry Engine

Responsibilities

- Distance calculation
- Touch detection
- Curvature detection
- Angle calculation
- Finger angle calculation

Current Functions

- distance()
- is_touching()
- is_curled()
- angle()
- thumb_angle()
- index_angle()
- middle_angle()
- ring_angle()
- little_angle()

Future Functions

- Palm Orientation
- Hand Orientation
- Finger Direction
- Curvature Analysis
- Symmetry Detection

---

## finger_counter.py

Finger Analysis Engine

Responsibilities

- Detect finger states
- Count raised fingers
- Support left and right hands

---

## hand_utils.py

Hand Utility Engine

Responsibilities

- Wrist distance
- Hand proximity
- Two-hand helper functions

---

## feature_extractor.py

Feature Engine

Responsibilities

Convert landmarks into reusable semantic features.

Current Features

### Hand Presence

- Left Hand
- Right Hand
- Both Hands

### Finger State

- Thumb Up
- Index Up
- Middle Up
- Ring Up
- Little Up

### Finger Count

- Left Finger Count
- Right Finger Count

### Touch Features

- Thumb ↔ Index
- Thumb ↔ Middle
- Thumb ↔ Ring
- Thumb ↔ Little

- Index ↔ Middle
- Middle ↔ Ring
- Ring ↔ Little

- Thumb ↔ Thumb (Both Hands)

### Curvature Features

- Thumb Curled
- Index Curled
- Middle Curled
- Ring Curled
- Little Curled

### Angle Features

- Thumb Angle
- Index Angle
- Middle Angle
- Ring Angle
- Little Angle

### Hand Features

- Wrist Distance
- Hands Close

---

## gesture_detector.py

Gesture Recognition Engine

Responsibilities

Recognize predefined gestures.

Current Gestures

- Open Palm
- Fist
- Victory
- Thumbs Up

---

## alphabet_rules.py

Recognition Rules

Responsibilities

Store recognition logic for ISL alphabets.

Current Alphabets

- A (Version 1)
- B (Version 1)

---

## alphabet_detector.py

Alphabet Engine

Responsibilities

- Execute alphabet rules
- Return recognized alphabet

---

## word_builder.py

Word Recognition Engine

Responsibilities

- Collect detected alphabets
- Remove duplicates
- Build words
- Return recognized word

---

# Recognition Pipeline

```text
Camera
      │
      ▼
MediaPipe
      │
      ▼
21 Hand Landmarks
      │
      ▼
PoseUtils
      │
      ▼
Geometry Engine
      │
      ▼
Feature Extractor
      │
      ├──────────────┐
      ▼              ▼
Gesture Detector  Alphabet Detector
                      │
                      ▼
                Word Builder
                      │
                      ▼
             Recognition Result
```

---

# Data Flow

```text
Webcam

↓

Raw Frame

↓

MediaPipe

↓

21 Landmarks

↓

Pose Wrapper

↓

Geometry Engine

↓

Feature Dictionary

↓

Gesture Detection

↓

Alphabet Detection

↓

Word Builder

↓

Display
```

---

# Current Feature Count

Hand Presence

- 3

Finger States

- 10

Finger Counts

- 2

Touch Features

- 15

Curvature Features

- 10

Finger Angles

- 10

Hand Relation

- 2

Total Features

**50+ Features**

---

# Design Principles

- Layered Architecture
- Modular Design
- Single Responsibility Principle
- Separation of Concerns
- Feature-Based Recognition
- Geometry-Based Recognition
- Code Reusability
- Scalability
- Maintainability
- Easy Unit Testing

---

# Current Status

Architecture Version

**v1.1**

Completed

- Camera Module
- MediaPipe Integration
- Hand Detection
- Left/Right Hand Identification
- Geometry Engine
- Pose Wrapper
- Feature Engine
- Gesture Recognition
- Alphabet Recognition Framework
- Word Builder

Current Alphabet Support

- A (Version 1)
- B (Version 1)

Upcoming

- Thumb Direction
- Palm Orientation
- Hand Orientation
- Finger Direction
- Improve A
- Improve B
- C–Z Recognition
- Sentence Recognition
- Speech Output
- Machine Learning Classifier