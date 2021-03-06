import portion
from Diffusion_Process.AbstractInfluenceFunction import AbstractInfluenceFunction

class EnhancedTipping(AbstractInfluenceFunction):
	
	def __init__(self, threshold, bound_update):
		self._threshold = threshold
		self._bnd_update = bound_update

	def influence(self, neigh, qualified_neigh, nas):
		bnd = portion.closed(0,1)
		reduced_neigh = 0

		for c in neigh:
			world = nas[c]
			labels = c.getLabels()
			for l in labels:
				if world.isSatisfied(l, portion.closed(1,1)):
					reduced_neigh += 1
					break

		if reduced_neigh != 0:
			if (len(qualified_neigh) / len(neigh)) > self._threshold:
				bnd = self._bnd_update

		return bnd

