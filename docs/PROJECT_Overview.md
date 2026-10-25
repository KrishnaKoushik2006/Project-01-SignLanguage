# PROJECT OVERVIEW

---

# Project Name

**Project-01 - Sign Language Recognition**

---

# Version

**v1.3.0**

---

# Project Status

🟢 **Version 1 Recognition Completed**

---

# Completed Sprints

- ✅ Sprint 1 – Development Environment

- ✅ Sprint 2 – Camera Engine

- ✅ Sprint 3 – Modular Architecture

- ✅ Sprint 4 – Vision Engine

- ✅ Sprint 5 – Finger Analysis

- ✅ Sprint 6 – Gesture Recognition

- ✅ Sprint 7 – Alphabet Recognition Framework

- ✅ Sprint 8 – Feature Extraction Architecture

- ✅ Sprint 9 – Geometry Engine

- ✅ Sprint 10 – Feature Engine & Word Builder

- ✅ Sprint 11 – Advanced Geometry & Alphabet Expansion

---

# Current Sprint

🚧 **Version 2 – Recognition Robustness & Advanced Features**

---

# Project Description

Project-01 - Sign Language Recognition is a real-time Computer Vision application that recognizes **Indian Sign Language (ISL)** using a webcam.

The project uses **MediaPipe Hands** to detect hand landmarks and converts those landmarks into reusable semantic features using a dedicated **Geometry Engine** and **Feature Engine**.

Those features are then used to recognize:

- Hand Gestures

- ISL Alphabets

- Words

The system is being developed using a modular layered architecture that emphasizes:

- Scalability

- Maintainability

- Reusability

- Software Engineering Best Practices

Beyond building a Sign Language Recognition system, this project is also a practical learning journey in:

- Computer Vision

- Artificial Intelligence

- Feature Engineering

- Software Engineering

- Human Computer Interaction

---

# Project Objectives

## Primary Objectives

- Detect one or two hands

- Track 21 MediaPipe landmarks

- Build a reusable Geometry Engine

- Extract semantic features

- Recognize ISL alphabets

- Build words

- Build sentences

- Convert text into speech

---

## Secondary Objectives

- Learn professional software architecture

- Learn Computer Vision fundamentals

- Learn Feature Engineering

- Learn debugging methodologies

- Build reusable AI modules

- Create a professional AI portfolio project

---

# Technology Stack

## Programming Language

- Python 3.12

---

## Libraries

- OpenCV

- MediaPipe

- NumPy

---

## Development Tools

- Visual Studio Code

- PowerShell

- Git (Planned)

- GitHub (Planned)

---

## Operating System

- Windows 11

---

# Project Structure

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

├── assets/

├── config/

├── datasets/

├── docs/

├── models/

├── output/

├── tests/

├── utils/

│

├── main.py

├── README.md

├── requirements.txt

└── .gitignore

---

# Current Features

## Development Environment

- Python Virtual Environment

- Dependency Management

- Stable Python Environment

---

## Camera Engine

- Webcam Access

- Live Video Streaming

- Real-Time Frame Capture

- Safe Camera Release

---

## Vision Engine

- MediaPipe Hands

- 21 Landmark Detection

- Left Hand Detection

- Right Hand Detection

- Two-Hand Tracking

- Skeleton Drawing

---

## Geometry Engine

Implemented

- Distance Calculation

- Touch Detection

- Finger Curvature

- Finger Angle Calculation

- Hand Distance Calculation

- Hand Vertical Distance

- Relative Hand Position

- Index Finger Distance

- Two-Hand Geometric Relationships

---

## Finger Analysis

- Finger State Detection

- Finger Counting

- Left Finger Count

- Right Finger Count

- Thumb State

- Index State

- Middle Finger State

- Ring Finger State

- Little Finger State

---

## Feature Engine

Implemented

### Hand Presence

- Left Hand

- Right Hand

- Both Hands

### Finger Features

- Finger States

- Finger Counts

### Touch Features

- Thumb ↔ Index

- Thumb ↔ Middle

- Thumb ↔ Ring

- Thumb ↔ Little

- Index ↔ Middle

- Middle ↔ Ring

- Ring ↔ Little

- Thumb ↔ Thumb

### Curvature Features

- Thumb Curled

- Index Curled

- Middle Curled

- Ring Curled

- Little Curled

### Finger Angles

- Thumb Angle

- Index Angle

- Middle Angle

- Ring Angle

- Little Angle

### Hand Relation

- Wrist Distance

- Hands Close

- Hand Vertical Distance

- Left Hand Above

- Right Hand Above

### Two-Hand Relationship

- Index Finger Distance

- Hands Crossed

- Right Index ↔ Left Index Distance

- Right Index ↔ Left Thumb Distance

- Right Index ↔ Left Line Distance

- Right Index Y-Line Progress

---

## Gesture Recognition

Supported Gestures

- Open Palm

- Fist

- Victory

- Thumbs Up

---

## Alphabet Recognition

Implemented

**26 / 26 Alphabets Completed**

### Static / Geometric Alphabets

- A

- B

- C

- D

- E

- F

- G

- K

- L

- M

- N

- O

- P

- Q

- R

- S

- T

- U

- V

- W

- X

- Z

### Motion / State-Based Alphabets

- H

- I

- J

- Y

### Recognition Capabilities

- Feature-Based Recognition

- Static Alphabet Recognition

- Motion-Based Recognition

- Temporal / State Recognition

- One-Hand Recognition

- Two-Hand Recognition

- Real-Capture Calibration

- Threshold-Based Recognition

- Detector Ordering

- Alphabet-Specific Rule System

---

# Version 1 Recognition Corrections

## I / L Recognition Conflict

I and L share a similar starting hand configuration.

The issue was solved using:

- Dedicated motion/state recognition

- More specific recognition conditions

- Correct detector ordering

- I detection before L detection

---

## K / P Recognition Conflict

P was initially being recognized as K.

The issue was solved by:

- Comparing actual captured feature values

- Refining K conditions

- Refining P conditions

- Using more specific geometric relationships

- Correct detector ordering

---

## T Recognition Correction

The initial T rule was based too heavily on theoretical geometry.

The rule was calibrated using actual captured feature values.

This improved recognition reliability for the real hand position.

---

## Q Recognition Correction

The Q rule existed but the detector was not calling detect_Q().

The detector originally followed:

P → R

instead of:

P → Q → R

The Q detector was integrated into the correct position.

The original index-finger distance threshold was also too restrictive for real captures.

The practical threshold was widened based on captured data.

The corrected Q rule successfully recognized 41 / 41 usable Q frames during validation.

---

# Recognition Pipeline

Camera

    │

    ▼

MediaPipe Hand Detection

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

    ▼

Feature Dictionary

    │

    ├──────────────┐
    ▼              ▼
Gesture Detector  Alphabet Detector
                       │
                       ├───────────────┐
                       ▼               ▼
                Static Recognition   Motion Recognition
                       │               │
                       └───────┬───────┘
                               ▼
                         Word Builder
                               │
                               ▼
                      Recognition Result
                               │
                               ▼
                        Display Output

---

# Recognition Architecture

The recognition system now uses two major recognition paths:

### Static Recognition

Used for alphabets whose recognition primarily depends on the geometric configuration of the hands and fingers.

The system evaluates:

- Finger States

- Finger Counts

- Touch Relationships

- Curvature

- Finger Angles

- Hand Position

- Hand Relationships

- Two-Hand Geometry

### Motion / Temporal Recognition

Used for alphabets where the movement or state transition of the hand is important.

Current motion/state alphabets:

- H

- I

- J

- Y

Motion recognition uses changes across frames rather than relying only on a single static frame.

---

# Development Roadmap

Sprint	Module	Status
Sprint 1	Development Environment	✅
Sprint 2	Camera Engine	✅
Sprint 3	Modular Architecture	✅
Sprint 4	Vision Engine	✅
Sprint 5	Finger Analysis	✅
Sprint 6	Gesture Recognition	✅
Sprint 7	Alphabet Framework	✅
Sprint 8	Feature Extraction Architecture	✅
Sprint 9	Geometry Engine	✅
Sprint 10	Feature Engine & Word Builder	✅
Sprint 11	Advanced Geometry & Alphabet Expansion	✅
Version 1	A–Z Alphabet Recognition	✅
Version 2	Recognition Robustness & Advanced Features	🚧
Version 2	Palm Orientation	⏳
Version 2	Hand Orientation	⏳
Version 2	Finger Direction	⏳
Version 2	Decision Engine	⏳
Version 2	Sentence Recognition	⏳
Version 2	Speech Generation	⏳
Future	Machine Learning Recognition	⏳

---

# Current Milestones

Completed

- ✅ Professional Project Structure

- ✅ Stable Development Environment

- ✅ Camera Engine

- ✅ Vision Engine

- ✅ Geometry Engine

- ✅ Feature Engine

- ✅ Gesture Recognition

- ✅ Alphabet Framework

- ✅ A–Z Alphabet Recognition

- ✅ Static Alphabet Recognition

- ✅ Motion / Temporal Alphabet Recognition

- ✅ Word Builder

- ✅ Real-Capture Rule Calibration

- ✅ Recognition Threshold Calibration

- ✅ Major V1 Recognition Conflicts Resolved

---

# Version 1 Completion

**Alphabet Recognition: 26 / 26**

All alphabet recognition rules required for Version 1 have been implemented and validated.

Static / Geometric

- A

- B

- C

- D

- E

- F

- G

- K

- L

- M

- N

- O

- P

- Q

- R

- S

- T

- U

- V

- W

- X

- Z

Motion / State

- H

- I

- J

- Y

Version 1 Recognition Status: 🟢 COMPLETE

---

# Current Stability

Environment

✅ Stable

Architecture

✅ Stable

Alphabet Recognition

✅ 26 / 26 Complete

Critical Bugs

None

Known Limitations

- Recognition thresholds are currently calibrated from real captures and may require further generalization.

- Some rules may still require improvement for different users, hand sizes, camera positions, lighting conditions, and hand orientations.

- Palm Orientation is not yet implemented.

- Hand Orientation is not yet implemented.

- Finger Direction features are not yet implemented.

- Version 1 is primarily geometry/rule based rather than machine-learning based.

---

# Future Enhancements

## Version 2

- Improve Recognition Robustness

- Improve Threshold Generalization

- Reduce False Positives

- Improve Multi-Hand Position Handling

- Palm Orientation

- Thumb Direction

- Hand Orientation

- Finger Direction

- Decision Engine

- Temporal Recognition Improvements

- Letter Confirmation

- Duplicate Detection Control

- Improve Word Builder

- Space Detection

- Backspace / Correction

- Word Completion

- Sentence Recognition

- Speech Output

---

## Future AI Development

- Dataset Development

- Machine Learning Classifier

- Model Training

- Model Evaluation

- Performance Optimization

- Real-Time ML Recognition

---

## Future Platforms

- Mobile Application

- Web Application

- Multi-language Support

---

# Learning Outcomes

## Software Engineering

- Modular Architecture

- Layered Architecture

- Feature Engineering

- Geometry Engine Design

- Debugging

- Refactoring

- Documentation

- Rule-Based System Design

- Real-Capture Calibration

- Threshold Calibration

- Recognition Pipeline Design

---

## Artificial Intelligence

- Computer Vision

- MediaPipe Hands

- Geometry-Based Recognition

- Feature Engineering

- Gesture Recognition

- Static Recognition

- Motion Recognition

- Temporal Recognition

- Real-Time Processing

---

## Professional Skills

- Software Design

- Engineering Workflow

- Testing

- Technical Documentation

- Project Planning

- Debugging Methodology

- Iterative Development

---

# Version 1 Development Lessons

- Theoretical geometry is not always sufficient for real-world recognition.

- Recognition rules should be calibrated using actual captured hand data.

- Similar hand configurations require highly specific conditions.

- Detector ordering can affect recognition results.

- Static and motion-based alphabets require different recognition strategies.

- Feature extraction should remain separate from alphabet-specific rules.

- Geometry calculations should remain reusable instead of being duplicated inside individual alphabet rules.

- Thresholds should be based on real capture ranges rather than arbitrary values.

- Every alphabet should be validated against actual camera input.

---

# Author

**Krishna Koushik**

AI Portfolio

Project-01

Sign Language Recognition

---

# Current Status

**Version:** **v1.3.0**

**Architecture:** 🟢 Stable

**Foundation:** ✅ Completed

**Recognition Version 1:** ✅ 26 / 26 Alphabets Completed

**Completed Sprint:** **Sprint 11**

**Current Phase:** **Version 2 – Recognition Robustness & Advanced Features**