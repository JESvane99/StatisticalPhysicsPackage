# {py:mod}`SttPhscsPckg.PartitionFunctions`

```{py:module} SttPhscsPckg.PartitionFunctions
```

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions
:allowtitles:
```

## Module Contents

### Functions

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`T_therm_equil_resevoir <SttPhscsPckg.PartitionFunctions.T_therm_equil_resevoir>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.T_therm_equil_resevoir
    :summary:
    ```
* - {py:obj}`Frac_partition_funcs <SttPhscsPckg.PartitionFunctions.Frac_partition_funcs>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.Frac_partition_funcs
    :summary:
    ```
* - {py:obj}`PF_average_energy <SttPhscsPckg.PartitionFunctions.PF_average_energy>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.PF_average_energy
    :summary:
    ```
* - {py:obj}`PF_heat_capacity <SttPhscsPckg.PartitionFunctions.PF_heat_capacity>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.PF_heat_capacity
    :summary:
    ```
* - {py:obj}`PF_prob_of_one_state <SttPhscsPckg.PartitionFunctions.PF_prob_of_one_state>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.PF_prob_of_one_state
    :summary:
    ```
* - {py:obj}`partition_func_template <SttPhscsPckg.PartitionFunctions.partition_func_template>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.partition_func_template
    :summary:
    ```
* - {py:obj}`symbolic_F_free_energy <SttPhscsPckg.PartitionFunctions.symbolic_F_free_energy>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.symbolic_F_free_energy
    :summary:
    ```
* - {py:obj}`create_arrays <SttPhscsPckg.PartitionFunctions.create_arrays>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.create_arrays
    :summary:
    ```
* - {py:obj}`energyMatrix <SttPhscsPckg.PartitionFunctions.energyMatrix>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.energyMatrix
    :summary:
    ```
````

### Data

````{list-table}
:class: autosummary longtable
:align: left

* - {py:obj}`n <SttPhscsPckg.PartitionFunctions.n>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.n
    :summary:
    ```
* - {py:obj}`U <SttPhscsPckg.PartitionFunctions.U>`
  - ```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.U
    :summary:
    ```
````

### API

````{py:data} n
:canonical: SttPhscsPckg.PartitionFunctions.n
:value: >
   'symbols(...)'

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.n
```

````

````{py:data} U
:canonical: SttPhscsPckg.PartitionFunctions.U
:value: >
   'symbols(...)'

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.U
```

````

````{py:function} T_therm_equil_resevoir(Delta_Energy, total_num)
:canonical: SttPhscsPckg.PartitionFunctions.T_therm_equil_resevoir

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.T_therm_equil_resevoir
```
````

````{py:function} Frac_partition_funcs(E_difference, T)
:canonical: SttPhscsPckg.PartitionFunctions.Frac_partition_funcs

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.Frac_partition_funcs
```
````

````{py:function} PF_average_energy(func, beta)
:canonical: SttPhscsPckg.PartitionFunctions.PF_average_energy

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.PF_average_energy
```
````

````{py:function} PF_heat_capacity(partition_func, beta)
:canonical: SttPhscsPckg.PartitionFunctions.PF_heat_capacity

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.PF_heat_capacity
```
````

````{py:function} PF_prob_of_one_state(func, energy=h * f, single_state=False)
:canonical: SttPhscsPckg.PartitionFunctions.PF_prob_of_one_state

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.PF_prob_of_one_state
```
````

````{py:function} partition_func_template(m=1, quant_single_state: list = [1], e_unit=None, e_input=None)
:canonical: SttPhscsPckg.PartitionFunctions.partition_func_template

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.partition_func_template
```
````

````{py:function} symbolic_F_free_energy(num_particles=1, stirling_approx=True)
:canonical: SttPhscsPckg.PartitionFunctions.symbolic_F_free_energy

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.symbolic_F_free_energy
```
````

````{py:function} create_arrays(r, k)
:canonical: SttPhscsPckg.PartitionFunctions.create_arrays

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.create_arrays
```
````

````{py:function} energyMatrix(n: int = 1, m: int = 1, qntt_prtcls: int = 1, nrg_type=None, ret_all: bool = False)
:canonical: SttPhscsPckg.PartitionFunctions.energyMatrix

```{autodoc2-docstring} SttPhscsPckg.PartitionFunctions.energyMatrix
```
````
