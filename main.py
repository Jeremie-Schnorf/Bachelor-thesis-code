import pandas


BPI_challenge_2019= pandas.read_csv("BPI_Challenge_2019.csv", sep=',')
print(BPI_challenge_2019)

def number_of_events(event_log):
    row_numbers = len(event_log)
    return (row_numbers)

def attribute_names (event_log):
    attr_names= (event_log.columns.values.tolist())
    return (attr_names)

def number_of_attributes (event_log):
    index_attr= attribute_names(event_log)
    num_attr=len(index_attr)
    return(num_attr)


def number_of_cases_eventCaseRatio (event_log, Case_ID):
    list_cases= event_log[Case_ID]
    number_cases= len(set(list(list_cases)))
    event_cases_ratio= number_of_events(event_log)/number_cases
    return [number_cases,event_cases_ratio]




def size_eventlog(eventlog):
    print("information about the size of the event log")
    print ("There are {}  events.".format(number_of_events(eventlog)))
    print("There are {} attributes".format(number_of_attributes(eventlog)))
    print("The attribute names are {}".format(attribute_names(eventlog)))
    print("There are {} cases.".format(number_of_cases_eventCaseRatio(BPI_challenge_2019,"Case ID")[0]))
    print("The cases to events ratio is {}.".format(number_of_cases_eventCaseRatio(BPI_challenge_2019,"Case ID")[1]))

size_eventlog(BPI_challenge_2019)



