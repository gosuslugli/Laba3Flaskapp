from PIL import Image, ImageEnhance
folder = "app/static/images/"
for i in range(1,5):
    image = Image.open(f"{folder}road{i}.jpg")
    enhancer = ImageEnhance.Brightness(image)

    # Уменьшаем экспозицию изображения
    exposure_factor = 0.2  # Уменьшение на 50%
    image_with_lower_exposure = enhancer.enhance(exposure_factor)

    # Сохраняем измененное изображение
    image_with_lower_exposure.save(f"{folder}dark_road{i}.jpg")

