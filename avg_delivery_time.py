import json
import argparse
from datetime import datetime, timedelta

# function to parse arguments
def parse_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("input_file")
  parser.add_argument("window_minutes", type=int)
  return parser.parse_args()

# function to read events from json file and create an array
def read_events(input_file):
  with open(input_file, "r") as file:
    events = [json.loads(line.strip()) for line in file] # clean any empty spaces
  return events

# main function to calculate the average each minute
def calculate_moving_averages(events, window_minutes):
  # get the first event and round down to the minute
  start_time = datetime.fromisoformat(events[0]['timestamp']).replace(second=0, microsecond=0) 
  # get the latest event and round up to the next minute (where the duration will enter the avg calculation)
  end_time = datetime.fromisoformat(events[-1]['timestamp']).replace(second=0, microsecond=0) + timedelta(minutes=1)

  current_minute = start_time # initiate the iterator for the outside loop 
  durations = [] # initiate the array to keep the durations to aggregate in each minute

  count = -1 # set the count of passed minutes to -1, so that only after the X'th minute it will reset the calculations
  while current_minute <= end_time:
    
    # if the window_size is reached, reset the durations array with only the last duration
    if count == window_minutes:
      durations = [durations[-1]]

    for event in events: # in each minute, search for translations
      timestamp = datetime.fromisoformat(event['timestamp']).replace(second=0, microsecond=0) + timedelta(minutes=1)
      if  timestamp == current_minute: # if there is a translation in this current minute
        durations.append(event['duration']) # add durations of translation to the array
    if len(durations) > 0: # if there are any translations
      avg_per_min = sum(durations)/len(durations) # calculate average
    else:
      avg_per_min = 0 # if no translations in this minute, the average is 0
    print(f'{{"date": "{current_minute.isoformat()}", "average_delivery_time": "{avg_per_min:.1f}"}}') # print the result for this minute

    current_minute += timedelta(minutes=1) # move to the next minute
    count += 1 # counter for the loop


def main():
  args = parse_args() # get arguments
  events = read_events(args.input_file) # read json events
  moving_averages = calculate_moving_averages(events, args.window_minutes) # calculate moving averages

if __name__ == "__main__":
  main()
