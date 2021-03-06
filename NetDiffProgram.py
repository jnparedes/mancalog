from NetDiffInterpretation import NetDiffInterpretation
import copy

class NetDiffProgram:

	def __init__(self, net_diff_graph, tmax, facts = [], local_rules = [], global_rules = []):
		self._net_diff_graph = net_diff_graph
		self._tmax = tmax
		self._facts = facts
		self._local_rules = local_rules
		self._global_rules = global_rules
		self._interp = None

	def diffusion(self):
		self._interp = NetDiffInterpretation(self._net_diff_graph, self._tmax)
		for fact in self._facts:
			self._interp.applyFact(fact)

		old_interp = copy.deepcopy(self._interp)
		self._apply_local_rules()

		#this while will be executed until a fixed point is reached
		while not old_interp == self._interp:
			old_interp = copy.deepcopy(self._interp)
			self._apply_local_rules()

		#global rules are not necessary for classic MANCaLog , I have used them in a MANCaLog extension
		for t in range(self._tmax + 1):
			for rule in self._global_rules:
				self._interp.applyGlobalRule(rule, t)

		return self._interp

	def _apply_local_rules(self):
		for t in range(self._tmax + 1):
			for rule in self._local_rules:
				self._interp.applyLocalRule(rule, t)
