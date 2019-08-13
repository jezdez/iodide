import * as monaco from "monaco-editor/esm/vs/editor/editor.api";

import { makeSuggestionList } from "./make-suggestion-list";

const { Keyword } = monaco.languages.CompletionItemKind;

// FIXME validChunkFlags should move to state-schema, or some other place
// where we keep globally relevant things like this.
export const validChunkFlags = ["skipRunAll"];

export const delimLineSuggestion = (lineSoFar, knownChunkTypes, lineNumber) => {
  let suggestions;
  if (lineSoFar === "%") {
    suggestions = makeSuggestionList(
      knownChunkTypes.map(ct => `%% ${ct}`),
      Keyword,
      { range: new monaco.Range(lineNumber, 1, lineNumber, 2) }
    );
  } else if (lineSoFar.match("^%%+$")) {
    const numPctSigns = lineSoFar.length;
    suggestions = makeSuggestionList(
      knownChunkTypes.map(ct => `${"%".repeat(numPctSigns)} ${ct}`),
      Keyword,
      { range: new monaco.Range(lineNumber, 1, lineNumber, numPctSigns) }
    );
  } else if (lineSoFar.match(new RegExp(knownChunkTypes.join("|")))) {
    // if the delimLine already includes a valid chunk type
    // then return the valid chunkflags as suggestions...
    suggestions = makeSuggestionList(validChunkFlags, Keyword);
  } else {
    // otherwise, suggest a chunk types without a prefix
    suggestions = makeSuggestionList(knownChunkTypes, Keyword);
  }
  return { suggestions };
};
