# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- the hints were backwards
- the new game button does not start a new game
- on even attempts when I guess correctly the secret it does not show the message shown when guessing correctly

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  60   |  go higher              go lower            'Go lower'
|  'new game' | a new game      no new game     'you already won. start a new game to play again.' 
|  61   |   to win              it did not output anything    n/a only blank hint

---

## 2. How did you use AI as a teammate?

- I used Claude to determine why the app was not working as intended. After receiving a response I manually verified and also added a test case to ensure issue was fixed. 
---

## 3. Debugging and testing your fixes

- One test I added was to check that the message shown to users was the correct one based on a user's guess.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
