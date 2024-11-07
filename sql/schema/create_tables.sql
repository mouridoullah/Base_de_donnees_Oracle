CREATE TABLE Clients (
    ID_Client NUMBER PRIMARY KEY,
    Nom VARCHAR2(100) NOT NULL,
    Adresse VARCHAR2(255),
    Email VARCHAR2(100) UNIQUE
);

CREATE TABLE Produits (
    ID_Produit NUMBER PRIMARY KEY,
    Nom VARCHAR2(100) NOT NULL,
    Description VARCHAR2(255),
    Prix NUMBER(10, 2) NOT NULL,
    Stock NUMBER DEFAULT 0
);

CREATE TABLE Commandes (
    ID_Commande NUMBER PRIMARY KEY,
    Date_Commande DATE DEFAULT SYSDATE,
    ID_Client NUMBER,
    FOREIGN KEY (ID_Client) REFERENCES Clients(ID_Client)
);

CREATE TABLE Details_Commande (
    ID_Detail NUMBER PRIMARY KEY,
    ID_Commande NUMBER,
    ID_Produit NUMBER,
    Quantite NUMBER NOT NULL,
    Prix_Unit NUMBER(10, 2) NOT NULL,
    FOREIGN KEY (ID_Commande) REFERENCES Commandes(ID_Commande),
    FOREIGN KEY (ID_Produit) REFERENCES Produits(ID_Produit)
);
