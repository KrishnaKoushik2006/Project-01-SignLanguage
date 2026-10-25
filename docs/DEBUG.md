# DEBUG GUIDE

This document records important debugging sessions, identified issues, solutions, and lessons learned throughout the development of Project-01 - Sign Language Recognition.

---

# Debugging Workflow

Whenever an issue occurs, follow this process:

Read the complete error message.
Identify the file and line number.
Understand the root cause before modifying code.
Apply the smallest possible fix.
Test the solution.
Verify that existing functionality still works.
Document the issue and its solution.

---

# Debug Session 001

## Error

AttributeError:

module 'mediapipe' has no attribute 'solutions'

## Investigation

- Verified Python version

- Verified Virtual Environment

- Verified MediaPipe installation

- Compared MediaPipe versions

## Root Cause

Python 3.14 was incompatible with the installed MediaPipe version.

## Resolution

- Installed Python 3.12

- Created a new Virtual Environment

- Installed MediaPipe 0.10.21

## Result

✅ Resolved

## Lessons Learned

- Always verify package compatibility.

- Prefer stable versions over the latest releases.

- Isolate every project using Virtual Environments.

---

# Debug Session 002

## Error

TypeError:

PoseUtils.init()

missing 1 required positional argument: 'landmarks'

## Investigation

- Checked traceback

- Reviewed FeatureExtractor

- Inspected PoseUtils constructor

## Root Cause

PoseUtils requires MediaPipe landmarks during initialization.

## Resolution

Instantiate PoseUtils only after hand landmarks are available.

## Result

✅ Resolved

## Lessons Learned

- Understand constructor requirements.

- Never instantiate objects without required dependencies.

---

# Debug Session 003

## Issue

FeatureExtractor could not separate left and right hands.

## Investigation

- Reviewed HandDetector

- Verified MediaPipe handedness

- Compared detector output with FeatureExtractor requirements

## Root Cause

HandDetector returned only MediaPipe results.

## Resolution

HandDetector now returns

- Processed Frame

- MediaPipe Results

- Left Hand

- Right Hand

## Result

✅ Resolved

## Lessons Learned

- Module outputs should match consumer requirements.

- Keep interfaces synchronized after architectural changes.

---

# Debug Session 004

## Issue

main.py became incompatible after introducing FeatureExtractor.

## Investigation

- Reviewed execution pipeline

- Tested module communication

- Verified feature extraction

## Root Cause

Application still used FingerCounter directly.

## Resolution

Refactored main.py to

- Use FeatureExtractor

- Display extracted features

- Pass feature dictionary to Alphabet Detector

## Result

✅ Resolved

---

# Debug Session 005

## Issue

Alphabet A stopped working after Feature Engine refactoring.

## Investigation

- Verified FingerCounter output

- Verified FeatureExtractor

- Compared extracted features with AlphabetRules

- Tested feature dictionary

## Root Cause

AlphabetDetector was still using the previous interface instead of the new feature dictionary.

## Resolution

Updated AlphabetDetector to

detect_alphabet(features)

instead of

detect_alphabet(hand_landmarks, fingers)

## Result

✅ Resolved

## Lessons Learned

- During architecture changes, update every dependent module.

- Interface changes should be propagated throughout the project.

---

# Debug Session 006

## Issue

Alphabet B was always detected as Alphabet A.

## Investigation

- Compared official ISL alphabet chart

- Displayed extracted features

- Compared A and B feature values

## Root Cause

Recognition rules only checked

- Finger Count

- Thumb State

Both A and B produced identical feature sets.

## Resolution

Introduced a new feature

thumbs_touching

using Geometry Engine.

Recognition now distinguishes

Thumbs Touching

↓

Letter B

## Result

✅ Resolved

## Lessons Learned

- Debug using feature values rather than guessing rules.

- Introduce reusable features instead of adding complex conditions.

---

# Debug Session 007

## Issue

PoseUtils became too large.

## Investigation

Reviewed responsibilities.

Found

- Landmark storage

- Distance calculations

- Touch detection

- Finger angles

inside a single class.

## Root Cause

Violation of Single Responsibility Principle.

## Resolution

Created

geometry.py

Moved

- Distance

- Touch Detection

- Finger Angles

- Curvature

into Geometry Engine.

PoseUtils now acts only as a Landmark Wrapper.

## Result

✅ Resolved

## Lessons Learned

- Separate data from mathematical computations.

- Small focused modules are easier to maintain.

---

# Debug Session 008

## Issue

False positives while recognizing Alphabet A.

## Investigation

Compared

- Official ISL A

- Two Thumbs Up gesture

Both produced almost identical features.

## Root Cause

Current feature set cannot distinguish thumb direction.

## Current Status

Expected Limitation

Not considered a software bug.

## Planned Improvement

Add

- Thumb Direction

- Palm Orientation

- Hand Orientation

These features will improve recognition accuracy.

## Result

⏳ Planned Improvement

---

# Debug Session 009

## Issue

Alphabet I was being confused with Alphabet L.

## Investigation

- Compared the finger-state conditions of I and L.

- Tested the actual captured hand configuration.

- Reviewed Alphabet Detector ordering.

- Compared static configuration with motion behaviour.

## Root Cause

I and L shared a similar starting hand configuration.

Both could satisfy

- Thumb Up

- Index Up

- Middle Down

- Ring Down

- Little Down

The detector therefore needed additional motion/state information.

## Resolution

- Added dedicated motion detection for I.

- Changed detector ordering.

- Checked I before L.

- Used motion/state behaviour to distinguish I from L.

## Result

✅ Resolved

## Lessons Learned

- Similar gestures may require temporal information.

- Detector ordering can affect recognition results.

- Static finger states are not always sufficient for motion-based alphabets.

---

# Debug Session 010

## Issue

Alphabet P was being detected as Alphabet K.

## Investigation

- Captured K and P separately.

- Compared extracted feature values.

- Compared K and P rule conditions.

- Reviewed Alphabet Detector ordering.

## Root Cause

K and P had overlapping geometric and finger-state conditions.

The K rule was matching before the detector reached P.

## Resolution

- Added more specific distinguishing conditions.

- Corrected K and P rules.

- Corrected detector ordering.

- Tested both signs using actual captures.

## Result

✅ Resolved

## Lessons Learned

- Similar alphabets require carefully selected distinguishing features.

- Rule ordering is part of the recognition system.

- Real captured feature values are more reliable than theoretical assumptions.

---

# Debug Session 011

## Issue

Alphabet T was not reliably recognized.

## Investigation

- Captured the T sign.

- Displayed extracted feature values.

- Compared actual values with the existing T rule.

- Identified differences between theoretical geometry and captured geometry.

## Root Cause

The original T rule was too dependent on expected theoretical geometry.

The actual captured feature values were different.

## Resolution

- Inspected real capture values.

- Adjusted the T rule.

- Re-tested the corrected rule.

## Result

✅ Resolved

## Lessons Learned

- Recognition rules must be calibrated using actual captures.

- Theoretical geometry should be treated as a starting point rather than the final threshold.

---

# Debug Session 012

## Issue

Alphabet Q returned Unknown even though a Q rule existed.

## Investigation

- Verified Q rule inside AlphabetRules.

- Verified that detect_Q() existed.

- Reviewed AlphabetDetector detection sequence.

- Checked the transition between P and R.

## Root Cause

detect_Q() was implemented but was not being called by AlphabetDetector.

The detector moved directly from

P

↓

R

Therefore the Q rule was never reached.

## Resolution

Added Q detection between P and R.

P

↓

Q

↓

R

## Result

✅ Resolved

## Lessons Learned

- A correctly implemented function is useless if it is not integrated into the execution path.

- Always verify both rule implementation and detector integration.

---

# Debug Session 013

## Issue

Q recognition remained unreliable after integrating the Q detector.

## Investigation

- Tested the corrected Q detector using actual captured frames.

- Displayed the Q feature values.

- Checked the index-finger distance condition.

- Compared the configured threshold with actual capture values.

## Root Cause

The original Q index-finger distance threshold was

0.12 - 0.28

Actual Q captures produced larger distances.

Some valid frames reached approximately

0.31.

Therefore valid Q frames were being rejected.

## Resolution

Changed the practical Q index-finger distance range to

0.12 - 0.40

Then re-tested the rule against the captured Q data.

## Result

✅ Resolved

The corrected Q rule recognized all 41 usable tested Q frames.

## Lessons Learned

- Thresholds must be based on real captured data.

- A theoretically reasonable threshold can still reject valid real-world input.

- Always test multiple frames instead of validating against a single frame.

---

# Debug Session 014

## Issue

Version 1 alphabet recognition required repeated rule corrections and calibration.

## Investigation

Reviewed the complete A–Z recognition system.

Tested

- Static alphabets

- Motion alphabets

- Two-hand alphabets

- Similar hand configurations

- Detector ordering

- Feature conditions

- Practical thresholds

## Root Cause

Several Version 1 rules were initially based on theoretical geometry and basic feature combinations.

Real captures revealed differences in

- Hand position

- Finger configuration

- Curvature

- Finger angles

- Touch relationships

- Two-hand relationships

- Practical distances

## Resolution

Performed real-capture calibration across the alphabet system.

Corrected

- I/L recognition

- K/P recognition

- T recognition

- Q integration

- Q threshold

- Detector ordering

- Feature conditions

## Result

✅ Version 1 Completed

All 26 alphabets are now implemented and recognized under the validated Version 1 capture and rule conditions.

## Lessons Learned

- Real-capture testing is essential.

- Feature values should drive rule development.

- Static and motion gestures require different recognition strategies.

- Similar gestures require carefully ordered and specific rules.

- Threshold calibration is an important part of geometric recognition.

General Debugging Tips

- Read the complete traceback.

- Never guess the cause.

- Verify the feature dictionary.

- Test one change at a time.

- Keep modules independent.

- Refactor only after understanding the problem.

- Compare actual captured values with expected values.

- Test recognition rules against multiple frames.

- Check detector ordering when similar alphabets conflict.

- Document every debugging session.

---

Debugging Tools

- Python Tracebacks

- VS Code Debugger

- MediaPipe Landmarks

- OpenCV Live Display

- Feature Overlay

- Geometry Engine

- Feature Dictionary

- Real-Capture Testing

---

Current Status
Category	Status
Critical Bugs	None
Active Bugs	None
Debug Sessions	14
Architecture	Stable
Feature Engine	Stable
Geometry Engine	Stable
Alphabet Recognition	26/26 Completed
Version 1	✅ Completed

---

Future Improvements

- Logging System

- Exception Logging

- Unit Testing

- Integration Testing

- Performance Profiling

- Automated Recognition Testing

- Multi-Frame Validation

- Recognition Confidence

- Better Threshold Generalization

---

Version 1 Debugging Summary

Major debugging achievements

- Resolved MediaPipe compatibility issues.

- Stabilized the Python development environment.

- Corrected FeatureExtractor integration.

- Separated left and right hand data.

- Refactored PoseUtils.

- Introduced Geometry Engine.

- Migrated to Feature-Based Recognition.

- Added reusable geometric features.

- Added Thumb-to-Thumb Touch Detection.

- Resolved I/L recognition conflict.

- Resolved K/P recognition conflict.

- Corrected T recognition.

- Integrated Q detection.

- Corrected Q threshold.

- Improved detector ordering.

- Calibrated alphabet rules using real captured data.

- Completed A–Z recognition.

Status

🟢 Stable

Version 1 debugging is complete.

Future debugging will focus primarily on recognition robustness, threshold generalization, false-positive reduction, temporal recognition, and Version 2 improvements rather than major architectural issues.