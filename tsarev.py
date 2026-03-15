import base64

with open('C:\\Users\\i.tsarev\\Desktop\\Файлы для теста\Версии заказа\Договор_1.docx.sig', 'rb') as f:
    data = f.read()
    b64_encoded_data = base64.b64encode(data)

print(b64_encoded_data.decode())

# import os
#
# file_path = r"C:\Users\i.tsarev\Desktop\Файлы для теста\Версии заказа\Договор_1.docx.sig"
# if not os.path.exists(file_path):
#     print("Файл не найден!")
# else:
#     with open(file_path, 'rb') as f:
#         data = f.read()
#         b64_encoded_data = base64.b64encode(data)
#
#     # Выводим в терминал
#     print(b64_encoded_data.decode())
#
#     # Сохраняем в файл
#     with open('encoded_base64.txt', 'w') as out_file:
#         out_file.write(b64_encoded_data.decode())
