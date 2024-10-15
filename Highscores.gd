extends Node

var highscores: Array = []

const MAX_SCORES = 10  # Limit the number of high scores to keep track of

func _ready():
	# Load highscores when the game starts
	save_highscores()
	load_highscores()

# Function to add a new high score
func add_highscore(player_name: String, score: int):
	# Insert the new score as a dictionary
	highscores.append({"name": player_name, "score": score})

	# Sort the high scores by score (highest first)
	highscores.sort_custom(_sort_scores)

	# Limit to the top MAX_SCORES entries
	if highscores.size() > MAX_SCORES:
		highscores.resize(MAX_SCORES)

	# Save highscores after adding a new one
	save_highscores()

# Custom sorting function to sort scores in descending order
func _sort_scores(a: Dictionary, b: Dictionary) -> int:
	return b["score"] - a["score"]

# Save highscores to a file
func save_highscores():
	var file = FileAccess.open("user://highscores.dat", FileAccess.WRITE)
	file.store_var(highscores)
	file.close()

# Load highscores from a file
func load_highscores():
	if FileAccess.file_exists("user://highscores.dat"):
		var file = FileAccess.open("user://highscores.dat", FileAccess.READ)
		highscores = file.get_var()
		file.close()
	else:
		# Initialize empty high scores list if no file exists
		highscores = []
		save_highscores()

# Display the highscores
func get_highscores() -> Array:
	return highscores
