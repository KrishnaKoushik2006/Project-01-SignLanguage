# CHANGELOG

All notable changes to this project will be documented in this file.

The project follows Semantic Versioning.

---

# Version 0.1.0 - Project Initialization

## Added

- Created AI Portfolio workspace.
- Created Project-01-SignLanguage project.
- Added professional folder structure.
- Added README.md.
- Added requirements.txt.
- Added .gitignore.

## Folder Structure

- app/
- assets/
- config/
- datasets/
- docs/
- models/
- output/
- tests/
- utils/

## Documentation

Created

- PROJECT_OVERVIEW.md
- CHANGELOG.md
- TODO.md
- BUGS.md
- FEATURES.md
- ARCHITECTURE.md

## Status

✅ Project Initialized

---

# Version 0.1.1 - Development Environment

## Added

- Installed Python
- Installed Visual Studio Code
- Created Virtual Environment
- Activated Virtual Environment

## Installed Packages

- OpenCV
- MediaPipe
- NumPy

## Status

✅ Development Environment Ready

---

# Version 0.1.2 - Camera Engine

## Added

- Webcam Engine
- Live Video Stream
- Keyboard Exit
- Camera Cleanup

## Status

✅ Camera Engine Completed

---

# Version 0.1.3 - Modular Architecture

## Added

- camera/
- vision/

Created

- camera.py
- hand_detector.py

## Refactored

- Camera logic moved from main.py
- Simplified application flow

## Status

✅ Modular Architecture Ready

---

# Version 0.1.4 - Environment Debugging

## Fixed

- Python 3.14 Compatibility
- MediaPipe Import Errors
- Virtual Environment Problems
- Package Version Conflicts

## Learned

- Virtual Environments
- Dependency Management
- Debugging Tracebacks

## Status

✅ Stable Environment

---

# Version 0.2.0 - Python Migration

## Changed

Migrated

Python 3.14

↓

Python 3.12

## Installed

- MediaPipe 0.10.21
- OpenCV
- NumPy

## Fixed

MediaPipe compatibility.

## Status

✅ Stable Development Platform

---

# Version 0.3.0 - Vision Engine

## Added

- MediaPipe Hands
- 21 Landmark Detection
- Two Hand Detection
- Skeleton Drawing
- Real-time Tracking

## Status

✅ Vision Engine Completed

---

# Version 0.4.0 - Gesture Recognition

## Added

Gesture Detector

Supported Gestures

- Open Palm
- Fist
- Victory
- Thumbs Up

## Status

✅ Gesture Recognition Completed

---

# Version 0.5.0 - Finger Analysis

## Added

Finger Counter

Implemented

- Finger States
- Finger Count
- Left Hand Support
- Right Hand Support

## Status

✅ Finger Analysis Completed

---

# Version 0.6.0 - Initial Alphabet Recognition

## Added

Alphabet Detector

Implemented

- ISL Alphabet Framework
- Real-time Alphabet Display

## Status

✅ Alphabet Framework Created

---

# Version 1.0.0 - Feature Extraction Architecture

## Major Update

Introduced Feature-Based Recognition.

## Added

### New Modules

- FeatureExtractor
- HandUtils
- PoseUtils
- AlphabetRules

### New Features

- Left Hand Detection
- Right Hand Detection
- Finger States
- Finger Counts
- Wrist Distance
- Hand Proximity

## Refactored

- HandDetector
- main.py
- AlphabetDetector

## Status

✅ Sprint 8 Completed

---

# Version 1.1.0 - Geometry Engine (Sprint 9)

## Major Update

Introduced reusable Geometry Engine.

## Added

### New Module

- geometry.py

### Geometry Functions

- Distance Calculation
- Touch Detection
- Curvature Detection
- Angle Calculation
- Finger Angle Calculation

### Finger Angle Features

- Thumb Angle
- Index Angle
- Middle Angle
- Ring Angle
- Little Angle

### Curvature Features

- Thumb Curled
- Index Curled
- Middle Curled
- Ring Curled
- Little Curled

## Refactored

- PoseUtils

PoseUtils is now only a Landmark Wrapper.

All geometry calculations were moved into Geometry Engine.

## Status

✅ Geometry Engine Completed

---

# Version 1.2.0 - Feature Engine Expansion (Sprint 10)

## Major Update

Completed Feature Engine Phase 1.

## Added

### Hand Features

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

### Hand Relation

- Wrist Distance
- Hands Close

### Alphabet Recognition

Implemented

- Letter A (Version 1)
- Letter B (Version 1)

### Word Recognition

Added

- Word Builder
- Duplicate Character Prevention

## Refactored

- FeatureExtractor
- AlphabetDetector
- AlphabetRules

Architecture is now

Camera

↓

MediaPipe

↓

PoseUtils

↓

Geometry

↓

FeatureExtractor

↓

Recognition Engine

## Status

✅ Sprint 10 Completed

---

# Current Project Status

| Module | Status |
|---------|--------|
| Development Environment | ✅ Completed |
| Camera Engine | ✅ Completed |
| MediaPipe Integration | ✅ Completed |
| Hand Detection | ✅ Completed |
| Left / Right Hand Detection | ✅ Completed |
| Geometry Engine | ✅ Completed |
| Pose Wrapper | ✅ Completed |
| Finger Counter | ✅ Completed |
| Feature Engine | ✅ Completed |
| Gesture Recognition | ✅ Completed |
| Alphabet Framework | ✅ Completed |
| Letter A | ✅ Version 1 |
| Letter B | ✅ Version 1 |
| Word Builder | ✅ Completed |
| Palm Orientation | ⏳ Sprint 11 |
| Thumb Direction | ⏳ Sprint 11 |
| Hand Orientation | ⏳ Sprint 11 |
| Alphabet C-Z | ⏳ Sprint 11 |
| Sentence Recognition | ⏳ Sprint 12 |
| Speech Output | ⏳ Sprint 12 |
| Machine Learning Model | ⏳ Version 2 |

---

# Current Version

**Version:** **1.2.0**

**Architecture:** Stable

**Foundation:** Completed ✅

**Current Sprint:** Sprint 10 ✅

**Next Sprint:** Sprint 11 – Advanced Geometry & Alphabet Expansion

---

# Milestone Progress

## Milestone 1 — Foundation

- ✅ Camera Engine
- ✅ Vision Engine
- ✅ Gesture Recognition
- ✅ Geometry Engine
- ✅ Feature Engine
- ✅ Alphabet Framework
- ✅ Word Builder

Status

**100% Completed**

---

## Milestone 2 — Recognition Engine

Upcoming

- Improve A
- Improve B
- Alphabet C-Z
- Decision Engine

Status

**Ready to Begin**