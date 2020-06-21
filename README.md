# telegram-tweet-archive
Quickly archive other people's tweet on Telegram

Following steps need to be done to create your bot:

1. Create telegram bot by messaging ```/newbot``` to [BotFather](https://t.me/botfather)
2. Register to [Twitter Developer Portal](https://developer.twitter.com/en/apps) and create an app
3. Install libraries ```python install -r requirements.txt```
4. Change the environment variables with your ones
5. Run the bot ```python archivebot.py```
6. Send the command to the bot, for example: ```/user ekremimamoglu``` (this command will download the latest 3000 tweets of the Mayor of Istanbul)
7. Profit.

Check [this blog post](https://projects.gokhanarkan.com/2020/06/21/quick-archive-someones-tweets) for further info.