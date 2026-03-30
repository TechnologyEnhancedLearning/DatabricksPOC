# Notes on what we want from GitHub Copilot, and databricks assistant

Context files for AI can be found at:

Team wide AI assistant instructions:
/Workspace/ a file called assistant_workspace_instructions.md

Your personal AI assistant instruction additions:
Workspace/users/yourusername a file called .assistant_instructions.md

Github Copilot context: /Workspace/Users/username/Branch/.github/copilot-instructions.md

Github agents can be made here if desired  Workspace/Users/username/.assistant

*If using both github copilot context and assistant_workspace_instructions it will be desireable to update both at the same time when changes are made*

# ⚠️WARNING⚠️
- Databricks AI has a low limit for requests so: 
   - write a detailed prompt to scaffold work
   - write a detailed prompt to review when done
   - write in sql and use to translate to python when learning python
   - use other external AI for questions not requiring access to files or our specific prebuilt prompts
   - prebuilt prompts can be used in external AI aswell
- Git copilot can be used manually but not as an automatic PR tool **yet** without paying for it (though it is planned to be free)
   
# Using github copilot in the short term  
   - for now can try [github copilot client](https://github.com/copilot) and select the repo. and use a prompt like
      > "Please confirm the name of the most recent pull request on this repo. Then using the .github/copilot-instructions.md as your context prompt provide a peer review of the pull requests code changes, by providing file names and lines."
   - on a second screen you may want to go to the pull request and click the file changes tab
   - if the bot needs help understanding describing certain files please consider helping it by adding this to the context file for future, so we can constantly improve its context

# Tips
- Do few high quality detailed prompts
- forward slash offers some prebuilt context options to select
- using inline ai button will focus on work in your window
- using it from the side bar means you can get it to find for example the closest example of what your trying to do in the project for reference
- tell it what you want it to consider, what you want to achieve, how you want it to help, the type of response you want, what your priorities are

# refs
[copilot in git code review](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/request-a-code-review/use-code-review)
[github custom context repo prompt generator](https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions)



