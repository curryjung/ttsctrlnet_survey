import os

# ref_audio_dir = "/mnt/CINELINGO_BACKUP/jaeseok/anycode/video_survey/audio/jvnv_ref"
# results_dir = "/mnt/CINELINGO_BACKUP/jaeseok/anycode/video_survey/audio/jvnv_results"
ref_audio_dir = "audio/jvnv_ref"
results_dir = "audio/jvnv_results"
models = ['elate', 'f5-tts', 'ours', 'voicebox', 'emoctrl', 'seamless']
models_subname = ["모델 A", "모델 B", "모델 C", "모델 D", "모델 E", "모델 F"]
dataset = 'part1' # jvnv
html_parts = []

# 시작 HTML
html_parts.append("""<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>TTS 감정 조절 평가</title>
  <style>
    body { font-family: sans-serif; padding: 20px; line-height: 1.6; max-width: 900px; margin: auto; }
    .section { border: 1px solid #ccc; padding: 20px; margin-bottom: 40px; border-radius: 10px; }
    .audio-block { margin: 10px 0; }
    fieldset { margin-bottom: 20px; }
    legend { font-weight: bold; margin-bottom: 5px; }
    label { margin-right: 15px; }
    .result-audio { margin-top: 30px; }
  </style>
</head>
<body>
<h1>TTS 감정 조절 설문</h1>
<form action="#" method="post">
""")

# 오디오 기준
ref_files = [f for f in os.listdir(ref_audio_dir) if f.endswith('.wav') or f.endswith('.mp3')]
print(ref_files)

for idx, ref_file in enumerate(sorted(ref_files)):
    ref_path = os.path.join(ref_audio_dir, ref_file)
    base_name = os.path.splitext(ref_file)[0]

    html_parts.append(f'<div class="section">\n<h2>참조 음성 {idx + 1}</h2>\n')
    html_parts.append(f'<audio controls src="{ref_path}"></audio>\n')

    for model in models:
        output_path = os.path.join(results_dir, model, ref_file)
        model_id = f"{idx+1}_{model.replace('-', '')}"
        model_subname = models_subname[models.index(model)]

        html_parts.append(f'<div class="result-audio">\n<h3>{model_subname} 결과</h3>\n')
        html_parts.append(f'<audio controls src="{output_path}"></audio>\n')

        for category, name in zip(
            ['목소리 유사도', '자연스러움', '감정 표현 유사 정도 & 감정 변화 유사 정도'],
            ['voice_similarity', 'naturalness', 'emotion_similarity']
        ):
            html_parts.append(f'<fieldset>\n<legend>{category}</legend>\n')
            for score in range(1, 6):
                html_parts.append(
                    f'<label><input type="radio" name="{name}_{model_id}_{dataset}" value="{score}">{score}점</label>\n'
                )
            html_parts.append('</fieldset>\n')

        html_parts.append('</div>\n')  # 결과 오디오 종료

    html_parts.append('</div>\n')  # 섹션 종료

# 끝 HTML
html_parts.append('<input type="submit" value="설문 제출">\n</form>\n</body>\n</html>')

# HTML 저장
with open("tts_survey.html", "w", encoding="utf-8") as f:
    f.write("".join(html_parts))

print("설문 HTML이 tts_survey.html 파일로 저장되었습니다.")