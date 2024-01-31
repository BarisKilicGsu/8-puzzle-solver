import numpy as np
from agent import *

class myAgent(Agent):
    def __init__(self, matrix):
        super().__init__(matrix)

    def solve_puzzle(self):

        self.frontier = PriorityQueue()
        self.explored = set()

        # Başlangıç düğümünü oluştur
        start_node = Node(None, self.find_tile_position(self.initial_matrix, 0), self.initial_matrix, 0, self.h(self.initial_matrix))
    
        # Başlangıç düğümünü kuyruğa ekle
        self.frontier.push(start_node, start_node.f_score)

        while not self.frontier.isEmpty():
            # En düşük F skoruna sahip düğümü al
            current_node = self.frontier.pop()
            self.expanded_node += 1

            # Hedef duruma ulaşıldı mı kontrol et
            if self.checkEqual(current_node.matrix, self.desired_matrix):
                return self.get_moves(current_node)
            
            # Düğümü keşfedilenler arasına ekle
            self.explored.add(tuple(map(tuple, current_node.matrix)))

            # Komşu düğümleri işle
            for direction in self.directions:
                x, y = current_node.position
                dx, dy = direction
                new_x, new_y = x + dx, y + dy

                # Yeni pozisyonun geçerli olup olmadığını kontrol et
                if 0 <= new_x < self.game_size and 0 <= new_y < self.game_size:
                    new_matrix = [list(row) for row in current_node.matrix]
                    new_matrix[x][y], new_matrix[new_x][new_y] = new_matrix[new_x][new_y], new_matrix[x][y]

                    # Yeni durum daha önce keşfedilmediyse frontier'e
                    if tuple(map(tuple, new_matrix)) not in self.explored:
                        new_node = Node(parent=current_node, position=(new_x, new_y), matrix=new_matrix, g_score=current_node.g_score + 1, h_score=self.h(new_matrix))
                        self.maximum_node_in_memory = max(self.maximum_node_in_memory, self.frontier.size()) 
                        if not self.frontier.contains(new_matrix):
                            self.generated_node += 1
                            self.frontier.push(new_node, new_node.f_score)
          

        return None


    def h(self, matrix):
        """
        Heuristic fonksiyonu: Taşların Manhattan mesafelerinin döndürür.
        """
        manhattan_distance = 0

        for i in range(self.game_size):
            for j in range(self.game_size):
                if matrix[i][j] != 0:
                    target_x, target_y = divmod(matrix[i][j] - 1, self.game_size)
                    manhattan_distance += abs(target_x - i) + abs(target_y - j)

        return manhattan_distance 


    