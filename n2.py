from fastapi import FastAPI, File, UploadFile
import cloudinary.uploader

app = FastAPI()

@app.post("/upload-avatar/")
async def upload_avatar(file: UploadFile):
    # Отримуємо дані для завантаження з запиту
    image_data = await file.read()
    # Завантажуємо аватар на Cloudinary
    upload_result = cloudinary.uploader.upload(image_data,
                                               folder="avatars",
                                               overwrite=True,
                                               width=150, height=150,
                                               crop="thumb")
    # Отримуємо URL завантаженого аватара з Cloudinary
    avatar_url = upload_result["secure_url"]
    # Повертаємо URL аватара як відповідь на запит
    return {"avatar_url": avatar_url}
