from qreader import QReader
import cv2
from sympy.core.random import choice


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


def read_qr_from_camera() -> None:
    """Считывает QR-коды в реальном времени с видео"""
    qreader = QReader()

    # Для видео укащываем путь к mp4.
    # Для веб-камеры оставляем 0
    cap = cv2.VideoCapture("/Users/sergejmolcan/QRrecognizer/IMG_0461.MOV")

    if not cap.isOpened():
        print('❌ Не удалось открыть видео или камеру')
        return
    print('📸 Поток запущен. Наведи камеру на QR-код или проиграй видео, \n Нажмите Q что бы выйти')

    while True:
        ret, frame = cap.read()
        if not ret:
            print('Запись завершена')
            break

        # Конвертация в RGB для QReader
        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Распознование QR-кода
        decoded_text = qreader.detect_and_decode(image=image_rgb)
        # Если QR найден выводим результат
        if decoded_text:
            print(f'Расшифрованный QR-код: {decoded_text}')

        #Отображаем видео
        cv2.imshow('QR-scaner', frame)

        # Выход по клавише 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print('Поток остановлен')

def main():
    print('Выберите режим считывания')
    print('1 -- Считывает QR-код изображения')
    print('2 -- Считывает QR-код видео/камеры')
    choice = input('Ведите 1 или 2: ').strip()

    if choice == '1':
        image_path = input('Введите путь к изображению с QR-кодом').strip()
        read_qr_from_image(image_path=image_path)
    elif choice == '2':
        read_qr_from_camera()
    else:
        print('Некорректный выбор ! Проверьте и запустите программу снова.')


if __name__ == '__main__':
    main()