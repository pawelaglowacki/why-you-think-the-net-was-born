import urllib
import random

#num = random.randint(1,99999)

zeros = "00000"

for i in range(1,99999):
  try:
    boob_id = zeros[0:len(zeros)-len(str(i))] + str(i)
    urllib.urlretrieve("http://media.oboobs.ru/boobs/" + boob_id + ".jpg", boob_id + ".jpg")
  except:
    pass
