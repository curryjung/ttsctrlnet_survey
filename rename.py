
import os

audio_dir = "/mnt/CINELINGO_BACKUP/jaeseok/anycode/video_survey/audio"


emochange_results_dir = os.path.join(audio_dir, "emochange_results")
emochange_ref_dir = os.path.join(audio_dir, "emochange_ref")


emochange_results_files = os.listdir(emochange_results_dir)
emochange_ref_files = os.listdir(emochange_ref_dir)


# for file in emochange_ref_files:
#     if file.endswith(".wav"):
#         print(file.split("_")[:3])
#         name = file.split("_")[:3]
#         name = "_".join(name)
#         print(name)
#         os.rename(os.path.join(emochange_ref_dir, file), os.path.join(emochange_ref_dir, name + ".wav"))


model_name_list = os.listdir(emochange_results_dir)

for model_name in model_name_list:
    if not model_name == "voicebox":
        continue
    for file in os.listdir(os.path.join(emochange_results_dir, model_name)):
        if file.endswith(".wav"):
            name = file.split("_")[:3]
            name = "_".join(name)
            os.rename(os.path.join(emochange_results_dir, model_name, file), os.path.join(emochange_results_dir, model_name, name + ".wav"))

# import pdb; pdb.set_trace()

