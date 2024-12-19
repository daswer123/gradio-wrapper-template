import gradio as gr

def create_input_media_ui(current_settings):
    ui_elements = {}

    def get_current_settings():
        return current_settings['youtube_quality'], current_settings['audio_format']
    
    with gr.Column():
        gr.Markdown("### Загрузите медиа")
        
        ui_elements['input_media'] = gr.File(
            label="Загрузите файл,Вы можете загрузить видео или аудио файл",
            file_types=["video", "audio"]
        )
        ui_elements["input_microphone"] = gr.Microphone(label="Ввод с микрофона",type='filepath')
        ui_elements["input_youtube_url"] = gr.Textbox(label="Введите ссылку на видео с YouTube")
        ui_elements["youtube_quality"] = gr.Dropdown(label="Качество видео",choices=["480p", "720p", "1080p"],value=get_current_settings()[0])
        ui_elements["audio_format"] = gr.Radio(label="Формат аудио",choices=["wav", "flac", "mp3"],value=get_current_settings()[1])

    
    return ui_elements