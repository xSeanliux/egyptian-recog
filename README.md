# Egyptian-recog
By Sean Liu, Casper Wang, Eric Xiao from CK high school

## Installation 
We have all the tools you need to evaluate and train your own network! But first, please run 
```egyptian-recog$ pip3 install -r requirements.txt```
to install all the prequisite requirements! Then, make sure to run 
```
make qt5py3
pyrcc5 -o libs/resources.py resources.qrc   
```
to be able to run `labelImg`.

## Goal
Tries to recognize Ancient Egyptian text from stelae or murals and the sort 
## Schedule

## What we have done

## Notes
* Change all the `filters=255` to `filters=[5 + n]*3`, where `n` is the number of classes in the `*.cfg` file. Also modify the `classes` parameter below. See [this tutorial](https://github.com/ultralytics/yolov3/wiki/Train-Custom-Data) for more info. 
