# How to Continue Work in a New Chat - Step by Step

## Step 1: Open the Status Document
Open this file first: `COMPLETION-STATUS.md`
- This contains the complete status summary
- Shows exactly what's done and what's remaining

## Step 2: Start Your New Chat
In Cursor, start a new chat/conversation.

## Step 3: Provide This Initial Prompt

Copy and paste this exact prompt to start:

```
I need to complete a MusicXML file for a string quartet movement. 

CURRENT STATUS:
- File: Quartet_Revisions_Nov_2026/Air/Movement-4/Air-Mov4-ExcellenceEdition.musicxml
- Violin I: Complete (measures 1-90)
- Violin II: Complete (measures 1-90)  
- Viola: Complete (measures 1-88)
- Cello: Measures 1-17 and 90 are complete
- REMAINING: Cello measures 18-89 (72 measures)

Please read COMPLETION-STATUS.md for full details, then complete the remaining Cello measures 18-89 following the exact specifications in Air-Mov4-COMPLETE-COMPOSITION.md.

The file is valid XML and opens in Sibelius. I need all 72 remaining measures added following the pattern from measures 1-17.
```

## Step 4: Reference Files to Share

If the AI needs more context, point them to these files:
1. `COMPLETION-STATUS.md` - Current status and what's needed
2. `Air-Mov4-COMPLETE-COMPOSITION.md` - Complete measure specifications
3. `add_cello_measures.py` - Python script that generates the measures
4. `Air-Mov4-ExcellenceEdition.musicxml` - The main file to edit

## Step 5: Key Information to Provide

**File Location:**
```
Quartet_Revisions_Nov_2026/Air/Movement-4/Air-Mov4-ExcellenceEdition.musicxml
```

**Insertion Point:**
- After measure 17 (around line 11048)
- Before measure 90

**Pattern:**
- Each measure = 4 quarter notes with pizzicato
- See measure 17 (lines 10978-11048) as template
- Measures 21-24 are arco with slurs (special case)
- Measure 89 is half note arco tenuto (special case)

**Measure Specifications:**
- M18-20: C3-E3-G3-C3 (C major, pizzicato)
- M21-24: E3-F#3-G3-A3, B3-C4-D4-E4 (arco, slurs, tenor marking)
- M25-88: Various pizzicato quarter notes per composition doc
- M89: G2 half note (arco, tenuto)

## Step 6: Verification Commands

After completion, verify with:
```
Check that all 90 measures are present for Cello part. Verify the file opens in Sibelius.
```

## Step 7: What Success Looks Like

✅ File has 90 measures for Cello (currently has 1-17 and 90)
✅ All measures follow correct pattern
✅ File opens in Sibelius without errors
✅ All pitches match Air-Mov4-COMPLETE-COMPOSITION.md specifications

---

## Quick Copy-Paste Prompt for New Chat

```
I'm completing a MusicXML string quartet file. 

STATUS: Cello part needs measures 18-89 added (72 measures). Measures 1-17 and 90 are done.

FILE: Quartet_Revisions_Nov_2026/Air/Movement-4/Air-Mov4-ExcellenceEdition.musicxml

Please:
1. Read COMPLETION-STATUS.md for full details
2. Read Air-Mov4-COMPLETE-COMPOSITION.md for measure specifications  
3. Add Cello measures 18-89 following the pattern from measures 1-17
4. Insert after measure 17 (line ~11048), before measure 90

Each measure = 4 quarter notes pizzicato (except M21-24 arco, M89 half note).
Complete all 72 remaining measures now.
```

---

## Files to Have Open/Ready

1. ✅ `COMPLETION-STATUS.md` - Status summary
2. ✅ `Air-Mov4-COMPLETE-COMPOSITION.md` - Specifications
3. ✅ `Air-Mov4-ExcellenceEdition.musicxml` - Main file to edit
4. ✅ `add_cello_measures.py` - Helper script (optional)

---

**You're ready to continue!** Just copy the prompt above into a new chat and the AI will have everything needed to complete the work.


