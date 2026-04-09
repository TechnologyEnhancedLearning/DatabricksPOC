# Not covered in POC



# Not done
- This document has excellent coverage and should be used to plan next steps and best practice examples [Dataquality](https://www.databricks.com/discover/pages/data-quality-management)
- read https://blogs.perficient.com/2025/03/19/delta-live-tables-and-great-expectations/
- environment branch rules stop pr directing against staging and prod make only correct branches mergeable (can always turn rule off in emergency)
- ~~version numbering~~ we can do release versioning manually makes more sense for us but it is not vital
- ~~enable copilot auto pr~~

# Team input in future
- black linting

# Should do!
- take names out of poc
- change from service principle PATs -> Research OAuth M2M via ENTRAID
- had a fail on the manual dev staging prod validation only in dev and staging seems something has expired so is there a connector or better option than expiring PAT
- **IMP** seperated tests requiring rerunning pipelines from those that dont (data quality, sql sp)
  - different job per test type and different notebook
- email addresses
- per environment with pipeline triggered emails so know whether an issue occured before or after and environment update
  - dab default email addresses
  - config in the workspace level outside of git
    - this may be how we should manage the config
    - J suggests https://www.databricks.com/discover/pages/access-control
  - notes
    - Bundle_Var_api_key in this fle
    - use secret or outside of git variables for emails and then set in github env secret like service principles alert_emails: 
    - BUNDLE_VAR_staging_alert_emails_  
- ~~seperating dabs~~ dont see the advantage, team may have reason for why its desired
  - can do bronze, silver, gold etc
  - means modular deployment
  - cicd would need to detect changes in folders in order to know which dab to deploy
  - wheels again may be needed for code between dabs but maybe not
  - cluster dealing with smaller sizes
- requirements.txt and requirements-dev.txt need sorting, individual installs need removing
- provide specific presets in addition to development prod mode for clarity
  - name_prefix:staging_ and trigger_pause_status:paused **hmm potentially better**
    - notebook_params ... so could preset environment
    - could set timout for safety
    - could set tags
    - email notifications
    - for clarity mode:production
    - i think mode:development
      - prepend [dev ${workspace.current_user.short_name}]
      - pause schedual triggers
      - pipelines marked as development
      - concurrent runs defaulted
      - disable deploment locks
- fix tests so tests requiring continuous pipeline no longer used in staging and prod

