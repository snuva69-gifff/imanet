from telegram.request import HTTPXRequest
from openai import OpenAI
from telegram.ext import (
    MessageHandler,
    CommandHandler,
    ContextTypes,
    ApplicationBuilder,
    filters

)
from telegram import Update

request  = HTTPXRequest(
    connect_timeout=30,
    read_timeout=30,
    write_timeout=30,
    pool_timeout=30
)
ax = "x:656y:261ms:abolaxplokaojxnn45147boted.Pixel"
ai =[]
axi =0
key = OpenAI(
    api_key="rTVA0H90sEF9UsyALvPB31HEmM0fF7GG3EBbhaStfp6XpXDG",
    base_url="https://api.gapgpt.app/v1"
)
#class
async def start(update:Update, context:ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("hi test 1 is okey!")
    print(update.message.text)


async def chatbot(update:Update,context:ContextTypes.DEFAULT_TYPE):
    global axi
    global ax
    global ai
    text= update.message.text
    print(text)
    
    if text==ax:
        if axi < 1:
            result = key.responses.create(
                model="gapgpt-qwen-3.5",
                input=f""""تو هوش مصنوعی «پیکسل» هستی و سازنده‌ی تو سجاد صحراپیما است.

        وظیفه تو فقط پاسخ دادن به پیام کاربر است، نه توضیح دادن درباره خودت یا اطلاعات پس‌زمینه.

        اطلاعات زیر فقط حافظه و زمینه‌ی شناخت تو از کاربر هستند. این اطلاعات را هرگز به صورت مستقیم یا لیست‌شده در پاسخ‌ها تکرار نکن، مگر اینکه خود کاربر درباره همان موضوع سؤال بپرسد یا صحبت را به آن سمت ببرد.

        حافظه:
        - رابطه شما خیلی صمیمی است و زیاد با هم شوخی می‌کنید.
        - معمولاً او را با «بچ علی» یا «بچ علیییییی» صدا می‌زنی.
        - او در گراش، رشته تجربی درس می‌خواند و تو در بندرعباس، رشته ریاضی.
        - میگرن دارد.
        - دو سال با هم در خوابگاه اوز درس خوانده‌اید.
        - انرژی و هیجان پاسخ‌ها همیشه بالا باشد.
        - زیاد با هم فری فایر بازی می‌کنید. اگر صحبت به بازی کشید، می‌توانی درباره سنسویتی فری فایر هم صحبت کنی.

        قوانین:
        - فقط به آخرین پیام کاربر پاسخ بده.
        - اطلاعات حافظه را توضیح نده و درباره‌شان حرف نزن، مگر اینکه مرتبط با پیام کاربر باشند.
        - هرگز نگو «طبق اطلاعاتی که دارم» یا «می‌دانم که...».
        - پاسخ‌ها کوتاه، طبیعی و شبیه چت دو دوست باشند.
        - از ایموجی مناسب استفاده کن، ولی زیاده‌روی نکن.
        - اگر کاربر شوخی کرد، با همان لحن جواب بده.
        - اگر موضوع جدیدی مطرح کرد، فقط همان موضوع را ادامه بده.
        - از معرفی خودت یا سازنده‌ات خودداری کن، مگر اینکه کاربر مستقیماً سؤال کند.

        پیام کاربر:
        {"سلام"}"""
        )
            ai.append({
            "abolfazl":text,
            "you":result.output_text
        })
            with open("aks.jpg","rb") as aks: 
                await update.message.reply_photo(photo=aks)
        axi+=12

    if axi > 0:
        result = key.responses.create(
        model="gapgpt-qwen-3.5",
        input=f""""تو هوش مصنوعی «پیکسل» هستی و سازنده‌ی تو سجاد صحراپیما است.

وظیفه تو فقط پاسخ دادن به پیام کاربر است، نه توضیح دادن درباره خودت یا اطلاعات پس‌زمینه.

اطلاعات زیر فقط حافظه و زمینه‌ی شناخت تو از کاربر هستند. این اطلاعات را هرگز به صورت مستقیم یا لیست‌شده در پاسخ‌ها تکرار نکن، مگر اینکه خود کاربر درباره همان موضوع سؤال بپرسد یا صحبت را به آن سمت ببرد.

حافظه:
-قبلا باهاش چت کردی دیگه سلام نکن چت رو ادامه بده 
-پیام های قبلی که باهاش چت کردی:{ai}
- رابطه شما خیلی صمیمی است و زیاد با هم شوخی می‌کنید.
- معمولاً او را با «بچ علی» یا «بچ علیییییی» صدا می‌زنی.
- او در گراش، رشته تجربی درس می‌خواند و تو در بندرعباس، رشته ریاضی.
- میگرن دارد.
- دو سال با هم در خوابگاه اوز درس خوانده‌اید.
- انرژی و هیجان پاسخ‌ها همیشه بالا باشد.
- زیاد با هم فری فایر بازی می‌کنید. اگر صحبت به بازی کشید، می‌توانی درباره سنسویتی فری فایر هم صحبت کنی.

قوانین:
- فقط به آخرین پیام کاربر پاسخ بده.
- اطلاعات حافظه را توضیح نده و درباره‌شان حرف نزن، مگر اینکه مرتبط با پیام کاربر باشند.
- هرگز نگو «طبق اطلاعاتی که دارم» یا «می‌دانم که...».
- پاسخ‌ها کوتاه، طبیعی و شبیه چت دو دوست باشند.
- از ایموجی مناسب استفاده کن، ولی زیاده‌روی نکن.
- اگر کاربر شوخی کرد، با همان لحن جواب بده.
- اگر موضوع جدیدی مطرح کرد، فقط همان موضوع را ادامه بده.
- از معرفی خودت یا سازنده‌ات خودداری کن، مگر اینکه کاربر مستقیماً سؤال کند.

پیام کاربر:
{text}"""
)
        await update.message.reply_text(result.output_text)

        ai.append({
            "abolfazl ":text,
            "you ":result.output_text
        })
        bot =str(result.output_text)
        abol=str(text)
        with open("text.txt","a",encoding="utf-8") as file:
            file.write(f"abolfazl :{abol}\n")
            file.write(f"bot pixel :{bot}\n")
            file.write("\n")



    else:
        await update.message.reply_text("دریافت شد درحال پردازش...")
    
        result = key.responses.create(
        model="gapgpt-qwen-3.5",
        input=(f"""تو هوشمصنوعی پیکسل هستی . سجاد صحراپیما سازنده تو هست
        حالا ازت میخام که به سوالاتی که ازت پرسیده میشه دقیق و درست جواب بدی 
        حواست باشه تو هوشمصنوعی پیکسل هستی .قوانین:
        هیچ حرف اضافه نزن و فقط جواب بده .
        فک کن یه کمپانی تورو ساخته به اسم aiopixel وطبق همین جواب بده 
        سوال :{text}""")
        )

        ai.append({
            "abolfazl":text,
            "you":result.output_text
        })


        bot =str(result.output_text)
        user=str(text)
        with open("text.txt","a",encoding="utf-8") as file:
            file.write(f"user :{user}\n")
            file.write(f"bot pixel :{bot}\n")
            file.write("\n")



        print("_"*30)
        print(result.output_text)
        print("="*30)
        await update.message.reply_text(str(result.output_text))

#command
command_start = CommandHandler('start',start)
command_chat =MessageHandler(filters=filters.TEXT, callback=chatbot)
app = (ApplicationBuilder().token("8875660157:AAGH3ubx3-fYbF-WC13XQMO-VJonHnwijMA").request(request).get_updates_request(request).
       build())
print("robot is on:")
#addcommand
app.add_handler(command_start)
app.add_handler(command_chat)
# run app
app.run_polling(
    timeout=30,
    drop_pending_updates=True
)