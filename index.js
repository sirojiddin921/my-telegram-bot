const TelegramBot = require('node-telegram-bot-api');

// Tokeningizni shu yerga joylashtiring
const API_TOKEN = '7897812912:AAGK-6fHZ34MrQpz71hlk9pKjeVJW4Wre-g';

// Botni polling rejimida ishga tushurish
const bot = new TelegramBot(API_TOKEN, { polling: true });

// Start komandasini qayta ishlash
bot.onText(/\/start/, (msg) => {
    const chatId = msg.chat.id;
    console.log('Start komandasi yuborildi'); // Start komandasi yuborilganda xabar chiqariladi
    bot.sendMessage(chatId, 'Assalomu alaykum! O\'zbekistonga xush kelibsiz.');
});

// Xabarlarni qayta ishlash
bot.on('message', (msg) => {
    const chatId = msg.chat.id;
    console.log('Xabar qabul qilindi:', msg.text); // Xabar qabul qilganda xabarni chiqaradi
    if (msg.text.toLowerCase() === 'salom') {
        bot.sendMessage(chatId, 'Salom! Yordam bera olishim mumkinmi?');
    }
});
