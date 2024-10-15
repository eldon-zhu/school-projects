extends Node

class_name RunningCostSystem

func handle_running_cost(entities: Array, delta: float) -> float:
	var total_running_cost = 0.0
	for entity in entities:
		var running_cost_component = entity.get_node("MoneySpentComponent")
		if running_cost_component != null:
			var running_cost = running_cost_component.running_cost
			var cost_for_this_frame = running_cost * delta  # Calculate cost for the current frame
			total_running_cost += cost_for_this_frame

	return total_running_cost
