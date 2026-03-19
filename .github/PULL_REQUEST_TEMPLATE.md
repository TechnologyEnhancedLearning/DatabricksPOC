Go to bottom for pull request template to complete

# Peer Review Guidance

## Who
- everyone should get to be reviewed
- everyone should get to review others
- hierachyless
- questions and answers equally useful, answering a question helps you concrete own understanding too through having to articulate it

## What it should be
- Collaborative :) :)
- Opportunity to discuss interesting approaches
- Share knowledge generally
- Share knowledge specifically
  - this is the opportunity to see new functions that may be used in future tasks to save work
  - there may be an easier way of solving a specific problem
- Celebrate work
- Be supportive
- Be seen
- An excuse for a call and a cup of tea
- If there is nothing to suggest you havent failed at doing a review, you dont have to find something, its just good work, so share that, or a picture of your cat
- A gate, work needs to be interacted with, by a few ppl before going out, we are looking for done not perfect, suggestions and discussion will often result in things useful for next time and learning rather than a change. Sometimes work is needed but it is an additional task, or at this point it maybe even a refactor task for example bring two bits of work in line where they can now share logic. However, sometimes too you will agree to do an extra commit because a change is low effort high value, or required. (Be careful of tasks growing from being atomic at this point in the process.)
- It can be nice practice for reviewers to tell the person who did the work they can now merge, its their work afterall. Some prefer people to just merge it for them.

## What it shoudnt be
- Unless requested linting is better done by AI or linters, no one likes their spelling, grammar etc picked up unless its requested
- Aiming for perfection
- an assessment

Ofter PR becomes a waving-through excerise in teams because
- its uncomfortable to make comments
- the context isnt enough to understand the work
- the task was too big to review easily
- or peer reviewers see it as not their work but an extra
And if this happens teams dont get the benefit of others practice, knowledge of areas theyve not written themselves, appreciation from someone who understands the work, and a natural slow unification/standardisation of approaches. So its important to make it an enjoyable priority.

## refs
[first google but its ok its tips on good peer reviews](https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/)

[How to refactor](https://nhsdigital.github.io/rap-community-of-practice/training_resources/coding_tips/refactoring-guide/)

---

# Pull Request Guidance
- You can open pull requests as drafts if you like

## Good things to do before a pull request 
These are not expectations, as the process become more practiced we will learn what should happen most times and what shouldnt. It is a way of having a joint concept of "good". And as a joint concept this doc should be changed overtime. (If it isnt then it will be because it failed).

### Sanity Checks
These ar not show stoppers just good to check
- checked commit names (some ppl like to squash commits to tidy them up but most dont)
  - commit per thing done
  - commit naming convention followed
- branch correctly named
- searched for any personal codes you use to leave notes for yourself when developing e.g. "zzzz" to help you tidy up
- If big table creation or change has Analyze Table been included to improve cost/efficiency. (for pipelines not exploratory notebooks etc)


### Contribute to code quality and the future
- lint (Run_lint targeted files and make improvements)
- tests (Run tests in dbx, write test)
- refactor (Can code be made more reuseable, testable)
- reuseable (Could you reuse existing code or refactor it to be reuseable)

### Contribute to tooling
- AI (add to dbx global, your dbx user name area, or github, context instruction md e.g preference in responses, recommendation it should or shouldnt make or providing context for files it doesnt understand)
- Turned exploratory code you have ran into labeled notebooks to share so others can easily run the same explorations
- Turned exploratory code you have ran into manual tests other developers can run

### Contribute to knowledge
- comments in code
- comments in jira task
- documentation in project
- discussion in pr

### Contribute to planning
- if this task highlighted a need for any task to be created please make these recommendations or open discussions

---

# Pull Request Form (Please Complete)
*based on https://github.com/TechnologyEnhancedLearning/LearningHub.Nhs.WebUI/blob/master/.github/pull_request_template.md?plain=1*



## JIRA link
Change this to the jira link to help your reviewers
[TD-####](https://hee-tis.atlassian.net/browse/TD-####)

## Description
_Describe what has changed and how that will affect the app. If relevant, add links to any sources/documentation you used. Highlight anything unusual and give people context around particular decisions._

## Screenshots
_Paste Screen Shots Here (This can be useful sometimes but is more useful for WebUI its totally optional.)_

## Checklists

### Checklist for the Author

This check list is to help you and your peer reviewers have a shared context.

It is not an expectation that everything will be ticked or even most, but a useful prompt if for example a review thinks unit-tests would of been useful, which is a comment that would be in the main comments rather than a comment on the file changes tab.

Peer reviewers should not fail based on this list, it is agile, we are looking for done.
Recommendation may be for future practice, for future refactor tasks, or just good to know. Some may be to refactor somework as part of this ticket. For example maybe a function already existed that does what your doing and there is low effort high benefit to using it instead. Then you would discus, agree to do another commit, make the changes and push.

*Put xs in them so they appear ticked in preview [x]*
- [ ] Checked files changed are the right ones, and they are changing the right things
- [ ] Checked the code by running tests or exploratory code
- [ ] Created Unit Tests
- [ ] Created Integration Tests
- [ ] Created Data Quality Tests
- [ ] Run tests in databricks in my user area
- [ ] Used Spark Expect
- [ ] Update my Jira ticket with useful context notes for testers
- [ ] Documented Work
- [ ] Recommended Jira tickets to the relevant person from needs emerging from this work
- [ ] Thanked testers and reviewers :)


### Checklist for Peer Reviewer(s) 
*there may be many peer reviewers but this is to ensure at least one person has ticked the boxes*
- [ ] Considered if additional tests needed
- [ ] Commented on individual files
- [ ] Commented in general PR
- [ ] Asked curious questions/offered alternative approaches
- [ ] Given praise (if its going to merge its worth praise)
- [ ] Offered to document or request tasks for any areas identified in discussions from the work
- [ ] Agreed additional commits/Approved and let author know
- [ ] Added any additional insight to the jira ticket for the testers

---

# After Merging to an Environment Branch
**If you are managing environment, you should always be a required peer reviewer for branches into dev, staging, prod**
Having approved the feature branch owner to merge, or merging the branch as part of approval it is vital to then check the environments and the gitaction pipeline.

## Checks for all environments
[Check git deployment action for that environment succeeded](https://github.com/TechnologyEnhancedLearning/DatabricksPOC/actions)
- Check the environment deployed to
- Check jobs and pipelines they should all pass though occasionally fails can happen that only require restart, unless expected they rarely should run more than a minute or two
  - remember to check all pages
- Check dashboards for usage, and recheck after an hour or day, for any unexpected behaviours such as step changes


## Dev
- Doesnt have continuous processes (see databricks.yml setup differences)

### Dev Checks
- qqqq dashboard needs creating
- [ ] [Dev dashboard](https://adb-3560006266579683.3.azuredatabricks.net/sql/dashboardsv3/01f11c8a7b89118788f1391e0e6afe7f/pages/19beeac3?o=3560006266579683)
- [ ] [Dev pipelines and jobs](https://adb-295718430158257.17.azuredatabricks.net/jobs?o=295718430158257)
- [ ] [Git actions](https://github.com/TechnologyEnhancedLearning/DatabricksPOC/actions)
- [ ] Checked Dev email address post deployment (qqqq would be good if deployment emailed the address so has a before and after)

## Staging
- Does have continuous processes (see databricks.yml setup differences)

### Staging Check
- qqqq dashboard needs creating
- [ ] [Staging dashboard](https://adb-3642283292081870.10.azuredatabricks.net/sql/dashboardsv3/01f11c8a699f1cfd981cc67dd50ab74f/pages/b36dd0e6?o=3642283292081870)
- [ ] [staging pipelines and jobs](https://adb-3642283292081870.10.azuredatabricks.net/jobs?o=3642283292081870)
- [ ] [Git actions](https://github.com/TechnologyEnhancedLearning/DatabricksPOC/actions)
- [ ] Checked Staging email address post deployment (qqqq would be good if deployment emailed the address so has a before and after)

## Prod
- Prod doesnt run test
- Does have continuous processes (see databricks.yml setup differences)
### Prod Checks
- qqqq dashboard needs creating
- [ ] [Prod dashboard](https://adb-7405617206100704.4.azuredatabricks.net/sql/dashboardsv3/01f12394d70414b8935a1d8390041e0f?o=7405617206100704)
- [ ] [Prod pipelines and jobs](https://adb-7405617206100704.4.azuredatabricks.net/jobs?o=7405617206100704)
- [ ] [Git actions](https://github.com/TechnologyEnhancedLearning/DatabricksPOC/actions)
- [ ] Checked Prod email address post deployment (qqqq would be good if deployment emailed the address so has a before and after)


