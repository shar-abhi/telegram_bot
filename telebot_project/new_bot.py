import argparse
import logging
import ollama

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)
querying = False


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    if querying:
        logger.info(f"Ollama will be responding")
        resp = ollama_model(queries=update.message.text)
        await update.message.reply_text(resp)
    else:
        logger.info(f"Going to reply to user {update.effective_user}")
        await update.message.reply_text(update.message.text)


def ollama_model(queries):

    response = ollama.chat(model="llama3.2", messages=[
        {
            'role': 'user',
            'content': queries,
        },
    ])
    logger.info("\nBot Wrote:\n==============\n{}".format(response['message']['content']))
    return response['message']['content']


async def query(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global querying
    querying = True
    user = update.effective_user
    await update.message.reply_html(f"Hi {user.mention_html()}, How can I assist you today?")


async def end(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    querying = False
    await update.message.reply_text("Going to quit the chat. Goodbye!!")


def main() -> None:
    argparser = argparse.ArgumentParser()
    argparser.add_argument("--token", help="Provide the Token ID obtained from Botfather", required=True, type=str)

    args, _ = argparser.parse_known_args()

    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(args.token).build()

    application.add_handler(CommandHandler("start", query))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("end", end))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()