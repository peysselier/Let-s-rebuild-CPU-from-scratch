# Mini CPU

64 registres de code

15 registres CPU

## Liste des opérations

- **ALU** : ADD, SUB, NOR, AND, XOR, RSH
- **CODE** : LDI,   

---

## Syntaxes

### Opérations d'ALU

- `Ri` : registre de destination (écrit)
- `Rj` et `Rk` : registres opérés

**Exemple avec SUB :**

`SUB Rj Rk Ri`

Dans `Ri`, on calcule `Rj - Rk`

---

### Opérations CODE

#### LDI

- Permet de mettre une valeur dans un registre du `Reg File`
- Syntaxe : LDI Ri A

- `Ri` : registre écrit  
- `A` : nombre en décimal
