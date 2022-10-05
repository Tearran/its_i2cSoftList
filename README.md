# its_i2cSoftList
I2c scanner

```bash
sudo apt update && sudo apt install git;
git clone https://github.com/Tearran/its_i2cSoftList
```
launch

```
python3 its_i2cSoftList -h 
```

```bash
Usage : i2c-scanner.py <datatype>
    -h   : Displays this help
    none : same as csv
    csv  : Displays Comma seperated list
    dict : Displays dictionary
    cli  : Displays readable

```

```
python3 its_i2cSoftList cli
```
``` bash 
Device @ 0x5a
        Name:   mlx90614
        Type:   sensor
        URL:    https://gitlab.com/tearran/its-i2cDevices

Device @ 0x68
        Name:   MPU-6050
        Type:   sensor
        URL:    https://gitlab.com/tearran/its-i2cDevices

Device @ 0x76
        Name:   bmp280
        Type:   sensor
        URL:    https://gitlab.com/tearran/its_bmp280

```
