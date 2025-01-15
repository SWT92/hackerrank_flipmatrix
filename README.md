# Please see explanation.pptx for visual understanding of how the methold works.

This problem statement is part of my evaluation within 30minute, however I could not get it done within 30min. 

While tackling the problem statement for I was thinking of rubiks cube, and tried flipRow(matrix, rowNum) and flipCol(matrix, colNum).
However I cant think of a dynamic way to flip the row or column such that all the biggest number will be on the top left quadrant.

I visualise flipping the row and column and realise that some of the numbers are only possible at some area, however I do not have a clear picture of what is going on.
Eventually I used huggingface's Qwen/Qwen2.5-Coder-32B-Instruct to try to understand the logical thinking.
It did give me a good idea of how to approach the issue, however the answer seems to be far from the result of what I want, even though it passess the HackerRank test cases.

I didnt understand how the logic works, until I google image for "hackerrank flip matrix" and saw this post [a href="https://dev.to/dt_writes/hackerranks-flipping-the-matrix-problem-3f37"]link here[/a]
I drew out similar stuff as seen on explaination.pptx and started to work on coding it out as seen on method1.py

While accidentally i realise method2.py works too, which is interesting, because it only does vertical mirror comparison instead of vertical and hortizontal mirror comparison. 
