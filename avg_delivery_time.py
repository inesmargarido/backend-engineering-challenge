import json
import argparse
from datetime import datetime, timedelta
from collections import deque

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

  # get only timestamp and duration of each event
  events = [(datetime.fromisoformat(event['timestamp']), event['duration']) for event in events]
  
  # get the first event's timestamp (rounded down to the minute)
  start_time = events[0][0].replace(second=0, microsecond=0)
  # get the latest event's timestamp and round up to the next minute
  end_time = events[-1][0].replace(second=0, microsecond=0) + timedelta(minutes=1)

  current_minute = start_time # initiate the iterator for the outside loop 
  durations = deque() # manage durations for the calculations
  i = 0 # iterator for events
  current_window_count = 0 # number of durations in the current window
  current_window_sum = 0 # sum of durations in the current window
  avg_per_min = 0 # variable to store the average calculation
  print_count = 0 # number of outputs already printed

  while current_minute <= end_time:
    # add durations to the deque which correspond to translations in the current minute
    while i < len(events) and (current_minute - timedelta(minutes=1) < events[i][0] <= current_minute):
      durations.append(events[i][1])
      current_window_sum += events[i][1]
      current_window_count += 1
      i += 1
    
    # calculate current average
    avg_per_min = current_window_sum/current_window_count if current_window_count > 0 else 0
  
    # print output
    print(f'{{"date": "{current_minute.isoformat()}", "average_delivery_time": "{avg_per_min:.1f}"}}')

    print_count += 1
    current_minute += timedelta(minutes=1)

    # if we reach the end of the window, slide window to the right 
    if print_count > window_minutes:
      removed_duration = durations.popleft() # remove the oldest duration from the deque
      current_window_sum -= removed_duration # remove from the sum
      current_window_count -= 1 # remove from the count
      print_count = 0 # reset counter


def main():
  args = parse_args()
  events = read_events(args.input_file)
  moving_averages = calculate_moving_averages(events, args.window_minutes)

if __name__ == "__main__":
  main()