# 🧪 Digital Notes Management System — Test Cases & QA Report

Welcome to the **Test Cases and Quality Assurance Documentation** for the **Digital Notes Management System**. This document outlines all functional test scenarios, test objectives, inputs, expected vs. actual results, and visual terminal execution evidence.

---

## 📋 System Overview

The **Digital Notes Management System** is a command-line interface (CLI) Python application designed for CRUD operations on personal notes with flat-file persistence.

- **Primary Program File:** `main.py`
- **Data Storage:** `notes.txt` (Format: `ID|Title|Content`)
- **Execution Command:** `python3 main.py`
- **Supported Operations:**
  1. `1. Add Notes` (Auto-increments `N<number>`, validates non-empty title)
  2. `2. View All Notes` (Formatted list display)
  3. `3. Search Notes` (Case-insensitive substring search in title & content)
  4. `4. Edit Notes` (Update existing note title and content by ID)
  5. `5. Delete Notes` (Delete note by ID and display remaining count)
  6. `6. Exit` (Graceful termination)

---

## 📊 Test Execution Summary Matrix

| Test Case ID | Test Case Title | Target Module | Input Test Data | Expected Output | Actual Output | Status |
| :--- | :--- | :--- | :--- | :--- | :--- | :---: |
| **TC-01** | [Add Note & Validation](./testcase1.md) | `add_note()` | Choice: `1`<br>Title: `Python Loops`<br>Content: `Learn for and while loops` | Note saved with ID (`N8`) and validation error for empty title | As Expected | `PASS` ✅ |
| **TC-02** | [View All Notes](./testcase2.md) | `view_notes()` | Choice: `2` | Formatted list displaying ID, Title, and Content for all notes | As Expected | `PASS` ✅ |
| **TC-03** | [Search Notes](./testcase3.md) | `search_notes()` | Choice: `3`<br>Keyword: `python` / `react` | Matching notes displayed; "Note not found." on non-match | As Expected | `PASS` ✅ |
| **TC-04** | [Edit & Delete Notes](./testcase4.md) | `edit_note()` & `delete_note()` | Choice: `4` (Edit `N4`)<br>Choice: `5` (Delete `N7`) | Note updated successfully; Note deleted and remaining count shown | As Expected | `PASS` ✅ |

---

## 📂 Test Cases Directory Index

Click any link below to view the detailed specification, test steps, input logs, and visual screenshots for each test case:

1. **[Test Case 1: Add Note (Option 1) & Validation](./testcase1.md)**
   - Tests auto-generating note IDs and non-empty title validation.
2. **[Test Case 2: View All Notes (Option 2)](./testcase2.md)**
   - Tests loading and formatting records from `notes.txt`.
3. **[Test Case 3: Search Notes by Keyword (Option 3)](./testcase3.md)**
   - Tests keyword matching across titles and note bodies, plus negative test case.
4. **[Test Case 4: Edit & Delete Notes (Options 4 & 5)](./testcase4.md)**
   - Tests updating existing note content and deleting notes by ID.

---

## 🖼️ Quick Visual Gallery

### Test Case 1: Add Note & Validation
![Test Case 1 Terminal Output](images/testcase1.svg)

### Test Case 2: View All Notes
![Test Case 2 Terminal Output](images/testcase2.svg)

### Test Case 3: Search Notes
![Test Case 3 Terminal Output](images/testcase3.svg)

### Test Case 4: Edit & Delete Notes
![Test Case 4 Terminal Output](images/testcase4.svg)

---

## 🛠️ How to Replace Images with Your Own Screenshots

If you have your own screenshots taken from your terminal:
1. Save your screenshot images as `testcase1.png`, `testcase2.png`, `testcase3.png`, and `testcase4.png`.
2. Move them into the `testcase/images/` folder (replacing the existing ones).
3. The markdown links in each file will automatically point to and display your custom screenshots!
