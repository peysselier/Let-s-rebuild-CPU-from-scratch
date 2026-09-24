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

#### ADI

- Permet d'ajouter une valeur à un registre du `Reg File`
- Syntaxe : ADI Ri A

- `Ri` : registre écrit  
- `A` : nombre en décimal

---

#### INC

- Permet de retrancher 1 à un registre
- Syntaxe : INC Ri

---

#### DEC

- Permet d'ajouter 1 à un registre
- Syntaxe : DEC Ri

---

### Opérations CODE

#### LDI

- Permet de mettre une valeur dans un registre du `Reg File`
- Syntaxe : LDI Ri A

- `Ri` : registre écrit  
- `A` : nombre en décimal

---

#### RSH

- fait un decalage à gauche bit à bit de la valeur du registre
- Syntaxe : RSH Ri

**Exemple**

`RSH R1`

Si R1 = 00100100, au coup de clock suivant, R1 = 01001000

