## TASK 1
### Goal:
- Create a linear regression model using python.
- Create a docker image for the same.
- Execute the python code using the container.

---

### Steps to use the Dockerfile and container
- Create an image using the Dockerfile <br>
  ``` docker build . -t salary_pred:v1``` 
- Run the container using the following command:
  ``` docker run salary_pred:v1```

Model error, coefficient and intercept will be the output.<br>

---
Medium Blog: 