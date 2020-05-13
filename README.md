# FWI HTTP Post Script

Intended for use with Four Winds Interactive's proprietary Progressive Jackpot Service software.

## About

This is a very basic python script intended to take a progressive xml file and merge it with the PJS MeterData.xml via the Four Winds HTTP Listener.  The Python script writes the local xml to the PJS machine via HTTP Post request.  It is assumed that the client is updating this progressive xml through their own means (presumably their own progressive integration).  It is also assumed the client’s local xml *exactly matches* the schema required, see [post-schema.xml](assets/post-schema.xml).  The purpose of this script is simply to merge the local xml with the PJS MeterData.xml so it can be distributed to the signage PCs through socket request/multicast IP.

## Machine Setup

1.  If you haven't already, install and configure FWI Progressive Jackpot Service on your designated machine/server.

2.	On the designated machine (the same PC with the progressive xml file), download the latest version of [Pyhton for Windows](https://www.python.org/downloads/windows/)

3.  Also install [Pip for Windows](https://pip.pypa.io/en/stable/installing/)

4.  Fetch the `progressivepost.py` script and copy it into the exact same UNC folder path as your progressive xml. 

## 

