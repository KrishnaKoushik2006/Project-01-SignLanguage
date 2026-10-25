# FEATURE LOG

---

Purpose

This document records every feature implemented in the Feature Engine.

The Feature Engine converts raw MediaPipe hand landmarks into reusable semantic computer vision features.

These features are used by:

- Gesture Recognition

- Alphabet Recognition

- Word Recognition

- Future Machine Learning Models

---

Feature Categories
Hand Presence
Finger State
Finger Count
Finger Touch
Finger Curvature
Finger Angles
Hand Relation
Two-Hand Relationship
Palm Orientation (Version 2)
Thumb Direction (Version 2)
Hand Orientation (Version 2)
Symmetry (Future)

---

Hand Presence

## left_hand

Meaning

True if the left hand is detected.

Used By

All two-hand alphabets.

Status

✅ Implemented

---

## right_hand

Meaning

True if the right hand is detected.

Used By

All two-hand alphabets.

Status

✅ Implemented

---

## both_hands

Meaning

True if both hands are detected simultaneously.

Used By

- A

- B

- H

- M

- N

- Q

- Future two-hand alphabets

Status

✅ Implemented

---

Finger State

## thumb_up

Meaning

Thumb is extended.

Status

✅ Implemented

---

## index_up

Meaning

Index finger is extended.

Status

✅ Implemented

---

## middle_up

Meaning

Middle finger is extended.

Status

✅ Implemented

---

## ring_up

Meaning

Ring finger is extended.

Status

✅ Implemented

---

## little_up

Meaning

Little finger is extended.

Status

✅ Implemented

---

Finger Count

## left_finger_count

Meaning

Number of raised fingers on the left hand.

Status

✅ Implemented

---

## right_finger_count

Meaning

Number of raised fingers on the right hand.

Status

✅ Implemented

---

Finger Touch

## thumb_touch_index

Meaning

Thumb tip touches index tip.

Status

✅ Implemented

---

## thumb_touch_middle

Meaning

Thumb tip touches middle tip.

Status

✅ Implemented

---

## thumb_touch_ring

Meaning

Thumb tip touches ring tip.

Status

✅ Implemented

---

## thumb_touch_little

Meaning

Thumb tip touches little tip.

Status

✅ Implemented

---

## index_touch_middle

Meaning

Index fingertip touches middle fingertip.

Status

✅ Implemented

---

## middle_touch_ring

Meaning

Middle fingertip touches ring fingertip.

Status

✅ Implemented

---

## ring_touch_little

Meaning

Ring fingertip touches little fingertip.

Status

✅ Implemented

---

## thumbs_touching

Meaning

Thumb tips of both hands are touching.

Used By

- Letter B

- Future two-hand alphabets

Status

✅ Implemented

---

Finger Curvature

## thumb_curled

Meaning

Thumb is curled.

Status

✅ Implemented

---

## index_curled

Meaning

Index finger is curled.

Status

✅ Implemented

---

## middle_curled

Meaning

Middle finger is curled.

Status

✅ Implemented

---

## ring_curled

Meaning

Ring finger is curled.

Status

✅ Implemented

---

## little_curled

Meaning

Little finger is curled.

Status

✅ Implemented

---

Finger Angles

## thumb_angle

Meaning

Angle formed by the thumb joints.

Status

✅ Implemented

---

## index_angle

Meaning

Angle formed by the index finger joints.

Status

✅ Implemented

---

## middle_angle

Meaning

Angle formed by the middle finger joints.

Status

✅ Implemented

---

## ring_angle

Meaning

Angle formed by the ring finger joints.

Status

✅ Implemented

---

## little_angle

Meaning

Angle formed by the little finger joints.

Status

✅ Implemented

---

Hand Relation

## wrist_distance

Meaning

Distance between the left and right wrists.

Status

✅ Implemented

---

## hands_close

Meaning

True if both hands are close together.

Status

✅ Implemented

---

Two-Hand Relationship

These features describe the geometric relationship between specific points of the two hands.

## hand_vertical_distance

Meaning

Vertical distance between the two hands.

Status

✅ Implemented

---

## left_hand_above

Meaning

True if the left hand is positioned above the right hand.

Status

✅ Implemented

---

## right_hand_above

Meaning

True if the right hand is positioned above the left hand.

Status

✅ Implemented

---

## index_fingers_distance

Meaning

Distance between the index fingers of the two hands.

Status

✅ Implemented

---

## hands_crossed

Meaning

Describes whether the two hands have crossed relative to their expected positions.

Status

✅ Implemented

---

## right_index_left_index_distance

Meaning

Distance between the right index finger and left index finger.

Status

✅ Implemented

---

## right_index_left_thumb_distance

Meaning

Distance between the right index finger and left thumb.

Status

✅ Implemented

---

## right_index_left_line_distance

Meaning

Geometric distance between the right index finger and the reference line formed by the left hand.

Status

✅ Implemented

---

## right_index_y_line_progress

Meaning

Measures the Y-axis positional relationship of the right index finger relative to the left-hand reference line.

Status

✅ Implemented

---

Motion / Temporal Recognition

Motion-based recognition is handled separately from purely static geometric features.

Used By

- H

- I

- J

- Y

Status

✅ Implemented

---

Alphabet Recognition Support

The Feature Engine currently provides the geometric and semantic features required for Version 1 alphabet recognition.

Implemented

- Letter A

- Letter B

- Letter C

- Letter D

- Letter E

- Letter F

- Letter G

- Letter H

- Letter I

- Letter J

- Letter K

- Letter L

- Letter M

- Letter N

- Letter O

- Letter P

- Letter Q

- Letter R

- Letter S

- Letter T

- Letter U

- Letter V

- Letter W

- Letter X

- Letter Y

- Letter Z

Status

✅ 26/26 Alphabets Supported

---

Planned Features

## Palm Orientation

- palm_front

- palm_back

- palm_left

- palm_right

Status

⏳ Version 2

---

## Thumb Direction

- thumb_left

- thumb_right

- thumbs_facing_each_other

Status

⏳ Version 2

---

## Hand Orientation

- vertical

- horizontal

- diagonal

Status

⏳ Version 2

---

## Hand Symmetry

- symmetric_pose

Status

⏳ Future

---

Current Statistics

Implemented Feature Categories

Hand Presence

3

Finger State

10

Finger Count

2

Finger Touch

15

Finger Curvature

10

Finger Angles

10

Hand Relation

2

Two-Hand Relationship

8

Motion / Temporal Recognition

Implemented

------------------------

Core Semantic Features

60+ Features

The Feature Engine now provides 60+ reusable semantic and geometric features for the Version 1 recognition system.

---

Current Version

Version

1.3.0

Recognition

Version 1 Completed

Sprint

10

Status

✅ Feature Engine Phase 1 Completed

---

Version 1 Completion

The Feature Engine successfully supports the complete Version 1 alphabet recognition system.

Implemented

- Static alphabet recognition

- Motion alphabet recognition

- Two-hand recognition

- Finger-state recognition

- Finger-count recognition

- Touch detection

- Curvature detection

- Finger-angle detection

- Hand relationship detection

- Two-hand geometric relationships

- Real-capture calibration

- Practical threshold calibration

Status

✅ Version 1 Completed

---

Next Milestone

Version 2

- Palm Orientation

- Thumb Direction

- Hand Orientation

- Improve Letter A

- Improve Letter B

- Improve recognition robustness

- Improve threshold generalization

- Reduce false positives

- Improve multi-hand position handling

- Improve temporal recognition

---

Notes

The Feature Engine is now the foundation of the Sign Language Recognition System.

All current Version 1 recognition modules use extracted semantic features rather than directly accessing MediaPipe landmarks.

The Feature Engine has evolved from basic finger-state detection into a reusable geometric feature system.

Version 1 established the complete A–Z recognition foundation.

Future development will expand the Feature Engine with orientation and directional features to improve recognition robustness and generalization.

The same feature architecture can later be reused by future Machine Learning models.