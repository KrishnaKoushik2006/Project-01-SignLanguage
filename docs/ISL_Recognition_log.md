# ISL RECOGNITION LOG

Project

Project-01 - Sign Language Recognition

Version: 2.1.0

---

Purpose

This document records the recognition rules, engineering decisions, feature requirements, testing results, and implementation progress for the Indian Sign Language (ISL) Recognition Engine.

It serves as the official reference for every implemented alphabet and ensures that all recognition rules follow a consistent, feature-based approach.

---

Recognition Pipeline
Camera

↓

MediaPipe Hand Detection

↓

21 Hand Landmarks

↓

Left / Right Hand Identification

↓

PoseUtils

↓

Geometry Engine

↓

Feature Extractor

↓

Feature Dictionary

↓

Alphabet Rules

↓

Alphabet Detector

↓

Word Builder

↓

Recognition Result

---

Recognition Philosophy

The recognition engine must never use raw MediaPipe landmarks directly.

Instead, every alphabet should be recognized using semantic features extracted by the Feature Engine.

Advantages

- Cleaner code

- Easier debugging

- Better maintainability

- Reusable features

- Easier Machine Learning integration

---

Current Feature Set
Hand Presence

- Left Hand

- Right Hand

- Both Hands

---

Finger Features

- Thumb State

- Index State

- Middle State

- Ring State

- Little State

- Left Finger Count

- Right Finger Count

---

Touch Features

- Thumb ↔ Index

- Thumb ↔ Middle

- Thumb ↔ Ring

- Thumb ↔ Little

- Index ↔ Middle

- Middle ↔ Ring

- Ring ↔ Little

- Thumb ↔ Thumb

---

Curvature Features

- Thumb Curled

- Index Curled

- Middle Curled

- Ring Curled

- Little Curled

---

Finger Angles

- Thumb Angle

- Index Angle

- Middle Angle

- Ring Angle

- Little Angle

---

Hand Relation

- Wrist Distance

- Hands Close

---

Two-Hand Relationship

- Hand Vertical Distance

- Left Hand Above

- Right Hand Above

- Index Fingers Distance

- Hands Crossed

- Right Index ↔ Left Index Distance

- Right Index ↔ Left Thumb Distance

- Right Index ↔ Left Line Distance

- Right Index Y-Line Progress

---

Motion / Temporal Recognition

- Motion-Based Recognition

- Temporal State Recognition

---

Planned Features (Version 2)
Palm Orientation

- Palm Front

- Palm Back

- Palm Left

- Palm Right

---

Thumb Direction

- Thumb Left

- Thumb Right

- Thumbs Facing Each Other

---

Hand Orientation

- Vertical

- Horizontal

- Diagonal

---

Future

- Finger Direction

- Hand Symmetry

- Advanced Motion Features

- Dynamic Gestures

---

Alphabet Progress
Letter	Type	Hands	Status
A	Static	Two	✅ Version 1
B	Static	Two	✅ Version 1
C	Static	One	✅ Version 1
D	Static	One	✅ Version 1
E	Static	One	✅ Version 1
F	Static	One	✅ Version 1
G	Static	One	✅ Version 1
H	Dynamic	Two	✅ Version 1
I	Dynamic	One	✅ Version 1
J	Dynamic	One	✅ Version 1
K	Static	One	✅ Version 1
L	Static	One	✅ Version 1
M	Static	Two	✅ Version 1
N	Static	Two	✅ Version 1
O	Static	One	✅ Version 1
P	Static	One	✅ Version 1
Q	Static	Two	✅ Version 1
R	Static	One	✅ Version 1
S	Static	One	✅ Version 1
T	Static	One	✅ Version 1
U	Static	One	✅ Version 1
V	Static	One	✅ Version 1
W	Static	One	✅ Version 1
X	Static	One	✅ Version 1
Y	Dynamic	One	✅ Version 1
Z	Static	One	✅ Version 1

---

Recognition Checklist

Every alphabet must answer the following questions before implementation.

Basic Information

- Static or Dynamic?

- One Hand or Two Hands?

- Difficulty?

---

Finger Configuration

- Thumb State

- Index State

- Middle State

- Ring State

- Little State

- Finger Count

---

Touch Features

- Thumb ↔ Finger

- Finger ↔ Finger

- Thumb ↔ Thumb

---

Geometry Features

- Finger Angles

- Finger Curvature

---

Hand Configuration

- Palm Orientation

- Hand Orientation

- Thumb Direction

- Symmetry

---

Validation

- Live Tested

- False Positive Checked

- False Negative Checked

- Stable Detection

---

Engineering Rules

- Never guess recognition rules.

- Every alphabet must follow an official ISL reference.

- Every rule must be tested using the webcam.

- Prefer semantic features over raw landmarks.

- Keep geometry calculations inside Geometry Engine.

- Keep recognition logic inside Alphabet Rules.

- Recognition rules should remain simple and readable.

- Improve the feature engine instead of adding complex recognition logic.

- Validate thresholds using actual captured feature values.

- Check detector ordering when similar alphabets can conflict.

---

Alphabet Template
Letter

A

---

Type

Static

---

Hands

One / Two

---

Difficulty

Easy / Medium / Hard

---

Finger States

- Thumb

- Index

- Middle

- Ring

- Little

---

Finger Count

-

---

Touch Features

-

---

Curvature

-

---

Finger Angles

-

---

Palm Orientation

-

---

Thumb Direction

-

---

Recognition Rule

(To be implemented)

---

Testing

☐ Not Tested

☐ Tested

☐ Verified

---

Completed Alphabets
Letter A
Type

Static

Hands

Two

Finger Count

1 per hand

Current Features Used

- Both Hands

- Left Finger Count

- Right Finger Count

- Left Thumb Up

- Right Thumb Up

- Thumbs Not Touching

Current Status

✅ Version 1

Known Limitation

A normal "two thumbs up" gesture may also be recognized as A.

Planned Improvement

- Thumb Direction

- Palm Orientation

- Hand Orientation

---

Letter B
Type

Static

Hands

Two

Finger Count

1 per hand

Current Features Used

- Both Hands

- Left Finger Count

- Right Finger Count

- Thumbs Touching

Current Status

✅ Version 1

---

Version 1 Recognition Corrections

During Version 1 development, several alphabet-specific recognition issues were identified and resolved through real-capture testing.

Major corrections included

- I/L Recognition Conflict

- K/P Recognition Conflict

- T Recognition Rule Mismatch

- Q Detector Integration

- Q Index Distance Threshold

- Detector Ordering

- Feature Condition Calibration

- Practical Threshold Calibration

I/L Conflict

I and L shared a similar starting hand configuration.

Resolution

- Dedicated motion detection for I

- Detector ordering correction

- I checked before L

K/P Conflict

P was initially detected as K.

Resolution

- Compared actual captured feature values

- Added distinguishing conditions

- Corrected K/P rules

- Corrected detector ordering

T Correction

T was not reliably recognized using the original theoretical conditions.

Resolution

- Inspected actual captured feature values

- Adjusted T rule

- Re-tested using actual captures

Q Correction

Q initially returned Unknown because detect_Q() was not integrated into the detector sequence.

Resolution

P

↓

Q

↓

R

The Q index distance threshold was also adjusted from

0.12 - 0.28

to

0.12 - 0.40

The corrected Q rule recognized all 41 usable tested Q frames.

---

Recognition Accuracy Notes

Current engine uses handcrafted feature rules.

Current strengths

- Modular

- Easy to debug

- Expandable

- Feature-based

- Real-capture calibrated

Current Version 1 limitations

- No palm orientation

- No thumb direction

- No hand orientation

- No confidence score

- No machine learning classifier

- Thresholds are currently calibrated for validated capture conditions

---

Current Engine Status
Completed

- Camera Engine

- MediaPipe Integration

- Hand Detection

- Left / Right Hand Detection

- Geometry Engine

- Feature Engine

- Gesture Recognition

- Alphabet Framework

- Letter A (Version 1)

- Letter B (Version 1)

- Letters C–Z (Version 1)

- Static Alphabet Recognition

- Motion Alphabet Recognition

- Two-Hand Recognition

- Real-Capture Calibration

- Threshold Calibration

- Word Builder

---

Version 1 Completion

The Version 1 recognition engine has successfully implemented all 26 alphabets.

Alphabet Status

26/26 Completed ✅

Recognition Types

- Static Recognition

- Motion Recognition

- Two-Hand Recognition

The Version 1 system is now considered the stable baseline for future development.

---

Version 2 Roadmap

- Thumb Direction

- Palm Orientation

- Hand Orientation

- Finger Direction

- Improve Letter A

- Improve Letter B

- Improve Recognition Robustness

- Improve Threshold Generalization

- Reduce False Positives

- Improve Multi-Hand Position Handling

- Improve Temporal Recognition

- Recognition Decision Engine

- Letter Confirmation

- Word Builder Improvements

---

Current Version

Version: 2.1.0

Completed Sprint: Sprint 10

Alphabet Recognition: 26/26 Completed ✅

Recognition Version: Version 1 Completed

Status: 🟢 Stable Foundation

The recognition engine is now fully feature-based and has completed the Version 1 A–Z recognition milestone.

Version 2 will focus on improving geometric robustness, recognition accuracy, threshold generalization, and temporal recognition.