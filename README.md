iPVP-MCV
=========================
iPVP-MCV was developed for the prediction of Phage virion proteins, system diagram are shown belw:
![image](https://user-images.githubusercontent.com/44895765/128601799-38ba42e5-b079-4b74-8840-7bc5841a5a49.png)

Installation Process
=========================
Required Python Packages:

Install: python (version >= 3.6)  
Install: sklearn (version >= 0.24.2)  
Install: numpy (version >= 1.19.2)    

pip install < package name >  
example: pip install sklearn  

or  
We can download from anaconda cloud.  

Usage
=========================
To run: $ iPVP-MCV-AAC.py  
        $ iPVP-MCV-DP-PSSM.py  
        $ iPVP-MCV-PSSM-composition.py  
        $ Ind-vote.py
        
The iPVP-MCV-AAC.py, iPVP-MCV-DP-PSSM.py and iPVP-MCV-PSSM-composition.py files implement the baseline models of iPVP-MCV, the Ind-vote.py integrates the outputs of these baseline models for final prediction.
 
If you want to use different training and test data, please change the directory name inside the file.
