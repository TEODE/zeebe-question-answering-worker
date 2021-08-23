Zeebe Question Answering Worker
================================

A [Zeebe](https://zeebe.io) question answering worker based on [Hugging Face](https://huggingface.co/) NLP pipeline

Configure
---------

Set a virtual python environment for version 3.7.10 and install requirements:

```bash
pip install -r requirements.txt 
```

Specify a local (after downloading under models folder) or an [Hugging Face question answering model](https://huggingface.co/models?pipeline_tag=question-answering) in the .env file

Due to high resource consumption of some models, we decided to make this worker configurable in term of task name and associated model.
For example, so it is possible to separate tasks and models with multiple workers for language handling :

* task `question-answering-en` and model (default will be downloaded at worker startup from Hugging Face's website)
* task `question-answering-fr` and local model `models/`

Run locally
-----------

If you have a local/docker-compose Zeebe running locally you can run/debug with:

```bash
python index.py
```

Run tests
---------

```bash
python -m unittest
```

Build with Docker
-----------------

```bash
docker build -t teode/question-answering-french-worker:v1.0.0 -f Dockerfile.fr .
```

Or download from the release section

Run with Docker
-----------------

You must have a local or a port-forwarded Zeebe gateway for the worker to connect then:

```bash
docker run --name zb-qa-fr-wkr zeebe-question-answering-french-worker
```

Usage
-----

Example BPMN with service task:

 ```xml
 <bpmn:serviceTask id="my-question-answering" name="My Question Answering">
   <bpmn:extensionElements>
     <zeebe:taskDefinition type="my-env-var-task-name" />
   </bpmn:extensionElements>
 </bpmn:serviceTask>
 ```

* the worker is registered for the type of your choice (set as an env var)
* required variables:
  * `question` - the question on context
  * `context` - the text to infer from
* jobs are completed with variables:
  * `answer` - the answer inferred from the text
  * `score` - the confidence (between 0 and 1) in the answer