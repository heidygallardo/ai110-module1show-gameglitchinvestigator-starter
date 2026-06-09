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
- I would explain Streamlist "reruns" and session state to a friend who has never used Streamlit by presenting and analogy to them. For them to think of reruns like restarting a vide game level every time any button is pressed. While session state being the file that keeps your score and latest progress saved despite any other button presses. 

---

## 5. Looking ahead: your developer habits

- One habit from this project I want to reuse is to verify AI's output rather than blindly pasting AI-generated code. 
- Next time I work with AI tools, I will forsure lead the AI and prompt it to do what I have in mind. 

