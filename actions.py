# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List,Union
from rasa_sdk.forms import FormAction
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, UserUtteranceReverted
from rasa_sdk.executor import CollectingDispatcher

# from database_action import RasaDatabase


# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         name = tracker.get_slot("name")
#         print("Name:",name)

#         dispatcher.utter_message(f"Hi! {name}, Welcome for corona virus test")

#         return []


class TestForm(FormAction):
    """Collects sales information and adds it to the spreadsheet"""

    def name(self) -> Text:
        return "test_form"
    
    @staticmethod
    def required_slots(tracker: Tracker):
        """A list of required slots that the form has to fill"""
        return ["name","address","number","fever","dry_cough","triedness","diarrhoea","sore_throat","smell"]
    
    def slot_mappings(self):
        return {
        "name": self.from_entity(entity="name", intent="form_name"),
        "address": self.from_entity(entity="address", intent="form_address"),
        "number": self.from_entity(entity="number", intent="form_number")
        }

    def submit(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ):
        score = []
        if tracker.get_slot('fever') == 'yes':
            score.append(1)
        else:
            score.append(0)
        if tracker.get_slot('dry_cough') == 'yes':
            score.append(1)
        else:
            score.append(0)
        if tracker.get_slot('triedness') == 'yes':
            score.append(1)
        else:
            score.append(0)
        if tracker.get_slot('diarrhoea') == 'yes':
            score.append(1)
        else:
            score.append(0)
        if tracker.get_slot('sore_throat') == 'yes':
            score.append(1)
        else:
            score.append(0)
        if tracker.get_slot('smell') == 'yes':
            score.append(1)
        else:
            score.append(0)
        if sum(score)<= 3:
            dispatcher.utter_message(template="utter_submit",s_name=tracker.get_slot('name'))
        else:
            dispatcher.utter_message(template="utter_neg_submit",s_name=tracker.get_slot('name'))
        # RasaDatabase(tracker.get_slot('name'),tracker.get_slot('address'),tracker.get_slot('number'))
        return []

class ActionFallbackAction(Action):

    def name(self) -> Text:
        return "action_default_ask_affirmation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(template="utter_ask_affirmation")

        return [UserUtteranceReverted()]