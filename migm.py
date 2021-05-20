from pyrogram import Client, filters
import sys, re, random, asyncio, emoji

class Ciente_script():

    cwb2 = 408101137
    shishi = [954122417]
    me = re.compile(r".+(?P<stamina>\W+Stamina: .+\n?).+")
    sms_quest = 'Foray is a dangerous activity. Someone can notice you and may'
    sms_go = 'You were strolling around on your horse when you noticed'
    sms_mob = 'You met some hostile creatures. Be careful:'
    sms_stamina_full = 'Stamina restored. You are ready for more adventures!'
    fcompile = re.compile(r".Forest [3|5]min \W\n.+")
    scompile = re.compile(r".+Swamp [4|6]min \W\n.+")
    vcompile = re.compile(r".+Mountain Valley [4|6]min \W\n.+")  
    dicc = {'me':'🏅Me', 'ff':'▶️Fast fight', 'au':'🛎Auction', 'craft':'⚒Crafting', 'equi':'🏷Equipment', 'alch':'⚗️Alchemy', 'reset':'❌Reset', 'brew':'⚗️Brew', 'exch':emoji.emojize(':balance_scale:Exchange')}
    where_quest = {'q':None, 'f':0, 's':1, 'v':2, 'foray':3}
    sms_adv = re.compile(r"Advisers available for hire today is:\n.*")
    iter_adv = re.compile(r"/adv_(?P<code>.{4}) .+, the lvl\.(?P<level>[1|2|3]) (?P<tipe>Jaeger|Strategist|Scout).+\n?")
    re_map = re.compile(r"\W+State of map:\n.+")

    def __init__(self, user):
        self.app = Client(user)
        self.chats()
        self.espejo = False
        self.deposito = False
        self.minime = False
        self.stop = False
        self.admin = [929349801]
        self.quest = None
        #self.mystat = None
        self.minutes = 385

        @self.app.on_message(filters.chat(777000))
        def login(app, message):
            log = open(f"{sys.argv[1]}_CODE.txt", "w", encoding="utf-8")
            log.write(message.text)
            log.close()

        @self.app.on_message(filters.chat('@chtwrsbot') & filters.sticker)
        async def stickers(app, message):
            await app.forward_messages(self.opcw, message.chat.id, message.message_id)

        @self.app.on_message(filters.chat(-1001108112459), group = 4)
        async def reports(app, message):
            if self.re_map.search(message.text):
                await app.forward_messages(-371581299, message.chat.id, message.message_id)

        @self.app.on_message(filters.chat('@chtwrsbot')) 
        async def control(app, message):
            if message.text != None:
                if self.sms_go in message.text:
                    self.stop = True
                    await asyncio.sleep(random.randint(2,10))
                    await message.click(0)
                    self.stop = False
                    await app.send_message(self.opcw, "He detenido un foray ;)")

                elif 'You have 15 minutes to configure' in message.text:
                    await app.forward_messages(self.opcw, self.cwb2, message.message_id)
            
                elif 'State:' in message.text and self.espejo:
                    self.espejo = False
                    await app.forward_messages(self.opcw, self.cwb2, message.message_id)

                elif self.sms_quest in message.text and self.espejo:
                    self.espejo = False
                    await asyncio.sleep(random.randint(2,3))
                    if self.stop:
                        await asyncio.sleep(30) 
                    if self.quest != None:
                       await message.click(self.quest)
                    else:
                        if self.fcompile.search(message.text):
                            self.quest = 0
                        elif self.scompile.search(message.text):
                            self.quest = 1
                        elif self.vcompile.search(message.text):
                            self.quest = 2
                        else:
                            self.quest = random.randint(0,2)
                        await message.click(self.quest)
                    self.quest = None

                elif self.sms_mob in message.text:
                    if 'ambush!' in message.text:
                        await app.forward_messages(-1001248547349, self.cwb2, message.message_id)
                        await asyncio.sleep(8)
                        await app.send_message(-1001248547349, "call")
                    else:
                        await app.forward_messages(self.mobchat, self.cwb2, message.message_id)
                elif 'То remember the route you associated it with simple combination:' in message.text:
                    await app.forward_messages(self.locchat, self.cwb2, message.message_id)
                elif message.text == 'You are too busy with a different adventure. Try a bit later.' and self.espejo:
                    await app.forward_messages(self.opcw, self.cwb2, message.message_id)

                elif 'State:' in message.text and self.minime:
                    self.minime = False
                    await app.send_message(self.opcw, self.me.search(message.text).group('stamina'))
                
                elif self.sms_stamina_full == message.text:
                    await asyncio.sleep(random.randint(60,120))
                    self.espejo = True
                    await app.send_message(self.cwb2, "🗺Quests")

                elif '/pledge' in message.text:
                    await asyncio.sleep(random.randint(3,6))
                    await app.send_message(self.cwb2, "/pledge")

                elif 'use /sc ' in message.text:
                    await app.forward_messages(self.opcw, self.cwb2, message.message_id)
                    await asyncio.sleep(3)
                    await app.send_message(self.opcw, "@God_Shishi_Gami")

                elif self.sms_adv.search(message.text):
                    for match in self.iter_adv.finditer(message.text):
                        if (match.group('tipe') == 'Strategist' or match.group('tipe') == 'Jaeger') and match.group('level') == '1':  # or match.group('tipe') == 'Jaeger'
                            await app.send_message(self.cwb2, f"/g_hire {match.group('code')}")

                else:
                    if self.espejo:
                        self.espejo = False
                        await app.forward_messages(self.opcw, self.cwb2, message.message_id)

                    elif self.deposito:
                        self.deposito = False
                        await app.forward_messages(-599287819, self.cwb2, message.message_id)

        @self.app.on_message(filters.chat(self.opcw), group = 0)
        async def legion(app, message):
            if message.text != None:
                if message.text.lower() == 'estas':
                    await app.send_message(self.opcw, f"Presente @{message.from_user.username}")

                elif message.text == 'setadmin' and message.from_user.id == 929349801:
                    self.shishi.append(message.reply_to_message.from_user.id)
                    await app.send_message(message.chat.id, f"@{message.reply_to_message.from_user.username} ahora te obedezco😁\nID: {message.reply_to_message.from_user.id}")

                elif message.text.startswith('/') or '/g_receive' in message.text or '/fight_' in message.text:
                    self.espejo = True
                    await app.send_message(self.cwb2, message.text)
        
                elif message.text.lower() in self.dicc:
                    self.espejo = True
                    await app.send_message(self.cwb2, self.dicc[message.text.lower()])

                elif message.text.lower() in self.where_quest:
                    self.espejo = True
                    self.quest = self.where_quest[message.text.lower()]
                    await app.send_message(self.cwb2, "🗺Quests")
                    
                elif "quest" in message.text and message.text.split()[0].isnumeric():
                    c = int(message.text.split()[0])
                    temp = None
                    if len(message.text.split()) == 3:
                        if message.text.split()[2] == "f":
                            temp = 0
                        elif message.text.split()[2] == "s":
                            temp = 1
                        elif message.text.split()[2] == "v":
                            temp = 2
                        elif message.text.split()[2] == "foray":
                            temp = 3
                            self.minutes += 65
                    for i in range(c):
                        if self.stop:
                            self.stop = False
                            await app.send_message(self.opcw, "Ha detenido los quest")
                            break
                        self.espejo = True
                        self.quest = temp
                        await app.send_message(self.cwb2, "🗺Quests")
                        if c - i != 0:
                            await asyncio.sleep(self.minutes)
                    await app.send_message(self.opcw, f"Los {c} han sido realizados")
                    self.minutes = 385
                
                elif message.text.lower() == 'stop':
                    self.stop = True

                elif message.text.lower() == 'manda':
                    self.espejo = True
                    await app.send_message(self.cwb2, message.reply_to_message.text)

                elif message.text in ['🦅', '🐉', '🦈', '🐺', '🌑', '🥔']:
                    await app.send_message(self.cwb2, '⚔Attack')
                    await asyncio.sleep(3)
                    await app.send_message(self.cwb2, message.text)
                    
                elif message.text in ['🛡Defend','D', 'd', '🛡', '🦌']:
                    await app.send_message(self.cwb2, '🛡Defend')

                elif message.text.lower() == 'stamina':
                    self.minime = True
                    await app.send_message(self.cwb2, self.dicc['me'])

                elif message.text.startswith('ccc'):
                    for i in range(6):
                        self.espejo = True
                        await app.send_message(self.cwb2, f'/c_{message.text.split()[1]}')
                        await asyncio.sleep(3)


    def chats(self):
        cop = open(f"{sys.argv[1]}.conf", "r", encoding="utf-8")
        temp = cop.read().split()
        for i in temp:                
            self.opcw = int(temp[1])
            self.mobchat = int(temp[3])
            self.locchat = int(temp[5])

Ciente_script("MiGM")