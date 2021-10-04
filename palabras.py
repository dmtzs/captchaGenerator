# pip install StringGenerator

import strgen

randomStr= strgen.StringGenerator("[\l\d]{5}").render_list(1, unique= True)

print(randomStr)