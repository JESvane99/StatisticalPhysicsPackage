[HOME](TOC)

# Gas in a Container

(GPS_effusion)=
## General problem solving

```{tip} Effusion problem and alike
:name: GPS_effusion_tip
When working with particles colliding with a small area
remember to work in 1 dimension first, and then think of the units that are given.
i.e. velocity is $\frac{m}{s}$ and in one direction it is okay to make use of the
approximation that half of the particles are moving at the wall and vice versa.
```

```{list-table} Praxis for [GP][d1]
:header-rows: 1
:name: pgpeffus

*   - Step
    - Brain usage
    - Quick maths
*   - 1
    - Write the number of Particles colliding with area as a function of time
    - ![Alt text](<../../../figures/Gasincontainer/image.png>)
*   - 2
    - Assume that m is the same for all molecules. From equation (1.12) in Schroeder, we know the contribution to the pressure from one of these molecules
    - ![Alt text](<../../../figures/Gasincontainer/image-1.png>)
*   - 3
    - Rearranging equation and taking the sum
    - ![Alt text](<../../../figures/Gasincontainer/image-2.png>)
    ![Alt text](<../../../figures/Gasincontainer/image-3.png>)
*   - 4
    - Now define $\overline{v_x} \Delta N = \sum_{v_x>0} v_x \Delta N_{v_x}$ with $\Delta N$ vx
is the total number of molecules hitting the wall within the time $\Delta t$
    - ![Alt text](<../../../figures/Gasincontainer/image-4.png>)
*   - 5 
    - rearranging to get $\Delta N = \frac{PA\Delta t}{2m \overline{v_x}}$ and using $v_x = \sqrt{\frac{kT}{m}}$
    - ![Alt text](<../../../figures/Gasincontainer/image-5.png>)
*   - 6
    - rewrite using the [Ideal Gas Law](../IdealGas/Averagemoleculesize.md#idgs)
    - ![Alt text](<../../../figures/Gasincontainer/image-6.png>)
```

![Alt text](<../../../figures/Gasincontainer/image-7.png>)



[TOC]: ../../index.rst
[d1]: ../../usage.md#usage

