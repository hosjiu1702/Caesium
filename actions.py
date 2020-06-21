from rasa_sdk import Action
from rasa_sdk.events import SlotSet


class ActionSaveThingToBuy(Action):
	def name(self):
		return "action_save_thing_to_buy"

	def run(self, dispatcher, tracker, domain):
		msg = "okie, em đã lưu lại rồi đó ạ."
		dispatcher.utter_message(text=msg)

		return [SlotSet("thing_to_buy", tracker.get_latest_entity_values(entity_type=))]


class ActionShowThingToBuy(Action):
	def name(self):
		return "action_show_thing_to_buy"

	def run(self, dispatcher, tracker, domain):
		assert tracker.get_slot("thing_to_buy") # sanity check
		msg = "List:\n"
		msg += "\n".join(tracker.get_slot(thing_to_buy))
		dispatcher.utter_message(text=msg)

		return []
