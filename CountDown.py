{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMQCfJpUgzkot0Qi0SC6xHr",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/luckycharmz1/CIS001_Intro_to-Comp.Sci./blob/main/CountDown.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "zUbNW0imiElT",
        "outputId": "2789ec8d-f2fc-41ba-9a58-f151182f9441"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a number: 5\n",
            "5\n",
            "4\n",
            "3\n",
            "2\n",
            "1\n",
            "0\n"
          ]
        }
      ],
      "source": [
        "number = int(input(\"Enter a number: \"))\n",
        "while number >= 0:\n",
        "  print(number)\n",
        "  number -=1"
      ]
    }
  ]
}