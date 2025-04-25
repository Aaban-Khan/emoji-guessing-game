<h1 align="center">🎮 Emoji Guessing Game (Basic & Intermediate) 🎮</h1>

<p align="center">
  <strong>A fun Python terminal game that challenges players to guess the meaning of emojis! Comes in two versions: Basic and Intermediate.</strong>
</p>

---

<h2>🚀 Features</h2>
<ul>
  <li>🧠 Random emoji is displayed and user guesses its meaning.</li>
  <li>🔊 Sound feedback using Pygame for win, lose, and exit actions.</li>
  <li>✅ Basic Version: unlimited tries, hint-based help, and score tracking.</li>
  <li>⚡ Intermediate Version:
    <ul>
      <li>⏱️ 7-second timeout to guess the answer.</li>
      <li>❌ Maximum of 5 wrong attempts per emoji.</li>
      <li>💬 Hint-based guidance with better control and sound alerts.</li>
    </ul>
  </li>
</ul>

---

<h2>🛠️ Technologies Used</h2>
<ul>
  <li><strong>Python:</strong> Base scripting and terminal logic</li>
  <li><strong>Pygame:</strong> Sound playback for game feedback</li>
  <li><strong>Inputimeout:</strong> Time-limited input for the intermediate version</li>
</ul>

---

<h2>📦 Folder Structure</h2>
<pre>
/01_main.py               -> Basic version of the game
/02_main.py               -> Intermediate version with timer and attempt limit
/requirements.txt         -> Python dependencies (pygame, inputimeout)
/audio/
  ├── win.wav             -> Sound on correct answer
  ├── lose.wav            -> Sound on incorrect guess
  └── exit.wav            -> Sound on exit
</pre>

---

<h2>⚙️ How to Use</h2>
<ol>
  <li>Clone the repository:</li>
  <pre>git clone https://github.com/Aaban-Khan/emoji-guessing-terminal.git</pre>

  <li>Install dependencies:</li>
  <pre>pip install -r requirements.txt</pre>

  <li>Run either version:</li>
  <pre>python 01_main.py</pre>
  or
  <pre>python 02_main.py</pre>

  <li>Make sure <code>audio</code> folder is present in the same directory.</li>
</ol>

---

<h2>🎯 Gameplay Overview</h2>
<ul>
  <li>Guess the meaning of a random emoji.</li>
  <li>Hints are provided if you get it wrong.</li>
  <li>Intermediate version gives 7 seconds to answer and limits you to 5 wrong attempts.</li>
</ul>

---

<h2>📜 License</h2>
<p>This project is licensed under the <strong>MIT License</strong> — feel free to use, modify, and share.</p>
