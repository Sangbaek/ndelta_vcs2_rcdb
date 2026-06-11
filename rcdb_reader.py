import rcdb
import pandas as pd
import argparse

RCDB_CONNECTION = "mysql://rcdb@hallcdb.jlab.org/vcs"

def rcdb_connect():
  return rcdb.RCDBProvider(RCDB_CONNECTION)

if __name__ == '__main__':
  parser = argparse.ArgumentParser(description='Read the run configuraiton data')
  parser.add_argument('-run', '--run_number', type=int, help='Run number to print out the rcdb')

  args = parser.parse_args()

  run_number = args.run_number
  rcdb_provider = rcdb_connect()
  rcdb_entry_this_run = rcdb_provider.get_run(run_number)

  print("Run: {}".format(run_number))
  print("Start time: {}".format(rcdb_entry_this_run.start_time))
  print("End time: {}".format(rcdb_entry_this_run.end_time))

  for condition in rcdb_entry_this_run.conditions:
    print(condition.value)

  rcdb_provider.disconnect()
