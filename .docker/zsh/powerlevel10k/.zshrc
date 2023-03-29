export LANG='en_US.UTF-8'
export LANGUAGE='en_US:en'
export LC_ALL='en_US.UTF-8'
export TERM=xterm

##### Zsh/Oh-my-Zsh Configuration
export ZSH="/home/python/.oh-my-zsh"

ZSH_THEME="powerlevel10k/powerlevel10k"
plugins=(git git-flow fast-syntax-highlighting zsh-autosuggestions zsh-completions )


export TERM=xterm-256color
source $ZSH/oh-my-zsh.sh

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
