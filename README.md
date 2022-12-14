# Toukei

## Overview

Python script that scans a Japanese text and gives statistics about the kanji :

<img src="https://user-images.githubusercontent.com/99618877/199957961-6f287f7f-a8b6-4672-ac20-a7d1a6b1eb71.png" width="600"/>

(Example: 『源氏物語』 Genji Monogatari)

## Fields

### General statistics

- 文字数: number of characters in the text
- 漢字数: number of kanji in the text
- 漢字割合: percentage of kanji in the text
- 唯一漢字: number of individual kanji
- 一回漢字: number of kanji only used once
- 平均文長: average sentence length

### Kyōiku kanji

- 第1学年: kanji taught in first grade (80 kanji)
- 第2学年: kanji taught in second grade (160 kanji)
- 第3学年: kanji taught in third grade (200 kanji)
- 第4学年: kanji taught in fourth grade (202 kanji)
- 第5学年: kanji taught in fifth grade (193 kanji)
- 第6学年: kanji taught in sixth grade (191 kanji)

### Kanji categories

- 教育漢字: kyōiku kanji (1026 kanji)
- 常用漢字: common use kanji (2136 kanji)
- 人名用漢字: kanji used in names (651 kanji)
- 表外字: other kanji
- 新字体: proportion of shinjitai kanji
- 旧字体: proportion of kyūjitai kanji

### JLPT Levels

- JLPT N5 (80 kanji)
- JLPT N4 (170 kanji)
- JLPT N3 (370 kanji)
- JLPT N2 (380 kanji)
- JLPT N1 (1136 kanji)
- JLPT++: kanji not present in the JLPT
