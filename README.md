# Biblioteca Pillow
Atividade realizada para aula de Linguagem de Programação 2.

<div align="center">
<img src="https://user-images.githubusercontent.com/110680526/199720183-bd1921aa-6ae9-427f-9cac-c1427997c9ed.png" width="700px" />
</div>

## O que é essa biblioteca?
Chamada de Python Imaging Library (expansão da sigla PIL), é uma biblioteca utilizada para processamento de imagens na linguagem Python. Oferece suporte para diversos formatos de imagem, tais como JPEG, PNG e BMP.

https://pillow.readthedocs.io/en/stable/

**O que podemos fazer utilizando a biblioteca PIL?**
- Alterar o tamanho da imagem com base nos pixels
- Colar imagens uma sobre as outras (Definir background)
<div align="center">
<img src="https://user-images.githubusercontent.com/110680526/199724325-c2688751-65de-401f-876a-7a807d3eba78.png" width="400px" />
</div>

- Utilizar array para criação de gif

## Instalação da biblioteca
Após a instalação do Python, abrir o cmd e executar o seguinte comando:
```
pip install pillow
```

## Código
```
from PIL import Image 
img = Image.open(r"C:\Users\Aluno\Desktop\python-logo.png")
img_cov = img.convert('L')
#show image
img_cov.show()
#save image
img_cov.save("python-logo-cinza.jpg")
```

### Imagem inicial:

<div align="center">
<img src="https://user-images.githubusercontent.com/110680526/199719487-30a49b98-61b6-4e23-9e16-2892a2c53319.png" width="700px" />
</div>


### Imagem após a formatação escalas de cinza:
<div align="center">
<img src="https://user-images.githubusercontent.com/110680526/199719807-ff585eb0-3250-437c-9331-dc66a734b488.png" width="900px" />
</div>


### Caminho da imagem
<div align="center">
<img src="https://user-images.githubusercontent.com/110680526/199719695-0006485c-95e6-4e74-9354-9263805dba7c.png" width="900px" />
</div>
