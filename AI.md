## Deep Learning 
### Deep Learning Basics
Deep learning is a subset of machine learning focused on neural networks with many layers.
#### What are neurons and layers?
Neurons and layers are the main parts of a neural network. A neural network consists of multiple neurons arranged in different layers. A neuron basically takes inputs from the previous layer. Its score is determined by the outputs of the neurons in the previous layer and weights of the connections. We apply weights to determine how important each input is for the output. We can think of bias as a threshold or offset that helps us classify the output. The output of a neuron may vary from negative infinitive to infinitive. However, we do not want such a wide range, so we normalize it between 0 and 1. 

Layers are a key part of a neural network. They help us solve the problem step-by-step. Each layer combines and processes some of the data, and at the end, it produces the output we want. Thus, multiple layers help the machine learn complex patterns, so it does not have to get the result directly from the raw data. Input layers are the data we give to the network, and output layers are the results we want at the end. Hidden layers are the in-between layers that helps us divide the problem into different parts.
#### How does training work conceptually?
Initially, we start with random weights and biases. We run the network on training data. Then, we compare the results with the desired outputs using a loss function. The goal is the minimize the difference. After comparing the results, the backpropagation step begins. Simply put, it checks the current layer and the previous layers, and makes adjustments to the weights and biases based on the error. We train over many samples so that model can understand different variations of the data. 
### Transformers
Transformers have revolutionized how machines understand language by processing all parts of a sentence at once.
#### Self-Attention
When a model reads a sentence like "**The cat sat on the mat**", it first separates the sentence into tokens, which are similar to words for us. Each token is then converted into a vector — a process called embedding. These vectors represent the meaning of tokens in a way that the model can understand.

Each vector can influence the other vectors depending on their relationship — for example an adjective can affect the meaning of a noun. This is important because we humans can naturally understand what a word like "*it*" refers to but, a model only sees a sequence of numbers. The model needs to find relationships between vectors to figure out things like what "*it*" refers to in a sentence. 

This process is called attention. It tells the model which tokens are more relevant to each other, helping it to understand the context and meaning more accurately. Note that this process does not occur in any particular order. It happens simultaneously. Therefore, it is a faster approach compared to traditional methods.
#### Positional Encoding
Since transformers do not process words in order, they need a way to understand the order of words — that is called positional encoding. Without it, there would be no difference between a sentence like "The cat in the tree" and "The tree in the cat". Positional encoding is a set of values that represents the position of each token in the sentence. These position values are added to the word embeddings before they go into the self-attention layers. This helps the model understand not just the word themselves, but also where they appear in the sentence. That is why positional encoding is essential in Transformers.
## Generative AI
### What is Generative AI?
Generative AI refers to models that can generate new content — such as text, images, music, or code — rather than just analyzing or classifying existing data.

Here are some use cases for different domains:
* Text
	* Email & essay writing
	* Language translation
	* Chatbots & support agents
* Image
	* Art and illustrations
	* Product mockups/design
	* Image upscaling/restoration
* Audio
	* Music generation
	* Text-to-speech synthesis
	* Voice cloning/dubbing
* Code
	* Code autocompletion
	* Code explanation/conversion
	* Unit test generation

### [Explore Hugging Face Model Hub](https://huggingface.co/models)
I searched for and briefly explored these models: `gpt2`, `gpt-neo`, `stable-diffusion-v1-5`, `llama-2-7b`, `bark`.
* **GPT-2:**  The model takes in text and generates text. It was trained on **WebText**, a dataset collected from publicly available web pages. There are four different model sizes: **117M**, **345M**, **762M**, and **1.5B** parameters. Developed by **OpenAI**, GPT-2 was one of the first large-scale autoregressive language models released openly.
* **GPT-Neo:** This model also takes in text and generates text. It was trained on **The Pile**, an open-source dataset containing diverse English text sources including books, Wikipedia, GitHub, and more. There are three variants: **125M**, **1.3B**, and **2.7B** parameters. GPT-Neo was developed by **EleutherAI** as an open alternative to GPT-3.
* **Stable Diffusion v1.5:** Th model takes in text and generates image. It was trained on **LAION-5B**, a large-scale dataset of image-text pairs scraped from the internet. The model size is approximately **900M** parameters. Developed by **Stability AI**, it uses a U-Net architecture with a latent diffusion approach.
* **Llama 2:** This model takes in text and generates text. It is trained on a combination of publicly available and licensed datasets, focusing on high-quality data sources. There are three sizes: **7B**, **13B**, and **70B** parameters. Developed by **Meta AI**, Llama 2 is designed for open access and efficient deployment.
* **Bark:** The model takes in text and generates audio. It was trained on text-audio pairs — includes diverse speech types, speaker types, and audio events. Not officially disclosed, but estimated model size is around **1-2B** parameters. It is developed by **SunoAI**.
## Adaptive AI and AI Agents
### Adaptive AI
Adaptive AI continuously learns and adopts itself to new conditions. Therefore, a better solution for the dynamic environment.
#### AI must adopt after deployment
Not everything in this world is fixed — life is dynamic. That's why traditional AI models are not enough for a rapidly changing world. The first thing comes to mind when talking about change is user preferences. People's opinion on some colors, cloths, or hobbies can shift over time. Adoptive AI is designed to learn from these changes and adjust its behavior accordingly.

But it is not just about user preferences. There are also other systems — like cybersecurity — that require adaptive AI. Threats constantly evolve, and a fixed, static model cannot keep up. Adoptive AI helps these systems stay current by continuously learning and responding to new situations.
#### Online Learning vs Batch Learning
Batch learning trains on large datasets all at once. It must be retrained from scratch whenever new data arrives. This approach has high computational cost and is less responsive to change. On the other hand, online learning processes data in small batches, often in real-time. It can continuously update itself without needing full retraining. Therefore, it is ideal for dynamic environments where data constantly changes.
