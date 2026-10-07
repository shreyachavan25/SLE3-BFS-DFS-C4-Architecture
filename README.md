# SLE-3: Full C4 Architecture Design – BFS/DFS Search System

## Course
**02AML204 – Introduction to Artificial Intelligence**

## Assignment
**SLE-3: Architectural Design using Full C4 Model**

## System
**BFS/DFS Search System**

---

## 1. Project Overview

This project presents the architectural design of a BFS/DFS Search System using the **Full C4 Model**.

The system is based on the search system developed and profiled in **SLE-2**. It represents the software architecture at four different levels, from the overall system context to the main code-level functions.

The four C4 levels covered in this project are:

1. **Context** – Shows the system and its interaction with the user.
2. **Container** – Shows the major building blocks of the system.
3. **Component** – Shows the internal components of the main Search Engine.
4. **Code** – Shows the important classes/functions used in the implementation.

---

## 2. System Description

The BFS/DFS Search System performs graph search using **Breadth-First Search (BFS)** and **Depth-First Search (DFS)**.

The user provides the graph/search input and the system processes it using the selected search algorithm.

The system maintains visited-node information, checks whether the goal has been reached, reconstructs the resulting path, and provides the final search result as output.

This architecture extends the search system used in **SLE-2**, where BFS and DFS performance was profiled and compared.

---

## 3. C4 Model Architecture

### Level 1 – Context Diagram

The Context diagram represents the complete system from a high-level perspective.

**Main elements:**

- User
- BFS/DFS Search System
- Search Result Output

**Interaction:**

`User → BFS/DFS Search System → Search Result Output`

The user provides the search input to the system. The system performs BFS or DFS and provides the search result as output.

![C4 Context Diagram](Diagrams/01_C4_Context.png)

---

### Level 2 – Container Diagram

The Container diagram divides the BFS/DFS Search System into its major functional building blocks.

The system contains the following containers:

#### 1. Input Module
Accepts and prepares the graph or search input provided by the user.

#### 2. Search Engine
Executes the selected BFS or DFS search algorithm.

#### 3. Visited / Memory Structure
Stores visited-node information to avoid unnecessary repeated processing.

#### 4. Goal Test
Checks whether the current node satisfies the required goal condition.

#### 5. Path / Result Reconstructor
Reconstructs the final path or search result after the goal is reached.

#### 6. Output Module
Displays the final search result to the user.

![C4 Container Diagram](Diagrams/02_C4_Container.png)

---

### Level 3 – Component Diagram

The Component diagram focuses on the **Search Engine**, which is the main container responsible for executing the search algorithm.

The main components are:

- **Frontier Queue / Stack** – Maintains nodes waiting to be processed.
- **Visited / Explored Set** – Tracks nodes that have already been explored.
- **Goal Test** – Checks whether the current node is the required goal.
- **Path Reconstructor** – Reconstructs the path from the search information.

These components work together to perform the search and produce the required result.

![C4 Component Diagram](Diagrams/03_C4_Component.png)

---

### Level 4 – Code Level Overview

The Code level identifies the main classes and functions involved in the implementation.

- `Graph / Problem Representation` – Represents the graph or search problem.
- `bfs()` – Performs Breadth-First Search.
- `dfs()` – Performs Depth-First Search.
- `Visited & Parent Tracking` – Maintains visited information and parent relationships.
- `reconstruct_path()` – Reconstructs the resulting path.

![C4 Code Level Diagram](Diagrams/04_C4_Code.png)

---

## 4. Design Decisions

- The **Search Engine** is treated as the main container because BFS and DFS are the core operations of the system.
- The system is divided into separate containers so that input, searching, visited-node management, goal checking, path reconstruction, and output have clear responsibilities.
- The Component level focuses only on the Search Engine, following the C4 model requirement to show the internal parts of one main container.
- The Code level contains only the main classes/functions instead of large source-code blocks.

---

## 5. AI Contribution Note

### AI Tools Used
ChatGPT was used as an AI assistance tool during the development of this SLE-3 architecture.

### What AI Helped With
AI assistance was used to understand the C4 Model, organize the architecture into Context, Container, Component, and Code levels, and improve the structure and documentation of the report.

### What I Did Myself
I selected the BFS/DFS Search System based on my SLE-2 work, created the C4 diagrams in diagrams.net, organized the project files, reviewed the architecture, and prepared the final submission.

---

## 6. Connection with SLE-2

This SLE-3 project continues the same BFS/DFS search system used in **SLE-2**.

In SLE-2, BFS and DFS were profiled and their performance was compared using profiling tools.

In SLE-3, the same system is represented architecturally using the **Full C4 Model**.

Therefore:

**SLE-2 → Performance Profiling**

**SLE-3 → Architectural Design**

---

## 7. Project Structure

```text
SLE3-BFS-DFS-C4-Architecture/
│
├── Diagrams/
│   ├── 01_C4_Context.png
│   ├── 02_C4_Container.png
│   ├── 03_C4_Component.png
│   └── 04_C4_Code.png
│
├── Report/
│   ├── SLE3_PRN_YourName.docx
│   └── SLE3_PRN_YourName.pdf
│
└── SLE3_BFS_DFS_C4_architecture.drawio