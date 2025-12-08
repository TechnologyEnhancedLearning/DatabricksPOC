-- ============================================================================
-- ONE-TIME SETUP: Create catalogs and schemas
-- ============================================================================
-- Run this in Databricks SQL Editor when setting up a new environment
--
-- POC Setup (current):
--   - Creates 3 separate catalogs in single Databricks instance
--   - our_catalog: Dev work with personal schemas per developer
--   - staging_catalog: Staging with shared schema
--   - prod_catalog: Production with shared schema
--
-- Production Setup (future with 3 Databricks instances):
--   - Create same catalog name on each instance
--   - Separation by different hosts, not catalog names
-- ============================================================================


-- qqqq Careful this applied it to all databricks
-- there is this
-- ISOLATION MODE ISOLATED    -- this line is the magic
  -- COMMENT 'POC-only – never visible outside this workspace';

-- Create catalogs using managed storage (Databricks handles storage automatically)
CREATE CATALOG IF NOT EXISTS our_catalog 
MANAGED LOCATION 'abfss://unity-catalog-storage@dbstoragenxhpv6mlq64wq.dfs.core.windows.net/295718430158257/our_catalog'
COMMENT 'Dev environment - personal schemas per developer';

CREATE CATALOG IF NOT EXISTS staging_catalog 
MANAGED LOCATION 'abfss://unity-catalog-storage@dbstoragenxhpv6mlq64wq.dfs.core.windows.net/295718430158257/staging_catalog'
COMMENT 'Staging environment - integration testing';

CREATE CATALOG IF NOT EXISTS prod_catalog 
MANAGED LOCATION 'abfss://unity-catalog-storage@dbstoragenxhpv6mlq64wq.dfs.core.windows.net/295718430158257/prod_catalog'
COMMENT 'Production environment - live data';

-- Create shared schemas for staging and prod
-- Dev schemas are created automatically per-user by the bundle deployment
-- (via schema: ${workspace.current_user.short_name} in databricks.yml)
CREATE SCHEMA IF NOT EXISTS staging_catalog.our_schema;
CREATE SCHEMA IF NOT EXISTS prod_catalog.our_schema;