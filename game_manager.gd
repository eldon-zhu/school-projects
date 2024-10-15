extends Node

var electricity_produced: float = 0.0
var electricity_consumed: float = 0.0
var player_money: float = 0.0
var environment_score: float = 0.0

# Initially set to false
var electricity_game_over: bool = false
var money_game_over: bool = false
var environment_game_over: bool = false

var player_final_score: float = 0.0

signal player_score(score: float)
signal game_over(value: bool)
signal one_sec_passed
signal one_round_passed

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	# Add timer to check every second
	var check_timer = Timer.new()
	check_timer.wait_time = 1.0 # Runs every 1.0 seconds
	check_timer.one_shot = false  # It will not only run once
	add_child(check_timer)  # Add the timer to the scene
	check_timer.connect("timeout", _on_check_timer_timeout)
	check_timer.start()
	
	# Timer to determine the end of 1 round
	var round_timer = Timer.new()
	round_timer.wait_time = 5.0
	round_timer.one_shot = false
	add_child(round_timer)
	round_timer.connect("timeout", _on_round_timer_timeout)
	round_timer.start()

func _on_round_timer_timeout() -> void:
	one_round_passed.emit()

func _on_check_timer_timeout() -> void:
	one_sec_passed.emit()
	
	# Timer to give player 10 seconds to fix issue, otherwise game over
	var fix_issue_timer = Timer.new()
	fix_issue_timer.wait_time = 10.0
	fix_issue_timer.one_shot = true
	add_child(fix_issue_timer)
	fix_issue_timer.connect("timeout", _on_fix_issue_timer_timeout)
	
	#Check if game over conditions are met
	if electricity_produced < electricity_consumed:
		electricity_game_over = true
	elif player_money == 0.0:
		money_game_over = true
	elif environment_score < 20:
		environment_game_over = true
	else:
		electricity_game_over = false
		money_game_over = false
		environment_game_over = false
		
	if electricity_game_over or money_game_over or environment_game_over:
		print("Oh no!")
		fix_issue_timer.start()
		if electricity_game_over:
			print("Produce more electricity!")
		if money_game_over:
			print("Make more money!")
		if environment_game_over:
			print("Save the environment!")
	else:
		print("Good!")

func _on_fix_issue_timer_timeout():
	if electricity_game_over or money_game_over or environment_game_over:
		end_game()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(_delta):
	pass

func end_game() -> void:
	print("Game over")
	player_score.emit(player_final_score)
	game_over.emit(true)
	get_tree().paused = true

func _on_game_electricity_produced(amount):
	electricity_produced = amount


func _on_game_electricity_consumed(amount):
	electricity_consumed = amount


func _on_game_environment_impact(amount):
	environment_score = amount


func _on_game_player_money_balance(amount):
	player_money = amount


func _on_game_player_final_score(amount):
	player_final_score = amount
