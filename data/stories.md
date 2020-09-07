## normal path
* greet
  - utter_botgreet
* bot_name
  - utter_bot_name
* introduction_corona_virus
  - utter_introduction_corona_virus
* prevention
  - utter_prevention
* symptoms
  - utter_symptoms
* spread_from_food
  - utter_spread_from_food
* spread_of_community
  - utter_spread_of_community
* deny
  - utter_thanks
* goodbye
  - utter_goodbye

## form  path
* greet
  - utter_botgreet
* bot_name
  - utter_bot_name
* introduction_corona_virus
  - utter_introduction_corona_virus
* fill_form
  - test_form
  - form{"name":"test_form"}
  - form{"name":null}
* deny
  - utter_thanks
* goodbye
  - utter_goodbye

## fallback story
* out_of_scope
  - utter_ask_repharse

## New Story

* greet
    - utter_botgreet
* prevention
    - utter_prevention
* fill_form
    - test_form
    - form{"name":"test_form"}
    - slot{"requested_slot":"name"}
* form_name{"name":"Arpan Osti"}
    - slot{"name":"Arpan Osti"}
    - test_form
    - slot{"name":"Arpan Osti"}
    - slot{"requested_slot":"address"}
* form_address{"address":"damak"}
    - slot{"address":"damak"}
    - test_form
    - slot{"address":"damak"}
    - slot{"requested_slot":"number"}
* form_number{"number":"9837236372"}
    - slot{"number":"9837236372"}
    - test_form
    - slot{"number":"9837236372"}
    - slot{"requested_slot":"fever"}
* form_fever{"fever":"No"}
    - slot{"fever":"No"}
    - test_form
    - slot{"fever":"No"}
    - slot{"requested_slot":"dry_cough"}
* form_dry_cough{"dry_cough":"yes"}
    - slot{"dry_cough":"yes"}
    - test_form
    - slot{"dry_cough":"yes"}
    - slot{"requested_slot":"triedness"}
* form_triedness{"triedness":"No"}
    - slot{"triedness":"No"}
    - test_form
    - slot{"triedness":"No"}
    - slot{"requested_slot":"diarrhoea"}
* form_diarrhoea{"diarrhoea":"yes"}
    - slot{"diarrhoea":"yes"}
    - test_form
    - slot{"diarrhoea":"yes"}
    - slot{"requested_slot":"sore_throat"}
* form_sore_throat{"sore_throat":"No"}
    - slot{"sore_throat":"No"}
    - test_form
    - slot{"sore_throat":"No"}
    - slot{"requested_slot":"smell"}
* form_smell{"smell":"yes"}
    - slot{"smell":"yes"}
    - test_form
    - slot{"smell":"yes"}
    - form{"name":null}
    - slot{"requested_slot":null}
