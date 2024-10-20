The next step is to make sure that  $\mathrm{TeV}$   has been installed on both com- puters. The remote  $\mathrm{TeV}$   installation will mainly be used in order to detect those plug-ins that can be used on the remote computer.  

When everything has been set up in this way, select  Insert  $\blacktriangleright$    Session  $\blacktriangleright$    Remote  in order to open the remote plug-in selector. Add the name of the remote server by typing its name or IP address and clicking on  Add . After a small pause, the remote server should appear in the list together with the remote plug-ins that are supported. You may now simply select the plug-in you want to use from the list. Notice that remote plug-ins may take a few seconds in order to boot.  

Servers that have been added to the list of remote plug-in servers will be remembered the next time you start TEX . You may use the buttons  Remove MACS and  Update  in order to remove a server from the list and to update the list of supported remote plug-ins.  
# Chapter 12 Get it your way  

# 12.1 Creating macros  

# 12.1.1 Hello Nebuchadnezzar  

We have encountered an avalanche of markup elements throughout this book. Why add your own ones on top of the existing? One possible reason is that you may wish to save time by introducing abbreviations for lengthy names or notations. Let us see how to do this by deﬁning your own  macros .  

Assume that we need the name of a king for our new novel and that Neb- uchadnezzar seems to be the perfect candidate. Then it is natural to introduce a new macro  king  as an abbreviation for Nebuchadnezzar. The easiest way to do this is to open the “macro deﬁnition widget” using  Tools  $\blacktriangleright$    Macros  $\blacktriangleright$    New macro . At the place of  enter-name , you may enter the name of your macro: “king”.   The corresponding body “Nebuchadnezzar” can be typed below the  $:=$  sign. When done (see Figure 12.1), simply click on  Ok . Now that your macro has been deﬁned, you can use it as many times as you wish by typing  \ k i n g  ↩ :  

Hello Nebuchadnezzar! Nebuchadnezzar: my beloved leader. Bye, bye, Nebuchadnezzar.  

One big advantage of using macros for abbreviations and special notations is that it suﬃces to modify the macro deﬁnitions whenever you change your mind: by positioning your cursor right after one of the  king  tags, you can edit the corresponding macro using  Focus  $\blacktriangleright$    Preferences  $\blacktriangleright$    Edit macro . Just change the body of the macro to “Arikesari Maravarman Nindraseer Nedumaaran”, if this is your new hero, and all Nebuchadnezzars will mutate accordingly.  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/c68ac80b2dc429f52b2216d52bf551e9a5d33b4e67bd270a57b01a41a5eb1220.jpg)  
Figure 12.1.  The widget for macro deﬁnitions.  
![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/4783be441e55754b9875ffa1540784224149822690cc8aee736796eacdb6d4e2.jpg)  
Figure 12.2.  Example of a matrix deﬁnition with arguments.  

# 12.1.2 Adding arguments  

As our next example, assume that we wish to deﬁne a macro  diag  that pro- duces a diagonal matrix  

$$
{\left(\begin{array}{l l l}{x_{1}}&{}&{}\\ {}&{\cdot}&{}\\ {}&{\cdot}&{}\\ {}&{}&{x_{n}}\end{array}\right)},
$$  

with the additional constraint that the symbols  $x$   and  $n$   can be changed each time the macro is used.  

After entering the name of the macro as in the previous example, you may use the  $\underline{{\mathfrak{x}}}_{\rightarrow}$  shortcut in order to insert additional macro arguments, say  $X$   and    $\boldsymbol{n}$  . When entering the body of the macro, these arguments can be used inside the body by typing  $\underline{{\lambda}}|\underline{{\mathbf{x}}}|\underline{{\mathbf{e}}}$  and  $\triangle\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\!\$  . The resulting macro deﬁnition should look like Figure 12.2. When applying the macro using  \ d i a g  ↩ , an empty and editable slot is provided for each argument. Notice that only the ﬁrst top-left occurrence of the parameter  $X$   can be edited, although the second one at the bottom-right will be updated accordingly during modiﬁcations.  

The widget for macro editing is mainly intended for quick definitions of simple macros. In particular, you may miss the menus and the toolbars of the usual editor. Nevertheless, most of the usual keyboard shortcuts do work, as well as the contextual menus that appear when pressing the right mouse button (if your mouse has a single button, then you should hold the control key  $\trianglelefteq$  while pressing that button). Whenever some keyboard shortcuts are preempted by the operating system, we also recall from section 2.3.5 that you may emulate the modiﬁer keys  ⌃ ,  ⌥ , and  ⌘ using  ⎋ . For instance,  $\underline{{\mathfrak{x}}}_{\rightarrow}$  is equivalent to  $\left.\S\right\vert\left.\S\right\vert\rightarrow\right]$  .  

You may have noticed that we used the  $\Delta$  key both for applying the  diag  macro and for inserting the macro arguments  $X$   and  $\boldsymbol{\eta}$  . The behavior of the  $\Delta$  key is context-dependent indeed. Inside the deﬁnition of a macro with arguments  $X$  and    $n_{.}$  , typing  $\triangle|\underline{{\boldsymbol{\bf x}}}|\underline{{\boldsymbol{\bf\epsilon}}}|$  will lead to the insertion of the macro argument  $X$  . In a context where the  diag  macro is deﬁned,  $\mathrm{TeV}$   will automatically apply this macro when typing  \ d i a g  ↩ . Notice that macro arguments are indicated  
![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/ce908a64abfddb8ea8afe4864ee1bb649c7af0e5556bd333d5c1ba1e367700cb.jpg)  
Figure 12.3.  Browsing the list of all macros using the macros editor.  

using a brown color, whereas tags are displayed in blue.  

Another technique that is useful for the deﬁnition of macros goes as follows. First design the prototype macro application in an ordinary   $\mathrm{TeV}$   window. That would simply be the diagonal matrix (12.1) for our example. Now copy this matrix and paste it inside the macro body when deﬁning the  diag  macro. Finally replace the variables  $x$   and    $n$   by the macro arguments  $X$   and  $\boldsymbol{n}$   that were entered using  $\Delta|{\underline{{\mathbf{x}}}}|{\underline{{\mathbf{e}}}}|$  and  $\triangle|\mathsf{n}|\bumpeq$  . This copy-and-paste technique will turn out to be even more powerful when editing style ﬁles, as described later in this chapter.  

# 12.1.3 Customizing an existing macro  

Whenever your cursor is inside or just after a markup element, you may cus- tomize the corresponding macro definition using  Focus  $\blacktriangleright$    Preferences  $\blacktriangleright$    Edit macro  or  $\mathscr{s}$    Edit macro . For example, assume that we entered the acronym GNU or L ASER  (using  \ a c r o n y m  ↩ or  Insert  $\blacktriangleright$    Content tag  $\blacktriangleright$    Acronym ). If you wish to change the default rendering (a small capitals font), you can cus- tomize the corresponding  acronym  macro by positioning your cursor inside the text GNU or L ASER  and opening the macro editor with  $\mathscr{s}$    Edit macro .  

In certain cases, it may also be handy to browse the list of all existing macros that are active in your current style. This can be done by opening the macros editor via  Tools    Macros    Edit macros : see Figure 12.3. You may find the  acronym macro in the list at the left-hand side, possibly after typing the ﬁrst few char- acters of the  Macro name . A short description of the macro is displayed in the Documentation  area, whenever available. The macro can be edited as usual in the  Macro deﬁnition  area.  
In Figure 12.3, we selected “ Source  mode” for editing the body of the macro, as indicated by the pull-down menu at the bottom-left of the window. This mode is usually most convenient for editing complex macros, whereas the default text mode tends to be more suitable for simple, visually oriented macros. We also notice that the macro editor shows macro deﬁnitions in an abridged manner: inside style ﬁles and packages the deﬁnition from Figure 12.3 would read  

# h assign j acronym jh macro j body jh with j font-shape j small-caps j body iii  

Before we explain the presentation and syntax of source code in full detail, let us ﬁrst analyze the customization of an existing macro on a more complex example.  

# 12.1.4 Anatomy of a macro  

The rendering of certain markup elements like  acronym  is quite straightfor- ward. Many macros are far more complex and may recursively depend on other macros.  

Assume for example that we wish to customize the  proof  □  environment using  ■ the macros editor and replace the “end-of-proof” symbol by . The internal structure of the  proof  is exposed by selecting  Source  instead of  Text  in the left bottom menu of the macros editor. For most styles, the source code is as fol- lows:  

h assign j proof j h macro j body j h render-proof jh proof-text ij body iii  

The preﬁx “render-” is used for submacros that speciﬁcally control the graph- ical layout. In this case, the arguments of  render-proof  are the (potentially translated) text “Proof” and the actual proof body. This additional level of indirection allows for the speciﬁcation of alternative proof texts:  

Continued proof of the master theorem. applying the master lemma.  We now conclude by □  

When customizing a macro, it is important to ﬁrst understand its structure and the intent of the other macros on which it relies. In many cases, you really want to customize one or more of these other macros. In our example, this leads us to examine the source code of the  render-proof  macro, which is given by  
The  surround  primitive provides a way to decorate large blocks of text (so- called “block markup”) at the left and at the right. In this case, the proof text is decorated with the end-of-proof symbol  □ , which is produced using the macro qed . The symbol is preceded by a “horizontal tab” that ﬂushes it to the right  ■ margin. It now suﬃces to change the deﬁnition of the  qed  macro to . The above proof then reads:  

Continued proof of the master theorem. applying the master lemma.  We now conclude by ■  

At this point, we succeeded in replacing the  □ symbol by  ■ , but let us push our explorations a bit farther. The  render-remark  macro is another even more central rendering macro, which is also used for remarks, notes, examples, etc. Its source code is as follows:  

h assign j render-remark j h macro j which j body j h render-enunciation jh remark-name j which h remark-sep iij body iii  

As you can see here,  render-remark  depends on its turn on a yet more central macro  render-enunciation , which is also used for theorems and exercises. This additional level of indirection is due to the fact that the bodies of major the- orem-like enunciations are usually emphasized, whereas proofs, remarks, and other less prominent enunciations do not the change the font of the main body. Examination of the deﬁnition of  render-remark  also reveals the possibility to specify an alternative rendering for the names of remarks (e.g. R EMARK  2.3) and the separator between this name and the corresponding body (usually a dot). Further investigations lead us to the source code of  render-enunciation :  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/43720e4438d23cba7c85c1f774de76345a4428f458972d322f4c454e8841bb55.jpg)  

We have now reached the explicit graphical layout macro  padded\*  that is used to add vertical whitespace before and after the enunciation.  

# assign j padded\*  

h padded-normal j large-padding-above j large-padding-below j body iii  

The precise amount of spacing is controlled by the style parameters  large- padding-above  and  large-padding-below . For all macros that depend on  padded\* , this leads to entries  Focus  $\blacktriangleright$  Preferences  $\blacktriangleright$  Large padding above  and  Large padding below  in the  Style parameters  group. If your cursor is inside a proof, then  
![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/f7afdb81883ad1e1bba39eeec6404a1b495422bed9436fb7154e18bba104850d.jpg)  
large-padding-above large-padding-below padded-normal  

you may change these style parameters. The  padded-normal  macro is deﬁned directly in terms of typesetting primitives that cannot be further customized:  

h assign j padded-normal j h macro j before j after j body j h surround jh vspace\* j before ih no-indent ijh htab j 0fn j ﬁrst ih vspace j after ij body iii  

Figure 12.4 summarizes the recursive dependencies of the  proof  macro. Once again: before customizing an existing macro deﬁned by the selected style, it is recommended to investigate its dependency tree and carefully identify those submacros that control the behavior that you wish to change.  

# 12.2 Pilgrimage to the source  

In the previous section, we have seen that it can be useful to select the “source code” rendering when editing macros. You may actually select this rendering style for any  $\mathrm{TeV}$   document using  ⌘⌥ s  or  Document  $\blacktriangleright$    Source  $\blacktriangleright$    Edit source tree , and for any selected portion of text using  ⌘ -  . For certain documents, this gives a better grip on their full structure and in particular reveals any hidden information such as folded content.  

However, contrary to  $\mathrm{LiTeX}$   and H TML  (among others), the preferred repre- sentation of  $\mathrm{TeV}$   documents is  not  based on ASCII texts. This makes the concept of “source code” somewhat ill-deﬁned for  $\mathrm{TEPX}_{\mathrm{MACS}}$   documents. As we will explain in this section, the best mental representation of a  $\mathrm{TeV}\mathrm{X}_{\mathrm{MACS}}$  document is to regard it as an abstract tree. There are many ways to render such trees on a screen, some of which are closer to the printed end-result, and some of which expose more of the hidden internal structure.  
# 12.2.1 Documents as trees  

From a more conceptual perspective, TEX MACS  systematically regards docu- ments as  trees . Consider for example the formula  

$$
{\frac{1}{x^{2}+y^{2}}}.
$$  

TEX  internally represents this formula by a tree 12.1 MACS  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/64ea4e6b91a27bf9cc9aac938e46383796cd0815bc5dd0a6c7a1278b9a9a09f8.jpg)  

The nodes of the tree are labeled by markup elements (internal primitives or user-deﬁned macros) and the leaves of the tree are ordinary text strings.  

Pursuing our conceptual perspective, one should distinguish between the abstract document tree and its graphical rendering. In particular, (12.3) is just an attempt to represent such a tree in a graphically pleasing way. The default rendering (12.2) is another representation and the “source code” rendering is yet another possible representation:  

$$
\langle\mathsf{f r a c}|1|\mathsf{x}\langle\mathsf{r s u p}|2\rangle+\mathsf{y}\langle\mathsf{r s u p}|2\rangle\rangle
$$  

The main virtue of “source code” with respect to other renderings is that it aims to make the full structure as transparent as possible. But even though TEX MACS proposes a default “source code” rendering, there is no intrinsic reason to prefer any particular such rendering over another one. For instance, scheme expressions provide an alternative that only involves plain ASCII text:  

We will come back to this representation in chapter 14, since it is particularly useful when using S CHEME  as an extension language for  $\mathrm{TeV}$  .  

# 12.2.2 Selecting your preferred presentation of source code  

The “source code” rendering of document trees can actually be customized via  Document  $\blacktriangleright$    Source  $\blacktriangleright$    Preferences . We invite you to play around with the diﬀerent possibilities in a document of your own (after enabling  Document    Source  $\blacktriangleright$    Source tree ).  
![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/6cc48e6ce3dc585b1c08c203eb1d729b466e982913462231e5a3cbebdfc267a1.jpg)  
Figure 12.5.  Diﬀerent styles for rendering the same source tree.  

First of all, you may choose your preferred “ Main presentation style ” among “angular”, “scheme”, “functional”, and   $\mathrm{"Z"}$  , as illustrated in the Figure 12.5.  

Secondly, you may wish to reserve a special treatment for certain tags, such as the formatting tags  concat  and  document  for horizontal and vertical concate- nation. In the menu  Tags with a special rendering  you may specify to which extent you want to treat such tags in a special way:  

Raw.  No tags receive a special treatment.  

Format.  All tags are rendered as source code, except for the formatting tags concat  and  document . Normal.  In addition to the formatting tags, a few other tags like  compound , value , and  arg  are rendered in a succinct way. Maximal.  At the moment, this option is not yet implemented. The inten- tion is to allow you to write your own customizations and to allow for a special rendering of basic mathematical operations such as  plus .  

These diﬀerent options are illustrated in Figure 12.6.  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/2c48a06af57b38368e42c37337668b59e353ffc56279a62bd77000df53d0e9cf.jpg)  
Figure 12.6.  Diﬀerent ways to render special tags.  
![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/654f1c3ba0125641f50469dbf669e3750f7f5d096ee6bc0096c2c907c5a73167.jpg)  
Figure 12.7.  Diﬀerent levels of compactiﬁcation.  

Another thing that can be controlled by the user is whether the presentation of tags should be compact or stretched out across several lines. In general, so- called  inline tags  are more readable when represented in a compact way. Inline tags are used for small pieces of content in the middle of a paragraph, such as a reference or an inline formula. On the other hand,  block tags  are used for longer pieces of content that may span over several paragraphs, such as proofs or item lists. In source code rendering, they typically look better when they are stretched out over several lines. Note that certain tags (like  em  for emphasized text) can be used both as inline and as block tags.  

The  Compactiﬁcation  menu proposes several levels of compactiﬁcation: None.  The tags are all stretched out across several lines. Inline.  All non-inline tags are stretched out across several lines.  

Normal.  All inline arguments at the start of the tag are represented in a compact way. As soon as we encounter a block argument, the remainder of the arguments are stretched out across several lines.  

Inline arguments.  All inline arguments are represented in a compact way and only block tags are stretched out across several lines.  

All.  All source code is represented in a compact way.  

The visual effect of the different levels of compact if i cation is illustrated in Figure 12.7.  

Finally, the  Closing style  menu allows you to specify the way closing tags should be rendered when the tag is stretched out across several lines. The rendering can either be minimalistic, compact, long, or recall the matching opening tag. The diﬀerent options are illustrated in Figure 12.8.  
![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/148d9186132cbb87aff8fc6076f180853d7ba881c8b6867b17e2987fcb2fef5e.jpg)  
Figure 12.8.  Diﬀerent ways to render closing tags.  

# 12.2.3 Data or program?  

When designing your macros, you will quickly ﬁnd out that  $\mathrm{TEPX}_{\mathrm{MACS}}$   macros have a dual character. Simple macros such as an abbreviation or a notation for diagonal matrices are usually visual in nature and best edited in the same way as ordinary text. More complex macros behave more like programs with local variables and subprograms. The source code representation tends to be more convenient for editing such macros. The borderline between textual data and macro programming is blurry: sometimes both aspects can be found in the same macro deﬁnition.  

$\mathrm{TeV}$   fully acknowledges this data-or-program duality and provides a few mechanisms to locally switch between normal and source style rendering. One typical use case is to quickly examine (and possibly modify) the “source code” of a small portion of text. For example, assume that we wish to study the markup that was used in order to produce “brown” and “jumps” in the frag- ment  

The quick  brown  fox  jumps  over the lazy dog.  

Then it suﬃces to select “brown fox jumps” and press  ⌘ -  (when activating the source tool using  Tools  $\blacktriangleright$    Source macros tool , you may also use  Source    Activation  $\blacktriangleright$    Deactivate ):  

The quick  h with j color j brown j brown i  fox  h move j jumps j j 0.5ex i over the lazy dog.  

This technique inserts an additional (invisible)  inactive\*  tag around the selec- tion. You have to remove this tag in order to switch back to the original presen- tation, e.g. by placing your cursor after the  $"\mathbf{\Phi}_{\mathbf{X}}"$   in “fox” and pressing  $\simeq$  . Recall that the source code for the entire document can be edited using  Document    Source  $\blacktriangleright$    Edit source tree .  
Conversely, when editing a macro deﬁnition in source mode, you may prefer the usual non-source rendering for the more graphical portions of text. Con- sider for instance the deﬁnition  

h assign j new-icon jh macro jh icon j tm_new_x4.png iii  

You may prefer the following presentation that was obtained by selecting  h icon j tm_new_x4.png i  and pressing  $\ {\frac{\ {\mathfrak{s e}}+{\big]}}{}}$  :  

assign new-icon macro  

A more complex example is the following:  

h assign j diag jh macro j var j dim j   var 𝟎 1 ⋅ ⋅ ⋅ var 𝟎 dim ii  

Here we activated the usual rendering for the matrix using  $\ {\mathfrak{s e}}_{+}$   , but switched back to source code rendering for the arguments  var  and  dim  using  ⌘ -  .  

# 12.2.4 The ASCII religion  

Let us brieﬂy discuss one aspect of source code that may not be of direct prac- tical interest, but which may give you some insight into the design philosophy behind   $\mathrm{TeV}$  .  

Programmers are accustomed to the use of ASCII as their privileged represen- tation of source code. Over decades, many tools have been developed in order to make ASCII-style programming highly eﬃcient. However, it is not so clear that a line of  $C++$   code such as  

$$
\mathsf{P\ =\ 23*p o w(x,3)*p o w(y,2)*z\ +\ 17*x*p o w(z,4)}
$$  

is easier to read than  

$$
P\!=\!23\,x^{3}y^{2}z+17\,x\,z^{4}
$$  

Similarly, some masochism is required to prefer  $\mathrm{LiTa}$   code  

$$
\begin{array}{r l}&{\mathtt{M}\ =\ \backslash\mathtt{l e f t}\left(\ \backslash\mathtt{b e g i n\{a r r a y\}\{c c c\}}\right.}\\ &{\left.\ 1\ \&\ \ \backslash\mathtt{a l p h a\_\{1,2\}\ \&\ \backslash a l p h a\_\{1,3\}\backslash\backslash}\right.}\\ &{\left.\ 0\ \ \&\ \ 1\ \ \&\ \ \backslash\mathtt{a l p h a\_\{2,3\}\backslash\backslash}\right.}\\ &{\left.\ 0\ \ \&\ \ 0\ \ \&\ \ 1\right.}\\ &{\left.\ \backslash\mathtt{e n d\{a r r a y\}\ \backslash r i g h t}\right)}\end{array}
$$  

over  

$$
M\!=\!\left(\!\begin{array}{c c c}{{1}}&{{\!\alpha_{1,2}}}&{{\!\alpha_{1,3}}}\\ {{0}}&{{1}}&{{\!\alpha_{2,3}}}\\ {{0}}&{{0}}&{{1}}\end{array}\!\right)
$$  
With an appropriate editor like   $\mathrm{TeV},$   we do not only claim that (12.5) and (12.7) can be entered faster than (12.4) and (12.6): we may also regard them as a better way to represent “source code”.  

In fact, we regard it as an interesting challenge to develop a “source code editor” that is at least as eﬃcient as traditional ASCII-based editors, but that allows for visually more attractive and readable presentations. The main advantage of existing editors is that the user is not constrained by the structure of a program. For instance, the following piece of code was made more readable through the manual insertion of spaces at appropriate places:  

# if  (cond) hop =  2 ; else holala=  3 ;  

However, the precise formatting policy does not appear in the document, so manual intervention will be necessary if the variable  cond  is renamed  c , or if the variable  holala  is renamed  hola .  

$\mathrm{TeV}$   is not really intended to be a program editor yet, so no tools are pro- vided for dealing with the above example in an automatic way. Nevertheless, the discussion applies in a lesser extent to the source code mode in   $\mathrm{TeV}\mathrm{X}_{\mathrm{MACS}}$  . New users may feel somewhat constrained by the document structure and dis- oriented by the fact that ASCII-style editing habits not always apply. These disadvantages are still felt by more experienced users, but compensated by the beneﬁts of the structured editing facilities. Nevertheless, it remains a challenge to make it even easier and more natural to edit source code.  

# 12.3 Grouping your macros together  

# 12.3.1 Preambles  

The macro editor is an eﬃcient tool for the deﬁnition of simple notations and for basic customizations of existing macros. The resulting macro (re-)deﬁn- itions are automatically stored in the  preamble  of your document. More experi- enced   $\mathrm{TeV}$   users often do not use the macro editor and prefer to directly edit the preamble using  ⌘⌥ p  or  Document  $\blacktriangleright$    Part      Show preamble . This has the advantage that you see all macro deﬁnitions at once. By putting them in a suitable order, you may also enhance their readability.  

Preambles are edited much in the same way as ordinary documents, except that you are in source mode. Copying and pasting in particular continues to work as usual. This is a powerful technique for the deﬁnition of complex macros: ﬁrst design a prototype macro application in an ordinary document, next copy and paste it into the body of your macro deﬁnition in the preamble, and ﬁnally perform the appropriate replacements of text by macro arguments.  
Besides macros, you may also edit environment variables using the macro editor. Examples of environment variables are the page size, the left margin, the text color, or the number of the current subsection. Some of these environ- ment variables can also be modiﬁed more directly using the  Document  menu. For example, the main text color for the document can be selected using  Doc- ument      Colors  $\blacktriangleright$    Foreground .  

Just like the  \  key allows you to apply a macro whenever it is deﬁned (see section 12.1.2), you may use it in order to obtain the value of any available envi- ronment variable. For example,  \ c o l o r  ↩ yields the value of the current text color. Inside source code, TEX MACS  uses a green color for such environ- ment variables, as in  color .  

# 12.3.2 Style packages  

The preamble contains style customizations that apply to one individual doc- ument. If you are particularly pleased with some of your customizations, then you may wish to bundle them in a  style package  that can be reused in other documents. One eﬃcient way to start a new style package is  Tools  $\blacktriangleright$    Macros    Extract style package : this collects all existing customizations in your current document (both macros and environment variables) and puts them into a new style package.  

Style packages are similar to usual   $\mathrm{TeV}$   documents, except that you edit them in source mode, just like preambles. When saving them to disk, you should also use the  .ts  extension instead of  .tm . The native TEX MACS style packages are stored in the directory  $\Updownarrow$  TEXMACS_PATH/packages , where  $\Updownarrow$  TEXMACS_PATH  points to the directory where you installed T E X MACS . You must put your own style packages in the same directory as the files that use them or in the directory  $\Updownarrow$  TEX MACS HOME PATH/packages , where  $\Updownarrow$  TEX MACS HOME PATH points to  \~/.TeXmacs  on U NIX  systems and to  C:\Documents and settings\ user_name \Application Data\TeXmacs  on W INDOWS . After saving your style package in this way, you may apply it to any of your TEX MACS ﬁles using  Document  $\blacktriangleright$    Style  $\blacktriangleright$    Add package  $\blacktriangleright$    Add other package .  

Style ﬁles  are a variant of style packages. Style ﬁles control the main document style, whereas style packages contain customizations that can be combined with other style ﬁles or packages. Style ﬁles must be complete in the sense that all major markup elements (such as  section ,  theorem ,  equation ,  bibliog- raphy ,  strong , etc.) should be deﬁned. Style packages typically contain extra personal notations or customizations of existing markup elements.  

The complete style of your current document can be extracted using  Tools    Macros      Extract style ﬁle . When saving style ﬁles to disk, you should again use the  .ts  extension. Native style ﬁles are stored in    $\Updownarrow$  TEXMACS_PATH/styles . You should put your own style ﬁles in    $\Updownarrow$  TEXMACS_HOME_PATH/styles  or in the same directory as the ﬁles that use them. The main style is selected using Document  $\blacktriangleright$    Style  and user-deﬁned styles are automatically listed there.  
# 12.4 The style-sheet language  

So far, we have discussed how to introduce new notations and how to produce simple customizations of existing macros. For the design of more complex macros,  $\mathrm{TeV}$   provides a special  style-sheet language . This language consists of a set of special primitives that allow you to locally modify an environment variable, choose between several renderings, perform length computations, etc. In this section, we give an introduction to some of the most important primitives. A full exposition is beyond the scope of this book; for more details, we refer to the reference guide that is found in  Help  $\blacktriangleright$  Reference guide .  

Throughout this section, we assume the editor to be in “source mode”, so that a top-level  Source  menu should be available.  

# 12.4.1 Assignments  

All user-deﬁned TEX MACS  macros and style variables are stored in the “current typesetting environment”. This environment associates tree values to string variables. Variables whose values are macros correspond to new primitives. The others are ordinary environment variables. The primitives for operating on the environment are available from  Source  $\blacktriangleright$    Deﬁne .  

You may permanently change the value of an environment variable using the assign  primitive, as in the example  

h assign j hi jh macro j Hi there! ii  

You may also locally change the values of one or several environment vari- ables using the  with  primitive:  

h with j font-series j bold j color j red j Bold red text  

The  with  primitive can also be used for local redeﬁnitions of macros:  

h with j  strong jh macro j  body jh with j  font-series j bold j  color j red j  body iijh strong j strong  text i i  

The value of an environment variable may be retrieved using the  value  primi- tive, as in the following code to increase a counter:  

h assign j my-counter jh plus j my-counter j 1 ii  

Here we recall that the default rendering of  h value  j  my-counter i  inside source code is  my-counter  (see sections 12.2.2 and 12.3.1). Our example actually shows that both left-hand sides of assignments and values of environment variables are emphasized in green, which should help to locate environment variables inside source code. Similarly, macro arguments can be recognized by their brown color.  

We recall that the value of an existing environment variable can be retrieved using the  $\Delta$   key. For instance,  \ m y - c o u n t e r  ↩ yields  my-counter . In source mode, you may also use the keyboard shortcuts  ⌘⌃ =  ,  ⌘⌃ w  , and  ⌘⌃ v to produce  assign ,  with , and  value  tags.  
# 12.4.2 Macro expansion  

The main interest of the style-sheet language is the possibility to define macros. These come in three ﬂavors: ordinary macros, macros which take an arbitrary number of arguments and external macros, whose expansion is computed by S CHEME  or a plug-in. The macro-related primitives are available from the Source  $\blacktriangleright$    Macro  menu. Below, we will only describe ordinary macros.  

Ordinary macros are deﬁned using  

h assign j my-macro jh macro j x 1 j ⋅⋅⋅ j x n j body ii  

After such an assignment,  my-macro  becomes a new primitive with    $n$   argu- ments, which may be called using  

# h my-macro j y 1 j j y n i  

Inside the body of the macro, the  arg  primitive may be used to retrieve the values of the arguments to the macro. Notice that the default rendering of  h arg j name i  inside source code is  name :  

h assign j hello jh macro j name j Hello  name , you look nice today!  

It is possible to call a macro with fewer or more arguments than the expected number. Superﬂuous arguments are simply ignored. Missing arguments take the nullary  uninit  primitive (with rendering  ? ) as value:  

h assign j hey j h macro j ﬁrst j second j h if j h equal j second j ? ij Hey  ﬁrst , you look lonely today... j Hey  ﬁrst  and  second , you form a nice couple! iii  

You are allowed to use macros as values:  

h assign j my-macro-copy j my-macro i  

However, when using this style of macro programming, one should keep in mind that  $\mathrm{TeV}$   macros use a call-by-name evaluation strategy, contrary to functional programming languages such as S CHEME  (see section 12.4.4 below). The  compound  tag may be used to apply macros that are the result of a com- putation:  
# 12.4.3 Formatting primitives  

Most  $\mathrm{TEPX}_{\mathrm{MACS}}$   presentation tags can be divided in two main categories:  inline tags and  block  tags. Inline tags are used for small pieces of text, whereas block tags can contain text that spans over several paragraphs. For instance,  frac  is a typical inline tag, whereas  theorem  is a typical block tag. Some tags (such as strong ) are inline if their argument is inline and block otherwise.  

The most primitive inline tag  concat  is used for horizontal concatenation: h concat  $|\left\langle\sf{w i t h}\left|\sf{c o l o r}\left|\sf{b l u e}\left|\sf{b l u e}\right\rangle\right|\left\langle\sf{e m}\left|\sf{e m p h a s i s}\right\rangle\right\rangle$   is rendered as  blue emphasis . Similarly, the most primitive block tag  document  is used for vertical succes- sions of paragraphs:  h document j First j Second j Third i  is rendered as  

First Second Third  

The  concat  and  document  tags are so common that their names are actu- ally hidden for the default rendering of source code (see section 12.2.2 and Figure 12.6).  

When writing macros, it is important to be aware of the inline or block nature of tags, because block tags inside a horizontal concatenation are not rendered in an adequate way. For example,  h concat j Left jh document j Top j Bottom ij Right i yields  

LeftTop Right Bottom instead of the expected LeftTop BottomRight  

If you need to surround a block tag with inline text, then you must use the surround  primitive:  

h assign j my-theorem j h macro j body j h surround jh no-indent ih with j font-series j bold j Theorem.  ijh right-ﬂush ij body iii  

In this example, we surrounded the body of the theorem with the bold text “ Theorem. ” on the left and a “right-ﬂush” on the right-hand side. Flushing to the right is important in order to make the blue bounding box around the theorem look nice when editing the body of the theorem.  
In most cases,  $\mathrm{TeV}$   does a good job in determining which tags are inline and which ones are not. However, you sometimes may wish to force a tag to be a block environment. For instance, the tag  very-important  deﬁned by  

h assign j very-important jh macro j body jh with j font-series j bold j color j red j body  

may be used both as an inline tag and as a block environment. When placing your cursor just before the  with -tag and hitting  $\bumpeq$  followed by  $\trianglelefteq$  , you obtain  

assign very-important  

h macro j body j h with j font-series j bold j color j red j body iii  

These actions inserted a  document  tag around the body of the macro. The  doc- ument  tag itself is invisible (you should select  Tags with special rendering  $\blacktriangleright$    raw in  Document  $\blacktriangleright$    Source  $\blacktriangleright$    Preferences  to make it visible), but its presence is indi- cated through the stretched rendering. Since the body of the macro is now a block, your tag  very-important  automatically becomes a block environment as well.  

Another important property of tags is whether they contain normal textual content or tabular content. For example, consider the deﬁnition of the stan- dard  eqnarray\*  tag (with a bit of the presentation markup being suppressed):  

# assign eqnarray\*  

h macro j body j h with j par-mode j center j mode j math j math-display j true j par-sep j 0.45fn j h surround  j h no-page-break\* ih vspace\*  j  0.5fn i j h vspace  j  0.5fn ih no- indent\* ij h tformat j h twith j table-hyphen j y ij h twith j table-width j 1par ij h twith j table-min-cols j 3 ij h twith j table-max-cols j 3 ij h cwith j 1 j -1 j 1 j 1 j cell-hpart j 1 ij h cwith j 1 j -1 j -1 j -1 j cell-hpart j 1 ij body iiiii  

The use of  surround  indicates that  eqnarray\*  is a block environment and the use of  tformat  speciﬁes that it is also a tabular environment. Moreover, the  twith and  cwith  are used to specify further formatting information: since we are a block environment, we enable hyphenation and let the table extend over the whole paragraph (unused space being equally distributed over the ﬁrst and last columns). Furthermore, we have speciﬁed that the table contains exactly three columns.  
Finally, it is important to bear in mind that style-sheets do not only specify the ﬁnal presentation of documents on paper: they also determine the way documents are presented during the editing phase. Above, we have already mentioned the use of the  right-ﬂush  tag in order to improve the rendering of visual border hints. Similarly, ﬂags can be used to indicate the presence of invisible arguments while editing a document:  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/9ea8ad605c9176ee45c2f1d4abdba42a1ed75782db936085af304743053449cd.jpg)  

More generally, the  speciﬁc  tag with ﬁrst argument “screen” may be used to display visual hints that are removed when printing the document (see sec- tion 7.6.2).  

# 12.4.4 Evaluation control  

The  Source  $\blacktriangleright$    Evaluation  menu contains several primitives to control the way expressions in the style-sheet language are evaluated. These primitives may in particular be used for the deﬁnition of “meta-macros” whose purpose is to deﬁne or redeﬁne other macros. One typical example is the  new-theorem  meta- macro for the deﬁnition of new theorems:  

h assign j new-theorem j h macro j name j text j h quasi j h assign jh unquote j name ij h macro j body j h surround jh no-indent ih strong jh unquote j text i .  ijh right-ﬂush ij body iiiiii  

When expanding  h new-theorem j theorem j Theorem i  in this example, we ﬁrst evaluate all  unquote  instructions inside the  quasi  primitive, which yields the expression  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/fc2143002ef9ad235b15dc6eeba35c4b0c2e1996361425b21f81a704c312282e.jpg)  

Next, this expression is evaluated, thereby deﬁning a macro  theorem .  
It should be noticed that the   $\mathrm{TeV}$   conventions for evaluation are slightly diﬀerent then those from conventional functional languages such as S CHEME . We recall that S CHEME  is the extension language for  $\mathrm{TEX}_{\mathrm{MACS}};$   see chapter 14 for a short introduction. The subtle diﬀerences between the style-sheet language and S CHEME  are motivated by our objective to make it as easy as possible for the user to write macros for typesetting purposes. Assuming that you know the basics of S CHEME , it is instructive to examine the diﬀerences on a few exam- ples.  

hen   $\mathrm{TeV}$   calls a mac ,...,  $\langle\mathsf{m a c r o}\,|\,x_{\perp}\,|\cdots|\,x_{n}\,|\,\mathsf{b o d y}\rangle$   with arguments  $\mathtt{y}_{1},\dots,

$   ${\tt y}_{\tt n},$  ,..., gument variables  $x_{\perp},\ldots,x_{n}$   are bound to the unevaluated expressio

  $\mathsf{y}_{1},\ldots,\mathsf{y}_{\mathfrak{n}},$  , and the body is evaluated with these bindings. The evaluation of  $\mathtt{y_{i}}$  takes place each time the argument  $X_{I}$   is actually used during the evaluation of the macro. In particular, when applying the macro    $\langle\mathsf{m a c r o}|x|x$   and again  $\left|x\right\rangle$   to an expression  $\mathtt{y},$  , the expression  y  is evaluated twice.  

In S CHEME , the literal bodies of S CHEME  macros are evaluated twice, whereas the arguments of functions are evaluated only once. On the other hand, when retrieving a variable (whether it is an argument or an environment variable), the value is not evaluated. Consequently, a  $\mathrm{TeV}$   macro  

h assign j foo jh macro j x jh blah j x j x iii  

corresponds to a S CHEME  macro  

( define-macro  (foo x) \`( let  ((x ( lambda  () ,x))) (blah (x) (x)))  

Conversely, the S CHEME  macro and function  

( define-macro  (foo x) (blah x x))

 ( define  (fun x) (blah x x))  

admit the following analogues in  $\mathrm{TeV}$  :  

h assign j foo jh macro j x jh eval jh blah jh quote-arg j x ijh quote-arg j x iiiii h assign j fun jh macro j x jh with j x\* j x jh blah jh quote-value j x\* ijh quote-value j x\* iiiii  

Here the primitives  quote-arg  and  quote-value  are used to retrieve the value of an argument or an environment variable. The  $\mathrm{T}_{\mathrm{E}}\mathrm{X}_{\mathrm{MACS}}$   primitives  eval ,  quote , quasiquote , and  unquote  behave in the same way as their S CHEME  analogues. The  quasi  primitive is a shortcut for quasi-quotation followed by evaluation.  

# 12.4.5 Control ﬂow  

The  Source  $\blacktriangleright$    Flow control  menu contains   $\mathrm{TeV}$   analogues of basic control ﬂow primitives that can be found in conventional programming languages:  if , case ,  while , and  for-each . However, be warned that the conditional constructs are quite fragile: they only apply to inline content and it is recommended that the various alternatives only aﬀect the rendering, not the structure. For instance, consider the fragment  
h assign j weird j h macro j body j h if jh my-condition ij Hi  body ! jh label j body iiii  

In the “then part” of the  if  primitive, the  body  argument is a regular macro argument that can be edited by the user (we say that it is  accessible ). In the “else part”, the  body  argument is a hidden parameter that should be deacti- vated before you can edit it. To remain on the safe side,  $\mathrm{TEPX}_{\mathrm{MACS}}$   considers the body  argument of the  weird  macro to be inaccessible, even when it is rendered according to the “then part”.  

The  if  primitive for conditional typesetting can be entered using  ⌘⌃ ?  and is by far the most important control ﬂow primitive. We recommend to mainly use it in combination with the  compound  primitive, as follows:  

h assign j rich-appendix j h macro j title j body j h compound j h if jh long-document ij chapter-appendix j section-appendix ij title j body iii  

In this example,  rich-appendix  is a block environment consisting of a title and a body, and that is rendered as a chapter for long documents and as a section for short ones. Notice that the following implementation would have been incorrect, since the  if  primitive currently only works for inline content:  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/9f9b49dda64b8b77d6049680a8347897d73ac61a2a5cce49eb6ff58214cbfc02.jpg)  

The  if  primitive can also be used in order to implement optional arguments:  

h assign j hey j h macro j ﬁrst j second j h if j h equal j second j ? ij Hey  ﬁrst , you look lonely today... j Hey  ﬁrst  and  second , you form a nice couple! iii  
However,  $\mathrm{TeV}$   is not clever enough to detect which arguments are optional and which arguments are accessible. This information should be specified manually using the  drd-props  primitive; see the reference guide for more infor- mation.  

# 12.4.6 Computational markup  

The menus  Source  $\blacktriangleright$    Arithmetic ,  Text ,  Tuple , and  Condition  contain different primitives for computing with integers, strings, tuples, and boolean values. For instance, in the following code, the  new-important  tag deﬁnes a new “impor- tant tag” as well as a red variant:  

h assign j new-important j h macro j name j h quasi j h concat j h assign j h unquote j name ij h macro j x jh with j font-series j bold j x iiij h assign j h unquote jh merge j name j -red iij h macro j x jh with j font-series j bold j color j red j x iiiiiii  

Here we use the  merge  primitive in order to concatenate two strings. Precise positioning is possible through appropriate computations with lengths:  

$$
|\langle\mathsf{a s s i g n}|c e n t e r\mathsf{-a x i s}|\langle\mathsf{m a c r o}|b o d y|\mathsf{\langle m o v e}|b o d y||\mathsf{\langle m i n u s}|\mathsf{0.5e x}|\mathsf{0.5h\rangle}\rangle\rangle\rangle|
$$  

The purpose of this macro is to vertically center the argument at the position of the fraction bar. This is achieved by moving it up by half the height    $0.5\,\mathrm{ex}$  of an  $\mathbf{x}$  -character and then back down by half the height  $0\cdot5\,\mathrm{h}$   of the argument itself (the length unit  h  is automatically deﬁned to be the height of the main body inside the  move  primitive).  
# Chapter 13  

# Designing with style  

The previous chapter gave a ﬁrst introduction to the stylesheet language and how to add your own macros. We are now ready to dive deeper into this topic and investigate how to design complete document styles and style packages.  

Scientiﬁc documents use a variety of style elements: section titles, item lists, theorems, headers, etc. New document styles are meant to oﬀer the complete functionality of the built-in styles, but with a special design, which might for instance be dictated by the “graphical charter” of a journal. Since it would be cumbersome to redevelop all standard macros from scratch, new styles are typically designed as customizations of existing ones. The bulk of this chapter is dedicated to explaining how this works.  

Style packages correspond to additional customizations that can be combined with any base style. This is typically useful for personal notations or when one or more macros need to be adapted in order to achieve a certain graphical eﬀect. The explanations in this chapter may serve for the development of style packages that customize the standard styles.  

Advanced users may also design style packages for new types of functionality such as literate programming or interactive courses. Such style packages are usually accompanied by extensions to the editor itself, in the form of keyboard shortcuts, special menu entries, or more complex editing routines. The next chapter gives a ﬁrst glimpse of how to develop such enhancements.  

# 13.1 Some words of caution  

We recall that one of the main aims of beautiful typesetting and graphical design is to be “invisible”: readers should focus on content and not be dis- tracted by typesetting details. This is a quite delicate task which is really a job for experts on typography. Entire books have been written on this topic; see for instance [4, 40].  

With the advent of typesetting software, the bulk of the traditional design tasks reduces to the development of high quality document styles.  A priori , this still requires the same kind of expertise, so why would you want to this your- self? One reason could be that you wish to reproduce the style of a particular journal. But maybe you just got bored aping your colleague next door and prefer to have some fun creating your own distinctive style instead.  
If you go down this road and design your own style, then it is tempting to introduce all kinds of fancy decorations for standard environments, such as boxes around theorems, drop shadows for section titles, your favorite pictures for list items, etc. Keep in mind that such phantasies may quickly saturate and irritate your readers. Instead, we invite you to search for more subtle ways to distinguish yourself. This can often be achieved through the careful selection of a few fonts, or by modifying some spacings or separators. For example, the simple use of a sans serif font for theorems will already distinguish your style from all built-in TEX MACS  styles:  

Theorem 13.1.  This statement has a distinctive look & feel.  

Notice that it is not necessary to refrain from all forms of ornaments. For instance, it may be all right to use the following type of main section titles:  

# My fancy section  

Although such titles are somewhat “aggressive”, they tend to occur only a few times in a document. As long as this is the only fantasy in your document style, this remains acceptable, while immediately ensuring a distinctive look and feel.  

Another thing that you should worry about is related to the dual “data versus program” nature of  $\mathrm{TeV}$   macros that we ﬁrst mentioned in sec- tion 12.2.3. Now the programming side becomes more significant when macros are grouped together in style ﬁles or packages. In many respects, the develop- ment of style ﬁles is analogous to writing software libraries, with macros in the role of library functions and subroutines. Besides aesthetical considerations, it is therefore important to think about issues like dependencies, maintainability, and orthogonality (i.e. how well do your macros combine with macros from other packages?).  

Once again, you should be guided by the notion of simplicity. The simpler your personal customizations are and the more they rely on standard mecha- nisms, the more likely they will continue to work well with future versions of TEX MACS  and in combination with other style packages. For example, if your macros crucially depend on some obscure internal macro that you found in one of the  $\mathrm{TeV}$   style packages, then they will break down if the internal macro happens to disappear in a future version of  $\mathrm{TeV}$  . Similarly, your macros may fail to work in combination with alternate styles that do not implement the required internal macro. For similar reasons, you should avoid complex macros that adjust the typesetting process in subtle ways: ongoing progress in the TEX MACS  typesetter may make it diﬃcult to maintain such macros.  
# 13.2 Anatomy of a style package  

Before you start designing your own style ﬁles, we recommend you take a closer look at the existing style files. One fairly complete example is the  svjour base style for articles published by S PRINGER  V ERLAG . This style is selected using  Document  $\blacktriangleright$    Style  $\blacktriangleright$    Article  $\blacktriangleright$    Springer  $\blacktriangleright$    svjour . After selecting this style, you may open the corresponding source ﬁle using  Document      Style  $\blacktriangleright$    Edit style .  

The first line of the  svjour  style file specifies the style packages on which the style is based. It essentially uses the same style packages as the standard article  style, together with one additional package  std-latex :  

h use-package j std j env-base j env-math j env-ﬂoat j env-program j header-article j title-base section-article std-latex  

The  std-latex  package is useful when adapting a  $\mathrm{LiTa}$   style ﬁle to TEX , MACS since it provides several macros that allow you to specify global style para- meters in “the L A TEX way”. For instance, the  svjour  style uses the following lines to specify the global margins and text width—both for single and double column articles:  

h assign j tex-odd-side-margin jh macro jh if jh equal j par-columns j 1 ij 0pt j -30pt iii h assign j tex-even-side-margin jh macro jh if jh equal j par-columns j 1 ij 0pt j -30pt iii h assign j tex-text-width jh macro jh if jh equal j par-columns j 1 ij 25.5cc j 17.8cm iii  

Various other global style parameters are speciﬁed in a similar way.  

The remainder of the  svjour  style ﬁle redeﬁnes some of the most signiﬁcant macros that determine the layout of articles. One may distinguish the following main categories:  

Speciﬁcation of the fonts and font sizes to be used.  

Rendering of sectional macros.  

Speciﬁcation of headers and footers to be used.  

Theorem-like environments.  

Item lists and enumerations.  

Rendering of the document title and the abstract.  

Let us brieﬂy study how some of these customizations were carried out for svjour . More general and detailed explanations will be provided in the sec- tions below.  
# Fonts and font sizes  

Style ﬁles for journals often specify the main document font and its variants with care. The  svjour  style speciﬁes the default font size to be    $10\,\mathrm{pt}$   with a    $0\,.\,2\,\mathtt{e m}$   interline space, but also redeﬁnes the standard tags for other font sizes, such as  small ,  large ,  smaller , etc. For example, the default rendering of footnotes uses a smaller font size that is speciﬁed through the  smaller  tag. The svjour  style redeﬁnes it to use a  9pt  font with a  $_{2\,\sf p t}$   interline space:  

h assign j smaller jh macro j x jh with j font-base-size j 9 j par-sep j 2pt j x iii  

# Sectional macros  

After the main document font and page layout, the rendering of section titles is the next most signiﬁcant characteristic of a scientiﬁc document style. Most journals use bold, emphasized, or small capital fonts, and carefully specify the amount of vertical space to be inserted before and after titles. Styles that were adapted from L A TEX by means of the  std-latex  package may reproduce TEX- style rubber spaces using the  tex-len  macro. For instance,  svjour  renders main section titles in the following way:  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/b5ab7889f323a02cef93aaeb384759f43e894059ce3db68b71584a0a0f6f6d09.jpg)  

Here  sectional-normal-bold  is a utility macro for rendering bold section titles. It also takes care of a few other issues such as forbidding page breaks just after the title.  

# Headers and footers  

Most styles determine headers and footers as a function of the title and names of the authors. TEX MACS  provides a few “call-back macros” for this purpose: header-title  (document title),  header-author  (document author),  header-primary (primary sections), and  header-secondary  (secondary sections). For example, the  header-author  macro is called with the name of the author as an argument, when specifying this information in the title of your document. The  svjour style exploits this mechanism to redeﬁne the even page header so as to contain the author's name:  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/a21811d1014fdefb4af0937faf30e98b384429cef786195f26d37b3e09e88414.jpg)  
# Theorem-like environments  

Scientiﬁc articles require many technical markup elements like theorems, enu- merations, algorithms, technical pictures, etc. Full-ﬂedged styles may redeﬁne the rendering of such markup elements. The standard   $\mathrm{TEPX}_{\mathrm{MACS}}$   styles con- tain a large number of macros that allow you to customize speciﬁc rendering aspects. For instance, the main rendering of theorem-like environments is con- trolled through the  render-theorem  macro. But it is also possible to change the font for the text “T HEOREM  3.6.” using  theorem-name , as well as the separator “.” after the number using  theorem-sep . For our example  svjour  style, we essentially have  

h assign j theorem-name jh macro j name jh with j font-series j bold j name iii h assign j theorem-sep jh macro j .  ii h assign j render-theorem j h macro j which j body j h padded-normal j 1fn j 1fn j h surround jh theorem-name j which h theorem-sep iijj with font-shape italic body  

In the deﬁnition of  render-theorem , the  padded-normal  macro is used for speci- fying the vertical padding around theorem-like environments. The  std-utils style package contains various other handy utility macros of this kind.  

# Lists and enumerations  

Different nesting levels of list environments typically require separate ren- dering styles. TEX MACS  provides the macros  enumerate-1 ,  enumerate-2 , etc. for top-level enumerations, second level sub-enumerations, and so on. Most style ﬁles limit themselves to three nesting levels; for  svjour , we have  

h assign j aligned-accolade-item jh macro j x jh aligned-item jh with j font-shape j right j { x } iiii h new-list j enumerate-1 j aligned-dot-item j identity i h new-list j enumerate-2 j aligned-accolade-item jh macro j x jh number j x j alpha iii h new-list j enumerate-3 j aligned-dot-item jh macro j x jh number j x j roman iii  

The  new-list  construct is used to deﬁne the macros  enumerate-1 ,  enumerate-2 , and  enumerate-3 ; its second argument is a macro that is used for rendering items; the third argument contains a macro that is used for transforming the numbers of items. The macros  aligned-item  and  aligned-dot-item  are standard rendering macros that can be redeﬁned. The rendering of lists themselves is controlled through the  render-list  macro.  

# Document titles and abstracts  

One of the most complex parts of style files concerns document titles and abstracts. The diﬃculty stems from the fact that title and abstract information should really be thought of as a collection of metadata for the document. The rendering then proceeds in two steps: one ﬁrst has to collect and reorganize the data in an appropriate way and then call lower-level rendering macros in an appropriate order. Here one has to keep in mind that a lot of informa- tion (keywords, subject classiﬁers, aﬃliations, etc.) is optional or may need to be recombined (various authors with multiple aﬃliations).  
It is recommended that style ﬁles only customize the ﬁnal rendering macros for title and abstract information. The title mainly consists of a succession of “blocks” that are rendered using the  doc-title-block  macro. Speciﬁc kinds of information are rendered using dedicated macros  doc-render-title ,  doc-subtitle , doc-date , etc. For example, the rendering of the main document title is deﬁned as follows for the  svjour  style:  

h assign j doc-render-title j h macro j x j h surround jjh vspace j 11.24pt ij h doc-title-block jh larger jh with j math-font-series j bold j font-series j bold j x iiiiii  

# 13.3 Some tips before things get technical  

Before going deeper into the technical details about how to control speciﬁc style elements, let us ﬁrst discuss a few general tips for the development of style packages.  

Which macros to redeﬁne  

Most standard style ﬁles and packages consist of a succession of macro deﬁ- nitions and speciﬁcations of default values for environment variables. When customizing an existing style, it is important to carefully select the macros and environment variables to be redeﬁned.  

Now certain tags in the standard style ﬁles are directly exposed to the end-user through the interface. For instance, you have direct access to the tags  strong and  section  through the menu entries  Insert  $\blacktriangleright$    Content tag  $\blacktriangleright$    Strong  and  Insert    Section  $\blacktriangleright$    Section . Other tags such as  section-title  or  render-theorem  are rather provided for customization purposes by developers of style ﬁles. Some style packages also deﬁne auxiliary helper macros for internal purposes.  

Although suﬃciently simple tags like  strong  can be redeﬁned directly in your own style ﬁles, this is not recommended for more complex tags such as  section . Indeed, the  section  tag takes care of many tasks: rendering the title, resetting the counter for subsections, entering the title into the table of contents, and so on. In order to customize complex tags of this kind, you should rather redeﬁne one or more of the “companion tags”  section-title ,  section-clean ,  section-toc , etc. that control these more speciﬁc subtasks.  
# Customizing existing macros  

Imagine that you want to change the rendering of a given tag, like  lemma . We have just seen that   $\mathrm{TeV}$   provides a set of carefully designed companion macros that can be customized to modify speciﬁc aspects of the rendering. For instance (see section 13.2), you are supposed to redeﬁne one of the macros render-theorem ,  theorem-name , or  theorem-sep  in order to customize the ren- dering of  lemma  and all other theorem-like environments.  

However, in some cases, it may not be clear which companion macro to cus- tomize. If we just wanted to change the presentation of lemmas and not of any other theorem-like environments, then we clearly cannot modify  render- theorem ,  theorem-name , or  theorem-sep . Besides, you may not want to spend too much time on understanding the macro hierarchy of   $\mathrm{TeV}\mathrm{X}_{\mathrm{MACS}},$   thereby ignoring the very existence of  render-theorem ,  theorem-name , and  theorem-sep .  

So imagine that you want all lemmas to appear in red. One thing you can always do is copy the original deﬁnition of the  lemma  macro to a safe place and redeﬁne it on top of the original deﬁnition:  

h assign j orig-lemma j lemma i h assign j lemma jh macro j body jh with j color j red jh orig-lemma j body iiii  

Alternatively, if only the text inside the lemma should be rendered in red, then you may do:  

h assign j orig-lemma j lemma i h assign j lemma jh macro j body jh orig-lemma jh with j color j red j body iiii  

However, be warned that this mechanism is somewhat fragile: if the name orig-lemma  was already in use (for instance, if you already performed a similar customization in another style package), then you may introduce a circular depe emma  $\rightarrow$  orig-lemma  $\rightarrow$  lemma  $\rightarrow$  orig-lemma  $\rightarrow\,\cdot\,\cdot\,\cdot$  . Here we note that TEX  $\mathrm{TeV}$   contains no safeguards against programming errors by devel- opers of style packages: inﬁnite loops of the above type will simply crash the editor.  

One obvious ﬁx is to choose the backup name  orig-lemma  with more care; e.g. uncolored-lemma  might be more appropriate. It is also a good idea to deﬁne the backup macro if only if no macro with the same name already exists; this can be done by using the  provide  primitive instead of  assign :  

At the end of section 13.7, the redeﬁnition of  inc-theorem  shows a more robust but subtle mechanism for customizing existing macros.  
# Local customizations  

Another frequent situation is that you only want to modify the rendering of a tag when it is used inside another one. On the web, the  Cascading Style Sheet language (CSS) provides a mechanism for doing this. In T E X MACS , you may sim- ulate this behavior by redeﬁning macros inside a  with . For example, imagine that we want to suppress the inter-paragraph space inside lists within the- orem-like environments. Then we may use:  

h assign j orig-render-theorem j render-theorem i h assign j render-theorem j h macro j name j body j h with j orig-render-list j render-list j h with j render-list jh macro j x jh orig-render-list jh with j par-par-sep j 0fn j x iiij h orig-render-theorem j name j body iiiii  

On the one hand, this mechanism is a bit more complex than CSS, where it suﬃces to respecify the  par-par-sep  attribute of lists inside theorems. On the other hand, it is also more powerful, since the  render-theorem  macro applies to all theorem-like environments at once.  

# Rely on the “standard utilities”  

The style package  std-utils  contains various useful “helper macros” that should make it easier to develop style packages. It mainly contains macros for  

• Writing block environments that extend over the entire paragraph width. Notice that the  title-base  package provides some additional macros for wide section titles. • Writing wide block environments that are padded, underlined, over- lined, or in framed boxes. • Recursive indentation. • Setting page headers and footers. Localization of text.  

It is good practice to rely on these standard macros whenever possible. Indeed, the low-level   $\mathrm{T}_{\mathrm{E}}\mathrm{X}_{\mathrm{MACS}}$   internals may be subject to minor changes. When building upon standard macros with a clear intention, you increase the upward compatibility of your style-sheets.  

# Internationalization  

Certain tags like theorems, ﬁgures, or bibliographies need to print English text like “Theorem”, “Figure”, or “References”. In order to allow this text to be cus- tomized, such tags usually come with companion macros  theorem-text ,  ﬁgure- text ,  bibliography-text , etc. For example, the  svjour  style redeﬁnes the  ﬁgure- text  macro to print “Fig.” instead of “Figure”. In order to automatically trans- late the text from English into the current language, you should pass it as an argument to the  localize  macro. For instance, the  section-base  package con- tains the following default deﬁnition of  bibliography-text :  
# h assign j bibliography-text jh macro jh localize j Bibliography iii  

The directory  $\Updownarrow$  TEXMACS_PATH/langs/natural/dic  contains the dictionaries for translations into the supported languages. Here    $\S$  TEXMACS_PATH  is the place where  $\mathrm{TeV}$   is installed on your system.  

# Converting L A TEX styles  

Style ﬁles for  $\mathrm{TeV/scriptstyle{L^{A}T E X}}$   are particularly complex and ill-behaved, with lots of auxiliary macros and style parameters without clear semantics. For this reason, the built-in  $\mathrm{Li^{A}T_{E}X}$   converters perform rather poorly on style ﬁles. TEX MACS  pro- vides equivalents for some of the most important   $\mathrm{LiTa}$   styles. If you wish to mimic another style, then we recommend that you proceed as follows:  

• Try to import the  $\mathrm{LiTeX}$   style ﬁle. Most of the structure will be lost, but the converter sometimes manages to import at least a few macros and environment variables. The result of the conversion may therefore provide a reasonable start for the development of a TEX MACS  equivalent for your   $\mathrm{LiTa}$   style.  

• Determine an existing TEX MACS  style that comes as close as possible to the desired style and base your new style on it using  use-package . Notice that the converter from the previous step may already have come up with a good proposal.  

• Add a line  h use-package j std-latex i  to your style ﬁle and customize the utility macros from that package in order to specify the most important layout parameters.  

• Patiently customize various other macros in order to match the desired style, following the mechanisms that will be described in the subsec- tions below.  

Concerning the third step, we notice that TEX MACS  does not always use the same conventions as TEX/L A TEX when it comes to global layout parameters. For example, the style parameters  \oddsidemargin  and  \evensidemargin for left margins on odd and even pages do not mean what you would think, since TEX automatically adds one extra inch. The  std-latex  package provides macros  tex-odd-side-margin  and  tex-even-side-margin  that mimic this somewhat twisted behavior in   $\mathrm{TeV}\mathrm{X}_{\mathrm{MACS}}$  . Various other style parameters  \textwidth , \topmargin ,  \jot ,  \above display skip , etc. admit similar analogues  tex- text-width ,  tex-top-margin ,  tex-jot ,  tex-above-display-skip .  
The  std-latex  package also deﬁnes a macro  tex-len  with three arguments default-length ,  plus , and  minus  that emulates the syntax of  $\mathrm{T}_{\mathrm{E}}\!\mathrm{X}$   rubber lengths. For example,    $\langle\mathsf{t e x-l e n}|\,1\,\mathsf{e m}|\,0\,.\,5\,\mathsf{e m}|\,0\,.\,25\,\mathsf{e m}\rangle$   stands for the rubber length with default, minimal, and maximal values  1em ,    $0.75\,\mathsf{e m},$   and    $1.5\,\mathsf{e m}$  , respec- tively. The corresponding   $\mathrm{TeV}$   syntax for this rubber length is  h tmlen  j  $0\,.75\,{\mathsf{e m}}\,|\,1\,{\mathsf{e m}}\,|\,1\,.5\,{\mathsf{e m}}\rangle$  . See pages 62 and 7.1 for more information on   $\mathrm{TeV}$  lengths.  

# 13.4 Customizing the general page layout  

The general layout of a document is mainly modified by setting the appropriate environment variables for page layout and paragraph layout (see the refer- ence manual for a complete list of these variables). For example, by including the following lines in your style ﬁle, you can set the page size to  letter  and the left and right margins to  1.25in :  

h assign j page-type j letter i h assign j page-odd j 1.25in i h assign j page-even j 1.25in i h assign j page-right j 1.25in i  

Recall from section 3.10 that the margins may be diﬀerent on even and odd pages; the environment variables  page-odd  and  page-right  correspond to the left and right margins on odd pages.  

Note that the environment variables for page layout are quite different in  $\mathrm{T}_{\mathrm{E}}\mathrm{X}_{\mathrm{MACS}}$   and  $\mathrm{T_{E}\!X/L^{A}T_{E}\!X}$  . In order to make it easier to adapt  $\mathrm{Li^{A}T_{E}X}$   style ﬁles to TEX , we have therefore provided the  std-latex  package, which emulates MACS the environment variables of   $\mathrm{TeV/LFX}$  . Typically, this allows you specify the global layout using declarations such as  

h assign j tex-odd-side-margin jh macro j 20pt ii h assign j tex-even-side-margin jh macro j 20pt ii h assign j tex-text-width jh macro j 33pc ii  

Notice that  page-odd ,  page-even , etc. are lengths, whereas  tex-odd-side-margin , tex-even-side-margin , etc. are macros that return a length.  

The page headers and footers are usually not determined by global environ- ment variables or macros, since they may change when a new chapter or section is started. Instead,  $\mathrm{TeV}\mathrm{X}_{\mathrm{MACS}}$   provides the call-back macros  header-title ,  header- author ,  header-primary , and  header-secondary . These macros get called when the document title or author are specified, or when a new primary or secondary section is started (by default, primary sections correspond to chapters in books, and to sections in articles). For instance, the following redeﬁnition makes the principal section name appear on even pages, together with the current page number and a wide underline.  
h assign j header-primary j h macro j title j nr j type j h assign j page-even-header j h quasiquote j h wide-std-underlined j h page-the-page ih htab j 5mm ih unquote j title iiiiii  

# 13.5 Processing title information  

The “titles” of scientific documents usually carry a lot of additional information about the authors, their aﬃliations, the creation date, grant acknowledgments, etc. For this reason,   $\mathrm{TeV}$   treats the title information as a miniature data- base, and the graphical rendering proceeds in two phases: the most relevant information is ﬁrst extracted from the database and reorganized. The actual rendering is done at a second stage, using dedicated macros for this purpose.  

The ﬁrst stage is fairly complex, since one has to deal with various optional data ﬁelds and potentially multiple authors with multiple aﬃliations. Var- ious styles may present the data in diﬀerent orders and one has to decide how to present common aﬃliations among coauthors (see section 3.3.1 for a few common styles). Since the required rewritings are rather intricate, they are not performed by TEX  macros, but rather through “external” S CHEME  rou- MACS tines whose precise description falls beyond the scope of this book.  

The second stage is more straightforward: for each kind of title information, there is a corresponding rendering macro that can be customized by particular styles. For instance, the main title, an optional subtitle, the creation date, and miscellaneous extra title ﬁelds are rendered using the macros  doc-title ,  doc- subtitle ,  doc-date , and  doc-misc . So if the date should appear in a bold italic typeface and at a distance of at least  $0\,.\,5\,\mathtt{f n}$   from the other title ﬁelds, then you may redeﬁne  doc-date  as  

# h assign j doc-date j h macro j x j h surround jh vspace\* j 0.5fn ijh vspace j 0.5fn ij h doc-title-block jh with j font-shape j italic j font-series j bold j x iiiii  

The helper macro  doc-title-block  should be used for rendering atomic blocks of title information; many styles implement this macro by centering title blocks, whereas other styles rather align them to the left.   $\mathrm{TeV}$   also uses the macro doc-make-title  for encapsulating all title information. You may specify an amount of padding between titles and the main text by customizing this macro.  
The rendering of author information is done using similar macros  author- name ,  author-affiliation ,  author-email ,  author-homepage , and  author-misc . These macros should rely on the macro  doc-author-block  for rendering atomic blocks of author information. In addition, TEX MACS  provides variants  author-aﬃlia- tion-note ,  author-email-note ,  author-homepage-note , and  author-misc-note  that are used when several authors share common information. These variants take one additional argument that contains the symbol (such as †) that is used to link the shared information to the corresponding authors.  

Author information is often rendered differently for documents with one versus several authors. In case of a single author, the  doc-author  macro is used for rendering the block with all author information. This macro behaves simi- larly to  doc-title ,  doc-subtitle , etc., and should rely on  doc-title-block  for its rendering. If there are multiple authors, then the  doc-authors  macro is used for rendering the complete list of authors (the macro uses one argument for each author), whereas the information of each individual author is encapsu- lated inside a block that is rendered using the  doc-authors-block  macro.  

Some further global metadata are provided in the abstract rather than in the title. The rendering of the abstract is controlled via the macro  render-abstract . In addition,  $\mathrm{TeV}$   provides the macro  abstract-keywords  for rendering a list of keywords (one argument for every keyword) and the macros  abstract-acm , abstract-msc , and  abstract-pacs  for specifying ACM, AMS, and PACS subject classiﬁers.  

# 13.6 Customizing sectional tags  

TEX MACS  provides the same sectional tags as L A TEX:  part ,  chapter ,  section ,  sub- section ,  subsubsection ,  paragraph ,  subparagraph , and  appendix . TEX MACS  also implements the unnumbered variants  part\* ,  chapter\* , etc. and special section- like tags  bibliography ,  table-of-contents ,  the-index ,  the-glossary ,  list-of-ﬁgures , list-of-tables .  

One important additional “predicate macro” is  sectional-short-style . If it eval- uates to  true , then appendices, tables of contents, etc. are considered to be at the same level as sections. In the contrary case, they are at the same level as chapters. Typically, articles use the short sectional style whereas books use the long style.  

The rendering of a sectional tag  $x$   is controlled through the macros  x -sep , x -post-sep ,  $\boldsymbol{x}.$  -title  and  $\boldsymbol{x}.$  -numbered-title . The  $\boldsymbol{x}.$  -sep  macro prints the separator between the section number and the section title. It defaults to the macro sectional-sep , which defaults in its turn to a wide space. For example, after redeﬁning  

sectional titles typically look as follows:  

# 13.1 – Hairy GNUs  
Similarly,  $\boldsymbol{x}\cdot$  -post-sep  prints the separator between the section title and subse- quent text. The  $\boldsymbol{x}\cdot$  -title  and  $\boldsymbol{x}.$  -numbered-title  macros respectively specify how to render unnumbered and numbered section titles. Usually, the user only needs to modify  $\boldsymbol{x}.$  -title , since  $\boldsymbol{x}\cdot$  -numbered-title  is based on  $\boldsymbol{x}\cdot$  -title . However, if the numbers have to be rendered in a particular way, then it may be necessary to redeﬁne  x -numbered-title . For instance, consider the redeﬁnition  

h assign j subsection-numbered-title j h macro j name j hsectional-normaljh with j font-series j bold jh the-subsection i .  i name iii  

This has the following eﬀect on the rendering of subsection titles:  

# 2.3. Very hairy GNUs  

Notice that the  sectional-normal  macro comes from the  section-base  style package. You may find several similar macros  sectional-normal-italic ,  sectional- centered-bold , etc. there for some of the most frequent ways to render section titles.  

There are two main rendering styles for sectional titles. By default, paragraphs and subparagraphs use a “short” rendering style, with a body that starts imme- diately after the title:  

# My paragraph Blah, blah, and more blahs...  

All other sectional tags use a   $"\mathrm{long}"^{\prime}$   rendering style, in which case the section title takes a separate line on its own:  

# My section  

Blah, blah, and more blahs...  

When customizing the rendering of sectional titles, we recommend that you follow the same conventions: render paragraphs and subparagraphs in the short way and all others in the long way.  

Besides their rendering, several other aspects of sectional tags can be cus- tomized:  

• The call-back macro    $\boldsymbol{x}.$  -clean  can be used for resetting some counters when a new section is started. For example, in order to preﬁx all stan- dard environments by the section counter, you may use the following lines:  

h assign j section-clean jh macro jh reset-subsection ih reset-std-env iii assign display-std-env macro nr section-preﬁx nr  
• The call-back macro  $\boldsymbol{x}\cdot$  -header  should be used in order to modify page headers and footers when a new section is started. Typically, this macro should call  header-primary  or  header-secondary , or do nothing. • The call-back macro  $\boldsymbol{x}.$  -toc  should be used in order to customize the way new sections appear in the table of contents.  

# 13.7 Customizing numbered textual environments  

TEX MACS  provides three standard types of numbered textual environments: theorem-like environments, remark-like environments, and exercise-like envi- ronments. The ﬁrst two types of environments are also called “enunciations”. The following aspects of numbered textual environments can easily be cus- tomized:  

• Adding new environments. • Modifying the rendering of the environments. • Numbering the theorems in a diﬀerent way.  

Deﬁning new environments  

It is possible to introduce new environments using the meta-macros  new-the- orem ,  new-remark , and  new-exercise . These environments take two arguments: the name of the environment and the name which is used for its rendering. For example, you may wish to deﬁne the environment  experiment  by  

h new-theorem j experiment j Experiment i  

The text “Experiment” will automatically be translated if your document is written in a foreign language, provided that there is an entry for this word in the   $\mathrm{TeV}$   dictionaries (see the section on internationalization on page 231).  

Customizing the rendering  

The main rendering of numbered textual environments can be customized by redeﬁning the macros  render-enunciation ,  render-theorem ,  render-remark , and render-exercise . These macros take the  name  of the environment (like “The- orem  $1.2{^{\prime\prime}}$  ) and its  body  as arguments. For instance, if you want theorems to appear in a slightly indented way, then you may redeﬁne  render-theorem  as follows:  

h assign j render-theorem j h macro j which j body j h padded-normal j 1fn j 1fn j h surround jh theorem-name j which h theorem-sep iijj h with j font-shape j italic j par-left jh plus j par-left j 1.5fn ij body iiiii  
This redeﬁnition produces the following eﬀect: T HEOREM  13.2.  This is a theorem that has been indented.  

The macros  render-theorem  and  render-remark  are both based on the macro render-enunciation . The only diﬀerence between theorems and remarks is that theorems typically use an italic font. Note that proofs are rendered using render-proof ; this macro is based on  render-remark .  

As you may have noticed by examining the above redeﬁnition of  render-the- orem , it is also possible to customize the way names of theorems are printed or redeﬁne the separator between the name and the body. Indeed, these aspects are controlled by the macros  theorem-name  and  theorem-sep . For example, consider the following redeﬁnitions:  

h assign j theorem-name jh macro j name jh with j color j dark red j font-series j bold j font- shape j small-caps j name iii h assign j theorem-sep jh macro j :  ii  

Then theorem-like environments will be rendered as follows:  

P ROPOSITION  13.3:  This proposition is rendered in is a fancy way.  

# Customization of the numbering  

All numbered environments such as sections and theorems come with coun- ters  section-nr ,  theorem-nr , etc. In order to increase, reset, or display the counter theorem-nr , you should use the companion macros  inc-theorem ,  reset-theorem , and  display-theorem . By redeﬁning these macros, you may customize the way in which environments are numbered. For instance, by redefining  inc-theorem , you may force theorems to reset the counter of corollaries:  

# quasi  

inc-theorem j h macro jh compound jh unquote j inc-theorem iih reset-corollary iiii  

Notice the trick with  quasi  and  unquote  in order to take into account any addi- tional action that might have been undertaken by the previous value of the macro  inc-theorem . Indeed,  h unquote  j  inc-theorem i  gets replaced by the pre- vious value of the macro  inc-theorem . This macro has zero arguments and h compound jh unquote j inc-theorem ii  simply evaluates its body.  
TEX MACS  organizes counters in various counter groups, which allows you to simultaneously reset all counters of a certain type at the start of a new section. The following code from the  number-long-article  style package is used in order to preﬁx all standard environments (theorems, equations, ﬁgures, etc.) with the number of the current section:  

h assign j section-clean jh macro jh reset-subsection ih reset-std-env iii h assign j display-std-env jh macro j nr jh section-preﬁx i nr ii  

# 13.8 Customizing list environments  

Item lists and enumerations are made up of two main ingredients: the outer list environment and the inner list items. For instance, consider the following list, together with its corresponding source code:  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/9fd6130d36c623e5b21e1b151538120b962d3178b91b5b967154a3454149729a.jpg)  

Then the  itemize  tag corresponds to the outer list environment, whereas the bullets of the inner list items are produced by the  item  tag.  

The rendering of the outer list environment is controlled by the  render-list macro, which takes the body of the list as its argument. For example, con- sider the following redeﬁnition of  render-list :  

h assign j render-list j h macro j body j h surround j h no-page-break\* ih vspace\* j 0.5fn ij h right-ﬂush ih vspace j 0.5fn ih no-indent\* ij h with j par-left jh plus j par-left j 3fn ij par-right jh plus j par-right j 3fn ij body iiii  

This redeﬁnition aﬀects the rendering of all list environments (itemize, enu- merate, etc.) and reduces their right margin by  3fn :  

• This text, which has been made so long that it does not ﬁt on a single line, is indented on the right-hand side by  3fn . 1. This text is indented by an additional  3fn  on the right-hand side, since it occurs inside a nested list environment.  

• Once again: this text, which has been made so long that it does not ﬁt on a single line, is indented on the right-hand side by  3fn .  
In a similar way, you may customize the rendering of list items by redeﬁning the macros  aligned-item  and  compact-item . Both these macros take the text for marking the item as their only argument (e.g. a bullet or a number). The macro  aligned-item  aligns the marker to the right (so that subsequent text is left-aligned), whereas  compact-item  aligns it to the left (so that subsequent text may not be aligned).  

For example, consider the following redeﬁnition of  aligned-item :  

h assign j aligned-item j h macro j x j h concat j h vspace\* j 0.5fn ij h with j par-ﬁrst j -3fn jh yes-indent iij h resize jh embbb j x ijh minus j 1r j 2.5fn ijjh plus j 1r j 0.5fn ijiiii  

Then items inside all list environments with aligned items will be “blackboard emboldened”:  

Items in aligned description lists are rendered using  aligned-item . First condition. Second condition. Items in compact description lists are rendered using  compact-item . Gnus and gnats.  Nice beasts. Micros and softies.  Evil beings.  

In this example, we used  $\mathsf{\langle r e s i z e|\langle e m b b b|x\rangle|\langle m i n u s|1r|2.5f n\rangle||\langle p l u s|1r|0.5f n\rangle|\rangle}$  h embbb  $\mid x\rangle$   inside a box of width  3fn : the new left limit of the 2.5fn  to the left of the original right limit    $1\mathtt{r}$  ; the new right limit is  0.5fn farther to the right. We next used    $\langle\bar{\mathsf{w i t h}}|p a r\!\!-\!\!\bar{f i r s t}|\!\!-\!3\mathsf{f n}|\langle\mathsf{y e s\!\!-\!\bar{n d e n t}}\rangle\rangle$   to move the resulting box  3fn  to the left, thereby aligning it to the right 13.1 .  

Remark 13.4.  Both  aligned-item  and  compact-item  are inline macros. They are also base macros for various other internal macros  aligned-space-item ,  long- compact-strong-dot-item , etc. that are used for the rendering of the diﬀerent types of lists ( itemize-arrow ,  description-long , etc.).  

The  std-list  package also provides a macro  new-list  to deﬁne new lists. Its syntax is  h new-list j name j item-render j item-transform i , where  name  is the name of the new list environment,  item-render  an (inline) macro for rendering the item and  item-transform  an additional transformation that is applied on the item text. For instance, the  enumerate-roman  environment is deﬁned by  
# Chapter 14 Extend beyond imagination  

One major feature of   $\mathrm{TeV}$   is the possibility to extend the editor using the G UILE -S CHEME  extension language . Such extensions can be simple, like a per- sonal boot file with frequently used keyboard shortcuts, or more complex, like a plug-in with special editing routines for documents of a particular type. The S CHEME  language can also be used interactively from within the editor or invoked by special markup like “actions”.  

Why S CHEME ? The choice may indeed seem somewhat odd if you are accus- tomed to more conventional programming languages such as  $C++,$  , J AVA , or P YTHON . In particular, S CHEME 's heavily parenthesized syntax may scare more than one person. But it turns out that this baroque syntax has several advantages for our application. For one thing, it is easy to learn. More impor- tantly, it enables us to treat programs and data in a uniform manner, which is particularly useful in the light of section 12.2.3. Other major advantages of S CHEME  are its interactivity and high level of abstraction.  

This chapter starts with a crash course on S CHEME  [56]. There are several more extensive books on this topic, such as [15, 11, 52]. We also recommend to take a look at the G UILE  reference manual [22], since this is the S CHEME  implemen- tation on which  $\mathrm{TeV}$   is currently based.  

The rest of the chapter provides an introduction to programming TEX MACS extensions in S CHEME . More explanations on this subject can be found in  Help    Scheme extensions . It is also instructive to take a look at those  $\mathrm{TeV}$   source ﬁles that are written in S CHEME . These ﬁles can be found in the  progs  subdi- rectory of the path  $\Updownarrow$  TEXMACS_PATH  where you installed  $\mathrm{TeV}$  . For instance,  $\Updownarrow$  TEXMACS_PATH/progs/math/math-kbd.scm  lists the keyboard shortcuts in math mode.  

# 14.1 A quick introduction to S CHEME  

# 14.1.1 S CHEME  sessions and atomic data types  

$\mathrm{TeV}$   uses S CHEME  through an interactive interpreter. For a ﬁrst encounter with the language, we invite you to launch an interactive S CHEME  session using Insert      Session  $\blacktriangleright$    Scheme . This allows you to enter commands after the S CHEME prompt and execute them by pressing  $\spadesuit$  :  

Scheme]    $(+~\mathbb{1}~\mathbb{1})$  ) 2  

As you can see in this stunning example, applying a function  f  to the arguments  $\mathsf{a}_{1},\hdots,\,\mathsf{a}_{\mathsf{n}}$     $(\mathtt{f}\ \ \mathtt{a_{1}}\ \ .\ .\ .\ \ \mathtt{a_{n}})$  . Besides numbers, other fundamental atomic data types in S CHEME  are booleans ( #t  and  #f ), characters ( #\a ,  #\b , #\c ,...), strings ( "hi" ,  "there" ,...) and symbols ( x ,  fun ,  gnu2018 ,  my-sym ,

  $\mathbf{x}/3*,\ldots)$  . The following mini-session shows a few typical computations with such objects:  
Scheme]  (  $\dot{.}>$   3 2 )  

#t Scheme]  ( if  ( >  2 3 )  "yes" "no" ) "no" Scheme]  ( string->list  "Bonjour" ) ( #\B #\o #\n #\j #\o #\u #\r ) Scheme]  ( string-append  "Hi" " " "there" "!" ) "Hi there!" Scheme]  ( string->symbol  "hop@boeh!stuff\*" )  

hop@boeh!stuff\*  

Scheme]  ( symbol?  'my-sym)  

#t  

One diﬀerence between strings and symbols is the notation, since strings need to be double quoted. Moreover, strings are literal constants, just like the num- bers  2  and  3.14 , whereas symbols are evaluated by S CHEME . One may prevent a S CHEME  expression from being evaluated using  '  as a preﬁx operator; this explains why we used  'my-sym  in order to obtain the symbol  my-sym . From a computational point of view, symbols are sometimes more efficient: the equality of two symbols can be checked in unit time, whereas all characters in two strings need to be compared.  

Symbols are also used as names for variables and functions. We note that S CHEME  is very ﬂexible when it comes to names of functions: all characters can be used except for whitespace and the special characters  ()[]{}#.,;'"\`\ . This makes it possible to use suggestive names  string->symbol  and  symbol?  for converters and predicates. Also note that the dash  -  tends to be used (instead of  _ ) as a connector for multiple-word function names such as  string-append . In particular, many function names are preﬁxed by the type of their principal argument.  

# 14.1.2 Lists and S CHEME  trees  

Expressions of the form    $(\mathbf{x}_{1}\ \ .\ .\ .\ \ \mathbf{x}_{\mathbf{n}})$   are also called  lists  and they are one of the most fundamental data structures in S CHEME . Lists are either constructed using  list  (from its list of entries) or  cons  (from the ﬁrst  head  entry and the tail  list of remaining entries):  

Scheme]  ( list    $(+~\,1~\,2~\,3)$  )  "hopsa"  ( =  2 3.4 )) ( 6  "hopsa" #f )  
Scheme]  ( cons    $(*\;\;1\;\;2\;\;3\;\;4\;\;5)$  ) ( list  6 7 8 9 10 ))  

# ( 120 6 7 8 9 10 )  

Notice that the second method corresponds to the way lists are stored in memory: the empty list corresponds to a special constant, whereas non-empty lists are stored as pairs with the ﬁrst element of the list and a pointer to the tail. One may test for emptiness using the  null?  predicate and access the head and the tail using the  car  and  cdr  accessors. Moreover,  ( caar  l) ,  ( cadr  l) , etc. can be used as shorthands for  ( car  ( car  l)) ,  ( car  ( cdr  l)) , etc.  

Scheme]  ( define  l ( list  1 2 3 )) Scheme]  ( list  ( null?  l) ( car  l) ( cdr  l) ( caddr  l) (null? (cdddr l)))  

# ( #f  1  ( 2 3 )  3  #t )  

Lists are also quite convenient for the representation of   $\mathrm{TeV}$   document √ fragments. For instance,  (frac (sqrt "a") "b")  represents the fraction  $\frac{\sqrt{a}}{b}$  . One may use the preﬁx operator  '  to construct explicit S CHEME  expressions of this kind, as we saw before in the case of symbols. The general mechanism is called  quoting  and it is extremely convenient:  

Scheme]  ( sqrt  "a" )  ;; try to apply the function sqrt to "a" Wrong type (expecting real number) :  "a" Scheme]  '( sqrt  "a" )  ;; prevent evaluation using quoting ( sqrt  "a" )  

S CHEME  also oﬀers the preﬁx operator  \`  for  quasi-quoting . Like quoting, quasi- quoting switches oﬀevaluation; however, the evaluation of speciﬁc parts of the expression can be switched on again using the preﬁx operators  ,  and  ,@ (called  unquoting  and  unquote-splicing ):  

Scheme]  \`(hop (hola ,  $({\it\Delta\phi}\ \ 1\ \ 2)$   ,( string->list  "hop" )) (hola ,  $(*~3~4)$  ) ,@( string->list  "hop" )))  

(hop (hola  3  ( #\h #\o #\p )) (hola  12  #\h #\o #\p ))  

Those S CHEME  expressions that correspond to snippets of  $\mathrm{TeV}$   documents will be called S CHEME  trees . A S CHEME  tree is either a string or a list of the form    $(\mathtt{l\ \ t_{1}\ \ \cdot\cdot\cdot\ \ t_{n}})$  , where  l  is a   $\mathrm{TeV}$   primitive or macro and  $\sf t_{\mathrm{1}},\dots,t_{\mathrm{n}}$  are other S CHEME  trees. One may convert such S CHEME  trees to actual TEX MACS trees and  vice versa  using the routines  stree->tree  and  tree->stree :  

Scheme]  ( stree->tree  '(math (frac ( sqrt  "a" )  "b" )))  $\frac{\sqrt{a}}{b}$  

Scheme]  ( define  my-name  "John" )  
Scheme]  ( stree->tree  

\`( concat  "My name is "  (strong ,my-name)  "." ))  

My name is  John .  

# 14.1.3 Declaring functions and macros  

New S CHEME  functions can be declared using  define :  

Scheme]  ( define  (fibonacci n) ( if  (  $\cdot<=\texttt{n}\,^{1}$  )  1 (  $^+$   (fibonacci ( -  n  1 )) (fibonacci ( -  n  2 )))))  

Scheme]  (fibonacci  25 )  

# 121393  

Scheme]  ( define  ( ..  i j) ( if  ( <  i j) ( cons  i ( ..  ( +  i  1 ) j)) ( list ))) Scheme]  ( .. 0 15 ) ( 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 )  

One important feature of S CHEME  is that it is a functional programming lan- guage: functions can both be used as arguments and return values for other functions. For example, you may use  apply  and  map  to apply a function to a list of arguments or to each element of a list:  

Scheme]  ( map  fibonacci ( .. 0 15 )) ( 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 )  

The following syntax allows use to deﬁne functions that return functions:  

Scheme]  ( define  ((unary-compose f g) x) (f (g x))) Scheme]  (unary-compose fibonacci fibonacci)  

#<procedure #f    $(\mathbf{x})\!>$  

Scheme]  ((unary-compose fibonacci fibonacci)  5 )  

# 34  

S CHEME  also provides syntactic sugar to declare functions with an arbitrary number of arguments. The following improvement of  unary-compose  shows an example:  

Scheme]  ( define  (( compose  f  .  gs)  .  xs) ( apply  f ( map  ( lambda  (g) ( apply  g xs)) gs)))  

Scheme]  (( compose - \* + )  1 2 3 4 ) ;; (- (\* 1 2 3 4) (  $\cdot+$   1 2 3 4)  
Notice that  ( lambda  (g) ( apply  g xs))  stands for the function that takes  g as input and that returns  ( apply  g xs) .  

Yet another powerful feature of S CHEME  is the possibility to enrich the lan- guage with new primitives, through the declaration of S CHEME  macros . This is done using the keyword  define-macro  that has a similar syntax as  define , but with the diﬀerence that the return value is evaluated a second time.  

Scheme]  ( define-macro  (sum i vals  .  body) \`( apply   $^+$   ( map  ( lambda  (,i) ,@body) ,vals))) Scheme]  (sum k ( .. 0 10 ) ( \*  k k)) ;; (apply   $^+$   (map (lambda (k) (\* k k)) (.. 0 10)))  

285  

This example also illustrates the power of quasi-quotation in combination with the macro system.  

$\mathrm{T}_{\mathrm{E}}\mathrm{X}_{\mathrm{MACS}}$   heavily relies on this possibility to extend the S CHEME  language with new macros. For instance, new keyboard shortcuts and menus can be deﬁned using the  kbd-map  and  tm-menu  macros, by means of a convenient syntax. In fact, function and macro declarations themselves should be done using  tm- define  and  tm-define-macro : as will be detailed in section 14.3.2 below, these enhanced versions of  define  and  define-macro  make it possible to overload functions and macros in a contextual way; they also allow you to enrich functions with extra information that may be exploited by the graph- ical user interface, such as “suggested values” for certain function arguments.  

# 14.1.4 Basic control structures  

Local variables in S CHEME  are introduced using the keyword  let\* , whereas set!  can be used to assign a new value to such a variable:  

Scheme]  ( define  $\begin{array}{r l}&{\tt{e f i n e\Psi\left(f o o\Psi\left.x\right)}}\\ &{\tt{(l e t^{*}\Psi\left(\left(a\Psi\left(*\textbf{x}\textbf{x}\right)\right)}\\ &{\tt\qquad\quad\left(b\Psi\left(+\textbf{a}\textbf{x}\right)\right)\right)}}\\ &{\tt{(s e t!\Psi\left.a\Psi\left(*\textbf{a}b\right)\right)}}\\ &{\tt{(+\Psi\left(a\textbf{x}\right)\right)}}\end{array}$  

Scheme]  (foo  100 )  

# 101000100  

The  if  primitive can be used both as an instruction and as an expression that returns a value. S CHEME  programmers also frequently rely on the  cond  prim- itive which provides an elegant abbreviation for expressions like  

( if  c 1  expr 1 ( if  c 2  expr 2 ... ))  
For instance:  

Scheme]  ( define  (mix l1 l2) ( cond  (( null?  l1) l2) (( null?  l2) l1) ( else  \`(,( car  l1) ,( car  l2) ,@(mix ( cdr  l1) ( cdr  l2))))))) Scheme]  (mix ( list  'a 'b 'c) ( list  1 2 3 4 5 ))  

(a  1  b  2  c  3 4 5 )  

The boolean combinators  and  and  or  can take an arbitrary number of argu- ments. In fact, the types of the arguments are allowed to be arbitrary with the property that any value distinct from  #f  is considered to be “true”. More precisely, the evaluation of  ( and    $\bf{x}_{1}\cdot\cdot\cdot\cdot\bf{x}_{n})$  )  stops as soon as the ﬁrst  $\mathbf{x_{i}}$   in the list evaluates to  #f  (in which the return value is  #f ). If this never happens, then the evaluation of  $\mathtt{x_{n}}$   is returned. Similar rules apply for the  or  primitive and various other functions that manipulate boolean values.  

Scheme]  ( define  a  #f ) Scheme]  ( define  (set!a b) ( set!  a b) a) Scheme]  ( list  ( and  "hi" "there" ) ( and  "hi"  (set!a  10 )  #f  (set!a  100 )) a) ( "there" #f  10 )  

# 14.2 Customizing the graphical user interface  

# 14.2.1 Your personal boot ﬁle  

So far, we have seen how to execute S CHEME  commands from interactive ses- sions. In order the develop more permanent S CHEME  code for  $\mathrm{TeV}\mathrm{X}_{\mathrm{MACS}},$   the simplest method is to create a personal boot ﬁle that should be named  

$\Updownarrow$  TEX MACS HOME PATH/progs/my-init-texmacs.scm  

We recall that  $\Updownarrow$  TEX MACS HOME PATH  usually points to the  .TeXmacs  subdirec- tory of your home directory  \~ . If it exists, then the personal boot ﬁle is assumed to contain a S CHEME  program that will be executed every time you launch

  $\mathrm{TeV}$  . As a ﬁrst test, you may create a personal boot ﬁle with a single line  

( display\*  "Hello world!\n" )  

Every time you launch   $\mathrm{TeV}$   from the command line, this should display Hello world!  on your terminal.  
# 14.2.2 Adding your own keyboard shortcuts  

You may use the command  kbd-map  in order to deﬁne new keyboard short- cuts. For example, if you wish to be able to start a new deﬁnition by typing D e f .  (and similarly for lemmas, propositions, and theorems), then it suﬃces to add the following code to your personal boot ﬁle:  

# ( kbd-map  

( "D e f ."  ( make  'definition)) ( "L e m ."  ( make  'lemma)) ( "P r o p ."  ( make  'proposition)) ( "T h ."  ( make  'theorem)))  

Each shortcut is of the form  (s cmd) , where  s  is a string of key-combinations and  cmd  the S CHEME  command that should be executed. The command  ( make name)  starts a new tag with a given  name  at the current cursor position.  

It is also possible to deﬁne shortcuts that only apply under certain circum- stances. Assume for instance that we wish to deﬁne the shortcut  p i  for  $\pi,$  but only in math mode. Assume in addition that we wish to be able to quickly enter  $\bar{\pi^{2}}$    and  $2\,\pi\mathrm{i}$   as variants. This can be achieved as follows:  

( kbd-map ( :mode  in-math? ) ( "p i" "<mathpi>" ) ( "p i var"  ( insert  '( concat  "<mathpi>"  (rsup  "2" )))) ( "p i var var"   $^{\dag}2*$  <mathpi>\*<mathi>" ))  

In this example, the command  ( insert  t)  is used to insert a given   $\mathrm{TeV}$  tree  t  at the current cursor position. Since the insertion of strings is very common, it is allowed to use  ( "p i" "<mathpi>" )  as a shorthand for ( "p i"  ( insert  "<mathpi>" )) .  

Special keys such as  $\bullet|,\;\bullet|,\;\bullet|,$   etc. carry special names  return ,  backspace , right , etc. Keyboard combinations using “Shift”, “Control”, “Alter”, and “Meta” are obtained using the prefixes  S- ,  C- ,  A- , and  M- . In order to define  $\twoheadrightarrow$  as a keyboard shortcut for inserting a big vertical space, one may therefore use  

# ( kbd-map ( "C-M-return"  ( insert  '(vspace  "2fn" ))))  

Some simple keyboard shortcuts such as  $\rightarrow$  or  $\nrightarrow$  are so heavily overloaded that  $\mathrm{TeV}$   treats them in a special way. For example,  $\rightarrow$  triggers the action ( kbd-right ) , which in turn invokes the function  kbd-horizontal  with suit- able arguments. Instead of redefining the  $\rightarrow$  shortcut, it is therefore better to customize the function  kbd-horizontal  whenever appropriate. The cus- tomization of existing functions will be discussed in more detail in section 14.3.2 below.  
# 14.2.3 Adding your own menus  

T E X MACS  menus are generated through special S CHEME  functions such as texmacs-menu ,  insert-menu , or  texmacs-extra-menu . Simple menus are created using the macro  menu-bind :  

( menu-bind  hello-menu (->  "Opening" ( "Dear Sir"  ( insert  "Dear Sir," )) ( "Dear Madam"  ( insert  "Dear Madam," ))) (->  "Closing" ( "Yours sincerely"  ( insert  "Yours sincerely," )) ( "Greetings"  ( insert  "Greetings," ))))  

Simple menu entries are of the form  (label cmd) , whereas  $->$   is used in order to create submenus. The menu  hello-menu  needs to be attached to one of the standard menus in order to be accessible through the interface. Top-level menus for your personal use should be added to  texmacs-extra-menu  (so that they will appear just before the  Focus  menu):  

( menu-bind  texmacs-extra-menu (  $'=>$   "Hello"  ( link  hello-menu)) ( former ))  

The syntax  $=>$   corresponds to a top-level pulldown submenu, whereas  former refers to the previous value of  texmacs-extra-menu . We will come back to the  former  primitive in section 14.3.2 below. Here it provides us with a clean mechanism to extend the menu  texmacs-extra-menu  more than once, if needed, possibly in diﬀerent S CHEME  modules.  

You may use  assuming  or  when  for conditional menus; in the case of  when , the conditional menu items are greyed whenever the condition is not met. In order to add  hello-menu  to  insert-menu  under the condition that we are using the letter style, you may proceed as follows:  
# 14.3 Extending the editor  

# 14.3.1 Manipulation of active content  

All   $\mathrm{TeV}$   documents or document fragments can be thought of as  trees . There are three data types that correspond to such trees:  

Scheme trees.  We have already encountered the type  stree  of  scheme trees in section 14.1.2; for instance, the scheme tree  (frac ( concat  "a"  $(\tt r s u p\phi^{\prime\prime}2^{\prime\prime})$  )    $\mathrm{"b+c\,"}$  )  represents the formula  $\frac{a^{2}}{b+c}$  + . Scheme trees can in principle be manipulated using stand-alone S CHEME  programs that do not even require   $\mathrm{TeV}$   to be installed on your computer.  

$\mathbf{TeV}\mathbf{X}_{\mathbf{MACS}}$   trees.  The type  tree  of    $T_{E}X_{M A C S}$   trees  is a data type that is hard- coded in the  $C++$   source code of   $\mathrm{TeV}$  . It can in particular be used to represent active document fragments that are visible in  $\mathrm{TeV}$   win- dows. The  tree  type is an extension to the S CHEME  language that is speciﬁc to   $\mathrm{TeV}$   and that is only available inside the editor.  

Hybrid trees.  Often, it is also convenient to mix the above types of trees into a super-type  tm  of so-called  hybrid trees . More precisely, a hybrid tree is either a string, a tree, or a list of the form    $(\mathbb{1}\;\;{\tt x}_{1}\;\;.\;.\;.\;\;{\tt x}_{\tt n})$  , where l  is a symbol and  $\mathbf{x}_{1},\,...,\,\mathbf{x_{n}}$  

Here is one example of each of these types of trees:  

Scheme]  ( define  st '(frac ( concat  "a"  (rsup  "2" ))  "b+c" )) Scheme]  ( define  tt ( stree->tree  st)) Scheme]  ( define  ht \`(math ( concat  ,tt  "+"  ,tt)))  

You may already have noticed that  tree  objects are pretty-printed inside S CHEME  sessions:  

Scheme]  ht  

(math ( concat  <tree <frac|a<rsup|2>|b+c>>  "+"  <tree

 <frac|a<rsup|2>|b+c>>))  

Scheme]  ( tm->tree  ht)  

$$
\frac{a^{2}}{b+c}\!+\!\frac{a^{2}}{b+c}
$$  

The predicates  stree? ,  tree? , and  tm?  can be used to test whether a given S CHEME  object is a tree of type  stree ,  tree , or  tm :  

Scheme]  ( map  ( lambda  (p?) ( map  p? ( list  st tt ht))) ( list stree? tree? tm? )) (( #t #f #f ) ( #f #t #f ) ( #t #t #t ))  
One special   $\mathrm{TeV}$   tree is the  root tree  ( root-tree ) . Each open TEX MACS document is a child of the root tree and vice versa. Arbitrary subtrees of the root tree are called  active trees  and each such subtree is aware of its position inside the root tree. Using dedicated S CHEME  routines from the tree API, this allows us to make changes in documents simply by assigning new values to active  $\mathrm{TeV}$   trees. In order to use these routines, one ﬁrst has to import them from the appropriate module:  

Scheme]  ( use-modules  (utils library  tree ))  

The following routine can then be implemented to clear the buffer being edited:  

Scheme]  ( define  (clear-document) ( tree-set  ( buffer-tree ) \`( document  "" )))  

Positions within trees are indicated through lists of numbers called  paths  and so are cursor positions. For instance, the superscript  2  in the S CHEME  tree (frac ( concat  "a"  (rsup  "2" ))    $\mathrm{"b+c\,"}$  )  corresponds to the path  ( 0 1 0 ) , whereas the cursor position just behind the  $^+$   in the denominator corre- sponds to the path  ( 1 2 ) :  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/e6062906eca1b03bc76169dc25f368343b22b8f7e5c947dc006c49b153598834.jpg)  

The primitives  tree-set ,  tree-ref , and  tm-ref  can be used for the modiﬁ- cation and retrieval of subtrees along paths:  

"2" Scheme]  ( tree-set  tt  0 1 0  "3" ) 3  

Scheme]  ( tm->tree  \`(math ,ht))  

$$
\frac{a^{3}}{b+c}\!+\!\frac{a^{3}}{b+c}
$$  

Another useful macro for writing editing routines is  with-innermost : it looks for the innermost tree at the current cursor position that matches a certain predicate, assigns this tree to a local variable, and then runs some code. If the predicate cannot be matched, then nothing is done. If a tag is provided instead of a predicate, then we test whether the root of the tree is labeled by that tag.  
Together with what precedes, we are now in a position to deﬁne a routine that swaps the numerator and the denominator of a fraction, and attach it to the keyboard shortcut  $\hat{\mathbf{\Omega}}$  :  

Scheme]  ( define  (fraction-swap) ( with-innermost  t 'frac ( tree-set  t \`(frac ,( tm-ref  t  1 ) ,( tm-ref  t  0 )))))  

Scheme]  ( kbd-map  (  ${\mathrm{"C-\%"}}$   (fraction-swap)))  

# 14.3.2 Contextual overloading  

For large software projects, it is important that diﬀerent modules can be devel- oped as independently as possible. The mechanism of  contextual overloading  is of great help here: it allows you to implement a default version of a routine in a base module, and then customize this implementation in other modules.  

In order to get the main idea, consider the implementation of a given function- ality, like hitting the return key. Depending on the context, diﬀerent actions have to be undertaken: by default, we start a new paragraph; inside a table, we start a new row; etc. A naive implementation would check all possible cases in a routine  kbd-enter  and call the appropriate routine. However, this makes it impossible to add a new case in a new module without modifying the module that deﬁnes  kbd-enter . By contrast, the system of contextual over- loading allows the user to  conditionally  redeﬁne the routine  kbd-enter  several times in distinct modules.  

Let us illustrate how this works on a simple example. Assume that we want to deﬁne a function  hello  that inserts “Hello” by default, but “ hello() ” in mode math, while positioning the cursor between the brackets, after the sixth char- acter. Using contextual overloading, this can be done as follows:  

![](https://cdn-xlab-data.openxlab.org.cn/pdf/dcfb24dc-759d-4368-aafd-357ee641075b.pdf/29d480f1f7b3a55d294234707a92c899dbbfe771d2c52095f5996e2853a3ec2b.jpg)  

The keyword  :mode  speciﬁes that the second declaration only applies in math- mode, when  ( in-math? )  evaluates to  #t . The order in which routines are over- loaded is important.  $\mathrm{TEPX}_{\mathrm{MACS}}$   first tries the latest (re)definition. If this definition does not satisfy the requirements, then it tries the before-last (re)deﬁnition, and so on until an implementation is found that matches the requirements. In particular, if we swap the two declarations in the above example, then the general unconditional deﬁnition of  hello  will always prevail. If the two dec- larations are made inside diﬀerent modules, then it is up to the user to ensure that the modules are loaded in the appropriate order.  
