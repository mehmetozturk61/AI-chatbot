This code is to understand the effects of the `temperature`, `top_k`, and `max_length` parameters of the **GPT-2** language model. I used a parameter grid and tested the prompt with a total of 48 different combinations of these parameter values. This way, I could observe the change in one parameter by keeping the other two constant, and repeating this with different values. 

There are three different parameters I tested:
* **Temperature:** It affects the diversity of the output. When it is `0`, the model always picks the most likely word. As it increases, the probability of picking less likely but more diverse words goes up.
* **Top-k:** This limits the number of token options the model considers. For example, `top_k = 40` means the model samples from the top 40 most likely next tokens.
* **Max Length:** This is the maximum number of tokens to generate in the response.

I gave the generated sentences to ChatGPT and asked it rate them from 1 to 5 on six different metrics: **clarity**, **coherence**, **factual accuracy**, **fluency**, **conciseness**, and **originality**. Then, I analyzed how the results changed with variation in each parameter. I calculated the average scores and plotted linear regression lines to observe potential correlations between parameters and the evaluation results.

## Findings
* Increasing temperature from `0.2` to `1.2` significantly improved **clarity**, **coherence**, **fluency**, **conciseness**, and **originality**. However, **factual accuracy** slightly decreased at higher temperatures.  
Low temperature (`0.2`) often produced repetitive outputs like:
*"and it will be able to do things like read and write... read and write... read and write.."*
As themperature increased, repetition decreased and diversity improved. but high values, (like `1.2`) sometimes caused the output to become less meaningful or coherent.
So there is a trade-off between creativity and reliability.

* For `top_k`, there was no consistent trend as values increased from 10 to 100. Some combinations led to slightly more creative results, but others did not. It may be less influential than the temperature in this experiment. Additionally, 10 might be so great to limit it.

* Increasing `max_length` from 50 to 150 had a slight positive effect on **clarity**, **coherence**, **fluency**, and **originality**. However, the changes were minor, and the results could vary depending on the content. Since the increase was small, the findings are not conclusive