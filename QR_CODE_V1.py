import qrcode
import time
# пример данных
print ("введите значение QR кода")
data = input()
# имя конечного файла
filename = "site_{}.png" .format(int(time.time()))
# генерируем qr-код
img = qrcode.make(data)
# сохраняем img в файл
img.save(filename)
