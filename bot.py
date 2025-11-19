import telebot
from telebot.types import Message
from config import BOT_TOKEN
from utils.music import download_youtube_song
from utils.spotify import search_spotify_track

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start(message: Message):
    bot.reply_to(message, "🎵 Music Bot Activated!\nUse /play <song name>")

@bot.message_handler(commands=['play'])
def play(message: Message):
    query = message.text.replace("/play", "").strip()
    if not query:
        return bot.reply_to(message, "Please type a song name.")

    # Spotify search
    song_from_spotify = search_spotify_track(query)
    if song_from_spotify:
        query = song_from_spotify

    bot.reply_to(message, f"Searching: {query}")

    file_path = download_youtube_song(query)
    audio = open(file_path, "rb")

    bot.send_audio(message.chat.id, audio)
    audio.close()

bot.polling(none_stop=True)
