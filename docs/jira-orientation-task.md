qqqq update based of J's jira task edits 
[Example Jira Task](https://hee-tis.atlassian.net/browse/TD-6922)


# Specific tasks

**Contribute to**
- do as much or as little as you like as long as there is a single change even a typo resolution, because we want to be able to do a git commit. Obviously I would love lots of input but decide for yourself.

**look through** literally to the detail that is useful, i may have put in some question prompts to help

**Add to your doc notes** because we will be looking at the same files for comment on files you are not contributing to, follow the instruction for making a doc, in docs with your name and just list file route and observations :)


- X review (make one little change to) 
	- **contribute to** pull_request template in .github folder
	- look at (just for gist) .github/copilot-instructions it might interest you its copilot building a context prompt for copilot based on the repo structure
	- **Add to your doc notes for** Any recommendation or questions
- X review (make one little change to)
	- **contribute to** "git branch and commit naming" in docs
	- **Add to your doc notes for** please can you look at the examples ive done ods_ingest, dlt,  would love more input on best processes that could be in here, especial maybe an end2end process would be brilliant
- X review (make one little change to) 
	- **look through** the project docs generally
	- **look through** github/workflow folder
	- **Read** 
		1. read pull request doc in in .github/
		2. Docs reviewed by
		3. Rest of docs folder .md files
	- **contribute to** tests/test-readme.md
- Phil
	- review the poc against any nhs githubs we can access
		- i have some ive managed to get access for
	- support people with exploring the poc
	- present the poc
	- make updates based on feedback
	- Ensure dabs are updating pipelines once deployed (test runner notepad deployed by job in personal seems to not have been updated - see todo in docs)
	


# Context for all tasks

*If you have any problems at all ask Phil :) this task can be done together if preferred, (whenever you do this kind of thing there will be some issues dont struggle thats not the purpose just ask :) )*

The purpose of the task is to:
- provide an opportunity to see the POC
- identify whats missing
- see if it works (we may need to add permissions for example)
- see documentation
- create a pull-request
- provide feedback on someone elses pull-request
- provide feedback after/in the task
	- Will do this in <name>-feedback.md (this isnt a typical approach but we wouldnt normally be working on the same text files much so its just for convenience)
		- improvements
		- what would make a better example
		- whats liked
		- what we could apply now


After the tasks are done and there is a pull-request we will have a meeting and merge the tasks in the meeting together as part of exploring the functionality.

The task is not about overcoming obstacles any issues just ask straight away :)

**To avoid code conflicts, change the file in the assignment and other changes add to a file **

The intention is that we will end up with documentation that would help anyone new to the project to be involved.

# Steps

*There is alot here you may wish to do each step at a different time and break it up a bit*

## This is the process of setting up a branch for your repo folder

Go to POC workspace
[POC DBX](https://adb-295718430158257.17.azuredatabricks.net/browse?o=295718430158257)
click branch tab to get here [branches tab github](https://github.com/TechnologyEnhancedLearning/DatabricksPOC/branches)
- Make a branch using your jira task name from source "main"
	- TD-<your jira task code>-Jira-Task-Name
		- (the td- means the task will automatically progress across the jira board as it moves through devOps)
	- copy the branch path
- I have created a repo folder in your user area
	- find git folder "DatabricksPOC"
	- click on the folder and change the git branch target to your new target

## Personal AI context configuration
At the top level of the workspace folder is a file called .assistant_workspace_instructions.md
My hope is that this file will be updated as a team as we develop more preferences for how AI responds in databricks. E.g. if we want it to stop recommending a package, or it needs better context for a certain type of file.

Look in your user space for a file called
.assistant_instructions.md
This is your personal AI instructions used in tandem with the global ones.

If you have preferences to how it responds put them in here.
E.g. When recommending sql to python conversions recommend me a similar file in the project I can use for comparison
Or provide context of the kind of work you will do.
Or just add a commented note to the file.

## Orientation
- create a file <name>-feedback.md
	- as you go any idea, preferences, things needing readmes more explanation, anything that helps please add in here copy paste the url to the file and just say what i could change :) thankyou
- go to the docs folder and look at the orientation readme
	- add to your notes file an improvement (it can be tiny) for the ods_ingest example
	- add to your notes file an improvement (it can be tiny) for the dlt example

## Test
*if some test dont work like data-test they may start working after you deploy your local dab later*
-skim test-readme.md
- go to run_tests
- run the whole file
- look through how the notebook is seperating the tests into sections, we could use different sections if we like
	- (Q) what is job.pytest_marks for?
- look at the end of the notebook where a fail is generated so cicd pipeline can fail after we have tried all the test
- run the tests with run_all at the top
- click on see performance in the bottom left of each code box as each finish as well as looking at the output
- look in the following files, click through to see the structure
	- tests/unit-tests/utils/test_reporter_logic.py
		- see how it test with a small df
		- the dlt is a wrapper python is the functionality that is wrapped
		- this can be compared to the previous code we saw
	- tests/unit-tests/transformations/test_date_transformations.py
		- this was added based off some real code that was simplified for the poc
			- actual code is here src/transformations/date_transforms.py
	- tests/integration-tests
		- tests/integration-tests/utils/test_loaders.py
			- this can be compared to the previous code we saw
			- its an integration test because it needs to interact with dbx for storage
			- there may be a better way but i found i had to create in the catalog a temp area for integration tests to store files
	- tests/data-quality-tests/bronze/ods/test_contact_details.py
		- look to the catalog to see whats being tested its the dlt output
		- for me that is dev_catalog philip_tate_bronze_ods contact details
		- if these tests fail for you it maybe resolved once we deploy the dab
		
## Review the assigned file
- make changes directly to the file this will give us changes to git commit
- for other comments, feedback, suggestions, add to the file you created for yourself in docs


	



## Extra bit if you like
- look at run_lint this is just a useful code check before deploying code, you can target a file with it, and its not in cicd

## Deploy personal dab
- look in databricks.yml
	- look at personal section, and then root_path workspace this is where your bundle will deployed
	- notice some pytest.marks are passed from the bundle as we may use some tests dependent on the environment
	- also notice the exclude sync for the prod environment
		- (Q) do you think these are the right things to exclude?
- go to your workspace, go to the top level, you should be able to see a rocket icon, under the folder and above the triangle square circle.
	- The source should be DatabricksPOC
	- the target change to personal (the rest are deployed by cicd)
	- hit deploy to deploy to the .bundle folder in your personal area at the top level so its outside of source control
- if you run your version of "[dev X] [personal] medallion_refresh run" you will run the two pipelines, create the tables in the catalog and the data tests should start working. (the testing job runs this same task so cicd will cause a data refresh currently so it can do the data quality checks, we may want to make this more targetted to files dataqualities checks cover, or just run the checks for specific tables we expect to be effected)
*I have seen some issue here so please have a look at what bundle resources are listed under the deploy*
	- some jobs should run on deploy
	- some pipelines should appear
- go to .bundle in your user space and look for recent files

## Commit and pull request

- click on the repo folder and the git symbol button next to the branch name to open git within databricks
- create a commit using commit naming doc from the docs folder
- click commit and push, then within the window click create pull request it appears as a link in the window
- **Really easy to forget** -> change the base drop down so your branch targets "dev-data-team-shared" not main.
- reviewers set to: X, Phil, X, X as reviewers
- assignee yourself
- labels documentation
- fillout the pullrequest md doc, switch to preview to see it
- look to the bottom for your list of commits
- there is a commits tab always worth a quick check, and files changed
- look through files changed and follow peer review guidance in pr template to comment or ask questions yourself for others to contribute to and give context. The discussion is the moment where the team gets to colaborate before something escapes to eventually prod
- click on the drop down where it says review required with a red cross, all checks passed with a green cross, merging is blocked with a red triangle. And open the all checks have passed drop down
	- doubly click on the pytest one
	- open run pytest against unit tests drop down on the right
	- you should see it logging tests have passed, these were run inside github, if you wish you can click workflow file, to see the code behind.
- Thats it, now just wait once your pull request is approved you can merge it

## Contribute to others pull requests
- give feedback in comments and in the changes tab on someoneelse pull request and once your happy approve their request (we can merge it in a meeting to see the cicd steps)






## Task checklist
[ ] Looked at .assistant_workspace_instructions.md
[ ] added an instructions to .assistant_instructions.md
[ ] asked the ai tool in databricks a question about the repo or a file in it
[ ] looked at files recommended in orientation doc
[ ] looked at test folder
[ ] ran tests
[ ] deployed personal dab
[ ] reviewed requested doc
[ ] added notes in <name>-.md
[ ] created pull request
[ ] commented on someone elses pull request




