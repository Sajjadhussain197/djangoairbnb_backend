CREATE TABLE CensusStateTerritory (
    CensusStateTerritoryID INT PRIMARY KEY,     CensusID INT,
    StateTerritoryID INT,                       Population INT,
    PopulationGrowthRate DECIMAL(5,2),          UrbanPopulationPercentage DECIMAL(5,2),
    RuralPopulationPercentage DECIMAL(5,2),     ParticipationRate DECIMAL(5,2),
    CreatedDate DATE,                           LastModifiedDate DATE,
    FOREIGN KEY (CensusID) REFERENCES Census(CensusID),
    FOREIGN KEY (StateTerritoryID) REFERENCES StateTerritory(StateTerritoryID)
);


