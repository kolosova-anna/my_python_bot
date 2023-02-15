from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *




app = ApplicationBuilder().token("5879740540:AAHyI88DtfvjEn5zsuVlmlIBf1RKn_Anvps").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("difference", diff_command))
app.add_handler(CommandHandler("product", product_command))
app.add_handler(CommandHandler("divide", divide_command))
app.add_handler(CommandHandler("exponent", exponent_command))
app.add_handler(CommandHandler("sqrt", sqrt_command))
app.add_handler(CommandHandler("complex_sum", compl_sum_command))
app.add_handler(CommandHandler("complex_difference", compl_diff_command))
app.add_handler(CommandHandler("complex_product", compl_product_command))
app.add_handler(CommandHandler("complex_divide", compl_divide_command))
print('server start')
app.run_polling()