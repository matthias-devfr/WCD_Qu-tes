1. Créer le dossier à la racine en exécutant la commande suivante dans PowerShell :
   ```
   New-item -path C:\ -name Documents_Entreprise -itemtype Directory
   ```

2. Ensuite, dans PowerShell, exécutez les commandes suivantes pour créer les sous-dossiers :
   - Créer le dossier RH :
     ```
     new-item -path C:\Documents_Entreprise -name RH -itemtype Directory
     ```
   - Créer le dossier Direction :
     ```
     new-item -path C:\Documents_Entreprise -name Direction -itemtype Directory
     ```
   - Créer le dossier Comptabilité :
     ```
     new-item -path C:\Documents_Entreprise -name Comptabilité -itemtype Directory
     ```

3. Pour créer les groupes dans Active Directory, exécutez les commandes suivantes :
   ```
   Get-ADgroup -identity "Direction"
   Get-ADgroup -identity "Comptabilité"
   Get-ADgroup -identity "RH"
   ```

4. Ouvrez le gestionnaire de serveur, puis cliquez sur **"Services de fichiers et de stockage"** > **"Partages"**.

5. Cliquez droit sur **Nouveau partage** > **Partage SMB-Rapide** > choisissez le dossier **Documents_Entreprise** > **Nommer le partage** `Docs`. Ensuite, configurez les permissions NTFS comme suit :
   - Ajoutez le groupe **Direction** et cochez **Lecture et écriture**.
   - Ajoutez le groupe **Comptabilité** et cochez **Lecture et écriture**.
   - Ajoutez le groupe **RH** et cochez **Lecture et écriture**.

6. Pour chaque dossier (RH, Direction, Comptabilité), faites un clic droit, puis sélectionnez **Propriétés**. Ensuite, dans l'onglet **Partage**, sélectionnez **Partage** et ajoutez le groupe correspondant au dossier en vérifiant bien que **Lecture et écriture** soient uniquement cochés.
```
