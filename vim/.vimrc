" Author : Pranesh Srinivasan
" Last Modified:  Tuesday 15 October 2010

set nocompatible "We are using vim!

" Turn on syntax if possible."
if has("syntax")
	syntax on
endif

"============================================================================
" General Settings
"============================================================================
set hlsearch "Highlight searches
set incsearch "Offer incremental search
set gdefault " Enable global substitution by default
set showmode " Show mode - Insert, Visual, Normal
set mousemodel=popup

" Set line numbering
set number

" Next a few indentation options"
set autoindent
set smartindent
set expandtab

" set the size of a tab to 4 space"
set tabstop=4
" set the size of an indent
set shiftwidth=4

"Gui Options - Uncomment these, if you want a no distractions gvim.
" set guioptions-=T
" set guioptions-=m
" set guioptions-=r
" set guioptions-=l
" set guioptions-=R
" set guioptions-=L

set lazyredraw      " Rendering much faster during macros
set scrolloff=3     " Scrolling rules
set sidescrolloff=2 " Scrolling rules 

filetype indent plugin on

set history=500
"set backup

set showcmd
set showfulltag     " show full string when completing

set wildmenu "Status Line completion
" set wildignore+=*.o,*.obj,*~

if has("folding")
	set foldenable
endif

set matchpairs+=<:>

"============================================================================
" Colorschemes
"============================================================================
" Nice colorschemes
" colorscheme evening
" colorscheme desert
" colorscheme inkpot
" colorscheme tolerable
" colorscheme ps_color
" colorscheme professional
" colorscheme candycode
" colorscheme biogoo
if has("gui_running")
    colorscheme desert
    " Other nice gui color schemes
    "colorscheme desert
    "colorscheme autumnleaf
else
    colorscheme evening
endif

"============================================================================
" Status Line
"============================================================================
set laststatus=2
set statusline=%F%m%r%h%w\ [%{&ff}]\ [ft=%Y]\ [%04ly,%04vx]\ [%Ll]
" hex status line[x\%02.2B]\ 
" ascii status line  [\%03.3b]\ 

set ruler "set ruler if possible

" Filetype plugins"
if has("eval")
    filetype on
    filetype plugin on
    filetype indent on
endif



"============================================================================
" Mappings
"============================================================================
let mapleader = "\\"

"Indenting using par
vmap <M-q> !par -jw60<CR>   

" A mapping to go down more lines quickly
" Or move around faster
nmap <M-j>  3j
nmap <M-k>  3k
nmap <M-h>  3h
nmap <M-l>  3l

" For moving around split windows
noremap <s-down>        <c-w>j
noremap <s-up>          <c-w>k
noremap <s-left>        <c-w>h
noremap <s-right>       <c-w>l

" Brings up prev tab excluding mini buf
nmap <M-Left> 	        :bp<CR>      
"Bring up next tab excluding mini buf
nmap <M-Right> 	        :bn<CR>      
nmap <M-Up>             :bfirst<CR>
nmap <M-Down>           :blast<CR>

noremap <F2>            :TlistToggle<CR>
