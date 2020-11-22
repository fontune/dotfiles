set nocompatible              " be iMproved, required
filetype off                  " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'

" USER PLUGINS

" Dracula Color Scheme
Plugin 'dracula/vim',{'name':'dracula'}
" ctrlp Fuzzy File Finder
Plugin 'ctrlpvim/ctrlp.vim'
" Goyo
Plugin 'junegunn/goyo.vim'
" Lightline status bar
Plugin 'itchyny/lightline.vim'
" TComment (Use gc)
Plugin 'tomtom/tcomment_vim'
" Goyo Colorscheme
Plugin 'reedes/vim-colors-pencil'
Plugin 'easymotion/vim-easymotion'
Plugin 'vim-gitgutter'
Plugin 'nathanaelkane/vim-indent-guides'
Plugin 'dhruvasagar/vim-table-mode'
Plugin 'Valloric/YouCompleteMe'

" All of your Plugins must be added before the following line
call vundle#end()            " required
filetype plugin indent on    " required
" To ignore plugin indent changes, instead use:
"filetype plugin on
"
" Brief help
" :PluginList       - lists configured plugins
" :PluginInstall    - installs plugins; append `!` to update or just :PluginUpdate
" :PluginSearch foo - searches for foo; append `!` to refresh local cache
" :PluginClean      - confirms removal of unused plugins; append `!` to auto-approve removal
"
" see :h vundle for more details or wiki for FAQ
" Put your non-Plugin stuff after this line

syntax on
set number
set tabstop=4
set softtabstop=4 " tabstop when in insert mode
set expandtab	" tabs are spaces
set showcmd
set cursorline
filetype indent on
set wildmenu
set lazyredraw
set showmatch " Highlight matching brackets
set incsearch " Search as characters are entered
set hlsearch " Highlight search matches


colorscheme dracula
highlight Normal ctermbg=NONE
highlight nonText ctermbg=NONE

let g:table_mode_corner="|"

let g:gitgutter_enabled = 1

let g:indent_guides_guide_size = 1
let g:indent_guides_color_change_percent = 3
let g:indent_guides_enable_on_vim_startup = 1

function! s:goyo_enter()
    colorscheme pencil
endfunction

function! s:goyo_leave()
    colorscheme dracula
endfunction

autocmd! User GoyoEnter nested call <SID>goyo_enter()
autocmd! User GoyoLeave nested call <SID>goyo_leave()

" Hybrid relative line numbers
set number relativenumber
