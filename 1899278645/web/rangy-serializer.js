/**
 * Serializer module for Rangy.
 * Serializes Ranges and Selections. An example use would be to store a user's selection on a particular page in a
 * cookie or local storage and restore it on the user's next visit to the same page.
 *
 * Part of Rangy, a cross-browser JavaScript range and selection library
 * https://github.com/timdown/rangy
 *
 * Depends on Rangy core.
 *
 * Copyright 2015, Tim Down
 * Licensed under the MIT license.
 * Version: 1.3.0
 * Build date: 10 May 2015
 */
!function(e,n){"function"==typeof define&&define.amd?define(["./rangy-core"],e):"undefined"!=typeof module&&"object"==typeof exports?module.exports=e(require("rangy")):e(n.rangy)}(function(e){return e.createModule("Serializer",["WrappedSelection"],function(e,n){function t(e){return e.replace(/</g,"&lt;").replace(/>/g,"&gt;")}function o(e,n){n=n||[];var r=e.nodeType,i=e.childNodes,c=i.length,a=[r,e.nodeName,c].join(":"),d="",u="";switch(r){case 3:d=t(e.nodeValue);break;case 8:d="<!--"+t(e.nodeValue)+"-->";break;default:d="<"+a+">",u="</>"}d&&n.push(d);for(var s=0;c>s;++s)o(i[s],n);return u&&n.push(u),n}function r(e){var n=o(e).join("");return w(n).toString(16)}function i(e,n,t){var o=[],r=e;for(t=t||R.getDocument(e).documentElement;r&&r!=t;)o.push(R.getNodeIndex(r,!0)),r=r.parentNode;return o.join("/")+":"+n}function c(e,t,o){t||(t=(o||document).documentElement);for(var r,i=e.split(":"),c=t,a=i[0]?i[0].split("/"):[],d=a.length;d--;){if(r=parseInt(a[d],10),!(r<c.childNodes.length))throw n.createError("deserializePosition() failed: node "+R.inspectNode(c)+" has no child with index "+r+", "+d);c=c.childNodes[r]}return new R.DomPosition(c,parseInt(i[1],10))}function a(t,o,c){if(c=c||e.DomRange.getRangeDocument(t).documentElement,!R.isOrIsAncestorOf(c,t.commonAncestorContainer))throw n.createError("serializeRange(): range "+t.inspect()+" is not wholly contained within specified root node "+R.inspectNode(c));var a=i(t.startContainer,t.startOffset,c)+","+i(t.endContainer,t.endOffset,c);return o||(a+="{"+r(c)+"}"),a}function d(t,o,i){o?i=i||R.getDocument(o):(i=i||document,o=i.documentElement);var a=S.exec(t),d=a[4];if(d){var u=r(o);if(d!==u)throw n.createError("deserializeRange(): checksums of serialized range root node ("+d+") and target root node ("+u+") do not match")}var s=c(a[1],o,i),l=c(a[2],o,i),f=e.createRange(i);return f.setStartAndEnd(s.node,s.offset,l.node,l.offset),f}function u(e,n,t){n||(n=(t||document).documentElement);var o=S.exec(e),i=o[3];return!i||i===r(n)}function s(n,t,o){n=e.getSelection(n);for(var r=n.getAllRanges(),i=[],c=0,d=r.length;d>c;++c)i[c]=a(r[c],t,o);return i.join("|")}function l(n,t,o){t?o=o||R.getWindow(t):(o=o||window,t=o.document.documentElement);for(var r=n.split("|"),i=e.getSelection(o),c=[],a=0,u=r.length;u>a;++a)c[a]=d(r[a],t,o.document);return i.setRanges(c),i}function f(e,n,t){var o;n?o=t?t.document:R.getDocument(n):(t=t||window,n=t.document.documentElement);for(var r=e.split("|"),i=0,c=r.length;c>i;++i)if(!u(r[i],n,o))return!1;return!0}function m(e){for(var n,t,o=e.split(/[;,]/),r=0,i=o.length;i>r;++r)if(n=o[r].split("="),n[0].replace(/^\s+/,"")==C&&(t=n[1]))return decodeURIComponent(t.replace(/\s+$/,""));return null}function p(e){e=e||window;var n=m(e.document.cookie);n&&l(n,e.doc)}function g(n,t){n=n||window,t="object"==typeof t?t:{};var o=t.expires?";expires="+t.expires.toUTCString():"",r=t.path?";path="+t.path:"",i=t.domain?";domain="+t.domain:"",c=t.secure?";secure":"",a=s(e.getSelection(n));n.document.cookie=encodeURIComponent(C)+"="+encodeURIComponent(a)+o+r+i+c}var h="undefined",v=e.util;(typeof encodeURIComponent==h||typeof decodeURIComponent==h)&&n.fail("encodeURIComponent and/or decodeURIComponent method is missing");var w=function(){function e(e){for(var n,t=[],o=0,r=e.length;r>o;++o)n=e.charCodeAt(o),128>n?t.push(n):2048>n?t.push(n>>6|192,63&n|128):t.push(n>>12|224,n>>6&63|128,63&n|128);return t}function n(){for(var e,n,t=[],o=0;256>o;++o){for(n=o,e=8;e--;)1==(1&n)?n=n>>>1^3988292384:n>>>=1;t[o]=n>>>0}return t}function t(){return o||(o=n()),o}var o=null;return function(n){for(var o,r=e(n),i=-1,c=t(),a=0,d=r.length;d>a;++a)o=255&(i^r[a]),i=i>>>8^c[o];return(-1^i)>>>0}}(),R=e.dom,S=/^([^,]+),([^,\{]+)(\{([^}]+)\})?$/,C="rangySerializedSelection";v.extend(e,{serializePosition:i,deserializePosition:c,serializeRange:a,deserializeRange:d,canDeserializeRange:u,serializeSelection:s,deserializeSelection:l,canDeserializeSelection:f,restoreSelectionFromCookie:p,saveSelectionCookie:g,getElementChecksum:r,nodeToInfoString:o}),v.crc32=w}),e},this);
