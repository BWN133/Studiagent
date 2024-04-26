GPT3 = "gpt-3.5-turbo-1106"
GPT4 = "gpt-4"
EVALUTAIONMODEL = GPT3 # tools eval difference model

SAMPLEQUESTION1 = "Mrs. Snyder used to spend 40 percent of her monthly income on rent and utilities. Her salary was recently increased by $600 so now her rent and utilities only amount to 25 percent of her monthly income. How much was her previous monthly income?"
SAMPLESOLUTION1 = ("Let her previous monthly income be p\n"
                   "The cost of her rent and utilities was 40 percent of p which is (40/100)*p = 2p/5\n"
                   "Her income was increased by $600 so it is now p+$600\n"
                   "The cost of her rent and utilities now amount to 25 percent of (p+$600) "
                   "which is (25/100)*(p+$600) = (p+$600)/4\nEquating both expressions for cost of rent and utilities: "
                   "2p/5 = (p+$600)/4\nMultiplying both sides of the equation by 20 gives 8p = 5p+$3000\nSubtracting 5p from both sides gives: "
                   "3p = $3000\nDividing both sides by 3 gives p = $1000")


