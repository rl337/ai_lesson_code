# AI lesson code

Starter code for the ten lessons that follow Lesson 0. Start with the matching lesson directory. Lessons 4–10 are reserved for future starter code.

Use Python 3.11 or newer with a virtual environment. In VS Code, choose **Python: Create Environment**, select **Venv**, then choose your interpreter. Open a new terminal with that environment active and run `python -m pip install -r requirements.txt`.

Start the LM Studio local server with a model loaded. In Bash or Zsh (Git Bash on Windows), configure the client before running a lesson:

```sh
export COURSE_MODEL_URL=http://localhost:1234/v1/chat/completions
export COURSE_MODEL_ID=YOUR_LOADED_MODEL_ID
```

Use the actual server address and model ID shown by LM Studio. See each lesson README for its run command.
