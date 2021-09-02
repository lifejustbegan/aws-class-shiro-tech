{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4903b421",
   "metadata": {},
   "outputs": [],
   "source": [
    "def pwchecker():\n",
    "\n",
    "    mypwrd = str(input(\"Please insert your password:\"))\n",
    "\n",
    "    if  mypwrd.isalpha() and len(mypwrd) >= 8 and len(mypwrd) <= 14:\n",
    "        \n",
    "            print(\"Great, You have successfully inserted your password\")\n",
    "    else:\n",
    "            print(\"Please insert a valid password\")\n",
    "            \n",
    "            print(\"\"\"Hint: password must be alphabet characters only and btwn 8 and 14 characters, both incusive\"\"\")\n",
    "            pwchecker()\n",
    "\n",
    "pwchecker()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
