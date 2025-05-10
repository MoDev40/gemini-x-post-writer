### 📄 `README.md`

# 🧠 Gemini AI X (Twitter) Post Generator

Generate clever, engaging, and potentially viral tweets using Google Gemini AI — and post them to X (Twitter) with your confirmation.

> Ideal for programmers, creators, educators, cybersecurity professionals, meme-lords, and more.

---

## 🚀 Features

- 🤖 Uses Google Gemini AI to generate high-quality tweets based on your topic.
- ✍️ Supports multiple content styles — programming, education, comedy, branding, and more.
- ✅ Confirmation before posting anything.
- 🐦 Posts to Twitter/X via API (if access is available) or lets you copy/paste manually.
- 📂 Includes a collection of specialized prompt templates (`prompts.md`).

---

## 🔧 Setup

1. **Clone the Repo**
   ```bash
   git clone https://github.com/MoDev40/gemini-x-post-writer.git
   cd gemini-x-post-writer
   
2. **Install Requirements**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` File**

   ```env
   GEMINI_API_KEY=your_gemini_api_key_here

   # Optional: only needed for auto-posting to Twitter/X
   X_API_KEY=your_consumer_key
   X_API_SECRET=your_consumer_secret
   X_ACCESS_TOKEN=your_access_token
   X_ACCESS_SECRET=your_access_secret
   ```

4. **Run the Script**

   ```bash
   python app.py
   ```

---

## 🛠 Requirements

* Python 3.8+
* [Google AI Studio](https://makersuite.google.com/) API key
* (Optional) [Twitter Developer Account](https://developer.twitter.com/) for auto-posting

---

## 📝 Usage

1. Run the script.
2. Enter a topic or idea you'd like to turn into a tweet.
3. Gemini will generate a tweet.
4. You can:

   * ✅ Post it to X (if you have API access)
   * 📋 Copy and manually post it
   * 🔁 Try again with a new idea

---

## 🔐 Access Limitations

* **Twitter API**: The free tier allows limited posting via API v2 not v1.1.
* **Gemini API**: Free tier allows reasonable usage per day/month. Use responsibly.

---

## 📚 Prompt Templates

This repo includes a `prompts.md` file with tailored prompts for different content types:

* General
* Coding
* Programming
* Education
* Social
* Content Creator
* Cybersecurity
* Phishing
* Branding
* Personal
* Comedy
* Fun & Memes
* Films

Feel free to customize or extend it.

---

## 🤝 Contributing

Pull requests welcome! If you have better prompts, want to add themes, or support scheduling, fork and open a PR.

---

## 📄 License

MIT License — Free to use and modify.

---

## ❤️ Credits

Built using:

* [Google Generative AI](https://ai.google.dev/)
* [Tweepy](https://www.tweepy.org/)
* [dotenv](https://pypi.org/project/python-dotenv/)

---
