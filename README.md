<img 
    style="display: block; 
           margin-left: auto;
           margin-right: auto;
           width: 20%;"
    src="./banner_img.png" 
    alt="Our logo">
</img>
<h1 style="text-align: center;">Stock Sim</h1>

 Python based trading simulator to practice trading or test algorithms which perform algorithmic trading. 

 Get live prices and stock data of 4000+ tickers listed on the Bombay stock exchange to perform transactions on.


<br>

# Modules
 Stock sim windows client : <https://github.com/ganesh-dagadi/stock_sim_client>

 Stock sim backend module : <https://github.com/ganesh-dagadi/stock_sim_backend>

<hr>

<br>

# Installation

## Prerequisites

<ul>
    <li>Python 3 with pip (make sure you have added python to path in windows)</li>
    <li>Postgresql version14</li>
</ul>

## Windows

 The client can be setup using `gdmm` module manager. Installation instructions for `gdmm` can be [found here](https://github.com/ganesh-dagadi/gdmm#installation). 

<br>

 To install globally, run

```
gdmm -c install -r stock_sim_client -u ganesh-dagadi
```
<br>

 To install in current directory, run

```
gdmm -c install -r stock_sim_client -u ganesh-dagadi -l
```
 if you installed in the currect directory, go to root of client 

`cd stock_sim_client`

 and create a file called `.env`

</br>

 open the file and enter the following:

```
DATABASE_PASSWORD = your postgresql postgres user password
```

 If you installed the module globally, go to `C:\Users\<username>\gdmm\modules\stock_sim_client`

 and follow the above steps to create `.env` file

### Setting up backend.

`gdmm ` automatically installs the backend module for stockSim. follow the steps [here](https://github.com/ganesh-dagadi/stock_sim_backend) to setup the backend.

# Running the application:

Running the applications depends on where you installed the module. 

### Locally:

navigate to the root of stock_sim_client and run,
```
gdmm -c run -l
```

### Globally:

Run the following command irrespective of the current directory

```
gdmm -c run -r stock_sim_client
```
