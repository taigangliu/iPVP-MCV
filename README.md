iPVP-MCV
=========================
iPVP-MCV was developed for the prediction of Phage virion proteins. The system diagram is as follows:
![image](https://user-images.githubusercontent.com/44895765/128601820-9b09ab05-bc76-40c3-b1db-c7f5399cb498.png)

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
