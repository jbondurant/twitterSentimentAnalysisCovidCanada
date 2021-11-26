import dateutil.parser
from datetime import datetime



def convert_time_to_int(time_given):
    datetimeThing = dateutil.parser.isoparse(time_given)
    datetimeTimeStamp = datetimeThing.timestamp()
    return datetimeTimeStamp;

def get_span_minutes(start_time, end_time):
    start_time_number = convert_time_to_int(start_time)
    end_time_number = convert_time_to_int(end_time)
    span_minutes = (end_time_number - start_time_number) / 60
    return span_minutes

#This method gives an initial shift of 2 minutes to the first sample
def span_to_splits(start_time, end_time, num_samples, start_time_shift):

    start_time_number = convert_time_to_int(start_time)
    end_time_number = convert_time_to_int(end_time)

    span = end_time_number - start_time_number
    step_size = span / (num_samples - 1)
    start_end_times_splits = []
    for i in range(num_samples):
        end_split_number = round(start_time_number + i * step_size, 0)
        start_split_number = end_split_number - start_time_shift
        if i == 0:
            end_split_number += 240
            start_split_number += 240
        end_split_time = datetime.utcfromtimestamp(end_split_number)
        start_split_time = datetime.utcfromtimestamp(start_split_number)

        end_split_time_string = end_split_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        start_split_time_string = start_split_time.strftime("%Y-%m-%dT%H:%M:%SZ")
        time_string_tuple = (start_split_time_string, end_split_time_string)
        start_end_times_splits.append(time_string_tuple)
    return start_end_times_splits





def main():
    start_time = '2021-11-19T00:00:00Z'
    end_time = '2021-11-22T00:00:00Z'
    span_minutes = get_span_minutes(start_time, end_time)
    sample_every_n_minutes = 8
    num_sample_batches = int((span_minutes / sample_every_n_minutes) + 1)
    start_time_shift = 120 #this puts the start time 2 minutes before the end time
    start_end_time_splits = span_to_splits(start_time, end_time, num_sample_batches, start_time_shift)
    x=1

if __name__ == '__main__':
    main()