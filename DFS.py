def dfs(adj_matrix, node):
	n = len(adj_matrix)
	if node < 0 or node >= n:
		print("Invalid node value.")
		return []

	reachable_nodes = [node]

	# Remove: print the matrix
	for i in range(n):
		print(adj_matrix[i])
	print()


	def follow_path(node, next):
		nonlocal adj_matrix
		nonlocal n
		nonlocal reachable_nodes

		while next < n:
			if adj_matrix[node][next] == 0:
				next += 1
			else:
				if next not in reachable_nodes:
					reachable_nodes.append(next)
					follow_path(next, 0)
				else:
					next += 1

	follow_path(node, 0)

	return reachable_nodes

				
adj_matrix_1 = [
		[0, 1, 0, 0],
		[1, 0, 1, 0],
		[0, 1, 0, 1],
		[0, 0, 1, 0]
]

adj_matrix_2 = [
		[0, 1, 0, 0],
		[1, 0, 1, 0],
		[0, 1, 0, 0],
		[0, 0, 0, 0]
]

adj_matrix_3 = [
		[0, 1, 0, 0],
		[1, 0, 0, 0],
		[0, 0, 0, 1],
		[0, 0, 1, 0]
]

print("Adjacent Matrix 1 tests")
print("Node 1")
print(dfs(adj_matrix_1, 1))
print()
print("Node 3")
print(dfs(adj_matrix_1, 3))
print()
print("Adjacent Matrix 2 tests")
print("Node 3")
print(dfs(adj_matrix_2, 3))
print()
print("Adjacent Matrix 3 tests")
print("Node 3")
print(dfs(adj_matrix_3, 3))
print()
print("Node 0")
print(dfs(adj_matrix_3, 0))