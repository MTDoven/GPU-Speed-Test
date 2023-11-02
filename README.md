# Single GPU Speed Test

A simple program used to measure the computing power of GPUs.

I conducted speed tests on various GPUs using a simple program. Matrix multiplication serves as the fundamental operation in both neural network training and inference, so I exclusively evaluated the performance of matrix multiplication across many different GPUs. 

In this way, the time consumed by cuda initialization can be excluded, and the GPU is 100% fully used during the whole test.

---

- **Here's the results:**

---

- Consumer GPUs:

|GPU|memory|float32|float16|bfloat16|
|:--:|:--:|:--:|:--:|:--:|
|RTX 2080Ti|11G / 22G|675ms|158ms|1200ms|
|RTX 3080|12G|279ms|135ms|135ms|
|RTX 3080Ti|12G|245ms|118ms|118ms|
|RTX 3080Ti Laptop|16G|593ms|180ms|178ms|
|RTX 3090|24G|247ms|117ms|115ms|
|RTX 4060Ti|8G / 16G|561ms|177ms|177ms|
|RTX 4090|24G|171ms|50ms|50ms|
|TITAN XP|12G|843ms|1050ms|2040ms|
|TITAN V|12G|825ms|178ms|867ms|
|TITAN RTX|24G|611ms|124ms|1086ms|

(The data of TITAN RTX is inferred from network data instead of the test.)

---

Professional GPUs:

|GPU|memory|float32|float16|bfloat16|
|:--:|:--:|:--:|:--:|:--:|
|Tesla T4|16G|2110ms|460ms|3480ms|
|Tesla P40|24G|875ms|1080ms|1970ms|
|Tesla V100|16G / 32G|618ms|102ms|794ms|
|Tesla A40|48G|176ms|80ms|82ms|
|Tesla A100|40G / 80G|89ms|46ms|42ms|
|Tesla H800|80G|164ms|13ms|12ms|
|RTX A4000|16G|392ms|165ms|162ms|
|RTX A5000|24G|533ms|99ms|96ms|
|Tesla P100|16G|1140ms|267ms|1400ms|

(The data of Tesla P100 is inferred from network data instead of the test.)

---

Source of test card:  
[GpushareCloud](https://gpushare.com/)  
[AutoDL](https://www.autodl.com/)  


