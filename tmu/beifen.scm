(delayed 
 (lazy-keyboard-force)
(kbd-map
  ("D e f ." (make 'definition))
  ("L e m ." (make 'lemma))
  ("P r o p ." (make 'proposition))
  ("T h ." (make 'theorem))
  ("C-m" (make 'script-input))
  ("@ r" (insert '(with "color" "red" "<#2665>")))
  ("= @ @" "=<infty>")
  ("M x ." "maxima")
  ("P y ." "pthon")
  ("G p ." "gnuplot")
  ("p 2 d" "tm_plot2d([M],[x,-10,10],[y,-3,7])")
  ("d b u g" "debugmode(true)")
  ("h j" "fullratsimp")
)
(use-modules (convert markdown init-markdown))


(document (provide "edit-insert-math" (macro (document (inactive (script-input "maxima" "default" ""))))) (assign "edit-insert-mathGnuplot" (macro (document (concat (inactive* "") (inactive (script-input "gnuplot" "default" "")))))) (assign "edit-insert-mathPython" (macro (document (inactive (script-input "python" "default" "")) ""))))
(define (propose-pdf-name)
  (with name (propose-name-buffer)
  (if (string-ends? name ".tmu")
    (string-append (string-drop-right name 3) ".pdf"))))

(define (export-to-proposed-pdf)
  (let ((pdf-name (propose-pdf-name)))
    (if (url-test? pdf-name "f")
      (user-confirm "File already exists. Really overwrite?" #f
        (lambda (answ)
        (when answ (wrapped-print-to-file pdf-name))))
      (wrapped-print-to-file pdf-name))))
(delayed (:idle 1000) (output-set-line-length 1000000000))
(kbd-map
  ("C-p" (export-to-proposed-pdf))
)
)
            





