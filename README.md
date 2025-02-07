# :microscope: Object Processing

[![build](../../actions/workflows/build.yml/badge.svg)](../../actions/)
![Platforms: Linux, MacOS, Windows](https://img.shields.io/badge/Platform-Linux%20%7C%20MacOS%20%7C%20Windows-blue.svg)
[![Language: Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Commits: Conventional](https://img.shields.io/badge/Commits-Conventional-blue.svg)](https://www.conventionalcommits.org/en/v1.0.0/)
[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

## :sparkles: Table of Contents

<!--toc start-->

- [:microscope: Object Processing](#microscope-object-processing)
  - [:sparkles: Table of Contents](#table-of-contents)
  - [:checkered_flag: Introduction](#checkeredflag-introduction)
  - [:handshake: Seeking Assistance](#handshake-seeking-assistance)
  - [:airplane: Project Overview](#airplane-project-overview)
  - [:tada: Program Specification](#tada-program-specification)

<!--toc end-->

## :checkered_flag: Introduction

If you are a student completing this project as part of a class at Allegheny
College, you can check the schedule on the course web site for the due date or
ask the course instructor for more information about the due date or check the
due date by clicking the appropriate box inside of this file. Please note that
the content provided in the `README.md` file for this GitHub repository is an
overview of the project and thus may not include the details for every step
needed to successfully complete every project deliverable. This means that you
may need to schedule a meeting during the course instructor's office hours to
discuss aspects of this project.

## :handshake: Seeking Assistance

Even though the course instructor will have covered all the concepts central
to this project before you start to work on it, please note that not every
detail needed to successfully complete the assignment will have been covered
during prior classroom sessions. This is by design as an important skill that
you must practice as an algorithm engineer is to search for and then understand
and ultimately apply the technical content found in additional resources.

## :airplane: Project Overview

This project invites you to implement and use a program called `objectprocessor`
that conducts an experiment to evaluate the performance of searching for data
that matches specific attributes of an object. When provided with an input file,
like the one in the `input/people.txt` file, the `objectprocessor` will process
instances of the `People` class that have the following attributes:

- `name: str`
- `country: str`
- `phone_number: str`
- `job: str`
- `email: str`

When it is comparing one of these attributes to the provided search string it
will do so using one of these approaches:

- Containment checking through the use of `in`
- Equality checking through the use of `==`
- Fuzzy matching through the use of the functions provided by the `rapidfuzz` package:
  - `ratio`
  - `partial_ratio`
  - `token_set_ratio`
  - `token_sort_ratio`
  - `weighted_ratio`
  - `quick_ratio`

In addition to providing all the functionality needed for searching any
attribute of the `Person` class, the `objectprocessor` program should be able
to save all the matching records inside of a specified file. The
`objectprocessor` program should also included "timing instrumentation" that
records the cost associated with various aspects of specified process such as
(i) the time needed to read or write the text file, (ii) the time needed to
complete the entire search process, and/or (iii) the time needed for perform
different types of string matches (i.e., matching with `in`, `==`, or one of
the functions from the `rapidfuzz` package) on a specific attribute of a
`Person` object. For instance, the `objectprocessor` could use the
[timeit](https://docs.python.org/3/library/timeit.html) package to measure the
performance of the `in` operator for different data containers, following one
of the approaches outlined in the article called [measure execution time with
timeit in Python](https://note.nkmk.me/en/python-timeit-measure/).

After cloning this repository to your computer, please take the following steps
to get started on the project:

- To install the necessary software for running the `objectprocessor` program
that you will create as a part of this project, you may consider installing and
using the [`devenv`](https://devenv.sh/getting-started/) tool, bearing in mind
that it is not necessary for you to install the `cachix` program that may be
referenced by these installation instructions. Please note that students who are
using Windows 11 should first install Windows subsystem for Linux (`wsl2`)
before attempting to install `devenv`. Once you have installed `devenv` and
cloned this repository to your computer, you can `cd` into the directory that
contains the `pyproject.toml` file and then type `devenv shell`. It is important
to note that the first time you run this command it may complete numerous steps
and take a considerable amount of time.
- Once this command completes correctly, you will have a Python development
environment that contains a recent version of Python and Poetry! You can verify
that you have the correct version of these two programs by typing:
  - `python --version`
  - `poetry --version`
- If you do not see a recent version of Python after typing the two
aforementioned commands, then it is possible that some part of the installation
process did not work correctly. If that occurs, then please read the following
suggestions and talk with the course instructor and a student technical leader
about what to do next.
- If some aspect of the installation with `devenv` did not work correctly, then
please resolve what is wrong before proceeding further! Alternatively, you may
install the aforementioned versions of Python and Poetry on your laptop using a
tool like [`mise`](https://mise.jdx.dev/). With that said, please make sure that
you use the most recent version of Python and Poetry to complete this project
and, whenever possible, those versions match the ones chosen in GitHub Actions.
This means that, to ensure that the results from running the experiments are
consistent and, as best as is possible, comparable to the results from other
computers, you should use exactly the same version of Python and Poetry on your
laptop and in GitHub Actions. For instance, when you run `containmentcheck` in
GitHub Actions, you should normally see that it is using at least Poetry version
`1.8.5` and Python version `3.12.8`.
- Before moving to the next step, you may need to again type `poetry install` in
order to avoid the appearance of warnings when you next run the
`objectprocessor` program. Now you can type the command `poetry run
objectprocessor --help` and explore how to use the program.

## :tada: Program Specification

Before implementing the program so that it adheres to the following requirements
and produces the expected output, please note that the program will not work
unless you add the required source code at the designated `TODO` markers. With
that said, after you complete a correct implementation of all the
`objectprocessor`'s features you can run it with the command `poetry run
objectprocessor --search-term rtorres@example.org --attribute email --input-file
input/people.txt --output-file output/people.txt --approach ratio` and
see that it produces output like the following.

```text
- Cindy Burns is a Pharmacist, hospital who lives in Dominican Republic. You can call this person at (102)481-3875 and
email them at rtorres@example.org
- James Thomas is a Programmer, systems who lives in Tokelau. You can call this person at (951)364-1795x64728 and email
them at utorres@example.org
- Jason Gordon is a Media planner who lives in Nepal. You can call this person at (466)767-1511 and email them at
rtorres@example.org
- Marie Cross is a Solicitor, Scotland who lives in Anguilla. You can call this person at 001-881-969-0016x4049 and email
them at htorres@example.org
- James Bentley is a Physiological scientist who lives in Honduras. You can call this person at 887.988.8745x787 and email
them at ntorres@example.org
- Amber Clayton is a Doctor, general practice who lives in Solomon Islands. You can call this person at 062.170.6657x32875
and email them at ambertorres@example.org
- Christopher Edwards is a IT consultant who lives in Netherlands Antilles. You can call this person at
001-886-784-5352x444 and email them at dtorres@example.org
- Timothy Fuller is a Designer, ceramics/pottery who lives in Poland. You can call this person at 001-233-006-6687x8340
and email them at utorres@example.org
- Elaine Parker is a Occupational therapist who lives in Micronesia. You can call this person at 447.187.0210 and email
them at ztorres@example.org
```

Please note that your implementation of the `objectprocessor` program should
work for all the specified experimental configurations in the introduction
to the project and in the `writing/reflection.md` file. For instance, this
means that `objectprocessor` should be able to determine if a provided search
string matches any of the possible attributes of an instance of the `Person`
class through the use of either `in`, or `==`, or any of the specified
functions in the `rapidfuzz` package. If you study the files in the
`objectprocessor/` directory you will see that they have many `TODO` markers
that designate the functions you must implement so as to ensure that
`objectprocessor` runs the desired experiment and produces the correct output.
Once you complete a task associated with a `TODO` marker, make sure that you
delete it and revise the prompt associated with the marker into a meaningful
comment.

Ultimately, you should design your own experiment and state and run experiments
to answer your own research questions, focusing on these key issues:

- **Data file**: either subsets of or the entire `input/people.txt` or
alternative files that contain rows of data with `Person` attributes
- **Input time**: the time overhead associated with reading in the specified
data file
- **Output time**: the time overhead associated with writing to a specified
file all the details about each matching instance of the `Person` class
- **Search time**: the time overhead associated with searching for a specified
search term using the various approaches for string comparison

It is important to note that the `writing/reflection.md` file contains more
details about the ways in which you should design the experiments for this
project. Please make sure that, during the second week of this assignment, you
meet with the course instructor to receive feedback on the design of your
experiment before you embark on conducting the experiments and analyzing the
data. Finally, here are other issues that you should keep in mind as you work
on the `containmentcheck` program:

- Once you have defined your research questions and received approval from the
course instructor to conduct an experiment that will answer them, you will
should decide where you will place timing instrumentation into the modules of
the program that contain the functionality that you will be benchmarking.
- To collect the performance data you should consider the use of Python packages
such as `timeit` or `time`. If you decide that other time packages are more
appropriate for your use case, then you may use them provided that you justify
your decision in a suitable section of the `writing/reflection.md` file.
- You must implement test cases for all the untested modules, excepting the
`main` module, while further ensuring that the test suite achieves the desired
level of code coverage. It is important to note that the coverage report
produced by the `pytest-cov` plugin will, by default, only report the coverage
for the test cases already defined in the `tests/` directory. This means that if
you have not already implemented a test suite for a module it will not appear in
the coverage report and thus the test coverage may appear artificially higher
than it is in actuality.
- If you have already installed the
[GatorGrade](https://github.com/GatorEducator/gatorgrade) program that runs the
automated grading checks provided by
[GatorGrader](https://github.com/GatorEducator/gatorgrader) you can, from the
repository's base directory, run the automated grading checks by typing
`gatorgrade --config config/gatorgrade.yml`.
- You may also review the output from running GatorGrader in GitHub Actions.
- Don't forget to provide all the required responses to the technical writing
prompts in the `writing/reflection.md` file.
- Please make sure that you completely delete the `TODO` markers and their
labels from all the provided source code. This means that instead of only
deleting the `TODO` marker from the code you should delete the `TODO` marker and
the entire prompt and then add your own comments to demonstrate that you
understand all the source code in this project.
- Please make sure that you also completely delete the `TODO` markers and their
labels from every line of the `writing/reflection.md` file. This means that you
should not simply delete the `TODO` marker but instead delete the entire prompt
so that your reflection is a document that contains polished technical writing
that is suitable for publication on your professional web site.
