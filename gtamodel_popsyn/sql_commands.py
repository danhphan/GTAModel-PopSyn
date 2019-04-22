TRANSFORM_PERSONS_TABLE_SQL_COMMANDS = [
    """
    DROP TABLE IF EXISTS GTA_PERSONS
    """,
    """CREATE TABLE GTA_PERSONS(HouseholdId INT(11),
        PersonNumber INT(11),
        Age smallint,
        Sex VARCHAR(1),
        License VARCHAR(1),
        TransitPass VARCHAR(1) DEFAULT '0',
        EmploymentStatus VARCHAR(1),
        Occupation VARCHAR(1),
        FreeParking VARCHAR(1) DEFAULT '0',
        StudentStatus VARCHAR(1),
        EmploymentZone smallint DEFAULT 0,
        SchoolZone smallint DEFAULT  0,
        ExpansionFactor smallint )
        as SELECT tempId as HouseholdId, PersonNumber, Age, Sex, License, '0' as TransitPass,
                  EmploymentStatus, Occupation, StudentStatus, '0' as FreeParking,  EmploymentZone,
                  '0' as SchoolZone, finalweight as ExpansionFactor
        from synpop_person order by tempId asc
    """
]

TRANSFORM_HOUSEHOLDS_TABLE_SQL_COMMANDS = [
    """
    drop table if exists GTA_HOUSEHOLDS
    """,
    """
    CREATE TABLE GTA_HOUSEHOLDS(
    HouseholdId INT(11),
    HouseholdZone SMALLINT,
    ExpansionFactor SMALLINT,
    NumberOfPersons TINYINT,
    DwellingType TINYINT,
    Vehicles TINYINT,
    IncomeClass TINYINT) 
    AS SELECT tempId as HouseholdId, maz as HouseholdZone, finalweight as ExpansionFactor, 
    DwellingType,NumberOfPersons,Vehicles,IncomeClass from synpop_hh
    order by tempId asc
    """
]

TRANSFORM_HOUSEHOLD_TOTALS_SQL_COMMANDS = [
    """
    drop table if exists gta_household_totals
    """,
    """
    CREATE TABLE gta_household_totals(
        Zone SMALLINT NOT NULL DEFAULT 0,
        ExpandedHouseholds INT NOT NULL DEFAULT 0
    )
    AS (SELECT  HouseholdZone as Zone, SUM(ExpansionFactor) as ExpandedHouseholds from GTA_HOUSEHOLDS 
    group by HouseholdZone)
    """
]