# [Unbabel] Data Engineering Challenge - Moving average of translations

## Requirements:
Python 3.7.x or higher

## How to run:
First, run this command to be able to execute the program from any directory, without the .py extension, and without needing a python call (using the setuptools library):
```pip install -e .```


Run the program like this:
```unbabel_cli --input_file input.json --window_size 10``` 
+ input.json is the input file, in the format described in the challenge
+ window_size is the number of minutes on which to perform the moving average calculation

## How to test:
Use an input file like the one on this folder - test.json - and choose a window size.
To check against the expected output in the challenge instructions, use:
```unbabel_cli test.json 10``` 

## Input format:
{"timestamp": "2018-12-26 18:11:08.509654", "translation_id": "5aa5b2f39f7254a75aa5", "source_language": "en", "target_language": "fr", "client_name": "airliberty", "event_name": "translation_delivered", "nr_words": 30, "duration": 20}
{"timestamp": "2018-12-26 18:15:19.903159", "translation_id": "5aa5b2f39f7254a75aa4", "source_language": "en", "target_language": "fr", "client_name": "airliberty", "event_name": "translation_delivered", "nr_words": 30, "duration": 31}
{"timestamp": "2018-12-26 18:23:19.903159", "translation_id": "5aa5b2f39f7254a75bb3", "source_language": "en", "target_language": "fr", "client_name": "taxi-eats", "event_name": "translation_delivered", "nr_words": 100, "duration": 54}

## Output format
{"date": "2018-12-26 18:11:00", "average_delivery_time": 0.0}
{"date": "2018-12-26 18:12:00", "average_delivery_time": 20.0}
{"date": "2018-12-26 18:13:00", "average_delivery_time": 20.0}
{"date": "2018-12-26 18:14:00", "average_delivery_time": 20.0}
{"date": "2018-12-26 18:15:00", "average_delivery_time": 20.0}
{"date": "2018-12-26 18:16:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:17:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:18:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:19:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:20:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:21:00", "average_delivery_time": 25.5}
{"date": "2018-12-26 18:22:00", "average_delivery_time": 31.0}
{"date": "2018-12-26 18:23:00", "average_delivery_time": 31.0}
{"date": "2018-12-26 18:24:00", "average_delivery_time": 42.5}

The output will appear in the command line.




