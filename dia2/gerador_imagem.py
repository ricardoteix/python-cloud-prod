from PIL import Image

image = Image.open('dia2/exemplo1.jpg')
nova = image.resize((500, 175))
nova.save("dia2/novo_exemplo1.jpg")

print(image.size)
print(nova.size)