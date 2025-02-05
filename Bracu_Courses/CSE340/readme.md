# CSE340:Computer Architecture

## Instructions: Language of the Computer



# [Practice Sheet](https://drive.google.com/drive/folders/1Vwk38CAlTkYjeZOFPMOMysnywpjD5QEd?usp=sharing)


# [Chapter 2](https://drive.google.com/drive/folders/1LZ2LcOuytkrOahjs3svDUF8xCjFJjmCu)
# [Chapter 3](https://drive.google.com/drive/u/0/folders/1YFkAhUtoHeVPX8sxzf-kgV9qHl9IBtcS)
# [Chapter 4](https://drive.google.com/drive/u/0/folders/1gdk4JfoV2sS0cvhZZDoD_BhhG1D7qppj)
# [Quiz](https://drive.google.com/drive/folders/1xtsBW011Jdyjz2f-wpqGAOmTscuU3pHl)


### Assembly Language 

#### **Arithmetic Operations**
1. **ADD (Add)**:  
   - Syntax: `add rd, rs1, rs2`  
   - Adds contents of `rs1` and `rs2`, stores result in `rd`.  
   - Example: `add x5, x1, x2` → `x5 = x1 + x2`.

2. **SUB (Subtract)**:  
   - Syntax: `sub rd, rs1, rs2`  
   - Subtracts `rs2` from `rs1`, stores result in `rd`.  
   - Example: `sub x5, x1, x2` → `x5 = x1 - x2`.

3. **ADDI (Add Immediate)**:  
   - Syntax: `addi rd, rs1, imm`  
   - Adds immediate value (`imm`) to `rs1`, stores result in `rd`.  
   - Example: `addi x5, x1, 10` → `x5 = x1 + 10`.



#### **Decision-Making Instructions**
1. **BEQ (Branch if Equal)**:  
   - Syntax: `beq rs1, rs2, label`  
   - Branches to `label` if `rs1 == rs2`.  

2. **BNE (Branch if Not Equal)**:  
   - Syntax: `bne rs1, rs2, label`  
   - Branches to `label` if `rs1 != rs2`.

3. **BLT (Branch if Less Than)**:  
   - Syntax: `blt rs1, rs2, label`  
   - Branches to `label` if `rs1 < rs2`.

4. **BGT (Branch if Greater Than)**:  
   - Syntax: `bgt rs1, rs2, label`  
   - Branches to `label` if `rs1 > rs2`.



#### **Bitwise and Shift Operations**
1. **SRLI (Shift Right Logical Immediate)**:  
   - Syntax: `srli rd, rs1, shamt`  
   - Shifts `rs1` right logically by `shamt` bits, stores result in `rd`.  
   - Example: `srli x5, x1, 2` → `x5 = x1 >> 2`.



#### **Load and Store Instructions**
1. **LUI (Load Upper Immediate)**:  
   - Syntax: `lui rd, imm`  
   - Loads immediate value into the upper 20 bits of `rd`, lower bits set to 0.  
   - Example: `lui x5, 0x12345` → `x5 = 0x12345000`.

2. **SB (Store Byte)**:  
   - Syntax: `sb rs2, offset(rs1)`  
   - Stores the least significant byte of `rs2` into memory at address `rs1 + offset`.  
   - Example: `sb x5, 0(x1)` → Stores `x5`’s byte into address at `x1`.

#### **Instruction Overview**
1. **OR (Bitwise OR)**  
   - Combines bits of two registers, bit-by-bit using OR logic.  
   - Syntax: `or rd, rs1, rs2`

2. **XOR (Bitwise XOR)**  
   - Combines bits of two registers, bit-by-bit using XOR logic.  
   - Syntax: `xor rd, rs1, rs2`

3. **AND (Bitwise AND)**  
   - Combines bits of two registers, bit-by-bit using AND logic.  
   - Syntax: `and rd, rs1, rs2`



### **Encoding and Structure**
These instructions use the **R-Type structure**:  
```
funct7 | rs2 | rs1 | funct3 | rd | opcode
```

- **opcode**: Common for all R-Type instructions (`0110011`).  
- **funct3**: Determines the specific operation:
  - `OR`: `110`
  - `XOR`: `100`
  - `AND`: `111`  
- **funct7**: Common for all (`0000000`).


#### **Instruction Types**
1. **R-Type**:  
   - Format: `add, sub, and, or, sll`  
   - Operates on registers, requires 3 operands (`rd`, `rs1`, `rs2`).

2. **I-Type**:  
   - Format: `addi, load`  
   - Operates with immediate values, requires 2 registers and an immediate (`rd`, `rs1`, imm).

3. **SB-Type** (Branch):  
   - Format: `beq, bne, blt, bgt`  
   - Used for conditional branching with two registers and an offset (`rs1`, `rs2`, offset).

4. **U-Type**:  
   - Format: `lui`  
   - Handles upper immediate values, used for addresses or large constants.

5. **UJ-Type** (Jump):  
   - Format: `jal`  
   - Used for unconditional jumps and saving return addresses.  


#### **R-Type Instruction (ADD, SUB, etc.)**
- **Structure**:  
  ```
  opcode | funct7 | rs2 | rs1 | funct3 | rd | opcode
  ```
  - **opcode**: Specifies operation type (e.g., 0110011 for R-Type).
  - **funct7**: Additional operation specifier (e.g., 0000000 for ADD).
  - **funct3**: Operation category (e.g., 000 for ADD/SUB).
  - **rs1, rs2**: Source registers.
  - **rd**: Destination register.

- **Example**: `add x5, x1, x2`  
  ```
  opcode: 0110011
  funct7: 0000000
  funct3: 000
  rs1: 00001 (x1)
  rs2: 00010 (x2)
  rd: 00101 (x5)
  Encoded: 0000000 00010 00001 000 00101 0110011
  ```

#### **I-Type Instruction (ADDI, SRLI, etc.)**
- **Structure**:  
  ```
  imm[11:0] | rs1 | funct3 | rd | opcode
  ```
  - **imm**: Immediate value (12 bits).
  - **opcode**: Specifies operation type (e.g., 0010011 for I-Type).
  - **funct3**: Operation category (e.g., 000 for ADDI).

- **Example**: `addi x5, x1, 10`  
  ```
  opcode: 0010011
  funct3: 000
  rs1: 00001 (x1)
  rd: 00101 (x5)
  imm: 000000001010 (10 in binary)
  Encoded: 000000001010 00001 000 00101 0010011
  ```

#### **SB-Type Instruction (BEQ, BNE, etc.)**
- **Structure**:  
  ```
  imm[12|10:5] | rs2 | rs1 | funct3 | imm[4:1|11] | opcode
  ```
  - **imm**: Offset for branching (split across the instruction).
  - **opcode**: Specifies operation type (e.g., 1100011 for SB-Type).

- **Example**: `beq x1, x2, offset` (offset = 16)  
  ```
  opcode: 1100011
  funct3: 000
  rs1: 00001 (x1)
  rs2: 00010 (x2)
  imm: 00000000010000 (16 in binary, split as above)
  Encoded: 000000 00010 00001 000 00001 1100011
  ```

#### **U-Type Instruction (LUI)**
- **Structure**:  
  ```
  imm[31:12] | rd | opcode
  ```
  - **imm**: 20-bit immediate value (upper bits).
  - **opcode**: Specifies operation type (e.g., 0110111 for LUI).

- **Example**: `lui x5, 0x12345`  
  ```
  opcode: 0110111
  rd: 00101 (x5)
  imm: 00010010001101000101
  Encoded: 00010010001101000101 00101 0110111
  ```

#### **UJ-Type Instruction (JAL)**
- **Structure**:  
  ```
  imm[20|10:1|11|19:12] | rd | opcode
  ```
  - **imm**: 20-bit immediate value (split across fields).
  - **opcode**: Specifies operation type (e.g., 1101111 for JAL).

- **Example**: `jal x1, offset` (offset = 2048)  
  ```
  opcode: 1101111
  rd: 00001 (x1)
  imm: 000000010000 (2048 in binary, split as above)
  Encoded: 000000010000 00001 1101111
  ```

1. **OR Instruction**: `or x5, x1, x2`  
   ```
   opcode: 0110011
   funct7: 0000000
   funct3: 110
   rs1: 00001 (x1)
   rs2: 00010 (x2)
   rd: 00101 (x5)
   Encoded: 0000000 00010 00001 110 00101 0110011
   ```

2. **XOR Instruction**: `xor x5, x1, x2`  
   ```
   opcode: 0110011
   funct7: 0000000
   funct3: 100
   rs1: 00001 (x1)
   rs2: 00010 (x2)
   rd: 00101 (x5)
   Encoded: 0000000 00010 00001 100 00101 0110011
   ```

3. **AND Instruction**: `and x5, x1, x2`  
   ```
   opcode: 0110011
   funct7: 0000000
   funct3: 111
   rs1: 00001 (x1)
   rs2: 00010 (x2)
   rd: 00101 (x5)
   Encoded: 0000000 00010 00001 111 00101 0110011
   ```

---

### **Immediate Versions (ORI, XORI, ANDI)**

These use the **I-Type structure**:  
```
imm[11:0] | rs1 | funct3 | rd | opcode
```

- **opcode**: Common for all I-Type (`0010011`).  
- **funct3**: Determines the specific operation:
  - `ORI`: `110`
  - `XORI`: `100`
  - `ANDI`: `111`  

#### Encoding Examples:

1. **ORI Instruction**: `ori x5, x1, 10`  
   ```
   opcode: 0010011
   funct3: 110
   rs1: 00001 (x1)
   rd: 00101 (x5)
   imm: 000000001010 (10 in binary)
   Encoded: 000000001010 00001 110 00101 0010011
   ```

2. **XORI Instruction**: `xori x5, x1, 10`  
   ```
   opcode: 0010011
   funct3: 100
   rs1: 00001 (x1)
   rd: 00101 (x5)
   imm: 000000001010 (10 in binary)
   Encoded: 000000001010 00001 100 00101 0010011
   ```

3. **ANDI Instruction**: `andi x5, x1, 10`  
   ```
   opcode: 0010011
   funct3: 111
   rs1: 00001 (x1)
   rd: 00101 (x5)
   imm: 000000001010 (10 in binary)
   Encoded: 000000001010 00001 111 00101 0010011
   ```

### **Summary of Encoding**
| **Instruction** | **Opcode** | **Funct3** | **Funct7** | **Type**   |
|------------------|------------|------------|------------|------------|
| `add`           | 0110011    | 000        | 0000000    | R-Type     |
| `sub`           | 0110011    | 000        | 0100000    | R-Type     |
| `addi`          | 0010011    | 000        | N/A        | I-Type     |
| `srli`          | 0010011    | 101        | 0000000    | I-Type     |
| `beq`           | 1100011    | 000        | N/A        | SB-Type    |
| `bne`           | 1100011    | 001        | N/A        | SB-Type    |
| `lui`           | 0110111    | N/A        | N/A        | U-Type     |
| `jal`           | 1101111    | N/A        | N/A        | UJ-Type    |
| `or`            | 0110011    | 110        | 0000000    | R-Type   |
| `xor`           | 0110011    | 100        | 0000000    | R-Type   |
| `and`           | 0110011    | 111        | 0000000    | R-Type   |
| `ori`           | 0010011    | 110        | N/A        | I-Type   |
| `xori`          | 0010011    | 100        | N/A        | I-Type   |
| `andi`          | 0010011    | 111        | N/A        | I-Type   | 


