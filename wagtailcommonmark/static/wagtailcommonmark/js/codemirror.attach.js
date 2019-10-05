const defaultCodeMirrorConfig = {
  gutter: true,
  lineNumbers: true,
  lineWrapping: true,
  theme: "default",
  mode: "markdown",
  viewportMargin: Infinity,
  extraKeys: {"Enter": "newlineAndIndentContinueMarkdownList"},
}

function codeMirrorAttach(id) {
  const element = document.getElementById(id);
  CodeMirror.fromTextArea(element, defaultCodeMirrorConfig)
}

