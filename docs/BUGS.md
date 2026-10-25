# BUGS

---

# Bug Tracking

This document records all identified bugs during development, their causes, solutions, and current status.

---

# Resolved Bugs

## Bug 001

### Title

MediaPipe Solutions Module Missing

**Status**

✅ Resolved

**Problem**

```
AttributeError:
module 'mediapipe' has no attribute 'solutions'
```

**Cause**

MediaPipe 0.10.35 was incompatible with Python 3.14.

**Solution**

- Installed Python 3.12
- Created a new virtual environment
- Installed MediaPipe 0.10.21

---

## Bug 002

### Title

Incorrect MediaPipe Package Structure

**Status**

✅ Resolved

**Problem**

MediaPipe Solutions API was unavailable.

**Cause**

Installed package did not expose the required `solutions` module.

**Solution**

Installed a compatible MediaPipe version.

---

## Bug 003

### Title

Virtual Environment Version Mismatch

**Status**

✅ Resolved

**Problem**

Existing virtual environment was created using Python 3.14.

**Cause**

Python version mismatch after changing interpreter.

**Solution**

- Deleted the old virtual environment
- Recreated the environment using Python 3.12

---

## Bug 004

### Title

FeatureExtractor - PoseUtils Initialization Error

**Status**

✅ Resolved

**Problem**

```
TypeError:
PoseUtils.__init__() missing 1 required positional argument: 'landmarks'
```

**Cause**

`PoseUtils` was instantiated without MediaPipe landmarks.

**Solution**

- Initialize PoseUtils only after hand detection.
- Pass `hand.landmark` while creating PoseUtils.

---

## Bug 005

### Title

Architecture Mismatch During Feature Engine Integration

**Status**

✅ Resolved

**Problem**

`HandDetector` returned only MediaPipe results while the Feature Engine required separated left and right hands.

**Cause**

Old architecture was still being used.

**Solution**

Updated `HandDetector` to return

- Processed Frame
- MediaPipe Results
- Left Hand
- Right Hand

---

## Bug 006

### Title

Feature Extraction Integration Failure

**Status**

✅ Resolved

**Problem**

`main.py` was still using FingerCounter directly.

**Cause**

Architecture changed from finger-based recognition to feature-based recognition.

**Solution**

Updated `main.py`

- Create FeatureExtractor
- Extract semantic features
- Display extracted features
- Pass features to Alphabet Detector

---

## Bug 007

### Title

PoseUtils Became Too Large

**Status**

✅ Resolved

**Problem**

`PoseUtils` contained landmark storage, geometry calculations and touch detection.

**Cause**

Violation of the Single Responsibility Principle.

**Solution**

Introduced `geometry.py`.

Architecture became

```
PoseUtils
↓

Geometry

↓

FeatureExtractor
```

---

## Bug 008

### Title

Geometry Logic Mixed With Landmark Wrapper

**Status**

✅ Resolved

**Problem**

Distance, touch and angle calculations were implemented inside `PoseUtils`.

**Cause**

Geometry functions were not isolated.

**Solution**

Created a dedicated `Geometry` engine.

Moved

- Distance
- Touch Detection
- Finger Angles
- Curvature

to `geometry.py`.

---

## Bug 009

### Title

Alphabet Detector Interface Mismatch

**Status**

✅ Resolved

**Problem**

Alphabet detector was still expecting

```
detect_alphabet(hand_landmarks, fingers)
```

after introducing the Feature Engine.

**Cause**

Old detector interface.

**Solution**

Updated to

```
detect_alphabet(features)
```

---

# Known Limitations

These are expected limitations and are **not software bugs**.

---

## Limitation 001

### Thumb Detection

Current thumb detection uses a simple X-coordinate comparison.

Impact

- Different hand orientations
- Rotated hands
- Mirrored poses

may produce incorrect thumb states.

Planned Improvement

- Palm Orientation
- Thumb Direction
- Hand Orientation

---

## Limitation 002

### Alphabet A

Current implementation of Alphabet A is Version 1.

Current Logic

- Both Hands
- One Thumb Up
- Thumb Tips Not Touching

Issue

A normal "two thumbs up" gesture may also satisfy the rule.

Planned Improvement

Use

- Thumb Direction
- Palm Orientation
- Hand Orientation

during Sprint 11.

---

## Limitation 003

### Alphabet B

Current implementation depends on

```
thumbs_touching
```

Issue

Recognition accuracy depends on the touch threshold.

Planned Improvement

Replace touch-only logic with

- Palm Orientation
- Thumb Direction
- Finger Angles

---

## Limitation 004

### Geometry Engine

Current Geometry Engine contains

- Distance
- Touch
- Curvature
- Finger Angles

Missing Features

- Palm Orientation
- Finger Direction
- Hand Orientation
- Symmetry

These will be added during Sprint 11.

---

# Active Bugs

None

---

# Future Bug Tracking

| ID | Title | Status | Cause | Solution |
|----|-------|--------|-------|----------|
| - | No Active Bugs | - | - | - |

---

# Bug Statistics

| Category | Count |
|----------|------:|
| Total Bugs Identified | 9 |
| Bugs Resolved | 9 |
| Active Bugs | 0 |
| Known Limitations | 4 |

---

# Current Status

**Bug Status:** 🟢 Stable

Sprint 10 completed successfully.

The application is architecturally stable.

Future work focuses on improving recognition accuracy through additional geometric features rather than fixing software defects.

Current Priority

- Sprint 11
- Geometry Improvements
- Alphabet Accuracy
- A–Z Recognition