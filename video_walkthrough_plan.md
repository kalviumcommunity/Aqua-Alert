# Video Walkthrough Plan: DataFrame Indexing and Slicing (~2 Minutes)

This plan is aligned to the milestone requirements: column selection, row selection by position and label, and combined row-column selection.

## 1. Introduction (15-20 Seconds)
- **Action**: Show your IDE with `dataframe_selection_demo.py` and terminal.
- **Script**: "Hello, I am [Your Name]. In this milestone, I will demonstrate selecting rows and columns in Pandas using indexing and slicing."

## 2. Selecting Columns by Name (25-30 Seconds)
- **Action**: Run `python dataframe_selection_demo.py` and point to the first section.
- **Key Points**:
    - Show single column selection: `df['ph_level']`.
    - Show multiple columns selection: `df[['location', 'ph_level', 'temperature_c']]`.
    - Explain result type difference: Series vs DataFrame.
- **Script**: "Selecting by column names is the most common operation. A single column returns a Series, while multiple columns return a DataFrame."

## 3. Selecting Rows by Position with iloc (25-30 Seconds)
- **Action**: Point to `df.iloc[2]` and `df.iloc[1:4]` output.
- **Key Points**:
    - `iloc` uses zero-based positions.
    - Slices are start-inclusive and stop-exclusive.
- **Script**: "I use iloc when I want row positions. For example, row index 2 is the third row, and slice 1:4 returns rows 1, 2, and 3."

## 4. Selecting Rows by Label with loc (25-30 Seconds)
- **Action**: Point to `set_index('sample_id')` and label-based outputs.
- **Key Points**:
    - `loc` uses explicit index labels.
    - Label slicing is inclusive on both ends.
- **Script**: "After setting sample_id as the index, I can select rows by labels. With loc, label ranges include both the start and end labels."

## 5. Selecting Rows and Columns Together (20-25 Seconds)
- **Action**: Point to combined selections using `iloc` and `loc`.
- **Key Points**:
    - Show positional combined subset.
    - Show label-based combined subset.
    - Mention avoiding chained indexing by selecting in one expression.
- **Script**: "Combined selection helps extract precise subsets safely. I specify rows and columns together in one expression for clarity and reliability."

## 6. Closing (10-15 Seconds)
- **Script**: "That completes the milestone: I selected columns, selected rows by position and label, and combined row-column selections with clear and intentional logic."

## Recording Checklist
- Keep the video around 2 minutes.
- Keep terminal output readable.
- Briefly explain when to use each approach: column names, iloc, and loc.
