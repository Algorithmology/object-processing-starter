# Object Processing

## Table of Contents

<!---toc start-->

* [Object Processing](#object-processing)
  * [Table of Contents](#table-of-contents)
  * [Add Your Name Here](#add-your-name-here)
  * [Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."](#re-type-the-sentence-i-adhered-to-the-allegheny-college-honor-code-while-completing-this-project)
  * [Program Output](#program-output)
    * [Report at least two examples of program output from when you ran the `systemsense` program](#report-at-least-two-examples-of-program-output-from-when-you-ran-the-systemsense-program)
      * [First output from running the `systemsense` program](#first-output-from-running-the-systemsense-program)
      * [Second output from running the `systemsense` program](#second-output-from-running-the-systemsense-program)
    * [Use two fenced code blocks to provide output from five different runs of `objectprocessor` with five different inputs](#use-two-fenced-code-blocks-to-provide-output-from-five-different-runs-of-objectprocessor-with-five-different-inputs)
      * [Provide the command the output for the first run of the `objectprocessor`](#provide-the-command-the-output-for-the-first-run-of-the-objectprocessor)
      * [Provide the command the output for the second run of the `objectprocessor`](#provide-the-command-the-output-for-the-second-run-of-the-objectprocessor)
      * [Provide the command the output for the third run of the `objectprocessor`](#provide-the-command-the-output-for-the-third-run-of-the-objectprocessor)
      * [Provide the command the output for the fourth run of the `objectprocessor`](#provide-the-command-the-output-for-the-fourth-run-of-the-objectprocessor)
      * [Provide the command the output for the fifth run of the `objectprocessor`](#provide-the-command-the-output-for-the-fifth-run-of-the-objectprocessor)
  * [Experiment Design](#experiment-design)
  * [Research Questions](#research-questions)
  * [Data Tables](#data-tables)
  * [Performance Analysis](#performance-analysis)
  * [Source Code](#source-code)
    * [Describe in detail the operation of the `PersonAttributes` declaration](#describe-in-detail-the-operation-of-the-personattributes-declaration)
    * [Describe in detail the operating of the `PersonAttributes` method call](#describe-in-detail-the-operating-of-the-personattributes-method-call)
    * [Describe in detail how the provided source code works](#describe-in-detail-how-the-provided-source-code-works)
  * [Professional Development](#professional-development)
    * [What are the benefits and drawbacks of object-oriented programming in Python?](#what-are-the-benefits-and-drawbacks-of-object-oriented-programming-in-python)
    * [What is challenging about designing an experiment to evaluate the performance of object processing?](#what-is-challenging-about-designing-an-experiment-to-evaluate-the-performance-of-object-processing)
    * [How do the empirical results suggest that you don't yet know the entire story about the performance of object processing?](#how-do-the-empirical-results-suggest-that-you-dont-yet-know-the-entire-story-about-the-performance-of-object-processing)
  * [Take Home Points](#take-home-points)

<!---toc end-->

## Add Your Name Here

## Re-type the sentence "I adhered to the Allegheny College Honor Code while completing this project."

TODO: You must retype the sentence here in order to digitally sign your pledge.

**IMPORTANT:** If you do not type the required sentence then the course
instructor will not know that you adhered to the Allegheny College Honor Code
while completing the project.

## Program Output

### Report at least two examples of program output from when you ran the `systemsense` program

#### First output from running the `systemsense` program

```text
output
```

#### Second output from running the `systemsense` program

```text
output
```

### Use two fenced code blocks to provide output from five different runs of `objectprocessor` with five different inputs

TODO: Provide the complete command-line for your use of the `objectprocessor` program

#### Provide the command the output for the first run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces

- `command`

```text
output
```

#### Provide the command the output for the second run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces

- `command`

```text
output
```

#### Provide the command the output for the third run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces

- `command`

```text
output
```

#### Provide the command the output for the fourth run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces

- `command`

```text
output
```

#### Provide the command the output for the fifth run of the `objectprocessor`

TODO: Provide your own example of a command and the output that it produces

- `command`

```text
output
```

## Experiment Design

TODO: Describe your design of the `objectprocessor` experiment that answers
your own research questions (as specified in the next subsection), focusing on
these key issues:

- **Data file**: either subsets of or the entire `input/people.txt` file or
alternative files that contain rows of data with `Person` attributes that can be
parsed and then transformed into instances of the `Person` class; this aspect of
the experiment may also investigate both the number of rows inside of the data
file and the contents of each row inside of the data file.
- **Input time**: the time overhead associated with reading in the specified
data file.
- **Output time**: the time overhead associated with writing to a specified file
all the details about each matching instance of the `Person` class.
- **Search time**: the time overhead associated with searching for a specified
search term using the various approaches for string comparison.

TODO: The **Search time** is a critical part of the experiment and, as you study it,
please make sure that you consider the following key issues:

- The search term that will control whether or not a specific attribute of the
`Person` class will be considered a match.
- The attribute that is a part of the each instance of the `Person` class that
will be subject to comparison with the search term.
- Whether the matching technique involves `in` or `==` or a fuzzy-matching
technique provided by the `rapidfuzz` library.
- If the fuzzy-matching technique is chosen, then which specific algorithm
provided by `rapidfuzz` should perform the matching, like `fuzz.ratio`.

TODO: You must justify every part of your experiment design and then furnish
output examples to demonstrate that your program generates correct data!

## Research Questions

TODO: Clearly state at least three research questions that you want to ask and
answer by using the `objectprocessor` program. You should provide the research
questions in a list that starts with "RQ" and ends with a question mark.

- TODO: State your first research question
- TODO: State your second research question
- TODO: State your third research question

TODO: Although the statement of three research questions is required for the
baseline associated with this project, you may need to state and answer
additional questions in order to develop a full-featured understanding of the
performance trade-offs evident through the use of the `objectprocessor`.

TODO: You must add instrumentation using tools like `timeit` to ensure that the
`objectprocessor` calculates and reports the time overhead data that you will
need to answer your research questions. Before you conduct your experiments,
please carefully confirm that `objectprocessor` calculates and reports the time
overhead values in a correct fashion.

## Data Tables

TODO: Use Markdown to provide one or more data tables that summarize the results
from running the `objectprocessor` program in different configurations. You
should provide enough data tables and output values to ensure that you can
answer all of your research questions and, if possible, use the empirical
results to classify the likely worst-case time complexity of each of the
algorithms that you studied in this algorithm engineering project.

### First Data Table

### Second Data Table

### Third Data Table

## Performance Analysis

TODO: Provide at least three paragraphs that explain which algorithms inside of
the `objectprocessor` are the fastest, by how much they are faster, and how you
knew that the algorithm was faster, referencing the data in the aforementioned
command outputs and the data tables to support your response. You should make
sure that you answer each of the at least three research questions that you
posed in a previous section of this report.

TODO: Make sure that your responses explain WHY certain configurations are faster!

TODO: It is not sufficient to ONLY explain WHICH configuration is faster!

## Source Code

### Describe in detail the operation of the `PersonAttributes` declaration

TODO: Provide a description of each line in the following source code

```python
@dataclass(frozen=True)
class PersonAttributes:
    """Define the PersonAttributes dataclass for constant(s)."""

    Name: str
    Country: str
    Phone_Number: str
    Job: str
    Email: str
```

### Describe in detail the operating of the `PersonAttributes` method call

TODO: Provide a description of each line in the following source code

```python
person_attributes = PersonAttributes(
    Name="name",
    Country="country",
    Phone_Number="phone_number",
    Job="job",
    Email="email",
)
```

### Describe in detail how the provided source code works

TODO: Provide a description of each line in the following source code

```python
def __init__(
    self, name: str, country: str, phone_number: str, job: str, email: str
) -> None:
    """Define the constructor for a person."""
    self.name = name
    self.country = country
    self.phone_number = phone_number
    self.job = job
    self.email = email
```

## Professional Development

### What are the benefits and drawbacks of object-oriented programming in Python?

TODO: Provide a one-paragraph response that answers this question in your own words.

### What is challenging about designing an experiment to evaluate the performance of object processing?

TODO: Provide a one-paragraph response that answers this question in your own words.

### How do the empirical results suggest that you don't yet know the entire story about the performance of object processing?

TODO: Provide a one-paragraph response that answers this question in your own words.

## Take Home Points

TODO: Provide a two to three sentence statement about the key takeaways from
conducting this experiment. Please note that the course instructor will display
some student takeaways on the course web site and use them to facilitate
follow-on class discussions.
