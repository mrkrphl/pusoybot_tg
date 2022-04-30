import os
def start_bot(updater):
    updater.start_webhook(listen="0.0.0.0",
                          port=int(int(os.environ.get('PORT', 5000))),
                          url_path='5084650563:AAGoOgqgmT9gNDSKt_LC5VmiITXPhrWUpsg')
    updater.bot.setWebhook('https://gentle-retreat-84776.herokuapp.com/' + '5084650563:AAGoOgqgmT9gNDSKt_LC5VmiITXPhrWUpsg')
    
