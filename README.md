## 1 - Preparing the environment

To start we can create a new folder in our local machine, to clone the source repository, and opened in VSCode.
<p align="center">
  <img src=".images/github_clone.png" alt="github clone terminal" width="50%">
</p>

After that, I remove the Github origin and add my new origin, a new repository in my Github account, to save the challenge solution.

```
$ git remote remove origin 
$ git remote add origin https://github.com/rsradulescu/IFCO-data-engineering-solution-test.git        
```

In VSCode, open terminal and:
- Create a new README file and updated.
- Configuring the Python virtual environment, with the latest stable python version (V3.12 at October 16)

```
$ python3 --version  
$ python3.12 -m venv venv 
```

- Now, a new folder was created, with the venv files, we need to activate it.

```
$ source venv/bin/activate   
```
- Create a requirement.txt file to list all the necesary Python libraries, and installed at once (if you don't know it at the beggining, you can just installing locally and later generate the requirement file with the command: $pip freeze > requirements.txt ). 

```
$ pip install -r requirements.txt
```

- Create the folders needed to organice the process: src folder for the python code and test folder for the test python code.

```
$ mkdir test
$ mkdir scr
```

## 2 - Developing the solution

NOTE: I decided to create one different python file for each requirement in the challenge. 

### Test 1: Distribution of Crate Type per Company

- Create the t1_orders_per_type.py file.
- Define 2 main functions: 
- - The first one to load the df with the content of orders.csv
- - The second one to get the distribution number group by company name and box type.
- To test this code I added the condition "if __name__ == __main__"

<p align="center">
  <img src=".images/1-get_distribution.png" alt="execute distribution python code" width="50%">
</p>

### Test 2: DataFrame of Orders with Full Name of the Contact
- Import first file we created before to use the load function.
- Create a function to receive a json object with contact data. Extract the name and subname and return the concatenation.
- If some of these values are missing, or the contact_data is empty, return the placeholder "John Doe".
- Apply the previous function to every row in the df.
- To test this code I added the condition "if __name__ == __main__"

<p align="center">
  <img src=".images/2-get_fullname.png" alt="get order id and full name python code" width="50%">
</p>





---------
Add quality scripts
- some of the company names seems same, I consider to get similar name as the same company, with a new column name.
- modeling