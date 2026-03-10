# Feedback

Collect feedback here qqqq


## Concerns to check
- Environments and Packages in https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/intro-to-python/ am i doing enough here is it set by my toml?

## Reviewing Other DBX Repos
- [Nice standard Git flow explanation a resource for getting a clear feel of the process and all things github](https://docs.github.com/en/get-started/using-github/github-flow)
  - add to git docs once other changes made


  ## Make a RAP doc 
[RAP](https://github.com/NHSDigital/rap-community-of-practice/tree/main/docs)
[what rap is why it matters high level gov stuff long strategy](https://analysisfunction.civilservice.gov.uk/policy-store/reproducible-analytical-pipelines-strategy/)

""What you need for RAP
There is no specific tool that is required to build a RAP, but both R and Python provide the power and flexibility to carry out end-to-end analytical processes, from data source to final presentation.

Once the minimum RAP has been implemented statisticians and analysts should attempt to further develop their pipeline using:

functions or code modularity
unit testing of functions
error handling for functions
documentation of functions
packaging
code style
input data validation
logging of data and the analysis
continuous integration
dependency management"

[Nice rap blog](https://analysisfunction.civilservice.gov.uk/blog/the-nature-of-reproducible-analytical-pipelines-rap/)
- should we do unit tests together initially, or pair code initially
“Just-in-time” learning is the best approach
"As we progressed through the project we were inevitably presented with new concepts or tasks unfamiliar to us as a working group. We got into the habit of tackling these with bespoke just-in-time training sessions for the team. When it came to test parts of the code we had developed, we held a unit testing session, facilitated by the BPI Team."
..."We had lots of sessions like this; when we needed to resolve merge conflicts in Git, complete peer reviewing and develop documentation"


doc git branch and comits add

"https://analysisfunction.civilservice.gov.uk/blog/the-nature-of-reproducible-analytical-pipelines-rap/"
- power of git
- was a learning curve
- "It’s a completely new way of working for us so it took some time for us to get to grips with it, but we got there. If we were to do this project again, I would push my team to use this to host their code from the first line they developed. I would also encourage them to get into the habit of committing to our repository much more frequently. When it came to quality assuring our pipeline, time elapsed between commits meant we had large chunks of code to check. This would have been a much more streamlined and manageable process had we used Git little and often from the start."


[cute rap overview friendly read]("https://nhsdigital.github.io/rap-community-of-practice/#what-is-rap")

""Recommendation 7: promote and resource ‘Reproducible Analytical Pipelines’ ... as the minimum standard for academic and NHS data analysis"
Data Saves Lives, 2022 government strategy report"

**Can we do this**
"Our RAP Service
The NHS England Data Science team offers support to NHSE teams looking to implement RAP.

We'll:

Work alongside your team for 6-12 weeks
Work with you to recreate one of your processes in the RAP way
Deliver training in Git, Python, R, Databricks, and anything else you'll need
Learn more:"

[Rap tools git pyspark etc great](https://nhsdigital.github.io/rap-community-of-practice/training_resources/git/introduction-to-git/)
- this is really good
- Learning hub python course 2 days
  - https://analysisfunction.civilservice.gov.uk/training/introduction-to-python/
- learning hub 2 day pyspark
  - https://analysisfunction.civilservice.gov.uk/training/introduction-to-pyspark/

[Rap 7min explanation 7 min questions vid nhs](https://www.youtube.com/watch?v=npEh7RmdTKM)
- python git etc
- process mapping 5.13
- advise write functions names at the beggining just dont populate them yet
  - write the test names for them too but dont create them yet

- DBX git testing, setting us up well for rap


- add this to code quality and the peer review doc
https://nhsdigital.github.io/rap-community-of-practice/training_resources/coding_tips/refactoring-guide/



[Time management starting to use Rap](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/rap-readiness/)
- e.g. 15 hours of tool training recommended
- think slice is what we are after as our next step i think!
- target a level of RAP <- we should do this

[Preparing for RAP List of code, docs, tool resource to help get rap ready](https://nhsdigital.github.io/rap-community-of-practice/tags/#preparing-for-rap)
- really useful list here
- coding tips section


Add to unit testing readme and PR
https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/unit-testing/
- provides good guidances
- good all these docs saying python and pytest

- add to PR does python have python doc strings
   """
   Converts temperatures in Fahrenheit to Celsius.

   Takes the input temperature (in Fahrenheit), calculates the value of
   the same temperature in Celsius, and then returns this value.

   Args:
      temp: a float value representing a temperature in Fahrenheit.

   Returns:
      The input temperature converted into Celsius

   Example:
      fahrenheit_to_celsius(temp=77)
      >>> 25.0
   """
   - this will help us identify when to use other functions, and how to adapt them if they need to change to support more callers


IDE and python over jupyter
  "Jupyter notebooks require quite a bit of arduous coding gymnastics to perform what in Python files would be simple imports"
  but make notebooks easier with utility functions to turn into python libraries sort of https://jupyter-notebook.readthedocs.io/en/4.x/examples/Notebook/rstversions/Importing%20Notebooks.html


Create Next steps doc
Next Steps. Future task

PT recommends
https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/thin-slice-strategy/ 
focus on one ingestion → dashboard process then slice

implement, review as a team, try to maximise RAP good practice using the pipeline

Everyone a reviewer for PR, take detours for simple training dives on anything that feels not right or is a blocker.
There are in the POC project good practice docs, references and some training reference for pyspark and python, unit testing etc.


[RAP massive gov doc maybe useful if looking for somehting specific its long](https://www.gov.uk/guidance/the-aqua-book)

[How to refactor](https://nhsdigital.github.io/rap-community-of-practice/training_resources/coding_tips/refactoring-guide/)

[click newbie for git guide for rap](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/skills_for_rap/git_for_rap/)

[Quality coding, e.g doc manual coding in repo?](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/workflow/quality-assuring-analytical-outputs/)


[RAP level really shows we are on the right track](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/)
- we probably aim for silver as should achieve alot but ensure baseline
- we also are looking at hitting most the gold with cicd, and databricks and dabs


[python style guide if interested, can be useful not just to lint but to help name etc](https://peps.python.org/pep-0008/)

https://nhsdigital.github.io/rap-community-of-practice/training_resources/pyspark/pyspark-style-guide/
"We avoid using pandas or koalas because it adds another layer of learning. The PySpark method chaining syntax is easy to learn, easy to read, and will be familiar for anyone who has used SQL."


pyspark dynamic modular queries lazy.

unit test, expected, error handling, edge cases <- alreay got this comment but make sure i put it in

python > pandas

[pyspark RAP](https://nhsdigital.github.io/rap-community-of-practice/training_resources/pyspark/) put this in PR

[another pyguide](https://github.com/google/styleguide/blob/gh-pages/pyguide.md)
[another approachable longer doc about RAP and what it involves](https://best-practice-and-impact.github.io/qa-of-code-guidance/principles.html)


[gov rap policies](https://github.com/NHSDigital/rap-community-of-practice/blob/main/docs/introduction_to_RAP/gov-policy-on-rap.md)


# Not really need but nice to cpmment somewhere
[open source 1](https://www.gov.uk/guidance/be-open-and-use-open-source)
[open source 2](https://gds.blog.gov.uk/2017/09/04/the-benefits-of-coding-in-the-open/)
[open source 3](https://github.com/nhsx/open-source-policy/blob/main/open-source-policy.md)

