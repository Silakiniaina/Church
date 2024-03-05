CREATE TABLE Croyant(
   id INT IDENTITY,
   nom VARCHAR(100)  NOT NULL,
   prenom VARCHAR(100)  NOT NULL,
   date_naissance DATE NOT NULL,
   email VARCHAR(50)  NOT NULL,
   mot_de_passe VARCHAR(254)  NOT NULL,
   PRIMARY KEY(id)
);

INSERT INTO Croyant(nom,prenom,date_naissance,email,mot_de_passe) VALUES 
    ('Ravelonarivo','Sanda','2005-07-12','sanda@gmail.com','admin')
;

CREATE TABLE Eglise(
   id INT IDENTITY,
   nom VARCHAR(100)  NOT NULL,
   PRIMARY KEY(id),
   UNIQUE(nom)
);

INSERT INTO Eglise(nom) VALUES 
    ('FJKM Antanambao'),
    ('FJKM Ikianja'),
    ('FJKM Ankadidambo')
;

CREATE TABLE Offrande(
   id INT IDENTITY,
   montant DECIMAL(18,2)   NOT NULL,
   numero_dimance SMALLINT NOT NULL,
   annee BIGINT NOT NULL,
   nombre INT NOT NULL,
   id_eglise INT,
   PRIMARY KEY(id),
   FOREIGN KEY(id_eglise) REFERENCES Eglise(id)
);

INSERT INTO Offrande(montant,numero_dimance,annee,nombre,id_eglise) VALUES
    (12000,1,2022,123,1),
    (13450,1,2022,123,2),
    (13450,1,2022,123,3),
    (45677,2,2022,523,1),
    (23456,2,2022,234,2),
    (52000,2,2022,445,3)
;