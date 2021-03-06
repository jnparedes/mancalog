import portion
from AbstractInfluenceFunction import AbstractInfluenceFunction

class Tipping(AbstractInfluenceFunction):
	
	def __init__(self, threshold, bound_update):
		self._threshold = threshold
		self._bnd_update = bound_update

	def influence(self, neigh, qualified_neigh, nas):
		bnd = portion.closed(0,1)
		if len(neigh) != 0:
			if (len(qualified_neigh) / len(neigh)) > self._threshold:
				bnd = self._bnd_update

		return bnd

