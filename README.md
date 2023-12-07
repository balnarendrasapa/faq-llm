# E-Commerce FAQ Chatbot using Parameter Efficient Fine Tuning with LoRA Technique

## Overview

This repository contains the code and resources for building an E-Commerce FAQ Chatbot using Parameter Efficient Fine Tuning with LoRA Technique. The project aims to develop a chatbot for an E-Commerce site by leveraging Large Language Models (LLMs) and adopting a fine-tuning approach using the Falcon-7B model. The fine-tuning is performed with Parameter Efficient Fine Tuning (PEFT) and the LoRA (Low-Rank Adaptation) Technique to enhance the model's performance.

## Authors

- **Bal Narendra Sapa** - University of New Haven - [Email](mailto:bsapa1@unh.newhaven.edu)
- **Ajay Kumar Jagu** - University of New Haven - [Email](mailto:ajagu1@unh.newhaven.edu)

## Table of Contents

1. [Introduction](#introduction)
2. [Objectives](#objectives)
3. [Related Work](#related-work)
4. [Dataset](#dataset)
5. [Methodology](#methodology)
6. [Results](#results)
7. [Conclusion](#conclusion)
8. [Acknowledgements](#acknowledgements)
9. [Deployment](#deployment)
10. [Code and Resources](#code-and-resources)
11. [References](#references)

## Introduction

In the fast-paced world of e-commerce, handling customer queries efficiently is crucial. This project introduces a chatbot solution leveraging advanced language models to automate responses to frequently asked questions. The fine-tuned model, Falcon-7B, is trained on a custom dataset extracted from Kaggle, addressing common user queries in the e-commerce domain.

## Objectives

1. **Efficient Customer Support:** Streamlining customer support by automating responses to frequently asked questions.
2. **Cost Savings through Automation:** Reducing operational costs by automating responses to routine inquiries.
3. **Enhanced Resource Allocation:** Optimizing human resources by automating responses to FAQs, allowing agents to focus on more complex issues.

## Related Work

The project builds upon pre-trained models, including OpenAI's GPT models and META's LLAMA models. It also explores existing chatbots like IBM Watson Assistant and Ada Healthcare Chatbot. The comparison between RAG (Retrieval Augmented Generation) and fine-tuned models is discussed.

## Dataset

The dataset, sourced from Kaggle, comprises 79 samples with questions and corresponding answers. The split includes 67 samples for training (85%) and 12 samples for testing (15%).

[Link to Dataset on Kaggle](https://www.kaggle.com/datasets/saadmakhdoom/ecommerce-faq-chatbot-dataset?select=Ecommerce_FAQ_Chatbot_dataset.json)

## Methodology

The methodology involves using the FALCON-7B model, fine-tuning with PEFT and LoRA Technique, and leveraging key libraries such as Transformers and Peft by Hugging Face. The process includes dataset preprocessing, LoRA adapters configuration, and model training.

## Results

The model demonstrates decreasing loss values across epochs, indicating positive training trends. The Bleu score, used for evaluation, showcases the model's proficiency in generating responses aligned with expected results.

## Conclusion

The project contributes to enhancing customer support in e-commerce through advanced language models. While the achieved results are promising, further experiments with larger datasets and continuous model refinement are recommended.

## Acknowledgements

Acknowledgments are extended to the developers of the FALCON-7B model, the Hugging Face community, Kaggle for hosting the dataset, and the faculty at the University of New Haven.

## Deployment

A Streamlit application has been developed for local use, requiring a GPU with at least 16 gigabytes of video RAM (vRAM) for optimal performance. the app in this repository. checkout in streamlit-app dir

## Code and Resources

- Fine-tuned Model on Hugging Face Model Hub: [Link to Hugging Face Model](https://huggingface.co/bnsapa/faq-llm)
- Kaggle Notebook for Walkthrough: [Link to Kaggle Notebook](https://www.kaggle.com/code/balnarendrasapa/fine-tuning-falcon-7b-with-faq-e-com-dataset)

Feel free to explore, experiment, and contribute to further improvements.

## References

1. [Language Models are Few-Shot Learners - Tom B. Brown et al (2020)](https://arxiv.org/abs/2005.14165)
2. [LLAMA 2: Open Foundation and Fine-Tuned Chat Models (2023)](https://arxiv.org/abs/2307.09288)
3. [Few-Shot Parameter-Efficient Fine-Tuning is Better and Cheaper than In-Context Learning - Haokun Liu et al (2022)](https://arxiv.org/abs/2205.05638)
4. [LoRA: Low-Rank Adaptation of Large Language Models - Edward J Hu et al (2021)](https://arxiv.org/abs/2106.09685)
5. [An overview of Bard: an early experiment with generative AI - James Manyika (2023)](https://ai.google/static/documents/google-about-bard.pdf)
6. [IBM Watson Assistant](https://www.ibm.com/products/watsonx-assistant)
7. [Hugging Face Blog on PEFT](https://huggingface.co/blog/peft)
