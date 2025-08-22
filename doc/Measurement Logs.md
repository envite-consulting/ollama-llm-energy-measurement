# Measurement Logs

This file contains informations connecting the repositories' version to the corresponding GMT runs

## Approach

- For each GMT run, a `git tag` should be specified. 
- This tag should then be referenced in the GMT runs' name. 
- All the information (name, repo, branch, `usage_scenario`-file) entered in the GMT run and its tag should be logged here

> Caveat: Currently, GMT only supports selecting git branches, not git tags. The reference to a tag is meant as a pointer for the user, not as a technical connection.

## Logs

> from newest to oldest.

---
### v1.1.2

**Description:** Same as v1.1/v1.1.1, but added Gemma 3 270M

#### General
**Repository**
```
https://github.com/envite-consulting/ollama-llm-energy-measurement
```
**Branch**
```
emailmeasurement
```
**Tag**
```
v1.1.2
```
#### Model-specific
**Measurement Name**
```
EMail Ollama Measurement Gemma 3 270M v1.1.2
```
**usage_scenario file**
```
usage_scenario_email_gemma3_270m.yml
```

---
### v1.1.1

**Description:** Same as v1.1 but fixed typo

#### General
**Repository**
```
https://github.com/envite-consulting/ollama-llm-energy-measurement
```
**Branch**
```
emailmeasurement
```
**Tag**
```
v1.1.1
```
#### Model-specific
**Measurement Name**
```
EMail Ollama Measurement Deepseek 1.5B v1.1.1
```
**usage_scenario file**
```
usage_scenario_email_deepseekr1_1_5b.yml
```

---
### v1.1
#### General
**Repository**
```
https://github.com/envite-consulting/ollama-llm-energy-measurement
```
**Branch**
```
emailmeasurement
```
**Tag**
```
v1.1
```
#### Model-specific
**Measurement Name**
```
EMail Ollama Measurement Deepseek 1.5B v1.1
```
**usage_scenario file**
```
usage_scenario_email_deepseekr1_1_5b.yml
```
---
**Measurement Name**
```
EMail Ollama Measurement Llama 3.2 3B v1.1
```
**usage_scenario file**
```
usage_scenario_email_llama32_3b.yml
```
---
**Measurement Name**
```
EMail Ollama Measurement Llama 3.2 1B v1.1
```
**usage_scenario file**
```
usage_scenario_email_llama32_1b.yml
```
---
**Measurement Name**
```
EMail Ollama Measurement Gemma 3 4b v1.1
```
**usage_scenario file**
```
usage_scenario_email_gemma3_4b.yml
```
---
**Measurement Name**
```
EMail Ollama Measurement Gemma3 1b v1.1
```
**usage_scenario file**
```
usage_scenario_email_gemma3_1b.yml
```