# pip install captcha
# Liga: https://pypi.org/project/captcha/

import captcha.image as capi

ima= capi.ImageCaptcha(width= 280, height= 90)

texto= "prueba"

ima.write(texto, "output.png")