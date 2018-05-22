import psutil

class Stats():

  @classmethod
  def porcentaje_cpu(cls):
    porcentaje = psutil.cpu_percent()
    return porcentaje

  @classmethod
  def memoria_disponible(cls):
    ram = psutil.virtual_memory().available
    return ram

  @classmethod
  def espacio_disco(cls):
    espacio = psutil.disk_usage('/').free
    return espacio
