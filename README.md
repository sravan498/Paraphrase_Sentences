# Sentence_paraphrasing_t5_model

### Project Structure -

Dataset:
This model was trained on T5 model which uses C4 dataset(Common Crawl's web crawl corpus).

#### Codes:
Files used:
<ol>
<li>app.py: runs on 6000 port, given a sentence the system tries to find the different variations of the question for the user input</li>
<li>logs: The file stores the logging of the service. The projects uses python standard logging to log date, time with information and error type.</li>
<li>dockerfile: The file consits of various commands and libraries to run the file in the docker </li>
</ol>

##### Dependencies: The project is built using python 3.X. Open source packges:
<ul>
<li>tensorflow(gpu)</li>
<li>tensorflow-hub</li>
<li>pytorch(CUDA 10.1)</li> 
<li>flask</li>
<li>numpy</li>
<li>transformers</li>
</ul>

#### Installing libraries:
requirements.txt: contains all the packages required to run the project. Run the below command to install the required libraries for the project
**pip install -r requirements.txt** 
Pytorch version needs to be installed depending upon the CUDA Version from pytorch.org

#### Build Docker Image:
<ol><li>Build docker using the command docker build -t myname/myapp </li>
<li>Run the  docker using  docker run -p 6000:6000 myname/myapp </li>
</ol>

#### Response from API:
Request Example: {"comment": query string}

Response Type: {"text" : answer string1 
                         answer string2 
                         answer string3}
