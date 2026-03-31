# Reproduceable Analytical Pipelines

## Refs

[RAP nhs digital community environments and packages](https://nhsdigital.github.io/rap-community-of-practice/training_resources/python/intro-to-python/) 
- guidance on RAP, and RAP levels to assess projects against
- python style guide
- how to write good functions
- how to write good tests


[RAP](https://github.com/NHSDigital/rap-community-of-practice/tree/main/docs)
[what rap is why it matters high level gov long strategy docs](https://analysisfunction.civilservice.gov.uk/policy-store/reproducible-analytical-pipelines-strategy/)
develop their pipeline using:

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


[Advice on how to implement RAP blog on one teams experience](https://analysisfunction.civilservice.gov.uk/blog/the-nature-of-reproducible-analytical-pipelines-rap/)
- power of git
- was a learning curve
- "It’s a completely new way of working for us so it took some time for us to get to grips with it, but we got there. If we were to do this project again, I would push my team to use this to host their code from the first line they developed. I would also encourage them to get into the habit of committing to our repository much more frequently. When it came to quality assuring our pipeline, time elapsed between commits meant we had large chunks of code to check. This would have been a much more streamlined and manageable process had we used Git little and often from the start."


[cute rap overview friendly read](https://nhsdigital.github.io/rap-community-of-practice/#what-is-rap)

""Recommendation 7: promote and resource ‘Reproducible Analytical Pipelines’ ... as the minimum standard for academic and NHS data analysis"
Data Saves Lives, 2022 government strategy report"


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
[RAP Refactoring guide](https://nhsdigital.github.io/rap-community-of-practice/training_resources/coding_tips/refactoring-guide/)



[Time management starting to use Rap](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/rap-readiness/)


[Preparing for RAP List of code, docs, tool resource to help get rap ready](https://nhsdigital.github.io/rap-community-of-practice/tags/#preparing-for-rap)
- **really useful list here**
- coding tips section


[Time management starting to use Rap](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/rap-readiness/)

[Recommends applying RAP thin slice first](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/thin-slice-strategy/)
focus on one ingestion → dashboard process then slice

Everyone a reviewer for PR, take detours for simple training dives and solving together anything that feels not right or is a blocker.
There are in the POC project good practice docs, references and some training reference for pyspark and python, unit testing etc.

[Rap Service](https://nhsdigital.github.io/rap-community-of-practice/#our-rap-service)
"Our RAP Service
The NHS England Data Science team offers support to NHSE teams looking to implement RAP.

We'll:

Work alongside your team for 6-12 weeks
Work with you to recreate one of your processes in the RAP way
Deliver training in Git, Python, R, Databricks, and anything else you'll need
Learn more:"

[another approachable longer doc about RAP and what it involves](https://best-practice-and-impact.github.io/qa-of-code-guidance/principles.html)


[Quality coding, e.g doc manual coding in repo?](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/workflow/quality-assuring-analytical-outputs/)

[RAP massive gov doc maybe useful if looking for something specific its long](https://www.gov.uk/guidance/the-aqua-book)

[click newbie for git guide for rap](https://nhsdigital.github.io/rap-community-of-practice/implementing_RAP/skills_for_rap/git_for_rap/)

[RAP Ratings Baseline, Bronze, Silver, Gold](https://nhsdigital.github.io/rap-community-of-practice/introduction_to_RAP/levels_of_RAP/)
- we probably aim for silver as should achieve alot but ensure baseline
- we also are looking at hitting most the gold with cicd, and databricks and dabs


[Excellent NHSDigital Rap practice docs](
https://github.com/NHSDigital/rap-community-of-practice/blob/main/docs/implementing_RAP/publishing_code/how-to-publish-your-code-in-the-open.md)




# Extras: Gov View
[gov rap policies](https://github.com/NHSDigital/rap-community-of-practice/blob/main/docs/introduction_to_RAP/gov-policy-on-rap.md)
[open source 1](https://www.gov.uk/guidance/be-open-and-use-open-source)
[open source 2](https://gds.blog.gov.uk/2017/09/04/the-benefits-of-coding-in-the-open/)
[open source 3](https://github.com/nhsx/open-source-policy/blob/main/open-source-policy.md)