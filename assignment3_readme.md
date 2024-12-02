# Calendar Booking System

This project implements a calendar system where events can be booked without causing double bookings. The system ensures that no two events overlap in time. The `Calendar` class manages the insertion of events using a binary tree structure.

## Changes Made

### 1. **Fixed Event Overlap Detection**
   - **Issue**: The original `insert` method used incorrect logic to check for overlaps, potentially allowing double bookings.
   - **Fix**: Updated the `insert` method to explicitly check for overlaps using the condition:
     ```python
     if node.start < self.end and node.end > self.start:
         return False  # Overlap detected
     ```
     This ensures that an event will not be inserted if it overlaps with an existing event.

### 2. **Corrected Tree Insertion Logic**
   - **Issue**: The original tree insertion logic used faulty conditions to decide whether to insert into the left or right subtree.
   - **Fix**: The new insertion logic ensures:
     - If the new event ends before the current event starts, it is inserted in the left subtree.
     - If the new event starts after the current event ends, it is inserted in the right subtree.
   - This guarantees proper sorting and non-overlapping insertion.

### 3. **Return `False` on Double Booking**
   - **Issue**: The original code did not correctly handle situations where an event could not be added due to overlaps.
   - **Fix**: The `insert` method now returns `False` if an event cannot be booked due to overlap, which is propagated back to the `book` method to signal failure.

## Example Usage

```python
calendar = Calendar()
print(calendar.book(5, 10))  # True
print(calendar.book(8, 13))  # False (overlap with [5, 10])
print(calendar.book(10, 15)) # True (no overlap)

