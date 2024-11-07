CREATE OR REPLACE PROCEDURE GetClientOrders (p_client_id IN NUMBER) IS
BEGIN
    FOR order_rec IN (SELECT * FROM Commandes WHERE ID_Client = p_client_id) LOOP
        DBMS_OUTPUT.PUT_LINE('Commande ID: ' || order_rec.ID_Commande || ', Date: ' || order_rec.Date_Commande);
    END LOOP;
END;
