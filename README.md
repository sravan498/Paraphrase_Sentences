# Sentence_paraphrasing_t5_model

### Project Structure -

Dataset: T5 model uses C4 dataset(Common Crawl's web crawl corpus). So we dont need to provide any external dataset to train this model

#### Codes:
<ol>
  
<li>app.py: runs on 6000 port, given a sentence the system tries to find the different variations of the question for the user input</li>

<li>logs: The file stores the logging of the service. The projects uses python standard logging to log date, time with information and error type.</li>

<li>dockerfile: The file consits of various commands and libraries to run the file in the docker </li>
</ol>

##### Dependencies: The project is built using python 3.X. Open source packges:

tensorflow(gpu)

tensorflow-hub

pytorch(CUDA 10.1)

flask

numpy

transformers

#### Installing libraries:
requirements.txt: contains all the packages required to run the project. Run the below command to install the required libraries for the project
**pip install -r requirements.txt** 

#### Build Docker Image:
<ol><li>Build docker using the command **docker build -t myname/myapp </li>
<li>Run the </li>
</ol>

#### Response from API:
Request Example: {"comment": query string}

Response Type: {"text" : answer string1 
                         answer string2 
                         answer string3}
