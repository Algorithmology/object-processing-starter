"""Extract and save the data about the person from the CSV file."""

from typing import List

from rapidfuzz import fuzz

from objectprocessor import approach, person

FUZZY_MATCH_THRESHOLD = 90

# TODO: look at the entire data set inside of the inputs/people.txt
# TODO: you may need to create and use different data sets, depending
#       on the experiments that you must conduct to answer your RQs


def extract_person_data(data: str) -> List[person.Person]:
    """Extract a specified data column from the provided textual contents."""
    # create an empty list of the data
    # note that the data file:
    # --> contains five columns
    # --> each of which contains textual data with a different meaning
    data_list = []
    # TODO: refer to the file called input/people.txt to learn more about
    # the format of the comma separated value (CSV) file that we must parse;
    # iterate through each line of the file and extract all relevant details
    # use the csv.reader to accomplish the task of parsing the CSV file
    # --> extract each of the attributes about a person from the line variable
    # --> construct a new instance of the Person class that contains all
    # of the attributes that were extracted from the CSV file
    # --> append the current instance of the person class to the data_list variable
    # return the list of all of the specified column
    return data_list


def write_person_data(
    file_name: str, person_data: List[person.Person]
) -> None:
    """Write the person data stored in a list to the specified file."""
    # create an empty list that will store the person data as a list of strings
    converted_person_data = []
    # TODO: iterate through every person inside of the person_data list
    # --> create a list out of this person where each of the person's
    # attributes are stored inside of an index in the list
    # --> append this converted person list to the list called converted_person_data
    # --> use the csv.writer approach and the writerows function to write out
    # the list of lists of strings that contain all of the person data


def find_matching_people(
    attribute: str,
    match: str,
    person_data: List[person.Person],
    find_approach: approach.SearchApproach = approach.SearchApproach.containment,
) -> List[person.Person]:
    """Find people who have matching data for a specified attribute."""
    # create an empty list of people who have an attribute matching the search term in match
    matching_people_list = []
    # TODO: iterate through all of the people in the person_data list
    # --> the current person has an attribute that contains the search term in match
    # --> add the current person to the matching_person_list
    # return the matching_person_list
    return matching_people_list


def is_matching_person(
    attribute: str,
    match: str,
    search_person: person.Person,
    find_approach: approach.SearchApproach,
) -> bool:
    """Dispatch to determine if the person's specified attribute contains the search term in match."""
    # TODO: use the attr approach to build up a function call based on
    # --> TODO: The string that is stored inside of the find_approach variable;
    # make sure that it is calling the function in this module.
    # Use one of the two standard, non-fuzzy functions
    # --> TODO: Call the function that was built up and return its result
    # Call the general-purpose fuzzy matching function
    return False


def is_matching_person_containment(
    attribute: str,
    match: str,
    search_person: person.Person,
) -> bool:
    """Use containment to determine if the person's specified attribute contains the search term in match."""
    # TODO: determine which attribute was provided and then
    # use the containment checking approach to determine
    # if there is an appropriate match
    return False


def is_matching_person_equality(
    attribute: str,
    match: str,
    search_person: person.Person,
) -> bool:
    """Use equality to determine if the person's specified attribute contains the search term in match."""
    # TODO: determine which attribute was provided and then
    # use the containment checking approach to determine
    # if there is an appropriate match
    return False


def is_matching_person_fuzzy(
    attribute: str,
    match: str,
    search_person: person.Person,
    find_approach: approach.SearchApproach,
) -> bool:
    """Use equality to determine if the person's specified attribute contains the search term in match."""
    # TODO: use getattr to build up a function call based on the string that is stored
    # in the find_approach variable; make sure to call one of the functions
    # provided by the rapidfuzz library that will return a floating-point value
    # Reference: https://github.com/rapidfuzz/RapidFuzz
    # Reference: https://rapidfuzz.github.io/RapidFuzz/
    rapid_fuzz_function = getattr(fuzz, f"{find_approach}")
    # TODO: determine which attribute was provided and then
    # use the containment checking approach to determine
    # if there is an appropriate match
    return False
