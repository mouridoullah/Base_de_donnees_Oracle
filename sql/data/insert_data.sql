INSERT INTO Clients (ID_Client, Nom, Adresse, Email) VALUES (1, 'Dupont', '123 Rue A', 'dupont@example.com');
INSERT INTO Produits (ID_Produit, Nom, Description, Prix, Stock) VALUES (1, 'Produit A', 'Description A', 15.50, 100);
INSERT INTO Commandes (ID_Commande, Date_Commande, ID_Client) VALUES (1, SYSDATE, 1);
INSERT INTO Details_Commande (ID_Detail, ID_Commande, ID_Produit, Quantite, Prix_Unit) VALUES (1, 1, 1, 2, 15.50);
