DROP TABLE IF EXISTS pumf_hh,pumf_person,hhtable,perstable;

DROP TEMPORARY TABLE IF EXISTS tempHH,
tempPer,
tempHH2,
tempPer2,
Numbers;

/*###################################################################################################*/
--									SETTING UP PUMF DATABASE
/*###################################################################################################*/

CREATE TABLE pumf_hh(
	HouseholdId INT NOT NULL,
	puma INT NULL,
	DwellingType INT NULL,
	NumberOfPersons SMALLINT NULL,
	Vehicles INT NULL,
	IncomeClass INT NULL,
	weight INT NULL,
	PRIMARY KEY(HouseholdId)
);


CREATE TABLE pumf_person(
	HouseholdId INT NOT NULL,
	puma INT NULL,
	PersonNumber INT NOT NULL,
	Age INT NULL,
	Sex VARCHAR(1) NULL,
	License VARCHAR(1) NULL,
	EmploymentStatus TINYINT NULL,
	Occupation TINYINT NULL,
	StudentStatus VARCHAR(1) NULL,
	EmploymentZone INT NULL,
	weight INT NULL,
	CONSTRAINT PK PRIMARY KEY(PersonNumber, HouseholdId)
);