import pygame
import random
import heapq
import math
import sys

# Initialize pygame
pygame.init()
grid_size = 20
cell_size = 30
screen = pygame.display.set_mode((grid_size * cell_size, grid_size * cell_size))
pygame.display.set_caption("Cyclone Evacuation Simulation")

# Load background image
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (grid_size * cell_size, grid_size * cell_size))

# Define grid and other parameters
grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]
population_density = 0.2
frames_per_second = 1  # Adjusted to slow down the simulation

# Colors and cell states
WHITE, BLUE, RED, GREEN = (255, 255, 255), (0, 0, 255), (255, 0, 0), (0, 255, 0)
EMPTY, RESIDENT, CYCLONE, SHELTER = 0, 1, 2, 2

# Resident class
class Resident(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 0, 0), (cell_size // 2, cell_size // 2), cell_size // 2 - 5)
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.path = None

    def update(self):
        if self.path:
            next_cell = self.path.pop(0)
            self.rect.x = next_cell[1] * cell_size
            self.rect.y = next_cell[0] * cell_size
            if not self.path:
                self.path = None

# Shelter class
class Shelter(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((cell_size, cell_size))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x * cell_size
        self.rect.y = y * cell_size
        self.capacity = 100  # Increased Shelter capacity
        self.residents = 0  # Number of residents currently in the shelter

# Sprite groups
all_sprites, residents, shelters = pygame.sprite.Group(), pygame.sprite.Group(), pygame.sprite.Group()

#Populate grid with residents
for i in range(grid_size):
    for j in range(grid_size):
        if random.random() < population_density:
            resident = Resident(j, i)
            residents.add(resident)
            all_sprites.add(resident)
            grid[i][j] = RESIDENT

# Define shelters with increased capacity
shelter_locations = [(15, 15)]  # Added extra shelters
for loc in shelter_locations:
    shelter = Shelter(*loc)
    shelters.add(shelter)
    all_sprites.add(shelter)
    grid[loc[0]][loc[1]] = SHELTER

# Heuristic function for A*
def heuristic(node, goal):
    return math.sqrt((node[0] - goal[0]) ** 2 + (node[1] - goal[1]) ** 2)

# A* algorithm
def astar(grid, start, goal):
    open_list = []
    closed_set = set()
    came_from = {}

    g_score = {(x, y): float("inf") for x in range(grid_size) for y in range(grid_size)}
    f_score = {(x, y): float("inf") for x in range(grid_size) for y in range(grid_size)}
    g_score[start] = 0
    f_score[start] = heuristic(start, goal)

    heapq.heappush(open_list, (f_score[start], start))

    while open_list:
        current = heapq.heappop(open_list)[1]

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.reverse()
            return path

        closed_set.add(current)
        for neighbor in get_neighbors(grid, current):
            if neighbor in closed_set:
                continue

            tentative_g_score = g_score[current] + 1

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)

                if neighbor not in [i[1] for i in open_list]:
                    heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None

# Neighbors function
def get_neighbors(grid, node):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    neighbors = []
    for dx, dy in directions:
        x, y = node[0] + dx, node[1] + dy
        if 0 <= x < grid_size and 0 <= y < grid_size:
            neighbors.append((x, y))
    return neighbors

# Find nearest shelter
def find_nearest_shelter_a_star(resident):
    nearest_shelter = None
    min_distance = float("inf")
    resident_pos = (resident.rect.y // cell_size, resident.rect.x // cell_size)

    for shelter in shelters:
        if shelter.capacity > shelter.residents:
            shelter_pos = (shelter.rect.y // cell_size, shelter.rect.x // cell_size)
            path = astar(grid, resident_pos, shelter_pos)

            if path and len(path) < min_distance:
                nearest_shelter = shelter
                min_distance = len(path)

    if nearest_shelter:
        nearest_shelter.residents += 1
        return path
    else:
        return None


# Cyclone path simulation
cyclone_path = [(0, 0)]
def update_cyclone_path():
    last_pos = cyclone_path[-1]
    next_pos = (last_pos[0] + random.choice([-1, 0, 1]), last_pos[1] + random.choice([-1, 0, 1]))
    if 0 <= next_pos[0] < grid_size and 0 <= next_pos[1] < grid_size:
        cyclone_path.append(next_pos)

# Main simulation loop
running = True
clock = pygame.time.Clock()
while running:
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    update_cyclone_path()

    for resident in residents:
        if not resident.path:
            path = find_nearest_shelter_a_star(resident)
            if path:
                resident.path = path
        resident.update()

    # Draw the grid
    for i in range(grid_size):
        for j in range(grid_size):
            #if grid[i][j] == RESIDENT:
                #pygame.draw.rect(screen, BLUE, (j * cell_size, i * cell_size, cell_size, cell_size))
            if grid[i][j] == CYCLONE:
                pygame.draw.rect(screen, RED, (j * cell_size, i * cell_size, cell_size, cell_size))
            elif grid[i][j] == SHELTER:
                pygame.draw.rect(screen, GREEN, (j * cell_size, i * cell_size, cell_size, cell_size))

    # Update and draw sprites
    all_sprites.update()
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(frames_per_second)

pygame.quit()
sys.exit()