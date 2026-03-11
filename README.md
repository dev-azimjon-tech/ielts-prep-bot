# ielts-prep-bot
## A Telegram Bot for Preparing For IELTS  

---------------------------------------------------------

## Features:
- Free Books
- Free Practice Books
- Speaking Practice With AI
- Free Consultation
- User's Progress Analyzer
- Free Resources

## User Flow:
1. User Enters and Registers (Only Name)
2. Chooses What to Do
3. Practises
4. Premium (AI Consultation)

## Tech Stack:
- Language: Python 3.10+
- Database: JSON

## Installation:
1. Clone the repository:
```bash
git clone https://github.com/dev-azimjon-tech/ielts-prep-bot.git
cd ielts-prep-bot
```
2. Create a virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate        # On Windows: venv\Scripts\activate
```
3. Install dependencies:
```bash
pip3 install -r requirements.txt
```
4. Create a `.env` file in the root directory and add your Telegram bot token:
```
TELEGRAM_TOKEN=your_token_here
```
5. Start the bot:
```bash
python main.py
```