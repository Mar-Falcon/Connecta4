from settings import BOARD_LENGTH


class LinearBoard():
	""""
	Clase que representa un tablero de una sola columna
	X un jugador
	O otro jugador
	None un espacio vacío
	"""

	def __init__(self):
		"""
		Una lista de None
		"""
		self._column = [None for i in range(BOARD_LENGTH)]
	
	def add(self, char):
		"""
		Juega en la primera posición disponible
		"""
		#siempre y cuando no este lleno...
		if not self.is_full():
			#Buscamos la primera posición libre (None)
			i = self._column.index(None)
			#lo sustituimos por char
			self._column[i] = char
		
	def is_full(self):
		return self._column[-1] != None

	def is_victory(self, char):
		return False

	def is_tie(self, char1, char2):
		"""
		No hay victroia ni de char1 ni de char2
		"""
		return (self.is_victory("X") == False) and (self.is_victory("O") == False)

	
