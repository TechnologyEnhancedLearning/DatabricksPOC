# External Storage Notes for POC

## Architecture DevOPs

[Original reference these notes support](https://youtu.be/VkjqViooMtQ)
The ideal is 
- one storage account per environment
- an additional storage account if we want shared, readonly, additive only no schema changes, catalogue all environments use as a raw source, we are likely not after this hub and spoke approach atm, and duplicating per environment means data impacts of prod will have been seen first in dev and staging
- databricks connector per storage account with permissions to the storage account
- one credential per connector
- workspaces only see their own catalogue and storage
- *Not sure if should have separate resource groups for staging and dev the seperation may not be worth it, but it would mean it dev staging prod will mirror each other better*
- catalogue
	- weak recommendation of external storage going into its own catalogue with appropriate name e.g. Prod_External_Readonly, Staging_External_Readonly, Dev_External_Readonly, but currently there is a prefferance to have it in the main catalogue.
	- IF using hub and spoke and sharing a storage source strong recommendation that is its own catalogue and very clearly marked as will be visible in all workspaces
- Data recommendations
	- Managed Data (data brought into databricks) > than external tables
	- RAP automated process > manual snapshots			
	- the workspaces should be mirrors of each other, so when something is different between them the question is never is it the setup or the code
- Where possible the storage and catalogue should mirror, so schema might be the name of the container, and its folders may be the tables for example

## Implementation
- databricks connector per storage account
	- permissions on local storage (and resource group for events, if its a storage supporting events)
		- EventGrid EventSubscription Contributor
		- EventGrid EventSubscription Contributor - Resource group (Inherited)
		- Storage Account Contributor
		- Storage Blob Data Contributor
		- Storage Queue Data Contributor
- Set up cred,  and external locations in the UI
	- Catalog > + > 
		- Credentials
			- will need permissions
			- this time will limit workspace to its workspace
		- External Locations sources
			- previously didnt give it permissions
			- browse should show the contents
- have set up the external location how it is consumed depends on what it is and best fit (less confident in this information so there may be a better approach)
	- we want it to become managed so we want to move the data in databricks not access it as an external table which is slower
		- autoloader for regular changing and best practice, if has queue on storage can make this more efficient
		- effectively importing it as a snapshot table
			- then using daily streaming if data is addatitive only
			- using a job to reimport
		
## Lessons
- We should not try and expose external storage in multiple workspaces it should have a single source of truth
	- this mean storage per environment
	- or a shared hub storage
- we did have a UI error redherring in seeing external storage but were able to access the storage in catalogue

## Notes from documentation
- There is reference of not connecting per container/folder to a table but going for the higher level so not repetitive and inviting mistakes
	

## Context notes
- office national statistic postcode directory onspd
	- expect to be schema breaking
- we dont have much in the way of static data sets
- ESR gives us 2 month old deltas (trud xml)
- ODS will be available via API in future
- table with a cloud is an external table we want to avoid this
- lightning bolt table is a streaming table the ideal is event triggered over cron jobs, but cron jobs fine
- **star schema** : one table that refernce all the other for joins like the centre of the stars

## Errors
- Error loading files.
Catalog 'databricks_tel_dev_uks' is not accessible in current workspace
This was actually because we wanted to the external storage not the databricks storage in the external location UI potentially, various approaches were tried to give permissions but that wasnt the issue.


## Refs our examples

- example works:
	- Databricks-PoC 
	- DatabricksPoCAccessConnector
	- unifiedrptdeltalake storageV2 working example

- example works:
	- databricks-tel-test-uks
	- teldeltalakedevtest
	- teldeltalakedevtest-connector

## Refs reading

- https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/deployment-guide/unity-catalog
	- Each metastore stores metadata for securable objects (for example, tables, views, volumes, external locations, shares) and the permissions that govern access to them.
		- when shared when not?
			- volumes
			- exernal locations
			- shares
			- can share storage accounts ...
	- region to region sharing again says dont duplicate
	- Use catalogs within a metastore to separate data by environment or domain. - yep
	- raw catalogue ... could be acceptable
	- recommends 3-10 catalogues per meta store ... we'd have 4
	- "Reading data from cloud storage that is not managed by Unity Catalog."
	- > Azure storage credentials use Azure Azure Databricks Access Connectors, which are managed identity resources. The Access Connector must be granted appropriate permissions on storage accounts using Azure RBAC (for example, Storage Blob Data Contributor role). - yep
	- "Use separate Access Connectors for different storage accounts or data domains (for example, uc-prod-sales-connector, uc-dev-engineering-connector)."
		- this aligns with my recommendation for ata we change
	- credential advice
		- **Limit network access using storage firewalls and private endpoints.**
		- **Enable Azure Monitor to audit access to storage accounts.**
	- Use external locations that align with catalog or schema boundaries (for example, one external location per catalog).
	- Use Unity Catalog managed tables instead of external locations when possible (simpler governance and optimization).
		- **does this mean we should plan to replace external with ingestion** - yes
	- Grant access to external locations only to users who need to create external tables.
- [hubpoke](https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/deployment-guide/unity-catalog#hub-and-spoke-design-pattern)
	- Avoid store prod date on dbfs databricks file system - i think we are doing this due to this issue currently
	- External location design patterns
		- Create external locations at the highest common path prefix to minimize the number of locations.
		- **So we should not do /ods, we should do storage account not schema**
	- i like this hub spoke but seems not relevant to our context and the worry would be data changing on prod before the change has happened in dev environments where if its problamatic we can catch it
- https://learn.microsoft.com/en-us/azure/databricks/data-governance/unity-catalog/best-practices#managed-and-external-tables
	- For most use cases. Databricks recommends managed tables and volumes because they allow you to take full advantage of Unity Catalog governance capabilities and performance optimizations, including:
		- Auto compaction
		- Auto optimize
		- Faster metadata reads (metadata caching)
		- Intelligent file size optimizations
	- **Databricks recommends that you eventually migrate external tables to managed tables.**
	- external You must support non-Delta or non-Iceberg tables, such as Parquet, Avro, ORC, and so forth.
	- **Databricks recommends that you create external tables using one external location per schema.**
		- before wasnt the recommendation per environment?
	- **use autoloader** to ingest external storage instead of exposing it as tables in dbx is prefered	
		- this may be more correct 
		- does it continuously change
- https://learn.microsoft.com/en-us/azure/databricks/lakehouse-architecture/
- https://learn.microsoft.com/en-us/azure/databricks/tables/delta-table#managed-tables
- https://learn.microsoft.com/en-us/azure/databricks/tables/delta-table#other-table-types
- for specific scenarios
	- streaming, materialised view
- https://learn.microsoft.com/en-us/azure/databricks/ldp/streaming-tables
	- Streaming tables are designed for append-only data sources and process inputs only once
	- **rather than using the UI we should use code so its git controlled for RAP reproduceable **
	> from pyspark import pipelines as dp
	```
	# Create a streaming table
	@dp.table
	def customers_bronze():
	  return (
		spark.readStream.format("cloudFiles")
		 .option("cloudFiles.format", "json")
		 .option("cloudFiles.inferColumnTypes", "true")
		 .load("/Volumes/path/to/files")
	  )
	```  