# Would like
- dab version numbered
- main git branch release versioned
- change logs between releases

# Recommended against
- its not like packages i dont think need bundle versions like dev-1.2.3
- no commit lint and tight rules its one change too many (git guidance instead)
  - this means no automated tagging so need manual process

# Importance
- do we think we will use it enough
- anything particulary important analytics wise
- may be a little more relevant is versioning wheels. It may be useful in future
  - i think you install wheel to the cluster, then you dont need to navigate the relative folder structure, there may also be clever things built in that keep the wheel up to date so dont need to rebuild
- i dont think we will need to roll back or if did would deploy git again, rolling back is messy anyway
- we can find a way to tag bundles to match release tag, but i dont think we will lose site of this in current team size and with an automatically deployed process will know whats been deployed.

# Potential Advice
- Review this unless there are other considerations then maybe for now dont worry about versioning
- consider manual tagging after prod merge, or release, and tag, though release just means zips we dont need you can generate commits and add notes
