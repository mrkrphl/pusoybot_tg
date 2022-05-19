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
    'd_A': 'CAACAgQAAxkDAAIw12KGEa5zs1cxNWooMQQoAzIFxoSfAAIZAwACtps0UCUNaRM-pUYnJAQ',
    'd_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_2.webp',
    'd_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_3.webp',
    'd_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_4.webp',
    'd_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_5.webp',
    'd_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_6.webp',
    'd_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_7.webp',
    'd_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_8.webp',
    'd_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_9.webp',
    'd_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_10.webp',
    'd_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_J.webp',
    'd_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_Q.webp',
    'd_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_K.webp',
    's_A': 'CAACAgQAAxkDAAIw5mKGEnVBjn9Y00AMXRwXZb5CUobtAAIZAwACtps0UCUNaRM-pUYnJAQ',
    's_2': 'CAACAgQAAxkDAAIw52KGEnXQrBk8ackuNkxJ3sAehPWRAAIGAwAC6ZU1UNsBOxymR696JAQ',
    's_3': 'CAACAgQAAxkDAAIw6GKGEnb0fA1CQCMGGyRtjv2FTi-cAAI-AwACcEw1UDGpEkIZ0UkeJAQ',
    's_4': 'CAACAgQAAxkDAAIw6WKGEnaJHGXMSTUPKZ5kJdsQ15PgAAI_AwACzDU8UCeOHr_1Wka9JAQ',
    's_5': 'CAACAgQAAxkDAAIw6mKGEnaq_KvkDqyDxlzTjxH05r_fAAIxAwACEjo1UDTN7P6f322sJAQ',
    's_6': 'CAACAgQAAxkDAAIw62KGEncIYZQAAbhRXMK62Mb2KcqzLQAC2AIAAk6PNVD5AAF-hd6mkHkkBA',
    's_7': 'CAACAgQAAxkDAAIw7GKGEnroBpXTvE-HI_sO4MpL61STAALcAgACyxE0UKdh5FoDaMbzJAQ',
    's_8': 'CAACAgQAAxkDAAIw7WKGEnsDX2qFOcGUtAhwo-Vxq3PpAAInAwACtZE1UM9qr_GXR5NqJAQ',
    's_9': 'CAACAgQAAxkDAAIw7mKGEnvkQ1NFf8YFmKuuQtJA8KAtAAJpAwACB5g9UIVAivtPA-APJAQ',
    's_10': 'CAACAgQAAxkDAAIw72KGEnxDg4H3ecijjNxPYMd9vsprAAIUAwAC1t00UIKWru1hFI_2JAQ',
    's_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_J.webp',
    's_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_Q.webp',
    's_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_K.webp',
    'h_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_A.webp',
    'h_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_2.webp',
    'h_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_3.webp',
    'h_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_4.webp',
    'h_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_5.webp',
    'h_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_6.webp',
    'h_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_7.webp',
    'h_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_8.webp',
    'h_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_9.webp',
    'h_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_10.webp',
    'h_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_J.webp',
    'h_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_Q.webp',
    'h_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_K.webp',
    'c_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_A.webp',
    'c_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_2.webp',
    'c_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_3.webp',
    'c_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_4.webp',
    'c_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_5.webp',
    'c_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_6.webp',
    'c_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_7.webp',
    'c_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_8.webp',
    'c_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_9.webp',
    'c_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_10.webp',
    'c_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_J.webp',
    'c_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_Q.webp',
    'c_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_K.webp',
    'option_info': 'BQADBAADxAIAAl9XmQABC5v3Z77VLfEC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg',
    '1':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/1.webp',
    '2':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/2.webp',
    '3':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/3.webp',
    '4':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/4.webp',
    '5':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/5.webp',
}
STICKER_GRAB = {
    'd_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_A.webp',
    'd_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_2.webp',
    'd_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_3.webp',
    'd_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_4.webp',
    'd_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_5.webp',
    'd_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_6.webp',
    'd_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_7.webp',
    'd_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_8.webp',
    'd_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_9.webp',
    'd_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_10.webp',
    'd_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_J.webp',
    'd_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_Q.webp',
    'd_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/d_K.webp',
    's_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_A.webp',
    's_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_2.webp',
    's_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_3.webp',
    's_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_4.webp',
    's_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_5.webp',
    's_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_6.webp',
    's_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_7.webp',
    's_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_8.webp',
    's_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_9.webp',
    's_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_10.webp',
    's_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_J.webp',
    's_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_Q.webp',
    's_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/s_K.webp',
    'h_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_A.webp',
    'h_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_2.webp',
    'h_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_3.webp',
    'h_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_4.webp',
    'h_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_5.webp',
    'h_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_6.webp',
    'h_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_7.webp',
    'h_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_8.webp',
    'h_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_9.webp',
    'h_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_10.webp',
    'h_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_J.webp',
    'h_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_Q.webp',
    'h_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/h_K.webp',
    'c_A': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_A.webp',
    'c_2': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_2.webp',
    'c_3': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_3.webp',
    'c_4': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_4.webp',
    'c_5': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_5.webp',
    'c_6': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_6.webp',
    'c_7': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_7.webp',
    'c_8': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_8.webp',
    'c_9': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_9.webp',
    'c_10': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_10.webp',
    'c_J': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_J.webp',
    'c_Q': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_Q.webp',
    'c_K': 'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/c_K.webp',
    'option_info': 'BQADBAADxAIAAl9XmQABC5v3Z77VLfEC',
    'option_pass': 'BQADBAAD-gIAAl9XmQABcEkAAbaZ4SicAg',
    '1':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/singles.webp',
    '2':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/pair.webp',
    '3':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/trio.webp',
    '4':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/quads.webp',
    '5':'https://raw.githubusercontent.com/mrkrphl/pusoybot_tg/updated/images/webp/fives.webp',
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
STICKERS_GRAY = {'d_A': 'CAACAgQAAxkDAAICr2HoLR5fAAEtySS3q-FtE19YLw07kwACwgIAAveUTVMvgvvvNWnWuSME', 
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
