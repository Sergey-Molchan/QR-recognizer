from qreader import QReader
import cv2


def read_qr_from_image(image_path: str) -> None:
    """Считываем QR-код с изображения"""

    #Создаем  экземпляр QReader
    qreader = QReader()

    # Читаем изображение сразу конвертируем в RGB
    image = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)

    # Распознавание QR-кода
    decoded_text = qreader.detect_and_decode(image=image)

    if decoded_text:
        print(f'✅ Расшифрованный QR-код: {decoded_text}')
    else:
        print('❌QR-код не найден или не читается 😭')


def main():
    '''Запрашиваем пользователя путь к изображению'''
    image_path1 = input('Введите путь к изображению с QR-кодом').strip()
    read_qr_from_image(image_path=image_path1)

if __name__ == '__main__':
    main()