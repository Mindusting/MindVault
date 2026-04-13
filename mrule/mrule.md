---
aliases:
  - Reglas de Mindusting
  - Mindusting Rules
author: Mindusting
corrected: false
headerFile: true
rating:
---

# REGLAS DE MINDUSTING

> [!unfinished-file]- ESTE APARTADO ESTÁ INCOMPLETO
> 
> En este apartado se van a documentar las reglas que se debe aplicar a la hora de redactar/estructurar la documentación; con la intención de que toda la documentación siga un patón lógico y predecible.
> 
> Esto le puede servir bien a los usuarios que estén leyendo mi documentación por primera vez ya que les puede ayudar a entender como está estructurada la vóvdea de notas, facilitando el encontrar una documentación en específico.
> 
> > [!todo] #TODO

%%

> [!cog] ESTRUCTURA BÁSICA DE DOCUMENTACIÓN DE LENGUAJE DE PROGRAMACIÓN
> - **Carpeta con el nombre del lenguaje**:
>     - **assets**: contiene dibujos, imágenes, diagramas, etc; que se use en la documentación local.
>     - **commands**: en caso de haber comandos se deben guardar aquí.
>     - **fundamentals**: contien los aspectos fundamentales del lenguaje de programación:
>         - **variables**
>         - **flow_control**
>         - **functions**
>         - **oop**
>         - **file_manachment**
>     - **theory**: contiene la teoría 

%%

Las carpetas describen categorías mientras que los dominios como puede ser "Web" se establecerán por etiquetas.

computing/ -> programming
de/ -> design

- `knoledge`
    - `computer_science`
        - `programming`
            - `fundamentals`
                - `function.md`
            - `design`
                - `white_box.md`
                - `black_box.md`
                - `flowchart.md`
                - `pattern`
                    - `singleton.md`
                    - `factory.md`
                    - `adapter.md`
            - `data_format`
                - `ascii.md`
                - `utf-8.md`
                - `json.md`
                - `yaml.md`
                - `csv.md`
            - `language`
                - `python`
                    - `py.md`
                - `java`
                    - `java.md`
                - `javascript`
                    - `js.md`
        - `software_development`
            - `framework`
                - `angular`
        - `markup_language`
            - `html`
                - `html.md`
            - `xml`
                - `xml.md`
            - `svg`
                - `svg.md`
            - `markdown`
                - `md.md`
            - `mermaid`
                - `mermaid.md`
            - `latex`
                - `latex.md`
        - `style_language`
            - `css`
                - `css.md`
            - `sass`
                - `sass.md`
        - `text_processing`
            - `regex`
                - `regex.md`
        - `dev_tools`
            - `ssh`
                - `ssh.md`
        - `system`
            - `linux`
                - `command`
                    - `cd.md`
                    - `ls.md`
                    - `mv.md`
                - `filesystem`
                - `permission`
            - `windows`
        - `computer_architecture`
            - `binary`
                - `binary.md`
            - `logic_gate`
            - `alu`
            - `cpu`
            - `memory`
        - `data_structure`
            - `array.md`
            - `vector.md`
            - `linked_list.md`
            - `stack.md`
            - `queue.md`
            - `hashtable.md`
            - `tree.md`
            - `graph.md`
        - `data_base`
            - `relational`
                - `theory`
                    - `relational_model.md`
                    - `normalization.md`
                - `query_language`
                    - `sql.md`
                - `system`
                    - `sqlite`
                        - `sqlite.md`
                    - `mysql`
                        - `mysql.md`
            - `nosql`
                - `model`
                    - `key_value.md`
                    - `document.md`
                    - `graph.md`
                - `system`
                    - `mongodb.md`
    - `mathemathic`
    - `physic`
    - `chemistry`
    - `biology`
    - `electronic`
    - `cooking`

```txt
/knowledge
|-/computer_science
| |-/programming
| | |-/fundamentals
| | |-/design
| | | |- white_box.md
| | | |-/pattern
| | | | |-singleton.md
| | |
| | |-/data_format
| | | |- ascii.md
| | | |- utf-8.md
| | | |- json.md
| | | |- yaml.md
| | | |- csv.md
| | |
| | |-/language
| | | |-/python
| | | | |- py.md
| | | |
| | | |-/java
| | | | |- java.md
| | | |
| | | |-/javascript
| | | | |- js.md
| |
| |-/software_development
| | |-/framework
| | | |-/angular
| |
| |-/markup_language
| | |- html.md
| | |- xml.md
| | |- svg.md
| | |- markdown.md
| | |- mermaid.md
| | |- latex.md
| |
| |-/style_language
| | |- css.md
| | |- sass.md
| |
| |-/text_processing
| | |- regex.md
| |
| |-/dev_tools
| | |- ssh.md
| |
| |-/systems
| | |-/linux
| | | |-/commands
| | | |-/filesystem
| | | |-/permissions
| | |
| | |-windows
| | 
| |-/computer_architecture
| | |-/binary
| | |-/logic_gates
| | |-/alu
| | |-/cpu
| | |-/memory
| |
| |-/data_structure
| | |- array.md
| | |- vector.md
| | |- linked_list.md
| | |- stack.md
| | |- squeue.md
| | |- hashtable.md
| | |- tree.md
| | |- graph.md
| |
| |-/data_bases
| | |-/relational
| | | |-/theory
| | | | |- relational_model.md
| | | | |- normalization.md
| | | |
| | | |-/query_language
| | | | |- sql.md
| | | |
| | | |-/system
| | | | |-/sqlite
| | | | |-/mysql
| | | | |-/sql-server
| | |
| | |-/nosql
| | | |-/models
| | | | |- key_value.md
| | | | |- document.md
| | | | |- graph.md
| | | |
| | | |-/system
| | | | |-/mongodb
|
|-/mathematics
|-/physics
|-/chemistry
|-/biology
|-/electronics
|-/cooking
```

```txt
Computer architecture index:
    00_information_representation
    01_digital_logic
    02_combinational_circuits
    03_sequential_circuits
    04_cpu_components
    05_cpu_design
    06_memory
    07_instruction_set
    08_io_and_peripherals
```
