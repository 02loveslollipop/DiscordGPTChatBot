import discord
import yaml
from console import Console

class ConfLoader:
    def __init__(self):
    
        try:
            config_file = open('config.yml')
            print(Console.info("Using config.yml"))
        except FileNotFoundError:
            print(Console.warning("You don't have a config.yml file, using example_config.yml"))
            config_file = open('example_config.yml')
        finally:
            try:
                config = yaml.load(config_file, Loader=yaml.FullLoader)
                self.prefix = config['bot']['prefix']
                self.name = config['bot']['name']
                self.bot_token = config['bot']['token']
                self.b_ask_tts = config['bot']['use_ask_tts']
                self.timeout = config['bot']['time_out']
            
                if config['bot']['use_short_prefix']:
                    self.s_prefix = config['bot']['short_prefix']
                    self.b_s_prefix = True
                else: 
                    self.b_s_prefix = False
                    self.s_prefix = ''

                if config['bot']['use_copypasta']:
                    self.t_copypasta = config['text']['copypasta']
                    self.n_copypasta = len(self.t_copypasta)
                else: n_copypasta = 0
                
                if config['bot']['use_audio']:
                    self.join = config['command']['join']
                    self.leave = config['command']['leave']
                    self.ask_voice = config['command']['ask_voice']
                    self.join_error = config['text']['join_error']
                    self.join_success = config['text']['join_success']
                    self.leave_success = config['text']['leave_success']
                    self.leave_error = config['text']['leave_error']
                    self.b_use_audio = True
                    if config['TTS']['engine'] == "gcloud":
                        from text2speech import GoogleCloudTTS
                        self.tts = GoogleCloudTTS(config['TTS']['model'])
                    elif config['TTS']['engine'] == "gtts":
                        from text2speech import Gtts
                        self.tts = Gtts(config['TTS']['language'],config['TTS']['tld'])
                else:
                    self.b_use_audio = False
                    self.join = None
                    self.leave = None
                
                self.open_ai_token = config['open_ai']['token']
                self.model = config['open_ai']['model']
                self.role = config['open_ai']['role']
                self.temperature = config['open_ai']['temperature']
                self.help_answer = config['text']['help']
                self.hello_answer = config['text']['hello']
                self.version_answer = config['text']['version']
                self.reset_error = config['text']['reset_error']
                self.reset_success = config['text']['reset_success']
                self.role_changed = config['text']['role_changed']
                self.hhelp = config['command']['help']
                self.hello = config['command']['hello']
                self.copypasta = config['command']['copypasta']
                self.version = config['command']['version']
                self.ask = config['command']['ask']
                self.ask_tts = config['command']['ask_tts']
                self.reset = config['command']['reset']
                self.change_role = config['command']['change_role']
                if config['status']['use_status']:
                    self.use_status = True
                    if config['status']['use_help_command'] and "{help_command}" in config['status']['text']:
                        self.text = config['status']['text']
                        self.text = self.text.format(help_command=(self.prefix + '.' + self.hhelp))
                    else:
                        self.text = config['status']['text']
                    if config['status']['status_type'] == 'game':
                        self.status = discord.Game(name=self.text)
                    elif config['status']['status_type'] == 'streaming':
                        self.url = config['status']['streaming_url']
                        self.status = discord.Streaming(name=self.text,url=self.url)
                    elif config['status']['status_type'] == 'listening':
                        self.status = discord.Activity(type=discord.ActivityType.listening, name=(self.text))
                    elif config['status']['status_type'] == 'watching':
                        self.status = discord.Activity(type=discord.ActivityType.watching, name=self.text)
                    else:
                        print(Console.warning("Status configuration isn't right please check it, status will be disable"))
                        self.use_status = False
                else: self.use_status = False
            
            except KeyError as err:
                import traceback
                print(Console.error(str(type(err))))
                print(Console.error(str(err.args)))
                print(Console.error(str(traceback.format_exc())))
                print(Console.warning("The bot couldn't start because of a bad configuration in confg.yml, please check your confg.yml"))
                exit()

        self.l_prefix = len(self.prefix)
        self.l_s_prefix = len(self.s_prefix)
        self.l_helo = len(self.hello)
        self.l_copypasta = len(self.copypasta)
        self.l_version = len(self.version)
        self.l_ask = len(self.ask)
        self.l_ask_tts = len(self.ask_tts)
        self.l_reset = len(self.reset)
        self.l_change_role = len(self.change_role)
        self.l_join = len(self.join)
        self.l_leave = len(self.leave)
        self.l_ask_voice = len(self.ask_voice)
