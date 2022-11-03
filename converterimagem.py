from PIL import Image 

img = Image.open(r"C:\Users\Aluno\Desktop\python-logo.png")

img_cov = img.convert('L')
#show image
img_cov.show()
#save image
img_cov.save("python-logo-cinza.jpg")

