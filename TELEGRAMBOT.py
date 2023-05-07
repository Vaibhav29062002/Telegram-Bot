import telebot


Token = "6275167168:AAFG440RbTZktYBoMSlk9qiF8q4YsTX124A"
bot = telebot.TeleBot(Token)


@bot.message_handler(['start', 'hello'])
def start(message):
    bot.reply_to(message, "Welcome to Store. You are a valuable customer to us. Kindly click here to access all the features /help")
@bot.message_handler(['Suggest'])
def start(message):
    bot.reply_to(message, "Tea with Noodles is the Perfect Combo.To order Select item no /2 , /6 and /7 ")


@bot.message_handler(['help'])
def help(message):
    bot.reply_to(message, """
    /start -> Greeting
    /INVENTORY -> Will give u all the items in Inventory
    /order -> Select the items to be purchased
    /help -> Will give you all command list
    /total ->Will give u the total bill
    /Status -> Will tell u about the status of your order
    /confirm -> Select yes or no for accepting or declining the order
    /Suggest -> Suggest you items to buy
    
    
    
    """)
@bot.message_handler(['INVENTORY'])
def INVENTORY(message):
    bot.reply_to(message, """ THE PRODUCT THAT ARE AVAILABLE ARE 
                          1 RICE
                                Price= 108 Rs/Kg
                                Quantity= 1kg,5Kg Packets Available
                                Type = Basmati
                                Brand = Fortune                         
                          2 MILK
                                Price= 54 Rs/L
                                Quantity= 1 litre Packets Available
                                Type = Toned
                                Brand = AMUL
                          3 SOYABEAN
                                Price= 10 Rs/packet
                                Quantity= 1 litre Packets Available
                                Type = Toned
                                Brand = Fortune  
                          4 MUSTARD OIL
                                Price= 145 Rs/litre
                                Quantity= 1 litre,5 litre
                                Type = Kachi Ghani
                                Brand = Fortune
                          5 SALT  
                                Price= 25 Rs/kg
                                Quantity= 1 kg
                                Type = Iodised Salt
                                Brand = Tata Salt
                          6 SUGAR  
                                Price= 60 Rs/kg
                                Quantity= 1 kg
                                Type = Refined Sugar
                                Brand = Madhur Sugar
                          7 NOODLES  
                                Price= 14 Rs/Packet
                                Quantity= 70gm
                                Type = Masala Instant Noodles
                                Brand = MAGGI
                          8 TOOTHPASTE  
                                Price= 105 Rs/Packet
                                Quantity= 200gm
                                Type = Natural Toothpaste
                                Brand = Patanjali Dant Kanti 
                          9 DETERGENT  
                                Price= 129 Rs/kg
                                Quantity= 1 Kg
                                Type = Wash Detergent
                                Brand = Surf Excel
                          10 ATTA  
                                Price= 65 Rs/kg
                                Quantity= 1 Kg
                                Type = Organic Atta
                                Brand = Aashirvaad
                          11 GHEE
                                Price=  580 Rs/packet
                                Quantity= 900 ml
                                Type = Desi Ghee
                                Brand = Ananda
                          12 SHAMPOO
                                Price=  72 Rs/kg
                                Quantity= 80 ml
                                Type = Desi Ghee
                                Brand = Ananda""")
@bot.message_handler(['order'])
def start(message):
    bot.reply_to(message, "Enter the Item No in Inventory to know the price. Kindly use / before the no")

@bot.message_handler(['1'])
def start(message):
    bot.reply_to(message, "RICE Price 108")
@bot.message_handler(['2'])
def start(message):
    bot.reply_to(message, "MILK Price 54")
@bot.message_handler(['3'])
def start(message):
    bot.reply_to(message, "SOYABEAN Price 10")
@bot.message_handler(['4'])
def start(message):
    bot.reply_to(message, "MUSTARD OIL Price 145")
@bot.message_handler(['5'])
def start(message):
    bot.reply_to(message, "SALT Price 25")
@bot.message_handler(['6'])
def start(message):
    bot.reply_to(message, "SUGAR Price 60")
@bot.message_handler(['7'])
def start(message):
    bot.reply_to(message, "NOODLES Price 14")
@bot.message_handler(['8'])
def start(message):
    bot.reply_to(message, "TOOTHPASTE Price 105")
@bot.message_handler(['9'])
def start(message):
    bot.reply_to(message, "DETERGENT Price 129")
@bot.message_handler(['10'])
def start(message):
    bot.reply_to(message, "ATTA Price 65")
@bot.message_handler(['11'])
def start(message):
    bot.reply_to(message, "GHEE Price 580")
@bot.message_handler(['12'])
def start(message):
    bot.reply_to(message, "SHAMPOO Price 72")
@bot.message_handler(['total'])
def start(message):
    bot.reply_to(message, "Kindly Enter the (/order)* (the quantity) to get the total")
@bot.message_handler(['confirm'])
def start(message):
    bot.reply_to(message, "Kindly Enter /yes if u want to confirm order or /no if u want to decline it")
@bot.message_handler(['yes'])
def start(message):
    bot.reply_to(message, "Wohoooooooo ! Order Accepted Succesfully")
@bot.message_handler(['no'])
def start(message):
    bot.reply_to(message, "We are really Sorry! for missing the opportunity to serve u.")
@bot.message_handler(['Status'])
def start(message):
    bot.reply_to(message, "Thanku for choosing our service")


@bot.message_handler()
def custom(message):
    try:
        msg = eval(message.text.strip())
    except Exception as e:
        msg = "Please use /start to interact."
    bot.reply_to(message, msg)


bot.polling()
