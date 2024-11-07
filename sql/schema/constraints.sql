ALTER TABLE Clients ADD CONSTRAINT chk_email CHECK (Email LIKE '%_@__%.__%');
ALTER TABLE Produits ADD CONSTRAINT chk_stock CHECK (Stock >= 0);
