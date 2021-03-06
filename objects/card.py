#Suits
from tokenize import String


DIAMONDS = 'd'
SPADES = 's'
HEARTS = 'h'
CLUBS = 'c'

SUITS_VALUES = {
    DIAMONDS:3,
    SPADES:2,
    HEARTS:1,
    CLUBS:0
}

SUIT_ICONS = {
    DIAMONDS:'♦',
    SPADES:'♠',
    HEARTS: '♥',
    CLUBS: '♣'
}

# Values
ACE = 'A'
TWO = '2'
THREE = '3'
FOUR = '4'
FIVE = '5'
SIX = '6'
SEVEN = '7'
EIGHT = '8'
NINE = '9'
TEN = '10'
JACK = 'J'
QUEEN = 'Q'
KING = 'K'

VALUE_VALUES = {
    THREE:3,
    FOUR:4,
    FIVE:5,
    SIX:6,
    SEVEN:7,
    EIGHT:8,
    NINE:9,
    TEN:10,
    JACK:11,
    QUEEN:12,
    KING:13,
    ACE:14,
    TWO:15
}

STICKERS = {
    'd_A': 'CAACAgQAAxkDAAIxS2KGIRUYsvBp0NR_iFiEpAXzwWM4AAICAwACpAw0UMeeWLaBdRmhJAQ',
    'd_2': 'CAACAgQAAxkDAAIxTGKGIRXoGTLgKjDHyYaGKyvBpR4jAALeAgACUdc1UDHfm3TfnnEiJAQ',
    'd_3': 'CAACAgQAAxkDAAIxTWKGIRbwO-X5AAEnD2pATmUP_OvCEQAC6QIAAnFlNFDOnYiW7YNbhyQE',
    'd_4': 'CAACAgQAAxkDAAIxTmKGIRa_6sz3203O73IAAfzXDeMfHgACKgMAAjjqNFCCrK8Z-wABLyIkBA',
    'd_5': 'CAACAgQAAxkDAAIxT2KGIRZBASmPkLr5ppVQ_a1nGMQIAAISAwACfB01UOmcF5-ExjfGJAQ',
    'd_6': 'CAACAgQAAxkDAAIxUGKGIRfg5NThe4mdlEdpRidcxRabAAJKAwACTrM8UBewg7ZUaN3eJAQ',
    'd_7': 'CAACAgQAAxkDAAIxUWKGIRpyxnI9YJCP9TyJurIzlXyjAALmAgACrBs1UFkEEuBauAQVJAQ',
    'd_8': 'CAACAgQAAxkDAAIxUmKGIRsP_7uedQyS_23gjMCXTypcAAL3AgACoHM1ULtVqnMczH-GJAQ',
    'd_9': 'CAACAgQAAxkDAAIxU2KGIRsYhWsyxYQaLd9_B0ikNtGtAAJCAwAC3e81UKezzL94i5qnJAQ',
    'd_10': 'CAACAgQAAxkDAAIxVWKGIVgHvNXTMY2NF2uNMwJGvNlmAAIQAwACUik0UEEG2nG6ubdWJAQ',
    'd_J': 'CAACAgQAAxkDAAIxVmKGIVnFjek0dFerJd4AARmZ6l-bjQACKQMAAg4sNVBgaxF5171ZCSQE',
    'd_Q': 'CAACAgQAAxkDAAIxV2KGIVmiibookUQ73YeXiD8Xb758AAI6AwACZEA8UJkG0DklobQbJAQ',
    'd_K': 'CAACAgQAAxkDAAIxWGKGIVkeVfIqaw3JB85vqUMVDtLUAAIxAwAC0hU0UOH8nnKPdFLnJAQ',
    's_A': 'CAACAgQAAxkDAAIxWWKGIVoQY6LI3xxeQnqfIglct2iQAALhAgACltY1UBSlFpSuiHK8JAQ',
    's_2': 'CAACAgQAAxkDAAIxWmKGIVqc9qILiqbvrRrI8mrdiajbAAIIAwACIts1UHP3rjY7HaoGJAQ',
    's_3': 'CAACAgQAAxkDAAIxW2KGIV9LuK8Ed3TXE3RFCmEV8k9WAAIYAwACys80UA4kDgo0wg91JAQ',
    's_4': 'CAACAgQAAxkDAAIxXGKGIV9gwHAf2eu1nzi3w5tS48fqAAIZAwAC4oc1ULLVmv_ADlhVJAQ',
    's_5': 'CAACAgQAAxkDAAIxXWKGIV8ZrSVVin6YtbjDuHwEhGo0AAIPAwACYIY0UCSdXgAB7yMXvyQE',
    's_6': 'CAACAgQAAxkDAAIxXmKGIWCmkN01ClsB1TtwMLTt_m6FAAIEAwAC9140UJTUXy977ZeDJAQ',
    's_7': 'CAACAgQAAxkDAAIxX2KGIWCRINRrPJKu3dn0GkodXcT7AAIiAwACJR81UDJQethCN4GJJAQ',
    's_8': 'CAACAgQAAxkDAAIw7WKGEnsDX2qFOcGUtAhwo-Vxq3PpAAInAwACtZE1UM9qr_GXR5NqJAQ',
    's_9': 'CAACAgQAAxkDAAIw7mKGEnvkQ1NFf8YFmKuuQtJA8KAtAAJpAwACB5g9UIVAivtPA-APJAQ',
    's_10': 'CAACAgQAAxkDAAIxYWKGIZEOCGMbZs4eT1YRpiN0NJO8AAIRAwACFGE1ULqLtdT7626oJAQ',
    's_J': 'CAACAgQAAxkDAAIxYmKGIZJUKrTlkQ2o6Xg_i1a78EPqAAILAwACw7w1UKMiZx2f2JJ5JAQ',
    's_Q': 'CAACAgQAAxkDAAIxY2KGIZNWCzjdEzgRSDd4Fk4-rNOvAAJEAwACFVw0UMnQxTIxanrvJAQ',
    's_K': 'CAACAgQAAxkDAAIxZGKGIZS7GT2h2zrFMNo9msEQgOoxAALkAgACCxM0UFUFyGNAuRkqJAQ',
    'h_A': 'CAACAgQAAxkDAAIxZWKGIZVfrSySC5YjvbgKL5uZJ4jNAAIkAwACBz41UN86LKVu-42QJAQ',
    'h_2': 'CAACAgQAAxkDAAIxZmKGIZfdmx7sBTURleuM5MI2EGlGAAIOAwACOvQ1UBspFePhcf3EJAQ',
    'h_3': 'CAACAgQAAxkDAAIxZ2KGIZj4A68ZRaYLp3rJzmvvRT2VAAIIAwAC_389UFgaxeBYOV1bJAQ',
    'h_4': 'CAACAgQAAxkDAAIxaGKGIZlontn-Z2SPKbTqFvi6RejPAAIaAwACOCs1UJcwj9hPkF9QJAQ',
    'h_5': 'CAACAgQAAxkDAAIxaWKGIZpjh4U9O2E12RMZR6bNwBN3AAIZAwACJ5o1UJi2F9B3h25cJAQ',
    'h_6': 'CAACAgQAAxkDAAIxamKGIZsAAZHeqsvm789Ltg5gyo_YcgACVwMAAkF2NFDprzui_CQvFiQE',
    'h_7': 'CAACAgQAAxkDAAIxa2KGIZ0lU59bKLnrzNCXt_9FnASkAALWAgAC6AQ1UC3l8zxLMgK7JAQ',
    'h_8': 'CAACAgQAAxkDAAIxbGKGIZ5rpQHbnjmt689xiGbC0KiTAAIFAwACXEQ0UJ6JlfE4csU7JAQ',
    'h_9': 'CAACAgQAAxkDAAIxbWKGIZ8oXSw21wYl380hSYAsnTEWAAIMAwACTiQ0UMbqBnffeCAtJAQ',
    'h_10': 'CAACAgQAAxkDAAIxbmKGIaABIPFfP-idzttdMMGXJswWAAL5AgAChds0UJF0HSN9p2ZkJAQ',
    'h_J': 'CAACAgQAAxkDAAIxb2KGIaH36eP-O1zVvt0aJGH5FK5FAAIPAwACLI01UD1VEJFucVG1JAQ',
    'h_Q': 'CAACAgQAAxkDAAIxcGKGIaOPiqL7ArNVIpQtlsOhVJzaAALyAgACoe00UAzvqzFxkgHOJAQ',
    'h_K': 'CAACAgQAAxkDAAIxcWKGIaQ5400LmId7RGM3a91UqpkxAAIgAwACQ-k0UNGiWEJKdKGWJAQ',
    'c_A': 'CAACAgQAAxkDAAIxcmKGIaWCLSW3uxVmWwUH9lXemnuWAAIaAwACbu40UJ0wgzKZQkefJAQ',
    'c_2': 'CAACAgQAAxkDAAIxc2KGIadLbFR9Y8ezKbTsbL0fzUBkAAIhAwACSoM0UIwHVPmEzdxGJAQ',
    'c_3': 'CAACAgQAAxkDAAIxdGKGIajT9fG6cEJyL5ySJ1DcoHK4AAL_AgACvIA0UGJZv9dS2KbHJAQ',
    'c_4': 'CAACAgQAAxkDAAIxdWKGIanwFQKUJYRQEvgzI2GynuVgAAIaAwACucQ0UCoQQhglgMhBJAQ',
    'c_5': 'CAACAgQAAxkDAAIxdmKGIavRQhAHM7tKaYTBlGKEYWQFAAIdAwACmys1UIGVd4eDt-pfJAQ',
    'c_6': 'CAACAgQAAxkDAAIxd2KGIazhzJ5351F_-ZzoHITeZU0iAAI-AwACl-Y0UIOlLBWQFptMJAQ',
    'c_7': 'CAACAgQAAxkDAAIxe2KGIhJFBriqv7-Cpup2SuWLW-BWAAIsAwACOE09UGHkQj1TGbMQJAQ',
    'c_8': 'CAACAgQAAxkDAAIxfGKGIhMLVySVuDPJGklM15YUNvX9AAIXAwACj341UKjJMjyDCnk9JAQ',
    'c_9': 'CAACAgQAAxkDAAIxfWKGIhVV6mArtqvtgIBdcSd-wvR1AAIoAwACx2Y8ULCbCU0z44QOJAQ',
    'c_10': 'CAACAgQAAxkDAAIxfmKGIhb1uD1Y1ARDCjJvxzUTOms8AALjAgACQlY0UAWk9pKBqYkhJAQ',
    'c_J': 'CAACAgQAAxkDAAIxf2KGIhhj9h9YJ_vsCDu3ijD7chMOAAImAwACwkk8UCM-RYkaI5-kJAQ',
    'c_Q': 'CAACAgQAAxkDAAIxjGKGIuHV7Zarf7cXhW2Jd4x2r4CYAAIxAwACxXM8UI3Pnnu83GAWJAQ',
    'c_K': 'CAACAgQAAxkDAAIxjWKGIuEW7IP3sFSVLmGlg7f8JthtAAIHAwACqck0ULiNykEPCo-jJAQ',
    'option_info': 'CAACAgQAAxkDAAIxjmKGIuFQWaG13_YsCxMY1fzcRMUbAALEAgACX1eZAAGi2Qy93IIQwiQE',
    'option_pass': 'CAACAgQAAxkDAAIxj2KGIuIJ5E-tCJ-LCAZhAWJT4z3mAAL6AgACX1eZAAFuilR5QnD-VyQE',
    '1': 'CAACAgQAAxkDAAIxkGKGIuKNA8tBDgj404HQHpOmhesNAAIgAwACb_Y1UEF-aKEalESrJAQ',
    '2': 'CAACAgQAAxkDAAIxkWKGIuO8SwY2XXjxJTfQT9cR1QrwAAI3AwACBug1UPH2qcFr3JwQJAQ',
    '3': 'CAACAgQAAxkDAAIxkmKGIuf3RSpA0NGYqwdci-gXkbECAAIgAwAC0qs8UOHM2mbf5FziJAQ',
    '4': 'CAACAgQAAxkDAAIxk2KGIun0FcMdcQ9QtufpvWul6EB8AAIiAwACJuo8UByjMroQnOiZJAQ',
    '5': 'CAACAgQAAxkDAAIxlGKGIurXvpNRnX9lHqA0KFDvSFL4AALkAgACMCY1UJlbFVXefKcQJAQ',
}
STICKER_GRAB = {
    'd_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_A.webp',
    'd_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_2.webp',
    'd_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_3.webp',
    'd_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_4.webp',
    'd_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_5.webp',
    'd_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_6.webp',
    'd_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_7.webp',
    'd_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_8.webp',
    'd_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_9.webp',
    'd_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_10.webp',
    'd_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_J.webp',
    'd_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_Q.webp',
    'd_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/d_K.webp',
    's_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_A.webp',
    's_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_2.webp',
    's_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_3.webp',
    's_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_4.webp',
    's_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_5.webp',
    's_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_6.webp',
    's_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_7.webp',
    's_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_8.webp',
    's_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_9.webp',
    's_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_10.webp',
    's_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_J.webp',
    's_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_Q.webp',
    's_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/s_K.webp',
    'h_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_A.webp',
    'h_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_2.webp',
    'h_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_3.webp',
    'h_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_4.webp',
    'h_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_5.webp',
    'h_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_6.webp',
    'h_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_7.webp',
    'h_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_8.webp',
    'h_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_9.webp',
    'h_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_10.webp',
    'h_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_J.webp',
    'h_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_Q.webp',
    'h_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/h_K.webp',
    'c_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_A.webp',
    'c_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_2.webp',
    'c_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_3.webp',
    'c_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_4.webp',
    'c_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_5.webp',
    'c_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_6.webp',
    'c_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_7.webp',
    'c_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_8.webp',
    'c_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_9.webp',
    'c_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_10.webp',
    'c_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_J.webp',
    'c_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_Q.webp',
    'c_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/c_K.webp',
    'option_info': 'BQADBAADxAIAAl9XmQABC5v3Z77VLfEC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg',
    '1':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/1.webp',
    '2':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/2.webp',
    '3':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/3.webp',
    '4':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/4.webp',
    '5':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs/5.webp',
}

STICKER_LOWSAT_GRAB = {
    'd_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_A.webp',
    'd_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_2.webp',
    'd_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_3.webp',
    'd_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_4.webp',
    'd_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_5.webp',
    'd_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_6.webp',
    'd_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_7.webp',
    'd_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_8.webp',
    'd_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_9.webp',
    'd_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_10.webp',
    'd_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_J.webp',
    'd_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_Q.webp',
    'd_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/d_K.webp',
    's_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_A.webp',
    's_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_2.webp',
    's_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_3.webp',
    's_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_4.webp',
    's_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_5.webp',
    's_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_6.webp',
    's_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_7.webp',
    's_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_8.webp',
    's_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_9.webp',
    's_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_10.webp',
    's_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_J.webp',
    's_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_Q.webp',
    's_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/s_K.webp',
    'h_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_A.webp',
    'h_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_2.webp',
    'h_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_3.webp',
    'h_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_4.webp',
    'h_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_5.webp',
    'h_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_6.webp',
    'h_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_7.webp',
    'h_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_8.webp',
    'h_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_9.webp',
    'h_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_10.webp',
    'h_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_J.webp',
    'h_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_Q.webp',
    'h_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/h_K.webp',
    'c_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_A.webp',
    'c_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_2.webp',
    'c_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_3.webp',
    'c_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_4.webp',
    'c_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_5.webp',
    'c_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_6.webp',
    'c_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_7.webp',
    'c_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_8.webp',
    'c_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_9.webp',
    'c_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_10.webp',
    'c_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_J.webp',
    'c_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_Q.webp',
    'c_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/c_K.webp',
    'option_info': 'BQADBAADxAIAAl9XmQABC5v3Z77VLfEC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg',
    '1':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/1.webp',
    '2':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/2.webp',
    '3':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/3.webp',
    '4':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/4.webp',
    '5':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webbs_lowsat/5.webp',
}

OLD_STICKERS = {
    'd_A': 'CAACAgQAAxkDAAIBxGHoJbcyk6bix-hlGtxzRLbgb3PvAAKmAgACFKJFU7w6WyfhYR9xIwQ',
    'd_2': 'CAACAgQAAxkDAAIGz2HpOEsWGiztgSCjf8ysg1jz3wyjAALXAgACCzpEU7Wba4PUo1t1IwQ',
    'd_3': 'CAACAgQAAxkDAAIBumHoJaY1h96GmMt92opq4ma_iRxgAALcAgAC1nJEU09rFm0UZ1B_IwQ',
    'd_4': 'CAACAgQAAxkDAAIBvWHoJalojqK8ldafpgx9M5c_VMj7AAK-AgACc5BMU6T8w6RTVnvaIwQ',
    'd_5': 'CAACAgQAAxkDAAIBuGHoJaTSDBfPyS1gXaXhD-83ny_YAALnAgAC22REU59fQQUma3DWIwQ',
    'd_6': 'CAACAgQAAxkDAAICL2HoKUvnAlAQLgAC0GG-X-Rki_8gAALSAgACpldEU2gaIVs7bGtIIwQ',
    'd_7': 'CAACAgQAAxkDAAIBwmHoJbRJobMlvddOnMF2F8yIrPUXAAL4AgACyCRFU7hrz87CziV-IwQ',
    'd_8': 'CAACAgQAAxkDAAIBu2HoJaZGKVjAA7DGDgR7KsllcPS0AALkAgACSUVEU-ZRhMGNdBa0IwQ',
    'd_9': 'CAACAgQAAxkDAAICF2HoKM2rrrMWsIeXDujvXTr_IyI7AALYAgAClQREU9sT50VtxJJwIwQ',
    'd_10': 'CAACAgQAAxkDAAICGmHoKNLHrOnn0Aft8yREXgsz2DC5AAK0AgAC6DxFU1zJLKrHzQLdIwQ',
    'd_J': 'CAACAgQAAxkDAAIBwWHoJbOwLIy5A7bk4limLk8vpjOwAALcAgAC_GtMUwV7BcFdab71IwQ',
    'd_Q': 'CAACAgQAAxkDAAIGxmHpOALQ7EyNPOnJSNNbS5kxVT7UAALFAgAClnpFU8cD-hzIxwABnyME',
    'd_K': 'CAACAgQAAxkDAAIBxWHoJbgIX0-U6yhcWelKH9pahSR7AAK9AgACcnZEU1RurVt75BwjIwQ',
    's_A': 'CAACAgQAAxkDAAICJWHoKOJ-41T4CDpAajaJzyJRlclDAALAAgACagABRFMz7nwjZ9GDOCME',
    's_2': 'CAACAgQAAxkDAAICJGHoKOKlHRU_szSaI6L708HsLDYCAAK_AgAC_wFFU5TQA2e7DoypIwQ',
    's_3': 'CAACAgQAAxkDAAIBvGHoJajz0XMlqc0ZSWt6PFHxXmjyAAKjAgACFYhEU-286J6U08P0IwQ',
    's_4': 'CAACAgQAAxkDAAIBwGHoJbHtDgu4VnSNw33Vw0s195dzAAKuAgACcWNFU9etokFsNiLkIwQ',
    's_5': 'CAACAgQAAxkDAAIByWHoJcPZLTvxPusaZR1fd40vWeTiAAKwAgACO6pEUxt110f7W1SjIwQ',
    's_6': 'CAACAgQAAxkDAAICIWHoKNoR6KknWhfvmaH7JA8lciWkAALMAgACR0FFUykIXm1GRUsmIwQ',
    's_7': 'CAACAgQAAxkDAAICHWHoKNTQLXGus_6VY2YBviIssYFSAAKwAgACy4xNU6oo-fjLCd_kIwQ',
    's_8': 'CAACAgQAAxkDAAIBy2HoJcfXniXqOTkhawQ8hSp2-BvNAAK4AgAC-xdMU-LkNOAsyVx8IwQ',
    's_9': 'CAACAgQAAxkDAAICHmHoKNhZatWgGca6Lo3R6RHRP-THAALuAgACxa1FU3qcL1o_yhGCIwQ',
    's_10': 'CAACAgQAAxkDAAICGWHoKNJDf4_6jXr76mPmZqKug44hAAL8AgAC1I9EU1j3KqUwPU8QIwQ',
    's_J': 'CAACAgQAAxkDAAIB9GHoJ2VjYkcOrXzX9Wjx_HAKbxO8AAIGAwACEAREU6kt_NdVs6JHIwQ',
    's_Q': 'CAACAgQAAxkDAAIB-GHoJ2sSsFfu-V7Dnjb2ZsqjD3mKAALNAgAClK1EUxDepfR1g1VWIwQ',
    's_K': 'CAACAgQAAxkDAAIBx2HoJb8_mTz3T8zYMRO4NID0VVihAAL7AgACBqlEU20DwwOXbnVjIwQ',
    'h_A': 'CAACAgQAAxkDAAIBw2HoJbU2zrDUVEDkEDQ4w6_XmOkiAAKwAgAC7FpEU1EOIputYTDdIwQ',
    'h_2': 'CAACAgQAAxkDAAICJ2HoKOR6lr19pmVM_jNthQ1eppIbAAIDAwAClHpFU8HR-jICPHF4IwQ',
    'h_3': 'CAACAgQAAxkDAAIBzGHoJceWWN4FfwuthFpTLlgamHS8AAK-AgACFsJMU8vW5yuhSpHgIwQ',
    'h_4': 'CAACAgQAAxkDAAICFWHoKMw_uUEAAZsIgo7uLCmXcYAlpgACogIAAs_iRVMFZBnGwkq8lyME',
    'h_5': 'CAACAgQAAxkDAAIBuGHoJaTSDBfPyS1gXaXhD-83ny_YAALnAgAC22REU59fQQUma3DWIwQ',
    'h_6': 'CAACAgQAAxkDAAIByGHoJcDlLqCH48604GMkNOGed5d-AAK7AgAC5WZEU9EJr80WQpaRIwQ',
    'h_7': 'CAACAgQAAxkDAAICH2HoKNkzQrXbx485Bf8bzr0qAQYlAALEAgACoBRMUxoKyOZGNShVIwQ',
    'h_8': 'CAACAgQAAxkDAAICI2HoKOAw7jj4OYMLXHooIT-DRVupAAK7AgACEgREU80sVRMs8Ov8IwQ',
    'h_9': 'CAACAgQAAxkDAAICE2HoKMuBh1WuArVnwYGFQa0UwNRtAALsAgACCyJEU2bokg9RuzzUIwQ',
    'h_10': 'CAACAgQAAxkDAAICImHoKNzMwg69xMvdXDEufNzRQ3odAAK6AgAC67JEU46PGpQ2Cjr8IwQ',
    'h_J': 'CAACAgQAAxkDAAICGGHoKM5N6CoPECjLk1KFBFb6yGcbAAKnAgAC7sdEU6e-1fTD3VP_IwQ',
    'h_Q': 'CAACAgQAAxkDAAICMGHoKUxRNQYicOZg-Mmq6Jo9ykzfAALtAgAC6CJEU7X9g2miS6NBIwQ',
    'h_K': 'CAACAgQAAxkDAAICHGHoKNOmvCApM5yYRXsL7afnS_gPAAKnAgAC7DlMU_EgSKXs-O8wIwQ',
    'c_A': 'CAACAgQAAxkDAAIB9WHoJ2crsi7TFspPcIsGN4gUnpqMAAKtAgACCpdFU9SfwkP0VaFtIwQ',
    'c_2': 'CAACAgQAAxkDAAICFGHoKMucSb1fm29lRyJZ1w1ldJFnAAKRAgACJzhNUwjaLIqd9nbJIwQ',
    'c_3': 'CAACAgQAAxkDAAICIGHoKNnhcP04q-ZGM0iquxAJlKOHAAKpAgACN9hFUzpAopJ9nFryIwQ',
    'c_4': 'CAACAgQAAxkDAAIB8mHoJ2SAR4wI0LcW2Dp1_MPseyO8AALgAgACDORFU_H1tFZ8JLrWIwQ',
    'c_5': 'CAACAgQAAxkDAAIBymHoJcVxTZ6wz4NwHHpeZeqHDtwIAAJ7AgACpW5MU_jRGglgSIApIwQ',
    'c_6': 'CAACAgQAAxkDAAIBv2HoJa9kqqpTc_H6RzNczrZP6TZvAALWAgAC6VREUwa5m3vydEBDIwQ',
    'c_7': 'CAACAgQAAxkDAAICFmHoKMwCWbiq1pc2yedghG6CsUjuAALDAgACXtRFU6CZ2GWkfaV6IwQ',
    'c_8': 'CAACAgQAAxkDAAICG2HoKNOLv56gpfGEuhtQJxdO7MkgAALBAgACejFEU9U_D1aKBjbaIwQ',
    'c_9': 'CAACAgQAAxkDAAIBxmHoJb1jMfq3lPqRc70L2sFswpyyAAKnAgACNRdFU8xtJkYq5_6HIwQ',
    'c_10': 'CAACAgQAAxkDAAICMWHoKUxaGAw8PEtcc9XTMsfU8j_aAAK1AgACqs9FU00cm1dwpYkIIwQ',
    'c_J': 'CAACAgQAAxkDAAIB82HoJ2Uj5lfcuyER4fzDdQq38cqdAAJ7AgACokVMUwABPzYf8iJbbiME',
    'c_Q': 'CAACAgQAAxkDAAIBvmHoJa2yZ2qnyIGWPJQ9JEPLb20LAALZAgACVFRFUxIzPlim-JrPIwQ',
    'c_K': 'CAACAgQAAxkDAAICJmHoKOPjPsYLo7_74HT3jkB5WOzqAALfAgAC50RFU9YoDJaFLLW_IwQ',
    'option_info': 'BQADBAADxAIAAl9XmQABC5v3Z77VLfEC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg',
    '1':'CAACAgQAAxkDAAICMmHoKUx7YXnwXrB7zzh2q7j0YdH4AALEAgACRT1FU39aUImHp-9NIwQ',
    '2':'CAACAgQAAxkDAAICM2HoKU3ik8PBjDqq71o7wGc_Pf-MAALPAgAC49ZFU_ZwKkhoPpuVIwQ',
    '3':'CAACAgQAAxkDAAICNGHoKU3HvaCecZ-lRjhkTrTtKDZMAALdAgACwjlEU8d9ftiedwY4IwQ',
    '4':'CAACAgQAAxkDAAICNWHoKVGTUrpmt7jLeH7M6dXDd7D-AAKQAgAC47dFU-736uhK5jQ8IwQ',
    '5':'CAACAgQAAxkDAAICNmHoKVITopVAj1uG6LoLleJiQXJPAAKbAgACoSlEU7PZ_civnBp8IwQ',
}
STICKERS_PACK = {
    "CAACAgUAAxkBAAIWS2I5UIPAAUd6c6p4plorK6gDstOcAAKIBQACLdzIVWSMsGIoWHugIwQ":"s_2",
    "CAACAgUAAxkBAAIWTGI5UIeKKdPoo0HgaXkiSOaXmjqqAAL5AgACYKdwVHSJ8yz32yOoIwQ":"s_3",
    "CAACAgUAAxkBAAIWTWI5UIgyLToClgXIXiXJDYIn59D4AAItBQACCDhoVHtE-Yx3S6uGIwQ":"s_4",
    "CAACAgUAAxkBAAIWTmI5UIg7jW1p0RGksxqORGLN8CkgAAI5BAACT4NwVH4gQMWaybQQIwQ":"s_5",
    "CAACAgUAAxkBAAIWT2I5UImWPK8HWCvf6DBXmBITNTcbAALUBQACPgFwVAHy4d-gE8dMIwQ":"s_6",
    "CAACAgUAAxkBAAIWUGI5UIl2HvLyC822L-X66OztX9GtAAKaBQACfKRpVJrezhi111XIIwQ":"s_7",
    "CAACAgUAAxkBAAIWUWI5UIqAPoOzG-yCeXj0XoDXXt62AAIJBAACJ_txVLM5xgH1kfGlIwQ":"s_8",
    "CAACAgUAAxkBAAIWUmI5UIqOYqhswJVscbhKys9c9x-8AAJJBQACDRJwVI4WcU7hGBg3IwQ":"s_9",
    "CAACAgUAAxkBAAIWU2I5UIri3pfFkzNI2AbqGw5cw9FuAAIxBAACiTVxVIMz8My1zX3SIwQ":"s_10",
    "CAACAgUAAxkBAAIWVGI5UIwWEqzoxzrBZtitKNSgrb56AAIJBQACLVFxVE22J7UQyGAbIwQ":"s_A",
    "CAACAgUAAxkBAAIWVWI5UIztePIXWNIgM6huCeglQURKAAJmBAACcStpVFrn17pWvcuYIwQ":"s_J",
    "CAACAgUAAxkBAAIWVmI5UI1ym400ZDvrUqzD9tiJE7DlAAJfBQACJg5xVAU-KqHsKzrjIwQ":"s_K",
    "CAACAgUAAxkBAAIWV2I5UI3SW98e6YewyA1DoKGUTrp_AAKZAwACnk9xVGzSv6L9ooE2IwQ":"s_Q",
    "CAACAgUAAxkBAAIWWWI5ULwv8avGa4C-gd_BvCLlN-8kAAI4BQACUUdwVPunS3S9VN5iIwQ":"d_2",
    "CAACAgUAAxkBAAIWWmI5ULy3KTaetxSm82Xfk8G3SpSbAAJYAwACusNwVIxnYUorNa51IwQ":"d_3",
    "CAACAgUAAxkBAAIWW2I5UL2dLQL-qWj_7iVAV80zvhdbAAIMBQACjhFwVCLlciL8V_xkIwQ":"d_4",
    "CAACAgUAAxkBAAIWXGI5UL4fQKHqp44AARNva3haD1BCTwACcgYAAoJ_aFQZ_esb_JyjSSME":"d_5",
    "CAACAgUAAxkBAAIWXWI5UL5MT5Q_419aGmwZCYzt_aEpAAI_BAACy_FwVGOlq1YAAYnL9iME":"d_6",
    "CAACAgUAAxkBAAIWXmI5UL6jGGUXoS0O5MrQ6MKRNv5iAAJZAwACMV9wVGeNn_ofrvZ6IwQ":"d_7",
    "CAACAgUAAxkBAAIWX2I5UL_TvwwhEVgr8StIMwEP-ZxBAAKOBAACWNBwVMR86hAycvA_IwQ":"d_8",
    "CAACAgUAAxkBAAIWYGI5UMBuGeLAPZgOO7Vp-DMzAAEDHwACawgAAslecFRsqqHclucO2CME":"d_9",
    "CAACAgUAAxkBAAIWYWI5UMDlLOMgyr-UhbQuN1Zg8HJKAAKEBAACLEpxVKObKK5znTHzIwQ":"d_10",
    "CAACAgUAAxkBAAIWYmI5UME6QpoDUHYbE61lgt0Gf7z3AAIMBAAC9xJxVM13Lb2Vzan1IwQ":"d_A",
    "CAACAgUAAxkBAAIWY2I5UMHR_nYnqvWqKgo0YIWQDIAKAAIUBAACj9pwVEEaaS8NOrCUIwQ":"d_J",
    "CAACAgUAAxkBAAIWZGI5UMI5jPdjXJH6G88dQGKN2BosAAL0BAACsSBwVIJZnx_YClmlIwQ":"d_K",
    "CAACAgUAAxkBAAIWZWI5UMM55jAsMW3oXjxo4SMH0WMUAALDBAACj9HIVaGQQLBO6uPOIwQ":"d_Q",
    "CAACAgUAAxkBAAIWZ2I5UO8tFhCX9hfYO58H8t0Y3FwEAAJ3BgACgVLRVSUFDl061oLbIwQ":"h_2",
    "CAACAgUAAxkBAAIWaGI5UPB852h9gBZwbgHBgt8e3O7hAAI4BQACxHLJVcd0GIB78dMEIwQ":"h_3",
    "CAACAgUAAxkBAAIWaWI5UPDFpMO28Tdw5fObdiDes43xAAKZBQAC8J7IVZEDhEBVx_-wIwQ":"h_4",
    "CAACAgUAAxkBAAIWamI5UPDk1VsxVEm5kcIH2YV2aP6NAAKoAwACMoHJVZPw9TNvn1jHIwQ":"h_5",
    "CAACAgUAAxkBAAIWa2I5UPDv7AU4ebTn9yS49z47JmCUAALBBgACusDQVbKt0Z7W2kjYIwQ":"h_6",
    "CAACAgUAAxkBAAIWbGI5UPCDQ1YpKFeXtMJcvIsPU-a9AAJhBwACuoLJVcQ1h-2O9yPyIwQ":"h_7",
    "CAACAgUAAxkBAAIWbWI5UPCziQIV4ZpmcPYLVZfK5hLrAAI_BAACZIfQVYoVQWlKwKazIwQ":"h_8",
    "CAACAgUAAxkBAAIWbmI5UPA6wr4xifJJgKnBdLFmmHjpAAKEBgACbZbIVRIZy4GUYbEBIwQ":"h_9",
    "CAACAgUAAxkBAAIWb2I5UPC9er0xUZx9w8U_WbKK-th1AAKwBAAC42fIVYonhrkOa6acIwQ":"h_10",
    "CAACAgUAAxkBAAIWcGI5UPBNJ5rq0N8tK4w84WpsCj5nAAJQBAACPCvIVRz6Z15Ok6fvIwQ":"h_A",
    "CAACAgUAAxkBAAIWcWI5UPIYfC3pLJbje0l2HUOyvJh3AAJIBQACXJTQVX1gtO_94sT-IwQ":"h_J",
    "CAACAgUAAxkBAAIWcmI5UPJRlzEGM2c1WClGHLt46jUKAAIFBQAC9mfJVUJvbyPWQKnvIwQ":"h_K",
    "CAACAgUAAxkBAAIWc2I5UPIKvkBGJgKxobaMvVuYCTGXAALtBQACiMPRVf-vlyb5Cs8PIwQ":"h_Q",
    "CAACAgUAAxkBAAIWdWI5URL7l6ER1xmW8lIL9J3WGyMlAALhBAACUdPQVRjB9dFIj3dAIwQ":"c_2",
    "CAACAgUAAxkBAAIWdmI5URO5JehL4X8OGExdxJgrIGo3AAJmBQAClIDQVXuowfdW6gzSIwQ":"c_3",
    "CAACAgUAAxkBAAIWd2I5URTHiRN3rd8oDwQV1YwrVll_AAKRBAACwprRVdWCi013cVAeIwQ":"c_4",
    "CAACAgUAAxkBAAIWeGI5URTrvUXdh48MrnGKwDoq2hJ2AAKuBgACd2HIVfn4I9NGOn0JIwQ":"c_5",
    "CAACAgUAAxkBAAIWeWI5URWQEE60DUHqcdww197R-aflAAL5BQAClajIVcn0dY-jnw0BIwQ":"c_6",
    "CAACAgUAAxkBAAIWemI5URVshjJySWHDymdKhRQJ3yBzAAKgBgACcqjJVb4HeLHcqLY1IwQ":"c_7",
    "CAACAgUAAxkBAAIWe2I5URafSOgOwh41skkxax9lPXD3AAJFBAACUtHJVTt_wJvkygFHIwQ":"c_8",
    "CAACAgUAAxkBAAIWfGI5UReTX8b8Zl5igqiHfndgG9iWAAI6BQAC7DzIVTBCbU7KKU6mIwQ":"c_9",
    "CAACAgUAAxkBAAIWfWI5URhUGfNQzmb-Twh79ObxdeRLAAKbBQACf43JVZD4DZiIhAK9IwQ":"c_10",
    "CAACAgUAAxkBAAIWfmI5URjroEAI2ZAhJgc1Ed8RGJXIAAJiBQAClQXJVdHZA_NOGS2wIwQ":"c_A",
    "CAACAgUAAxkBAAIWf2I5URhcHTf_fNtvLB80i_cgW0-3AAIVBgACvpvJVYdqh3BO3jcOIwQ":"c_J",
    "CAACAgUAAxkBAAIWgGI5URgG-6lNaoawfSWgotOjobK4AAL-AwACeuPIVesgZiCYafTpIwQ":"c_K",
    "CAACAgUAAxkBAAIWgWI5URkVihVpqTyz25A2e3RHx4wLAAINBAACA07RVYKeyzPQ-NQRIwQ":"c_Q",
}
OLD_STICKERS_GRAY = {'d_A': 'CAACAgQAAxkDAAICr2HoLR5fAAEtySS3q-FtE19YLw07kwACwgIAAveUTVMvgvvvNWnWuSME', 
                'd_2': 'CAACAgQAAxkDAAIClGHoLMbGsAlQcL0F8ICg_KLNs3FEAAK_AgACu0JEU2FosTKYahEJIwQ', 
                'd_3': 'CAACAgQAAxkDAAICmmHoLM1giWNH805Qr7BY2iZQk4pJAAIYAwACgKJFU4n6wl4NnWBIIwQ', 
                'd_4': 'CAACAgQAAxkDAAICeWHoLGib_52u2z8VpgABiRgQ-FnGkwACmwIAAncvRFP2HN2gR3VLiiME', 
                'd_5': 'CAACAgQAAxkDAAICqWHoLRiMzPD5jBIKn_F9nIfHT111AAKbAgACtwREU6M-z6em0puzIwQ', 
                'd_6': 'CAACAgQAAxkDAAIChGHoLHoVYyB8R2N1L57CYseP76W0AAKNAgACfotMU6Wxhlmk8PrLIwQ', 
                'd_7': 'CAACAgQAAxkDAAICtWHoLSi8rXjuX4ZaFctTrLayYg31AAL-AgACLJREU-F4aib7ZkIXIwQ', 
                'd_8': 'CAACAgQAAxkDAAICd2HoLGZCTMcytKXCrYsDw4SYfUFcAALBAgACzqtFU_3i2NU9sLAUIwQ', 
                'd_9': 'CAACAgQAAxkDAAICtGHoLSauJhtEvAqx5y7jial5viY7AAIRAwACJDBFU3qa4e7BaTRfIwQ', 
                'd_10': 'CAACAgQAAxkDAAIClmHoLMqHJDMpEa-CB3sjP28dT_MwAAL0AgACPoVEU7n6iU9CwJczIwQ', 
                'd_J': 'CAACAgQAAxkDAAICeGHoLGcqgT6fdxLpCxzFQ-uf7322AALJAgACOB5EU0BAtuTzLVg3IwQ', 
                'd_Q': 'CAACAgQAAxkDAAIChWHoLHuk58WGJCIlRrFehf6yYyCyAAKbAgACqaNMU1wdZdQpZ5PIIwQ', 
                'd_K': 'CAACAgQAAxkDAAICmGHoLMx2v0K91pWWkyyTZHEwbnKuAAIBAwACikpEU_v9EVrM81T8IwQ', 
                's_A': 'CAACAgQAAxkDAAICg2HoLHkKA2JMmzsXYTNJaquBgz6AAALkAgAC-d9EU-jD30SGgH9JIwQ', 
                's_2': 'CAACAgQAAxkDAAICfmHoLHLg3UDos0g77qK4rcd8IGhzAAIJAwACYgREU5IaIYstWSVjIwQ', 
                's_3': 'CAACAgQAAxkDAAICrmHoLRy3vZId7xOkobSmnn1WIYyNAALvAgACqF5EU2-pdw_2AUpeIwQ', 
                's_4': 'CAACAgQAAxkDAAIClWHoLMmymv_VTxGC1TPOFlruITbwAAIgAwAChQJFU7sz6CJbovcGIwQ', 
                's_5': 'CAACAgQAAxkDAAICpmHoLRHbYvEh3GbS61s5phzqf1inAAL5AgACF5BFU6phJzp5EO1NIwQ', 
                's_6': 'CAACAgQAAxkDAAICkGHoLMRUOXx9k8rrRzQAAdAD-IEdbwACwwIAAlPXRFMJyO97OrkooiME', 
                's_7': 'CAACAgQAAxkDAAICdmHoLGWDaPdyUVk7AqVcCVhQfxdnAALBAgACLydEUw0bnWfmj2VwIwQ', 
                's_8': 'CAACAgQAAxkDAAICsGHoLR6Z0yPo0_K-FoXz0ju-FtKYAALWAgACtz9EU91vlykg301BIwQ', 
                's_9': 'CAACAgQAAxkDAAICrWHoLRy6W66nKSxkBj8yrkxDJUV2AAKhAgAC_aZNU9h6hd3nick_IwQ', 
                's_10': 'CAACAgQAAxkDAAICmWHoLMzm_sLdrnED0y_y-96_QGPRAAKnAgAC3wFMUzl_BPzlSbH7IwQ', 
                's_J': 'CAACAgQAAxkDAAICsWHoLSJTtP_I0yUoZBJa3zTn170-AAMDAAK6MUVTJ8-4D9fPXG4jBA', 
                's_Q': 'CAACAgQAAxkDAAICk2HoLMYxE62wXOWjm19CQwUd4ZKUAAKeAgAC-W5NUzkCuEzHLdHWIwQ', 
                's_K': 'CAACAgQAAxkDAAICq2HoLRtrVw8nyE_xoRYTw-qahJMYAAIUAwACA4pEU64bdYV0PiKQIwQ', 
                'h_A': 'CAACAgQAAxkDAAICgGHoLHVL9P_I3NWLch9mLErkmZTPAALQAgAC3E1FUx9TrrZagjl5IwQ', 
                'h_2': 'CAACAgQAAxkDAAICpWHoLRFYJ9bUGQLW2jCKN7o5MNN0AAL5AgAC-HxEU6GjEOxTbilzIwQ', 
                'h_3': 'CAACAgQAAxkDAAICdWHoLGXmOJ9j8hYOM_TMBC7ONIlCAAKtAgACyiVEU6qsWCl8knfEIwQ', 
                'h_4': 'CAACAgQAAxkDAAICf2HoLHS3O3jxkmI-HJ3aK4dHjYn4AAK6AgACS4BEU7Fhf8YafWLMIwQ', 
                'h_5': 'CAACAgQAAxkDAAICrGHoLRsnJXApscrn5-Dz3Idl_6wAA-cCAAI6bEVTyz7Hainh9ikjBA', 
                'h_6': 'CAACAgQAAxkDAAICqGHoLRUb_YUvW-ww7YKkuz243dcMAALPAgACB2hEU-KbfFJMfwwYIwQ', 
                'h_7': 'CAACAgQAAxkDAAICpGHoLRBjAAE9D9tPi5QcNOC001PCuQACwwIAAsvDRVO05mGREcD0NiME', 
                'h_8': 'CAACAgQAAxkDAAICkmHoLMXs_nRhrWubwFwjMSW43fPGAAKuAgACUTtFU__wJhVmlOawIwQ', 
                'h_9': 'CAACAgQAAxkDAAICs2HoLSSKaLFqsR-cBy7Dj8u9UB5nAALKAgAC7YZFU8sjLtbc6MM9IwQ', 
                'h_10': 'CAACAgQAAxkDAAICgWHoLHb3HI_axm3Q5aE-LkRLKeBBAALEAgACDN5EU4Sn_ycok8v1IwQ', 
                'h_J': 'CAACAgQAAxkDAAICfWHoLG4PGbvxyca85rbTR2LFunQgAAK9AgACc2ZEU3PlfA5WBkzBIwQ', 
                'h_Q': 'CAACAgQAAxkDAAIChmHoLHwFdBz5U_q9_3Z-hFjTVJcRAALZAgACMGFEUy7Btisa935xIwQ', 
                'h_K': 'CAACAgQAAxkDAAICo2HoLRDcES6uDcAhKi60xFUIBNAtAAIGAwACkUZFU2Wrurt-M8vHIwQ', 
                'c_A': 'CAACAgQAAxkDAAICdGHoLGKRxEhe-v2dgdrNq9yIyq7ZAALMAgACTEFEU_SbB7oR946WIwQ',
                'c_2': 'CAACAgQAAxkDAAICfGHoLGz0_wW8vZL0FijySyZ4EJa4AALLAgAC8yxFU8y89p8-ljOqIwQ', 
                'c_3': 'CAACAgQAAxkDAAICh2HoLH1orJzRydMCW44kJGA4svj9AAL-AgAC36REU4Sl0Ea5D0xDIwQ', 
                'c_4': 'CAACAgQAAxkDAAICp2HoLRNZRESq981WJpcC8nzGd99tAAL1AgACXcNEU5wObPwTC94DIwQ', 
                'c_5': 'CAACAgQAAxkDAAICgmHoLHefEIsSykISFBjwBu2d5aXHAAKpAgAC3y9EU4o_UKPC_qQYIwQ', 
                'c_6': 'CAACAgQAAxkDAAICsmHoLSJedB43oEooLdNj5o8QuFovAAJ-AgACBJREU7MiOPKV1QUbIwQ', 
                'c_7': 'CAACAgQAAxkDAAICl2HoLMs0cnIJPJOutkrHXwHD8JLaAALfAgACZbVFU17lJblDu5OIIwQ', 
                'c_8': 'CAACAgQAAxkDAAICtmHoLSn3svTue_-KDLzBUhEQvAJSAALDAgACXCtEU3EHejSF_8T-IwQ', 
                'c_9': 'CAACAgQAAxkDAAICqmHoLRlBmCti2IGH9M8Hhmrb7bSJAALSAgAC7ZBFU2xJRdyTRRLyIwQ', 
                'c_10': 'CAACAgQAAxkDAAICemHoLGmoGNhsiYMI5wQvUVsSkcnRAALhAgAC28pEUzS9ztMw9eEaIwQ', 
                'c_J': 'CAACAgQAAxkDAAICiGHoLH7dKVU6fEFfAr_r4fAP6BVIAAK_AgACdSZFUwG4AdPYToWwIwQ', 
                'c_Q': 'CAACAgQAAxkDAAICkWHoLMT9SO5ebik8rHoWt4uNrJyuAALNAgACMsNEU_Jv1DnuBiRnIwQ', 
                'c_K': 'CAACAgQAAxkDAAICe2HoLGp_f79fcuv8UNcRlfJJZ_FMAALPAgACwFFFU-CpmlMsm-TIIwQ'}

STICKERS_GRAY = {
    'd_A': 'CAACAgQAAxkDAAIxqmKGKDKsHPof2zzMn7fkHHI2rkO-AAJDAwACKnk0UKOkoqHqpcnuJAQ',
    'd_2': 'CAACAgQAAxkDAAIxq2KGKDRmZc5jeBEzNsrrAAFgVwffsgACDAMAAu39NFBx_bODKy3C2CQE',
    'd_3': 'CAACAgQAAxkDAAIxrGKGKDVcihEZBgozBTM1C_DmEdgNAAJNAwAC2-g1UFiJswopQR84JAQ',
    'd_4': 'CAACAgQAAxkDAAIxrWKGKDZrMdMvtiw3ul4lHteiBgoWAAIdAwACM100UKrwr--ClWb4JAQ',
    'd_5': 'CAACAgQAAxkDAAIxrmKGKDfd7by-ngABvWEyxwPj34F_WAACAQMAApARPFBRV0EQfmsc6CQE',
    'd_6': 'CAACAgQAAxkDAAIxr2KGKDlXHWjFdxDAp4mW800vfjGxAAIjAwACLU89UO_I9hw1ub0BJAQ',
    'd_7': 'CAACAgQAAxkDAAIxsGKGKDppikbd3nMd_ZswISgaIujYAAI0AwAC39M1UAXFA5NcmD1xJAQ',
    'd_8': 'CAACAgQAAxkDAAIxsWKGKDuHpYGadTuCw89sodUui7IIAALuAgACRPI1UBI6u9w6uR84JAQ',
    'd_9': 'CAACAgQAAxkDAAIxsmKGKDwpbina9W9Sgz8Z7tAjZqgJAAIyAwACKhU1UN4SjHLMvK-kJAQ',
    'd_10': 'CAACAgQAAxkDAAIxs2KGKD3_NJqS-MjZv6W6bOPRZDCgAAIWAwACDeo0UL8SiRAcQPQIJAQ',
    'd_J': 'CAACAgQAAxkDAAIxtGKGKD60vZrWvr3fJ-7i9LzDXloYAAJCAwACOrw9UJboBXQK8WoFJAQ',
    'd_Q': 'CAACAgQAAxkDAAIxtWKGKEA1tp3TCeevwaBJAhJh8nBcAAIoAwACMBc8UGKn5rZaEX34JAQ',
    'd_K': 'CAACAgQAAxkDAAIxtmKGKEEl_JST1pSYDS29EBdILNV9AAItAwAC8EQ1UHPr1Qyld6r-JAQ',
    's_A': 'CAACAgQAAxkDAAIxt2KGKEIei_CrzRo5lvBm7pg695ENAAIYAwACD6Q1UBGgC_s_O8d8JAQ',
    's_2': 'CAACAgQAAxkDAAIxuGKGKETcDZSQHB461S2JuXTWRvGOAAIzAwACCs09UB1KgXEljn2jJAQ',
    's_3': 'CAACAgQAAxkDAAIxuWKGKEXYQqm3Qk1mJezEo-AFo6DeAAJTAwACdr40UCaXBY30V4lNJAQ',
    's_4': 'CAACAgQAAxkDAAIxumKGKElbsAo6va0uXubAuyBqvVdAAAImAwACato0UIiqMJhya3vvJAQ',
    's_5': 'CAACAgQAAxkDAAIxu2KGKEqrBinVdiuCQIOIBWkw_qCfAAJlAwAC3-o0UKmvwuoNu41AJAQ',
    's_6': 'CAACAgQAAxkDAAIxvGKGKEvU4ytSr77sblCDgzd40wOqAAIvAwACmeo1UEA6_aQqWvVlJAQ',
    's_7': 'CAACAgQAAxkDAAIxxGKGKMYwZ6nirdUQ1AwEQqzYXSB7AALYAgACVbc0UIc-sKlEQPsKJAQ',
    's_8': 'CAACAgQAAxkDAAIxxWKGKMf57QFvm5k1X_vKOMINGjgBAAI-AwACF_Q9UNcG3eArqNkCJAQ',
    's_9': 'CAACAgQAAxkDAAIxxmKGKMj02XPaiU5M0iACDvvfUNdtAAI4AwACurI1UNqfYhCqoHY4JAQ',
    's_10': 'CAACAgQAAxkDAAIxx2KGKMkq78q1EA9tQHAzTAFwnaxYAAIZAwACTlM0UHSwH92wOYqcJAQ',
    's_J': 'CAACAgQAAxkDAAIxyGKGKMlHg9i9nZ9kDAsVRTn3JtUqAAIvAwAC8XY0UFplYLo7LJFvJAQ',
    's_Q': 'CAACAgQAAxkDAAIxyWKGKMqLZ5gkHmh0r3Rke2Zuj69oAAJOAwACMWs0UELM3d7uxFJTJAQ',
    's_K': 'CAACAgQAAxkDAAIxymKGKM63ncYiqW4eNGMq5HnIWAxLAAIeAwACuXk1UCeMvIRwqmYbJAQ',
    'h_A': 'CAACAgQAAxkDAAIxy2KGKM8cH7u9pjFyNHZivX-sLtx9AAIkAwAClls1UDsaEcyZXiIYJAQ',
    'h_2': 'CAACAgQAAxkDAAIxzGKGKNDZryz7nEgTrfqGX0rcIKegAALyAgAChcY1UPC2ixvTFaJdJAQ',
    'h_3': 'CAACAgQAAxkDAAIxzWKGKNLndJIblfV3np644AXtt7BcAAJDAwACTGA9UBXEF61VsYwEJAQ',
    'h_4': 'CAACAgQAAxkDAAIxzmKGKNPJLNym0sKkouVJt1rlPXCsAAITAwACLkY0UELUZRVoVBNSJAQ',
    'h_5': 'CAACAgQAAxkDAAIxz2KGKNUgobTJ9Eq_HRCspYA1nw2vAAIUAwAC7hk1UGeICzG9HfkxJAQ',
    'h_6': 'CAACAgQAAxkDAAIx0GKGKNdEWBauGziADQjA3x6bEYZMAAItAwACn-U1UO8bJbprqVmVJAQ',
    'h_7': 'CAACAgQAAxkDAAIx0WKGKNmULH7kviAjNjq-7tzJoIj6AAIWAwACYqY9UD7gEDQJRs3HJAQ',
    'h_8': 'CAACAgQAAxkDAAIx0mKGKNt87g6xouzXtSPuYo7uwXqqAALvAgACtCs1UNMMPOVK2ea-JAQ',
    'h_9': 'CAACAgQAAxkDAAIx02KGKNxnx3D4i0GmvNU4BlNQm9_zAAIpAwACHYg0UO2lm7V50QwDJAQ',
    'h_10': 'CAACAgQAAxkDAAIx1GKGKN5YpPElRJcwZPU4Gf8vS7STAAL_AgAC1EM0UKhrCEjqYgvvJAQ',
    'h_J': 'CAACAgQAAxkDAAIx1WKGKOGwxEpTToP8B1Dy6rLK1YChAAIpAwACW_I8UCPp39Ps5RFVJAQ',
    'h_Q': 'CAACAgQAAxkDAAIx1mKGKOOaH3rSjedOk04rS0YYEBJaAALRAgACRxE1UH0sbvk_L5neJAQ',
    'h_K': 'CAACAgQAAxkDAAIx12KGKOXC-uvrAaBTKl2ZYC7pYB5gAALsAgACDwABNFBB1qla8Z2W8CQE',
    'c_A': 'CAACAgQAAxkDAAIx2GKGKOeHgC0VWbBslO6D5j8GwtFHAAIVAwACfUw1UG1pwyTVoK8XJAQ',
    'c_2': 'CAACAgQAAxkDAAIx2mKGKRWcqsDZuw_4OFaQ0RCaE3wHAAIPAwAC9240UG-JJZUWXPlvJAQ',
    'c_3': 'CAACAgQAAxkDAAIx22KGKRZarQOp4vro1vDCoKJDrUMCAAJLAwACJH00UJwZRsd7qz9uJAQ',
    'c_4': 'CAACAgQAAxkDAAIx3GKGKRgMSQoPaRh9JH1KTTTSBXrWAAJJAwACsAo1ULG4ZcCTPGR7JAQ',
    'c_5': 'CAACAgQAAxkDAAIx3WKGKRl1qqu_ufWIwM5QE2abpGjWAAILAwACEqw1UBOEYG_9LVJGJAQ',
    'c_6': 'CAACAgQAAxkDAAIx3mKGKRuwwzV2-FN9e0-qn_zDduBmAAIcAwACPkI1UH8MXc6YmAZMJAQ',
    'c_7': 'CAACAgQAAxkDAAIx32KGKRw12BbY2d7FCZiYYj4wQYaMAAI6AwACqYk8UJEhMpeLr20TJAQ',
    'c_8': 'CAACAgQAAxkDAAIx4GKGKR1jHcTJplxy8vEQG0b6r6KKAAJOAwACIdk8UA-7n2aRs8SRJAQ',
    'c_9': 'CAACAgQAAxkDAAIx4WKGKR5NqFScpwwtIhUNAnwagtTrAAIpAwAC_mg0ULAvmd2-eHZ3JAQ',
    'c_10': 'CAACAgQAAxkDAAIx4mKGKR-z0G75uTbXJN-mLwVOLcjTAAITAwACHuk0UMh8y7CmuQ23JAQ',
    'c_J': 'CAACAgQAAxkDAAIx42KGKSFuaGRQ5pEzdcLoxHPhoNBoAAL3AgACppE1UNq6c1bChnZWJAQ',
    'c_Q': 'CAACAgQAAxkDAAIx5GKGKSISzXsRkCxFVP_wwzkadDcvAAJxAwAC33o0UE0na4QUjkuCJAQ',
    'c_K': 'CAACAgQAAxkDAAIx5WKGKSL6d4twNYpIWsIgZt7XujuYAAIVAwACvJQ9UOU39PDbpHqAJAQ',
    }


class Card(object):
    """This class represents a card"""
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return '%s_%s' % (self.suit, self.value)

    def __repr__(self):
        return '%s%s' % (SUIT_ICONS[self.suit], self.value.capitalize())

    def __eq__(self, other):
        if type(other) is str:
            suit,val = str(other).split('_')
            othercard = Card(suit,val)
        else:
            othercard = other
        """Needed for sorting the cards"""
        return SUITS_VALUES[self.suit] == SUITS_VALUES[othercard.suit] and VALUE_VALUES[self.value] == VALUE_VALUES[othercard.value] 

    def __lt__(self, other):
        """Needed for sorting the cards"""
        if type(other) is str:
            other = from_str(other)
        if(VALUE_VALUES[self.value] == VALUE_VALUES[other.value]):
            return SUITS_VALUES[self.suit] < SUITS_VALUES[other.suit]
        if self.value == '0':
            return True
        elif other.value == '0':
            return False
        return VALUE_VALUES[self.value] < VALUE_VALUES[other.value]

    def compare_suit(self,other):
        """Needed for comparing suits"""
        #True if higher; False if lower
        if(self.suit == 'd'):
            return True
        if(self.suit == 's'):
            if(other.suit == 'd'):
                return False
        if(self.suit == 'h'):
            if(other.suit == 'd' or other.suit == 's'):
                return False
        if(self.suit == 'c'):
            return False
        return True

    def get_numval(self):
        return VALUE_VALUES[self.value]
    
def from_str(string):
    """Decodes a Card object from a string"""
    suit, value = string.split('_')
    return Card(suit, value)
