"use strict";(self.webpackChunk_JUPYTERLAB_CORE_OUTPUT=self.webpackChunk_JUPYTERLAB_CORE_OUTPUT||[]).push([[883],{20883:(e,t,n)=>{n.r(t),n.d(t,{erlang:()=>Z});var r=["-type","-spec","-export_type","-opaque"],i=["after","begin","catch","case","cond","end","fun","if","let","of","query","receive","try","when"],o=/[\->,;]/,a=["->",";",","],c=["and","andalso","band","bnot","bor","bsl","bsr","bxor","div","not","or","orelse","rem","xor"],u=/[\+\-\*\/<>=\|:!]/,s=["=","+","-","*","/",">",">=","<","=<","=:=","==","=/=","/=","||","<-","!"],l=/[<\(\[\{]/,_=["<<","(","[","{"],f=/[>\)\]\}]/,p=["}","]",")",">>"],m=["is_atom","is_binary","is_bitstring","is_boolean","is_float","is_function","is_integer","is_list","is_number","is_pid","is_port","is_record","is_reference","is_tuple","atom","binary","bitstring","boolean","function","integer","list","number","pid","port","record","reference","tuple"],d=["abs","adler32","adler32_combine","alive","apply","atom_to_binary","atom_to_list","binary_to_atom","binary_to_existing_atom","binary_to_list","binary_to_term","bit_size","bitstring_to_list","byte_size","check_process_code","contact_binary","crc32","crc32_combine","date","decode_packet","delete_module","disconnect_node","element","erase","exit","float","float_to_list","garbage_collect","get","get_keys","group_leader","halt","hd","integer_to_list","internal_bif","iolist_size","iolist_to_binary","is_alive","is_atom","is_binary","is_bitstring","is_boolean","is_float","is_function","is_integer","is_list","is_number","is_pid","is_port","is_process_alive","is_record","is_reference","is_tuple","length","link","list_to_atom","list_to_binary","list_to_bitstring","list_to_existing_atom","list_to_float","list_to_integer","list_to_pid","list_to_tuple","load_module","make_ref","module_loaded","monitor_node","node","node_link","node_unlink","nodes","notalive","now","open_port","pid_to_list","port_close","port_command","port_connect","port_control","pre_loaded","process_flag","process_info","processes","purge_module","put","register","registered","round","self","setelement","size","spawn","spawn_link","spawn_monitor","spawn_opt","split_binary","statistics","term_to_binary","time","throw","tl","trunc","tuple_size","tuple_to_list","unlink","unregister","whereis"],b=/[\w@Ø-ÞÀ-Öß-öø-ÿ]/,k=/[0-7]{1,3}|[bdefnrstv\\"']|\^[a-zA-Z]|x[0-9a-zA-Z]{2}|x{[0-9a-zA-Z]+}/;function g(e,t,n){if(1==e.current().length&&t.test(e.current())){for(e.backUp(1);t.test(e.peek());)if(e.next(),x(e.current(),n))return!0;e.backUp(e.current().length-1)}return!1}function h(e,t,n){if(1==e.current().length&&t.test(e.current())){for(;t.test(e.peek());)e.next();for(;0<e.current().length;){if(x(e.current(),n))return!0;e.backUp(1)}e.next()}return!1}function y(e){return w(e,'"',"\\")}function v(e){return w(e,"'","\\")}function w(e,t,n){for(;!e.eol();){var r=e.next();if(r==t)return!0;r==n&&e.next()}return!1}function x(e,t){return-1<t.indexOf(e)}function S(e,t,n){switch(function(e,t){"comment"!=t.type&&"whitespace"!=t.type&&(e.tokenStack=function(e,t){var n=e.length-1;return 0<n&&"record"===e[n].type&&"dot"===t.type?e.pop():0<n&&"group"===e[n].type?(e.pop(),e.push(t)):e.push(t),e}(e.tokenStack,t),e.tokenStack=function(e){if(!e.length)return e;var t=e.length-1;if("dot"===e[t].type)return[];if(t>1&&"fun"===e[t].type&&"fun"===e[t-1].token)return e.slice(0,t-1);switch(e[t].token){case"}":return W(e,{g:["{"]});case"]":return W(e,{i:["["]});case")":return W(e,{i:["("]});case">>":return W(e,{i:["<<"]});case"end":return W(e,{i:["begin","case","fun","if","receive","try"]});case",":return W(e,{e:["begin","try","when","->",",","(","[","{","<<"]});case"->":return W(e,{r:["when"],m:["try","if","case","receive"]});case";":return W(e,{E:["case","fun","if","receive","try","when"]});case"catch":return W(e,{e:["try"]});case"of":return W(e,{e:["case"]});case"after":return W(e,{e:["receive","try"]});default:return e}}(e.tokenStack))}(e,function(e,t){return U(t.current(),t.column(),t.indentation(),e)}(n,t)),n){case"atom":case"boolean":return"atom";case"attribute":return"attribute";case"builtin":return"builtin";case"close_paren":case"colon":case"dot":case"open_paren":case"separator":default:return null;case"comment":return"comment";case"error":return"error";case"fun":return"meta";case"function":return"tag";case"guard":return"property";case"keyword":return"keyword";case"macro":return"macroName";case"number":return"number";case"operator":return"operator";case"record":return"bracket";case"string":return"string";case"type":return"def";case"variable":return"variable"}}function U(e,t,n,r){return{token:e,column:t,indent:n,type:r}}function z(e){return U(e,0,0,e)}function E(e,t){var n=e.tokenStack.length,r=t||1;return!(n<r)&&e.tokenStack[n-r]}function W(e,t){for(var n in t)for(var r=e.length-1,i=t[n],o=r-1;-1<o;o--)if(x(e[o].token,i)){var a=e.slice(0,o);switch(n){case"m":return a.concat(e[o]).concat(e[r]);case"r":return a.concat(e[r]);case"i":return a;case"g":return a.concat(z("group"));case"E":case"e":return a.concat(e[o])}}return"E"==n?[]:e}function T(e,t){var n=e.tokenStack,r=A(n,"token",t);return!!O(n[r])&&n[r]}function A(e,t,n){for(var r=e.length-1;-1<r;r--)if(x(e[r][t],n))return r;return!1}function O(e){return!1!==e&&null!=e}const Z={name:"erlang",startState:()=>({tokenStack:[],in_string:!1,in_atom:!1}),token:function(e,t){if(t.in_string)return t.in_string=!y(e),S(t,e,"string");if(t.in_atom)return t.in_atom=!v(e),S(t,e,"atom");if(e.eatSpace())return S(t,e,"whitespace");if(!E(t)&&e.match(/-\s*[a-zß-öø-ÿ][\wØ-ÞÀ-Öß-öø-ÿ]*/))return x(e.current(),r)?S(t,e,"type"):S(t,e,"attribute");var n=e.next();if("%"==n)return e.skipToEnd(),S(t,e,"comment");if(":"==n)return S(t,e,"colon");if("?"==n)return e.eatSpace(),e.eatWhile(b),S(t,e,"macro");if("#"==n)return e.eatSpace(),e.eatWhile(b),S(t,e,"record");if("$"==n)return"\\"!=e.next()||e.match(k)?S(t,e,"number"):S(t,e,"error");if("."==n)return S(t,e,"dot");if("'"==n){if(!(t.in_atom=!v(e))){if(e.match(/\s*\/\s*[0-9]/,!1))return e.match(/\s*\/\s*[0-9]/,!0),S(t,e,"fun");if(e.match(/\s*\(/,!1)||e.match(/\s*:/,!1))return S(t,e,"function")}return S(t,e,"atom")}if('"'==n)return t.in_string=!y(e),S(t,e,"string");if(/[A-Z_Ø-ÞÀ-Ö]/.test(n))return e.eatWhile(b),S(t,e,"variable");if(/[a-z_ß-öø-ÿ]/.test(n)){if(e.eatWhile(b),e.match(/\s*\/\s*[0-9]/,!1))return e.match(/\s*\/\s*[0-9]/,!0),S(t,e,"fun");var w=e.current();return x(w,i)?S(t,e,"keyword"):x(w,c)?S(t,e,"operator"):e.match(/\s*\(/,!1)?!x(w,d)||":"==E(t).token&&"erlang"!=E(t,2).token?x(w,m)?S(t,e,"guard"):S(t,e,"function"):S(t,e,"builtin"):":"==function(e){var t=e.match(/^\s*([^\s%])/,!1);return t?t[1]:""}(e)?S(t,e,"erlang"==w?"builtin":"function"):x(w,["true","false"])?S(t,e,"boolean"):S(t,e,"atom")}var U=/[0-9]/;return U.test(n)?(e.eatWhile(U),e.eat("#")?e.eatWhile(/[0-9a-zA-Z]/)||e.backUp(1):e.eat(".")&&(e.eatWhile(U)?e.eat(/[eE]/)&&(e.eat(/[-+]/)?e.eatWhile(U)||e.backUp(2):e.eatWhile(U)||e.backUp(1)):e.backUp(1)),S(t,e,"number")):g(e,l,_)?S(t,e,"open_paren"):g(e,f,p)?S(t,e,"close_paren"):h(e,o,a)?S(t,e,"separator"):h(e,u,s)?S(t,e,"operator"):S(t,e,null)},indent:function(e,t,n){var r,i,o=O(i=t.match(/,|[a-z]+|\}|\]|\)|>>|\|+|\(/))&&0===i.index?i[0]:"",a=E(e,1),c=E(e,2);return e.in_string||e.in_atom?null:c?"when"==a.token?a.column+n.unit:"when"===o&&"function"===c.type?c.indent+n.unit:"("===o&&"fun"===a.token?a.column+3:"catch"===o&&(r=T(e,["try"]))?r.column:x(o,["end","after","of"])?(r=T(e,["begin","case","fun","if","receive","try"]))?r.column:null:x(o,p)?(r=T(e,_))?r.column:null:x(a.token,[",","|","||"])||x(o,[",","|","||"])?(r=function(e){var t=e.tokenStack.slice(0,-1),n=A(t,"type",["open_paren"]);return!!O(t[n])&&t[n]}(e))?r.column+r.token.length:n.unit:"->"==a.token?x(c.token,["receive","case","if","try"])?c.column+n.unit+n.unit:c.column+n.unit:x(a.token,_)?a.column+a.token.length:(r=function(e){var t=e.tokenStack,n=A(t,"type",["open_paren","separator","keyword"]),r=A(t,"type",["operator"]);return O(n)&&O(r)&&n<r?t[n+1]:!!O(n)&&t[n]}(e),O(r)?r.column+n.unit:0):0},languageData:{commentTokens:{line:"%"}}}}}]);