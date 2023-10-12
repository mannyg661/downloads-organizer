import shutil
import os


def file_manager(source_dir, destination_dir):
    videos = ('.mp4', '.avi', '.mov', '.mkv')
    audio = ('.wav', '.mp3', '.MP3')
    compressed = ('.zip', '.rar', '.archive')
    pictures = ('.jpg', '.jpeg', '.png', '.svg')
    code = ('.html', '.css', '.scss', '.sass', '.py')
    programs = ('.msi', '.exe')
    text = ".txt"
    file_names = os.listdir(source_dir)

    for file_name in file_names:
        if os.path.join(source_dir, file_name).endswith(tuple(audio)):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'audios'))

        if os.path.join(source_dir, file_name).endswith(tuple(videos)):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'videos'))

        if os.path.join(source_dir, file_name).endswith(tuple(compressed)):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'zip'))

        if os.path.join(source_dir, file_name).endswith('pdf'):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pdf'))

        if os.path.join(source_dir, file_name).endswith(tuple(code)):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'code'))

        if os.path.join(source_dir, file_name).endswith(tuple(pictures)):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'pictures'))

        if os.path.join(source_dir, file_name).endswith(tuple(text)):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'text'))

        if os.path.join(source_dir, file_name).endswith(tuple(programs)):
            shutil.move(os.path.join(source_dir, file_name), os.path.join(destination_dir, 'programs'))

    print('Your files have bene organized')


file_manager('C:\\Users\\naria\\Downloads', 'C:\\Users\\naria\\Downloads')
