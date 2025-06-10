class CryptoBuddy:
    def __init__(self):
        self.name = "CryptoBuddy"
        self.tone = "Friendly and supportive"
        self.crypto_db = {
            "Bitcoin": {
                "price_trend": "rising",
                "market_cap": "high",
                "energy_use": "high",
                "sustainability_score": 3/10
            },
            "Ethereum": {
                "price_trend": "stable",
                "market_cap": "high",
                "energy_use": "medium",
                "sustainability_score": 6/10
            },
            "Cardano": {
                "price_trend": "rising",
                "market_cap": "medium",
                "energy_use": "low",
                "sustainability_score": 8/10
            }
        }

    def respond(self, message):
        message = message.lower().strip()

        # Greetings
        if "hi" in message or "hello" in message:
            return "Hey there! 👋 I'm CryptoBuddy. Ready to explore some smart crypto choices?"

        # Trending
        elif "trending" in message or "rising" in message:
            trending = [coin for coin in self.crypto_db if self.crypto_db[coin]["price_trend"] == "rising"]
            return f"These coins are currently trending up 📈: {', '.join(trending)}"

        # Sustainability
        elif "sustainable" in message or "eco" in message:
            best = max(self.crypto_db, key=lambda x: self.crypto_db[x]["sustainability_score"])
            return f"🌱 {best} is the most sustainable coin out there with a high eco score!"

        # Long-term investment advice
        elif "long-term" in message or "growth" in message:
            for coin, data in self.crypto_db.items():
                if data["price_trend"] == "rising" and data["sustainability_score"] > 0.7:
                    return f"🚀 {coin} is trending up and has a top-tier sustainability score! Great for long-term growth!"

        # Help or fallback
        elif "help" in message:
            return ("You can ask me things like:\n"
                    "- Which crypto is trending up?\n"
                    "- What's the most sustainable coin?\n"
                    "- Which coin is good for long-term growth?\n"
                    "- Or just say hi!")

        elif "name" in message:
            return "I'm CryptoBuddy – your friendly crypto guide! 🤖"

        elif "bye" in message or "exit" in message:
            return "Goodbye and happy investing! 💰 Remember: Crypto is risky—always do your own research!"

        else:
            return "Hmm 🤔 I didn't get that. Try asking about trending coins, sustainability, or say 'help'."


# Example usage
chatbot = CryptoBuddy()
while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("CryptoBuddy:", chatbot.respond("bye"))
        break
    print("CryptoBuddy:", chatbot.respond(user_input))
