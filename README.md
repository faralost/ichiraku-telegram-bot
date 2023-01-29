# Telegram Bot Ichiraku

This is a Telegram bot that I wrote for our chat with friends to have fun by interacting with it. The bot is built using the [Aiogram](https://docs.aiogram.dev/) library for Python.


## Features
- **GPT**: Integrated chatGPT to our bot.
- **Sakura**: The bot will send random photo of my cat Sakura.
- **Kakura**: The bot will send random photo of my cat Sakura goes to the toilet.
- **Wedding**: The bot will send random photo from wedding of our friends.
- **Fact**: The bot will send you random fact.
- **Quote**: The bot will send you random quote from Anime series that we have watched.
- **Game**: Simple game where you have to guess the number.

## Scheduled Tasks
- **Good morning**: Every morning, Bishkek time, the bot wishes good morning and sends the weather of those cities where my friends live.

## How to use
1. Search for the bot on Telegram by its username (Ichiraku Bot) or invite it to a group chat using the link: [t.me/kg_ichiraku_bot](https://t.me/kg_ichiraku_bot)
2. Start the bot by typing `/start`

## How to run the bot locally
1. Clone the repository
2. Go to the root directory of the project, create the .env file and fill it in as .env.example shows.
3. To run the project:

```
docker compose up --build -d
```

## Used External Services
- [OpenAi](https://openai.com/): Integration of chatGPT.
- [Animechan](https://animechan.vercel.app/): To get Anime quotes.
- [ApiNinjas](https://api-ninjas.com/): To get facts.
- [OpenWeather](https://openweathermap.org/): To get weather.
- [Imagekit](https://imagekit.io/): To store photos.
