from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime
from spy import log
from math import sqrt

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'Hi {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'/hi\n/help\n/time\n/sum\n/difference\n/product\n'\
        f'/divide\n/exponent\n/sqrt\n/complex_sum\n/complex_difference\n/complex_product\n'\
        f'/complex_divide')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    y = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def diff_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    y = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    await update.message.reply_text(f'{x} - {y} = {x - y}')

async def product_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    y = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    await update.message.reply_text(f'{x} * {y} = {x * y}')

async def divide_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    y = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    if y != 0:
        await update.message.reply_text(f'{x} / {y} = {x / y}')
    else:
        await update.message.reply_text(f'Division is impossible')

async def exponent_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    y = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    await update.message.reply_text(f'{x} ** {y} = {x ** y}')

async def sqrt_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    x = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    await update.message.reply_text(f'square root of {x} = {sqrt(x)}')

async def compl_sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    a = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    b = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    a1 = int(items[3]) if items[3].isnumeric() else await update.message.reply_text(f'input Error')
    b1 = int(items[4]) if items[4].isnumeric() else await update.message.reply_text(f'input Error')
    x = complex(a, b)
    y = complex(a1, b1)
    await update.message.reply_text(f'{x} + {y} = {x + y}')

async def compl_diff_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    a = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    b = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    a1 = int(items[3]) if items[3].isnumeric() else await update.message.reply_text(f'input Error')
    b1 = int(items[4]) if items[4].isnumeric() else await update.message.reply_text(f'input Error')
    x = complex(a, b)
    y = complex(a1, b1)
    await update.message.reply_text(f'{x} - {y} = {x - y}')

async def compl_product_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    a = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    b = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    a1 = int(items[3]) if items[3].isnumeric() else await update.message.reply_text(f'input Error')
    b1 = int(items[4]) if items[4].isnumeric() else await update.message.reply_text(f'input Error')
    x = complex(a, b)
    y = complex(a1, b1)
    await update.message.reply_text(f'{x} * {y} = {x * y}')

async def compl_divide_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    log(update, context)
    msg = update.message.text
    items = msg.split()
    a = int(items[1]) if items[1].isnumeric() else await update.message.reply_text(f'input Error')
    b = int(items[2]) if items[2].isnumeric() else await update.message.reply_text(f'input Error')
    a1 = int(items[3]) if items[3].isnumeric() else await update.message.reply_text(f'input Error')
    b1 = int(items[4]) if items[4].isnumeric() else await update.message.reply_text(f'input Error')
    x = complex(a, b)
    y = complex(a1, b1)
    if y != 0:
        await update.message.reply_text(f'{x} / {y} = {x / y}')
    else:
        await update.message.reply_text(f'Division is impossible')