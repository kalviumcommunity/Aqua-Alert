# Video Walkthrough Plan: Data Splitting (~2-3 Minutes)

This plan is aligned to the milestone requirements: splitting strategy justification, code walkthrough, and leakage prevention.

## 1. Why Split? (30 Seconds)
- **Action**: Show a slide or bullet points in your IDE (e.g., in `data_splitting.py` comments).
- **Script**: "Before I train our model, I must ensure our evaluation is honest. If I use the same data for training and testing, I am measuring memorization rather than learning. Splitting the data into training and testing sets allows us to simulate real-world performance on unseen data and detect overfitting early."

## 2. Strategy Justification (30 Seconds)
- **Action**: Show the `perform_data_split` function.
- **Script**: "For the Aqua-Alert project, I am using an 80/20 split. Because we are dealing with a classification problem where we need to predict binary outcomes, I've implemented a **Stratified Split**. This preserves the class balance across both sets. I've also fixed the `random_state` to 42 to ensure that our results are completely reproducible by any other engineer."

## 3. Code Walkthrough (45 Seconds)
- **Action**: Run `python data_splitting.py` and scroll through the output.
- **Script**: "Here is the implementation. First, I separate our features X from our target column y. Then, using Scikit-Learn's `train_test_split`, I create our four subsets. You can see the shapes here: 400 samples for training and 100 for testing. Most importantly, look at the class distributions—they are nearly identical between the sets, confirming that our stratification worked perfectly."

## 4. Leakage Prevention (30 Seconds)
- **Action**: Highlight the "Leakage Prevention Confirmation" section in the terminal.
- **Script**: "Critically, no preprocessing like scaling or encoding has been performed yet. Fitting transformations on the whole dataset before splitting would leak future information into our training set. We will fit our preprocessors strictly on the training set only in the next phase of the project."

## 5. Closing (15 Seconds)
- **Script**: "That concludes the data splitting milestone. We have a robust, honest foundation for our model evaluation. Thank you!"

## Recording Checklist
- [ ] Keep the video under 3 minutes.
- [ ] Ensure terminal text size is readable.
- [ ] Explicitly mention **random_state** and **stratification**.
- [ ] Show the percentage distribution of classes in the output.
