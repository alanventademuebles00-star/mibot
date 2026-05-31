import pytesseract
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# 🔧 Ruta Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 🔑 Token
TOKEN = "8837907216:AAF7hIqptFDYwi-7FX5QEYEEvZIE5WsyIaw"

usuarios = []


async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.message.from_user.id

    # 📸 OCR DE IMÁGENES
    if update.message.photo:

        file = await update.message.photo[-1].get_file()
        await file.download_to_drive("img.jpg")

        text = pytesseract.image_to_string("img.jpg")

        print("TEXTO LEÍDO:", text)

        texto = text.lower()

        if "yape" in texto:

            numeros = re.findall(r"\d+", texto)

            if numeros:

                # limpiar números
                numeros = [int(n) for n in numeros]

                # buscar exactamente 10
                if 10 in numeros:

                    await update.message.reply_video(
                        video=open("video.mp4", "rb"),
                        caption="380 LA HORA BB SOLO SANTA ANITA"
                    )

                else:

                    await update.message.reply_text(
                        "⚠️ Yape detectado pero no es 10 soles"
                    )

            else:

                await update.message.reply_text(
                    "📸 Yape detectado pero no pude leer el monto"
                )

        else:

            await update.message.reply_text(
                "📸 Imagen recibida, no detecté Yape"
            )

        return

    # 💬 TEXTO
    mensaje = update.message.text.lower()

    # 👤 PRIMER MENSAJE
    if user_id not in usuarios:

        usuarios.append(user_id)

        await update.message.reply_photo(
            photo=open("foto.jpg", "rb"),
            caption="Hola bb soy Marian venezolana en Lima recién 2 semanas vendo mi contenido a 10 soles, después de eso te doy información de salidas"
        )
        return

    # 🔁 RESPUESTAS

    if "que viene" in mensaje or "cuantos videos" in mensaje:

        await update.message.reply_text(
            "3 VIDEOS MIO COJIENDO DESPUES DE ESO TE DOY INFO DE SALIDAS"
        )

    elif "regalas una foto" in mensaje or "prueba" in mensaje:

        await update.message.reply_text(
            "NO ENVIO FOTOS GRATIS NI PRUEBAS SI DESEAS LA INFO DE SALIDAS YA SABES COMO ES"
        )

    elif "yape" in mensaje or "numero" in mensaje:

        await update.message.reply_text(
            "993774203 LUISA H. YAPE HAZLO AHI ME ENVIAS CAPTURA POR ACA"
        )

    elif "pareja" in mensaje or "soltera" in mensaje or "novio" in mensaje:

        await update.message.reply_text(
            "MI AMOR SI QUIERES INFO DE SALIDAS ES DESPUES DEL CONTENIDO ASI DE SIMPLE"
        )

    elif "lima" in mensaje:

        await update.message.reply_text(
            "OBVIO EN LIMA"
        )

    elif "haces salidas" in mensaje:

        await update.message.reply_text(
            "OBVIO MI AMOR INFO DE SALIDAS DESPUES DEL CONTENIDO"
        )

    else:

        await update.message.reply_text(
            "MI AMOR INFO DE SALIDAS DESPUES DEL CONTENIDO 💋"
        )


app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.ALL, responder))

print("BOT ACTIVADO")

app.run_polling()