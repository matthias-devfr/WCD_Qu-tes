# **==Découpage symétrique :==**  
  
### 1. **Besoins en équipements :** 

- **Pôle Informatique** : 50 équipements
- **Pôle Développement** : 12 équipements
- **Pôle Administratif** : 20 équipements
- **Pôle Technicien** : 15 équipements

Le pôle ayant le plus grand besoin est le **Pôle Informatique** avec **50 équipements**.

### 2. **Calcul du sous-réseau :** 

**Calcul de la puissance de 2 :**
- \( 2^6 = 64 \) *(chaque sous-réseau aura donc (64-2=) 62 IP disponibles, suffisant pour 50 équipements)*

**Calcul du CIDR :**
- \( 32 - 6 = 26 \) → Le CIDR est donc **/26**.

### **3. Création des sous-réseaux :**

 #### 1. Pôle Informatique
- **Adresse réseau** : 172.16.1.0/26
- **Adresse de diffusion (Broadcast)** : 172.16.1.63

 #### 2. Pôle Développement
- **Adresse réseau** : 172.16.1.64/26
- **Adresse de diffusion (Broadcast)** : 172.16.1.127

#### 3. Pôle Administratif
- **Adresse réseau** : 172.16.1.128/26
- **Adresse de diffusion (Broadcast)** : 172.16.1.191

#### 4. Pôle Technicien
- **Adresse réseau** : 172.16.1.192/26
- **Adresse de diffusion (Broadcast)** : 172.16.1.255

## **==Découpage asymétrique :==**

### Déterminer le CIDR de chaque sous-réseau

1. **Pôle Informatique** :
    - Besoin : 50 équipements
    - Puissance de 2 suffisante : \( 2^6 = 64 \)
    - CIDR : \( 32 - 6 = 26 \)
  
2. **Pôle Administratif** :
    - Besoin : 20 équipements
    - Puissance de 2 suffisante : \( 2^5 = 32 \)
    - CIDR : \( 32 - 5 = 27 \)

3. **Pôle Technicien** :
    - Besoin : 15 équipements
    - Puissance de 2 suffisante : \( 2^4 = 16 \)
    - CIDR : \( 32 - 4 = 28 \)

4. **Pôle Développement** :
    - Besoin : 12 équipements
    - Puissance de 2 suffisante : \( 2^4 = 16 \)
    - CIDR : \( 32 - 4 = 28 \)

## Découpage en sous-réseaux
### 1. Pôle Informatique /26

- **Adresse réseau** : 172.16.1.0/26
- **Adresse de diffusion (Broadcast)** : 172.16.1.63

### 2. Pôle Administratif /27

- **Adresse réseau** : 172.16.1.64/27
- **Adresse de diffusion (Broadcast)** : 172.16.1.95

### 3. Pôle Technicien /28

- **Adresse réseau** : 172.16.1.96/28
- **Adresse de diffusion (Broadcast)** : 172.16.1.111

### 4. Pôle Développement /28

- **Adresse réseau** : 172.16.1.112/28
- **Adresse de diffusion (Broadcast)** : 172.16.1.127
