## happy_path_1 (greet -> request_buy- > say_thanks)
* greet
 - utter_say_hi_1	
* request_buy
 - action_save_thing_to_buy{"thing_to_buy": ""}
* say_thanks
 - utter_welcome_1

## happy_path_2 (greet -> request_buy)
* greet{"assistant_name": "xesi"}
 - utter_say_hi_2
* request_buy
 - action_save_thing_to_buy

## happy_path_3 (what_to_buy -> say_thanks -> say_bye)
* what_to_buy
 - action_show_thing_to_buy
* say_thanks
 - utter_welcome_2
* say_bye
 - utter_say_bye_1

## happy_path_4 (what_to_buy -> say_bye)
* what_to_buy
 - action_show_thing_to_buy
* say_bye{"assistant_name": "xesi"}
 - utter_say_bye_2
