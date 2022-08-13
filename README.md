<img 
    style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 20%;"
    src="./banner_img.png" 
    alt="Our logo">
</img>
<h1 style="text-align: center;">Stock Sim</h1>

### Python based trading simulator to practice trading or test algorithms which perform algorithmic trading. 

### Get live prices and stock data of 100,000+ tickers to perform transactions on.

<hr>

<br>

# Modules
### Stock sim windows client : <https://github.com/ganesh-dagadi/stock_sim_client>

### Stock sim backend module : <https://github.com/ganesh-dagadi/stock_sim_backend>

<hr>

<br>

# Installation

## Prerequisites

<ul>
    <li>Python 3 with pip (make sure you have added python to path in windows)</li>
    <li>Postgresql version14</li>
</ul>

## Windows

### The client can be setup using `gdmm` module manager. Installation instructions for `gdmm` can be [found here](https://github.com/ganesh-dagadi/gdmm). 

<br>

### To install globally, run

```
gdmm -c install -r stock_sim_client -u ganesh-dagadi
```
<br>

### To install in current directory, run

```
gdmm -c install -r stock_sim_client -u ganesh-dagadi -l
```
### if you installed in the currect directory, go to root of client 

`cd stock_sim_client`

### and create a file called `.env`

</br>

### open the file and enter the following:

```
DATABASE_PASSWORD = your postgresql postgres user password
```

### If you installed the module globally, go to `C:\Users\<username>\gdmm\modules\stock_sim_client`

### and follow the above steps to create `.env` file



